import datetime
birthdate = datetime.date(2002, 3, 31)
current_date = datetime.date.today()
days_alive = (current_date - birthdate).days
print(f"Youve been alive for {days_alive} days")