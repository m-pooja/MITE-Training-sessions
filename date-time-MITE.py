d1 = "10/24/2017"
d2 = "11/24/2016"
max(d1,d2)
d1 - d2

import datetime
d1 = datetime.date(2016,11,24)
d2 = datetime.date(2017,10,24)
max(d1,d2)
print(d2 - d1)
import datetime
century_start = datetime.date(2000,1,1)
today = datetime.date.today()
print(century_start,today)
print("We are",today-century_start,"days into this century")
