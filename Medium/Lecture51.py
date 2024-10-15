import datetime


# Getting both date and time
current_time=datetime.datetime.now()
print(current_time)

# Current date only

current_date=datetime.datetime.today()
print(current_date)

# Get time only

time_only=datetime.datetime.now()
time_only=time_only.strftime("%H : %M : %S")
print(time_only)

# Set date
new_date=datetime.date(2024,1,6)
print(new_date)



# Entering specific date and time

target_date=datetime.datetime(2025,1,26,12,59,10)
print(target_date)

if target_date<current_time:
    print("Date has already passed")
else:
    print("Date not passed yet")