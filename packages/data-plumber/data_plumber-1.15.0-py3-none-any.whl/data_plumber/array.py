"""
# data_plumber/array.py

This module defines the `Pipearray`-class, a means to issue `Pipeline`-
executions on identical input data with a single command.
"""

from .pipeline import Pipeline
from .output import PipelineOutput


class Pipearray:
    """
    A `Pipearray` allows for the vectorized execution of multiple
    `Pipeline`s, i.e. all `Pipeline`s are executed on the same input
    data. `Pipearray`s can be used as labeled or anonymous arrays: If at
    least one `Pipeline` is passed to the constructor via keyword
    argument, a labeled `Pipearray` is generated (otherwise it is
    anonymous). A labeled `Pipearray` returns a dictionary of
    `PipelineOutput` (where the keys correspond to the keywords given at
    instantiation or the `Pipeline`'s ids in cases where the keyword has
    been omitted), whereas in the opposite case a list of
    `PipelineOutput`s is returned.

    Example usage:
     >>> from data_plumber import Pipearray, Pipeline
     >>> Pipearray(
             validation_aspect_1=Pipeline(...),
             validation_aspect_2=Pipeline(...)
         )
     <data_plumber.array.Pipearray object at ...>
     >>> Pipearray(
             validation_aspect_1=Pipeline(...),
             validation_aspect_2=Pipeline(...)
         ).run(...)
     <dict[str, PipelineOutput]>
    """
    def __init__(
        self,
        *args: Pipeline,
        **kwargs: Pipeline
    ) -> None:
        if kwargs:  # labeled Pipearray
            self._pipelines: dict[str, Pipeline] | list[Pipeline] = {}
            self._pipelines.update(kwargs)
            self._pipelines.update({p.id: p for p in args})
        else:  # anonymous Pipearray
            self._pipelines = []
            self._pipelines.extend(args)

    def run(
        self,
        **kwargs
    ) -> list[PipelineOutput] | dict[str, PipelineOutput]:
        """
        Trigger `Pipearray` execution.

        Keyword arguments:
        kwargs -- keyword arguments that are passed into `Pipeline`s as
                  keyword arguments
        """

        if isinstance(self._pipelines, dict):
            return {k: p.run(**kwargs) for k, p in self._pipelines.items()}
        return [p.run(**kwargs) for p in self._pipelines]
