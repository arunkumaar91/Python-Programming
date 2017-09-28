import webbrowser
import time

totalBreak = 3
breakCount = 0

print("Program Start time is: " +time.ctime())
while(breakCount<totalBreak):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=JGwWNGJdvx8")
    breakCount = breakCount + 1;
