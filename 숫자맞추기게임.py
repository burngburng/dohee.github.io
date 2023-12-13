#숫자 맞추기 게임 (재귀함수 쓸거면 반복문 쓸 필요 없음.)

import random

secret_number = random.randint(1,100)
count = 0

def question() : 
    sel_number = input("1부터 100까지의 숫자를 입력하세요. ")
    sel_number = int(sel_number)
    return sel_number


def comparision(num1, count) : 
    
        count +=1 
    
        if secret_number == num1 :  
            print("축하합니다!", count, "번째에 숫자를 맞추었습니다.")
        
        elif secret_number < num1 :            
            print("더 작은 수를 입력하세요.")
            result = question()
            comparision(result, count)
            
        elif secret_number > num1 : 
            print("더 큰 수를 입력하세요. ")
            result = question()
            comparision(result, count)
            
        else : 
            print("종료합니다.")

            

comparision(question(), count)

