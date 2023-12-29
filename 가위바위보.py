# 가위 바위 보 

import random
from random import choice

r_s_p = ['가위', '바위', '보']

a = input("가위바위보 중 하나를 입력하세요.")

x = random.choice(r_s_p)

if x == "가위" : 
    if a == "바위" :
        print(x, "vs", a , "=", "당신은 이겼습니다.")
    elif a == "가위" :
        print(x, "vs", a , "=", "비겼습니다.")
    elif a == "보" : 
        print(x, "vs", a , "=", "당신은 졌습니다.")

elif x == "바위" :
    if a == "바위" :
        print(x, "vs", a , "=", "비겼습니다.")
    elif a == "가위" :
        print(x, "vs", a , "=", "당신은 졌습니다.")
    elif a == "보" : 
        print(x, "vs", a , "=", "당신은 이겼습니다.")
        
elif x == "보" : 
    if a == "바위" :
        print(x, "vs", a , "=", "당신은 졌습니다.")
    elif a == "가위" :
        print(x, "vs", a , "=", "당신은 이겼습니다.")
    elif a == "보" : 
        print(x, "vs", a , "=", "비겼습니다.")
    
