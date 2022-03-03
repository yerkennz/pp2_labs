from datetime import date, timedelta
print("Today:", date.today())
print("Tomorrow:", date.today() + timedelta(1))
print("Yesterday:", date.today() - timedelta(1))