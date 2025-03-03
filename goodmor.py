import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour =int(time.strftime('%H'))


if(hour<12):
    print("Good Morning")
elif(hour>12):
    print("good Afternoon")
else:
    print("Good Evening")
