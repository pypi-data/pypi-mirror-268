"""Helper functions to analyze the results of experiments."""

import abc
import json
from textwrap import indent
from typing import Any, Dict, Tuple
import pandas as pd
from torch import Value
import wandb
import tqdm
from hydra.core.hydra_config import HydraConfig
import logging
from pathlib import Path
import glob

from experiment_lab.core.base_config import BaseConfig


logger = logging.getLogger(__name__)

api = None


def get_api_instance() -> wandb.Api:
    """Gets an instance of the wandb api.

    Returns:
        wandb.Api: The wandb api instance.
    """
    global api
    if api is None:
        api = wandb.Api()
    return api


class BaseAnalysis(abc.ABC):
    """A generic base experiment analysis class."""

    def __init__(self, cfg: BaseConfig) -> None:
        """The constructor for the BaseAnalysis class.

        Args:
            cfg (BaseConfig): The config to analyze with.
        """
        self.cfg = cfg

    def load_data(self) -> Tuple[pd.DataFrame, Dict[str, Dict[str, Any]]]:
        """Function to load the run data of an experiment.

        Raises:
            ValueError: If wandb config is not specified, raise a ValueError.
            ValueError: If load_from_output_dir is set to true without any outputs to load, raise a ValueError.

        Returns:
            Tuple[pd.DataFrame, Dict[str, Dict[str, Any]]]: The dataframe containing all the run data and the dict containing all the configs.
        """
        if not self.cfg.analysis.load_from_output_dir:
            if self.cfg.wandb is None:
                raise ValueError("Not wandb config specified")
            api = get_api_instance()
            wandb_runs = api.runs(
                path=self.cfg.wandb["project"],
                filters={
                    "$and": [
                        {"state": "finished"},
                        {"config.experiment_name": self.cfg.experiment_name},
                    ]
                    + self.cfg.analysis.filters,
                },
                include_sweeps=False,
            )

            full_df = []

            configs = {}

            for wandb_run in tqdm.tqdm(wandb_runs):
                if self.cfg.analysis.all_keys_per_step:
                    df = pd.DataFrame(
                        wandb_run.scan_history(keys=self.cfg.analysis.wandb_keys),
                    )
                else:
                    df = pd.DataFrame()
                    for key in self.cfg.analysis.wandb_keys:
                        temp_df = pd.DataFrame(
                            wandb_run.scan_history(keys=[key]),
                        )
                        df = pd.merge(
                            df, temp_df, left_index=True, right_index=True, how="outer"
                        )
                df["experiment_id"] = wandb_run.config["experiment_id"]
                df["run_id"] = wandb_run.id
                if wandb_run.config["experiment_id"] not in configs:
                    configs[wandb_run.config["experiment_id"]] = wandb_run.config
                if self.cfg.analysis.index is not None:
                    df.set_index(
                        ["experiment_id", "run_id", self.cfg.analysis.index],
                        inplace=True,
                    )
                else:
                    df.set_index(["experiment_id", "run_id"], append=True, inplace=True)
                    df = df.reorder_levels([1, 2, 0])

                full_df.append(df)

            full_df = pd.concat(full_df)
            full_df.sort_index(inplace=True)
        else:
            if self.cfg.analysis.output_dir_to_load_from is None:
                root_output_dir = Path(self.output_directory).parent.parent.absolute()
                glob_results = sorted(glob.glob(f"{root_output_dir}/*/*/run_data.pkl"))
                if len(glob_results) == 0:
                    raise ValueError(
                        "Cannot load results from output directory since there are no other analysis runs."
                    )
                output_dir_to_load_from = Path(glob_results[-1]).parent
            else:
                output_dir_to_load_from = self.cfg.analysis.output_dir_to_load_from
            full_df = pd.read_pickle(f"{output_dir_to_load_from}/run_data.pkl")
            with open(f"{output_dir_to_load_from}/configs.json", "r") as f:
                configs = json.load(f)

        full_df.to_pickle(f"{self.output_directory}/run_data.pkl")
        with open(f"{self.output_directory}/configs.json", "w") as f:
            json.dump(configs, f, indent=4)

        return full_df, configs

    def _analyze_wrapper(self) -> Any:
        """A wrapper for the analyze function.

        Returns:
            Any: The results of the analysis.
        """
        self.output_directory = HydraConfig.get().runtime.output_dir
        df, configs = self.load_data()
        results = self.analyze(df=df, configs=configs)
        logger.info(results)
        return results

    @abc.abstractmethod
    def analyze(self, df: pd.DataFrame, configs: Dict[str, Dict[str, Any]]) -> Any:
        """Runs the analysis for the experiment.

        Args:
            df (pd.DataFrame): The results dataframe from wandb.
            configs (Dict[str, Dict[str, Any]]): The configs for each experiment.

        Returns:
            Any: The results of the analysis.
        """
        pass
