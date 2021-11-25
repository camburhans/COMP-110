"""A vaccination calculator."""


# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
pop: int = int(input("Population: "))
doses_admin: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
tgt_pct: int = int(input("Target %: "))

# Math stuff here
ppl_vac: float = float(doses_admin / 2)
pct_vac1: float = float(ppl_vac / pop)
pct_vac2: float = float(pct_vac1 * 100)
pct_left1: float = float(tgt_pct - pct_vac2)
pct_left2: float = float(pct_left1 / 100)
ppl_in_need: float = float(pct_left2 * pop)
doses_needed: float = float(ppl_in_need * 2)
days_left: int = int(round(doses_needed / doses_per_day))

# Date stuff here
today: datetime = datetime.today()
tgt_d8: timedelta = timedelta(days_left) + today
tgt_day: str = tgt_d8.strftime("%B %d, %Y")

tgt_pct2: str = str(tgt_pct)
days_left2: str = str(days_left)
tgt_day2: str = str(tgt_day)
print("We will reach " + tgt_pct2 + "% vaccination in " + days_left2 + " days, which falls on " + tgt_day2 + ".")
