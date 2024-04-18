"""
Model base specification module.
"""
from __future__ import annotations

from digitalhub_core.entities._base.spec import Spec, SpecParams


class ModelSpec(Spec):
    """
    Model specifications.
    """

    def __init__(self, **kwargs) -> None:
        """
        Constructor.
        """

        self._any_setter(**kwargs)


class ModelParams(SpecParams):
    """
    Model parameters.
    """


class ModelSpecModel(ModelSpec):
    """
    Model specifications.
    """


class ModelSpecParams(ModelParams):
    """
    Model parameters.
    """
