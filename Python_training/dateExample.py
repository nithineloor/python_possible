from datetime import datetime, timedelta

now = datetime.now()
print('all contents inside variable now')
print(now)
current_time = now.time # to take and display current time from  variable "now"
print(current_time)
updated_time = datetime.now() - timedelta(hours=10,minutes=30) 

up_time=updated_time.time()

print("Current Time =", up_time )