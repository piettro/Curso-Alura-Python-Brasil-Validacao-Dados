from datetime import datetime, timedelta
from dates import DateBr

print(datetime.today())

created_date = DateBr()
print(created_date.created_month())
print(created_date.week_day())
print(created_date)