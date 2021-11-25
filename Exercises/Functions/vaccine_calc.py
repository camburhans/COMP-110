"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730398410"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    _days: int = int(days_to_target(population, doses, doses_per_day, target))
    _date: str = str(future_date(_days))
    print("We will reach " + str(target) + "% vaccination in " + str(_days) + " days, which falls on " + _date + ".")


def days_to_target(pop: int, dose: int, dpd: int, target: int) -> int:
    """Determining days until target % is reached."""
    ppl: float = float(dose / 2)
    pct: float = float((ppl / pop) * 100)
    pct_left: float = float((target - pct) / 100)
    ppl_left: float = float(pct_left * pop)
    doses_needed: float = float(ppl_left * 2)
    days_left: int = int(round(doses_needed / dpd))
    return days_left


def future_date(days: int) -> str:
    """Determining the date that the target wil be reached."""
    today: datetime = datetime.today()
    tgt_d8: timedelta = timedelta(days) + today
    tgt_day: str = str(tgt_d8.strftime("%B %d, %Y"))
    return tgt_day


if __name__ == "__main__":
    main()
