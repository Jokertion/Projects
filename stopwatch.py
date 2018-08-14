# ! python3
# stopwatch.py
# 秒表程序--计圈计时功能
import time

input()
print('计时开始.')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('圈数 # %s: 总时:【%s】\t圈时:【%s】'
              % (lap_num, total_time, lap_time))
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('\nDone.')
