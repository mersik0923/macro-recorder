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

while round(time.time()-start_time2,3) <= stopwatch:
    now_time = round(time.time()-start_time2,3)
    
    for recorded_time in list(time_click_down.keys()):
        if recorded_time <= now_time:
            keyboard.press(time_click_down[recorded_time])
            del time_click_down[recorded_time]

    for recorded_time in list(time_click_up.keys()):
        if recorded_time <= now_time:
            keyboard.release(time_click_up[recorded_time])
            del time_click_up[recorded_time]

