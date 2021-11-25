"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730398410"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Initialize constructor."""
        self.values = values

    def __repr__(self) -> str:
        """Rep method."""
        return f"Simpy({self.values})"

    def fill(self, fill_val: float, amount: int) -> None:
        """Fill method."""
        results: list[float] = []
        for i in range(amount):
            results.append(fill_val)
        self.values = results
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """The arrange method."""
        results: list[float] = []
        assert step != 0
        while start < stop:
            results.append(start)
            start += step
        if stop < start:
            results.append(start)
            start += step
        self.values = results

    def sum(self) -> float:
        """The sum method."""
        self.values = sum(self.values)
        return self.values

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The adding method."""
        results: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                results.append(self.values[i] + rhs.values[i])
        else:
            for item in self.values:
                results.append(item + rhs)
        return Simpy(results)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The power method."""
        results: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                results.append(self.values[i] ** rhs.values[i])
        else:
            for item in self.values:
                results.append(item ** rhs)
        return Simpy(results)

    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The mod method."""
        results: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                results.append(self.values[i] % rhs.values[i])
        else:
            for item in self.values:
                results.append(item % rhs)
        return Simpy(results)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """The equality method."""
        results: list[float] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] == rhs.values[i]:
                    results.append(True)
                else:
                    results.append(False)
        else:
            for item in self.values:
                if item == rhs:
                    results.append(True)
                else:
                    results.append(False)
        return Simpy(results)

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """The greater than method."""
        results: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                if self.values[i] > rhs.values[i]:
                    results.append(True)
                else:
                    results.append(False)
        else:
            for item in self.values:
                if item > rhs:
                    results.append(True)
                else:
                    results.append(False)
        return Simpy(results)

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """The getitem method."""
        results: list[float] = []
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            for i in range(len(self.values)):
                if rhs.values[i] is True:
                    results.append(self.values[i])
        return Simpy(results)
