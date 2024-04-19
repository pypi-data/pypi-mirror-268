from abc import ABC, abstractmethod
import numpy as np
from typing import Iterable


class Feature(ABC):
    @abstractmethod
    def __init__(
        self, settings: dict, ch_names: Iterable[str], sfreq: int | float
    ) -> None:
        pass

    @staticmethod
    @abstractmethod
    def test_settings(
        settings: dict,
        ch_names: Iterable[str],
        sfreq: int | float,
    ):
        """Method to check passed settings"""
        pass

    @abstractmethod
    def calc_feature(self, data: np.array, features_compute: dict) -> dict:
        """
        Feature calculation method. Each method needs to loop through all channels

        Parameters
        ----------
        data : np.array
            (channels, time)
        features_compute : dict
        ch_names : Iterable[str]

        Returns
        -------
        dict
        """
        pass
