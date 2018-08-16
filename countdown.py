#! python3
# countdown.py
# 倒计时提醒程序
import time
import subprocess

time_left = 5
while time_left > 0:
    print('Time left:%ds' % time_left)
    time.sleep(1)
    time_left -= 1

subprocess.Popen(['start', 'alarm.wav'], shell=True)
