import time
from playsound import playsound 
from datetime import datetime
alarmtime= "16:16"
while True:
    localTime=datetime.now().strftime('%H:%M')
    if localTime == alarmtime:
        print("working")
        playsound("sound_alarm.mp3")
        break
    else:
        print("not yet")
        time.sleep(10)

