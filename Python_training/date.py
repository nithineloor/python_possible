from datetime import datetime, timedelta
x = int(input())
now = datetime.now()
print(now)

updated_time = datetime.now() + timedelta(days=x)

print('In',x,'days the date wil be',updated_time)