import mouse
import keyboard
import time

time_click_down = {} # 딕셔너리 선언
time_click_up = {} # 딕셔너리 선언

start_time = time.time()

def on_key_press(event): # 키 눌렸을 때 함수
    t = round(time.time()-start_time,3)
    if event.event_type == "down": # 키를 누름
        if t not in time_click_down: # t가 딕셔너리 안에 없다면 실행
            time_click_down[t] = [] # values를 리스트로 가짐.
        time_click_down[t].append(event.name) # values 리스트에 키 누적 저장
    if event.event_type == "up": # 키를 뗌
        if t not in time_click_up: # t가 딕셔너리 안에 없다면 실행
            time_click_up[t] = [] # values를 리스트로 가짐.
        time_click_up[t].append(event.name) # values 리스트에 키 누적 저장

keyboard.hook(on_key_press) 
keyboard.wait('esc') # esc 누를 시 함수 대기

stopwatch = round(time.time()-start_time,3) # 녹화 시간 (프로그램 시작~esc 클릭)

start_time2 = round(time.time(),3)


while round(time.time()-start_time2,3) <= stopwatch: # 녹화 시간동안 반복
    now_time = round(time.time()-start_time2,3) # 반복 할 때 마다 현재 시간 변경
    
    for recorded_time in list(time_click_down.keys()): # 키가 눌린 시간 하나씩 꺼내며 반복
        if recorded_time <= now_time: # 정상 or 키가 씹혔을 때 실행
            for button in list(time_click_down[recorded_time]): # 동시 클릭된 키입력을 가진 리스트에서 키 하나씩 가져오기 및 반복
                keyboard.press(button) # 키 누르기
            del time_click_down[recorded_time] # 지나간 시간 지우기

    for recorded_time in list(time_click_up.keys()): # 키가 떼진 시간 하나씩 꺼내며 반복
        if recorded_time <= now_time:
            for button in list(time_click_up[recorded_time]):
                keyboard.release(button)
            del time_click_up[recorded_time]