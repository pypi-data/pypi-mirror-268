import os
import shutil
import yaml

from typing import Optional, Union, List

from cbcflow.core.database import LocalLibraryDatabase
from cbcflow.core.utils import get_uid_index_for_object_array


class Aggregator:
    def __init__(self, path_to_recipe: Optional[str] = None) -> None:
        """Load configuration information from recipe.yml

        Parameters
        ==========
        path_to_recipe : Optional[str]
            The path to the recipe.yml file; if not passed assumes it can be found in the current working directory
        """
        if path_to_recipe is None:
            path_to_recipe = "recipe.yml"
        with open(path_to_recipe, "r") as f:
            recipe_contents = yaml.safe_load(f)
        self.output_directory = recipe_contents["general"]["output_directory"]
        self.cbcflow_library = recipe_contents["general"]["cbcflow_library"]
        self.cbcflow_library.load_library_metadata_dict()
        self.guaranteed_far_threshold = recipe_contents["parameter_estimation"][
            "guaranteed_far_threshold"
        ]
        self.best_effort_superevents = recipe_contents["parameter_estimation"][
            "best_effort_superevents"
        ]
        self._get_parameter_estimation_catalog_event_list()

    def _get_parameter_estimation_catalog_event_list(self):
        """Gets the events in the parameter estimation catalog, from those that past the guaranteed the far threshold
        plus those set as best effort events
        """
        self.parameter_estimation_catalog_event_list = list()
        for superevent, metadata in self.cbcflow_library.metadata_dict.items():
            # Read this off of the first event for now
            # In the future add field to schema to save value from the gwtc_get() table?
            superevent_far = float(metadata["GraceDB"]["Events"][0]["FAR"])
            if superevent_far <= self.guaranteed_far_threshold:
                self.parameter_estimation_catalog_event_list.append(superevent)
        self.parameter_estimation_catalog_event_list += self.best_effort_superevents

    @property
    def cbcflow_library(self) -> LocalLibraryDatabase:
        """The cbcflow library used to build the catalog product"""
        return self._cbcflow_library

    @cbcflow_library.setter
    def cbcflow_library(self, library: Union[str, LocalLibraryDatabase]):
        if isinstance(library, LocalLibraryDatabase):
            self._cbcflow_library = library
        elif isinstance(library, str):
            self._cbcflow_library = LocalLibraryDatabase(library)

    @property
    def best_effort_superevents(self) -> List[str]:
        return self._best_effort_superevents

    @best_effort_superevents.setter
    def best_effort_superevents(self, config_value: Union[None, List]) -> None:
        if config_value is None:
            self._best_effort_superevents = []
        else:
            self.best_effort_superevents = config_value

    @property
    def guaranteed_far_threshold(self) -> float:
        return self._guaranteed_far_threshold

    @guaranteed_far_threshold.setter
    def guaranteed_far_threshold(self, threshold) -> None:
        self._guaranteed_far_threshold = float(threshold)

    def fetch_illustrative_parameter_estimation_results(self):
        """Copies pesummary result .hdf5's for the illustrative result from each event in the pe catalog list"""
        for superevent in self.parameter_estimation_catalog_event_list:
            illustrative_result_id = self.cbcflow_library.metadata_dict[superevent][
                "ParameterEstimation"
            ]["IllustrativeResult"]
            # Should be pesummary results in the future! But that's not accessible presently with ROTA results (should just be an addition to the monitor?)
            # So save bilby result file instead for now
            results = self.cbcflow_library.metadata_dict[superevent][
                "ParameterEstimation"
            ]["Results"]
            try:
                illustrative_result_index = get_uid_index_for_object_array(
                    illustrative_result_id, results
                )
            except ValueError:
                print(
                    f"For superevent {superevent} IllustrativeResult mixes upper and lower case, but the UID is uppercase"
                )
                # temporary fix for some IllustrativeResult being e.g. 'Exp2' when the UID is 'EXP2'
                illustrative_result_index = get_uid_index_for_object_array(
                    illustrative_result_id.upper(), results
                )
            # We're assuming that both we and the result are on CIT
            try:
                illustrative_result_path = results[illustrative_result_index][
                    "ResultFile"
                ]["Path"].replace("CIT:", "")
            except KeyError:
                print(
                    f"For superevent {superevent} couldn't find preferred ResultFile, defaulting to online result"
                )
                # Some ROTA uploads are broken, in the meantime do this
                illustrative_result_index = get_uid_index_for_object_array(
                    "online", results
                )
                illustrative_result_path = results[illustrative_result_index][
                    "ResultFile"
                ]["Path"].replace("CIT:", "")

            shutil.copy(
                illustrative_result_path,
                os.path.join(self.output_directory, f"{superevent}-result.hdf5"),
            )


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("recipe", type=str, help="The recipe for data aggregation")
    args = parser.parse_args()

    aggregator = Aggregator(path_to_recipe=args.recipe)
    aggregator.fetch_illustrative_parameter_estimation_results()
