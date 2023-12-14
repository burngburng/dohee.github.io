#3. 숫자 맞추기 게임 _ 사용자버전 -> 이미 나왔던 수 못나오게 하면 정확도 더 높아짐! 

import random

secret_num = input("숫자를 입력하세요.")
secret_num = int(secret_num)

select_num = random.randint(1,100)

count = 0 
list1 = [] # 최솟값 리스트
list2 = [] # 최댓값 리스트 

def comparision (num1, count, list1, list2) :
    count += 1
    
    if secret_num == num1 :
        print("축하합니다!", count, "번째에 맞췄습니다.")
        return
    
    elif secret_num < num1 : 
        list1.append(num1)
        print("더 작은 수를 입력하세요.")
        if count == 1 : 
            num1 = random.randint(1, num1)
        else : 
            num1 = random.randint(list2[-1], num1)
        comparision(num1, count, list1, list2)
    
    elif secret_num > num1 : 
        list2.append(num1)
        print("더 큰 수를 입력하세요.")
        if count == 1 : 
            num1 = random.randint(num1, 100)
        else : 
            num1 = random.randint(num1, list1[-1])
        comparision(num1, count, list1, list2) 
    
    else :
        print("종료합니다.")       
        

comparision(select_num, count, list1, list2) 

