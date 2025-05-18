import time

print("Start time:", time.time())
cal_time = time.time() * 600
print("End time:", cal_time)

print("Time left:", (cal_time - time.time()) / 600, "minutes")
