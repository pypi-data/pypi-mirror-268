"""Models for the UTE Wrapper."""

from typing import TypedDict


class EnergyEntry(TypedDict):
    """Energy entry dict."""

    kwh: float
    aproximated_cost_in_uyu: float
    day_in_week: str


class TotalEntry(TypedDict, total=False):
    """Total entry dict."""

    sum_in_kwh: float
    aproximated_cost_in_uyu: float
    daily_average_cost: float


class ActiveEnergy(TypedDict, total=False):
    """Active energy dict."""

    total: TotalEntry
    dates: dict[str, EnergyEntry]
