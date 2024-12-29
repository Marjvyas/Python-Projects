import time,datetime
target_time=input("Enter your target time(dd/mm/yyyy HH:MM:SS):")
d1,t1=[x for x in target_time.split(' ')]
now=datetime.datetime.now()
new=now.strftime("%d/%m/%y %H:%M:%S")
d2,t2=[x for x in new.split(' ')]
new_target=time.strptime(target_time,"%d/%m/%Y %H:%M:%S")
if d1==d2:
    if t1==t2:
        print("Your targeted time is the recent time...")
    elif t1>t2:
        print("The targeted time not come yet..")
    else:
        print("You crossed the targeted time...")
elif d1>d2:
    print("The targeted time not come yet..")
else:
    print("You crossed the targeted time...")
