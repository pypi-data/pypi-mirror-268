from __future__ import annotations

import warnings

from typing import Any, Optional

import jijmodeling as jm

from jijzept.response.base import BaseResponse


class JijModelingResponse(BaseResponse):
    """Return object from JijZept."""

    def __init__(self, sample_set: Optional[jm.SampleSet] = None):
        if sample_set is None:
            self._sample_set = jm.SampleSet(
                record=jm.Record({"x": []}, [0]),
                evaluation=jm.Evaluation([]),
                measuring_time=jm.MeasuringTime(),
            )
        else:
            self._sample_set = sample_set
        super().__init__()

    @classmethod
    def from_json_obj(cls, json_obj) -> Any:
        """Generate object from JSON object.

        Args:
            json_obj (str): JSON object

        Returns:
            Any: object
        """
        return cls(jm.SampleSet.from_json(json_obj["sample_set"]))

    @classmethod
    def empty_data(cls) -> Any:
        """Create an empty object.

        Returns:
            Any: Empty object.
        """
        return cls()

    def set_variable_labels(self, var_labels: dict[int, str]):
        """Set variable labels.

        Args:
            var_labels (dict[int, str]): Dictionary of variable labels.
        """
        self._variable_labels = var_labels

    @property
    def variable_labels(self) -> dict[int, str]:
        """Return variable labels.

        Returns:
            dict[int, str]: Dictionary of variable labels.
        """
        return self._variable_labels

    def get_sampleset(self) -> jm.experimental.SampleSet:
        """
        Return a row oriented SampleSet object.

        Returns:
            jm.experimental.SampleSet: A row oriented SampleSet object.
        """
        return jm.experimental.from_old_sampleset(self._sample_set)
