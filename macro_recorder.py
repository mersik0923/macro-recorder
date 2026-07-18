import mouse
import keyboard
import time

time_click_down = {} # 예시
time_click_up = {} # 예시

start_time = time.time()

def on_key_press(event):
    if event.event_type == "down":
        time_click_down[round(time.time()-start_time,3)] = event.name
    if event.event_type == "up":
        time_click_up[round(time.time()-start_time,3)] = event.name

keyboard.hook(on_key_press)
keyboard.wait('esc')

stopwatch = round(time.time()-start_time,3)

start_time2 = round(time.time(),3)

while round(time.time()-start_time2,3) != stopwatch:
    if round(time.time()-start_time2,3) in time_click_down:
        keyboard.press(time_click_down[round(time.time()-start_time2,3)])