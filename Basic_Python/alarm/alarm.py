
import time,datetime,pygame

pygame.mixer.init()
pygame.mixer.music.load("alarmsong.mp3")

# Get alarm time from user
alarm_time_str=input("Enter alarm time(HH:MM:SS):")
alarm_time=time.strptime(alarm_time_str,'%H:%M:%S')

while True:
    x1 = datetime.datetime.now()
    x_str=x1.strftime('%H:%M:%S')
    x=time.strptime(x_str,'%H:%M:%S')

    if alarm_time<x:
        print("Invalid alarm time...")
        break
    if x_str == alarm_time_str:
        print("wake up!")
        pygame.mixer.music.play(loops=-1)
        # while pygame.mixer.music.get_busy():
        #     time.sleep(1)
        input("Press enter to stop:")
        break
    print(x_str)
    time.sleep(1)  # Check every second



