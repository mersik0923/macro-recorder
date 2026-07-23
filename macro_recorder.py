import mouse
import keyboard
import time

time_click_down = [] # 리스트 선언
time_click_up = [] # 리스트 선언

start_time = time.time()

def on_key_press(event): # 키 눌렸을 때 함수
    if event.event_type == "down": # 키를 누름
        time_click_down[round(time.time()-start_time,3)] = event.name
    if event.event_type == "up": # 키를 뗌
        time_click_up[round(time.time()-start_time,3)] = event.name

keyboard.hook(on_key_press) 
keyboard.wait('esc') # esc 누를 시 함수 대기

stopwatch = round(time.time()-start_time,3) # 녹화 시간 (프로그램 시작~esc 클릭)

start_time2 = round(time.time(),3)

while round(time.time()-start_time2,3) <= stopwatch: # 녹화 시간동안 반복
    now_time = round(time.time()-start_time2,3) # 반복 할 때 마다 현재 시간 변경
    
    for recorded_time in list(time_click_down.keys()):
        if recorded_time <= now_time:
            keyboard.press(time_click_down[recorded_time])
            del time_click_down[recorded_time]

    for recorded_time in list(time_click_up.keys()):
        if recorded_time <= now_time:
            keyboard.release(time_click_up[recorded_time])
            del time_click_up[recorded_time]

