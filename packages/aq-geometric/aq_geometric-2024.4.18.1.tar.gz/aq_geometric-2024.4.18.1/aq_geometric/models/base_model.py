import os
from typing import Tuple, Dict, Union, List

import torch
import numpy as np
import pandas as pd
from torch_geometric.data import Data


class BaseModel(torch.nn.Module):
    r"""Base class for all models."""
    def __init__(self, name: str = "BaseModel",
                 guid: str = "00000000-0000-0000-0000-000000000000",
                 stations: Union[List, None] = None,
                 features: List[str] = [],
                 targets: List[str] = [],
                 num_samples_in_node_feature: int = -1,
                 num_samples_in_node_target: int = -1,   
                 **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.guid = guid
        self.stations = stations
        self.features = features
        self.targets = targets
        self.num_samples_in_node_feature = num_samples_in_node_feature
        self.num_samples_in_node_target = num_samples_in_node_target
        self.num_features_in_node_feature: int = len(self.features),
        self.num_features_in_node_target: int = len(self.targets),
        self.kwargs = kwargs

    def save(self, path: str):
        """Save the model to a file."""
        # ensure the model is on the CPU
        self.cpu()

        # ensure the path exists
        # check if the path has a directory
        if os.path.dirname(path):
            # create the directory if it does not exist
            os.makedirs(os.path.dirname(path), exist_ok=True)

        # gather the model data
        model_data = {
            "name": self.name,
            "guid": self.guid,
            "stations": self.stations,
            "features": self.features,
            "targets": self.targets,
            "num_samples_in_node_feature": self.num_samples_in_node_feature,
            "num_samples_in_node_target": self.num_samples_in_node_target,
            "state_dict": self.state_dict(),
            **self.kwargs
        }
        # save the model data
        torch.save(model_data, path)

    def load(self, path: str):
        """Load the model from a file."""
        # load the model data
        model_data = torch.load(path)

        # set the model data
        self.name = model_data["name"]
        self.guid = model_data["guid"]
        self.stations = model_data["stations"]
        self.features = model_data["features"]
        self.targets = model_data["targets"]
        self.num_samples_in_node_feature = model_data["num_samples_in_node_feature"]
        self.num_samples_in_node_target = model_data["num_samples_in_node_target"]
        self.num_features_in_node_feature = len(self.features)
        self.num_features_in_node_target = len(self.targets)
        
        self.load_state_dict(model_data["state_dict"])

        # set the kwargs
        for key, value in model_data.items():
            if key not in ["name", "guid", "stations", "features", "targets", "num_samples_in_node_feature", "num_samples_in_node_target", "num_features_in_node_feature", "num_features_in_node_target", "state_dict"]:
                setattr(self, key, value)

    def __repr__(self):
        """Use the torch default representation, add new attrs."""
        representation = super().__repr__()
        
        # add new lines with the name, guid, and stations
        representation += f"\nName: {self.name}"
        representation += f"\nGUID: {self.guid}"
        representation += f"\nStations: {self.stations}"
        representation += f"\nFeatures: {self.features}"
        representation += f"\nTargets: {self.targets}"
        representation += f"\nNum samples in node feature: {self.num_samples_in_node_feature}"
        representation += f"\nNum samples in node target: {self.num_samples_in_node_target}"
        representation += f"\nNum features in node feature: {self.num_features_in_node_feature}"
        representation += f"\nNum features in node target: {self.num_features_in_node_target}"

        return representation

    def generate_forecasts(
        self,
        graph: "Data",
        targets: List[str],
        include_history: bool = False,
        verbose: bool = False,
    ) -> Tuple[Dict[str, pd.DataFrame], np.ndarray, np.ndarray]:
        """
        Generate forecasts using the model provided
        """
        raise NotImplementedError


    def forecasts_df_to_db(
        self,
        engine: str,
        graph: "Data",
        target_dfs: Dict[str, pd.DataFrame],
        run_id: Union[str, None] = None,
        chunksize: int = 1000,
        continue_on_error: bool = False,
        verbose: bool = False,
    ) -> int:
        """
        Write the forecasts to the database
        """
        raise NotImplementedError

    def forecasts_graph_to_json(
        self,
        graph: "Data",
        targets: List[str],
        target_dfs: Dict[str, pd.DataFrame],
        verbose: bool = False,
    ) -> dict:
        """Prepare the forecast in json format"""
        raise NotImplementedError
