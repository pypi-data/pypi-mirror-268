"""Forcing related functionality for HBV, see `eWaterCyle documentation <https://ewatercycle.readthedocs.io/en/latest/autoapi/ewatercycle/base/forcing/index.html>`_ for more detail."""
# Based on https://github.com/eWaterCycle/ewatercycle-marrmot/blob/main/src/ewatercycle_marrmot/forcing.py

from ewatercycle.base.forcing import DefaultForcing

class LorenzForcing(DefaultForcing):
    """Container for Lorenz forcing data.

    Args:


    Examples:

        From existing forcing data:

        .. code-block:: python

            from ewatercycle.forcing import sources

            forcing = sources.LorenzForcing(
                directory='/home/davidhaasnoot/Code/Forcing/',
                start_time=0.0,
                end_time=20.0,
                F=8,
                dt=1e-3
            )

        Inherited from base forcing:
            shape: Path to a shape file. Used for spatial selection: can be None
            directory: Directory where forcing data files are stored.
            start_time: Start time of forcing in UTC and ISO format string e.g 'YYYY-MM-DDTHH:MM:SSZ'.
            end_time: End time of forcing in UTC and ISO format string e.g. 'YYYY-MM-DDTHH:MM:SSZ'.

    """

    # either a forcing file is supplied
    F: float = 8
    dt: float = 1e-3

