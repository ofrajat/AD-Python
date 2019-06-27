import pyttsx3
import time
name=input("Please input your name:")
engine = pyttsx3.init()
engine.setProperty('rate',100)

#get time
built_in=[]
sep_time=[]
get_time=[]
time_list=[]
built_in=time.ctime()
sep_time=built_in.split()
get_time=sep_time[3]
time_list=get_time.split(':')
current_hour=time_list[0]

#greeting

if int(current_hour) < 12:
    engine.say('Good Morning' + str(name))
    engine.runAndWait()
    engine.stop()

if 12 < int(current_hour) < 5:
    engine.say('Good Afternoon' + str(name))
    engine.runAndWait()
    engine.stop()

if 5 < int(current_hour) < 20:
    engine.say('Good Evening' + str(name))
    engine.runAndWait()
    engine.stop()


if int(current_hour) > 20:
    engine.say('Good Night' + str(name))
    engine.runAndWait()
    engine.stop()


