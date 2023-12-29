# 비밀번호 생성기  

import random
import string

a = input("비밀번호에 들어갈 숫자를 띄어쓰기로 구분하여 입력하시오.")

a_list = []

password = []

a_list.extend(a.split())

b = input("위의 숫자를 포함한 원하는 비밀번호의 길이를 입력하시오.")
b = int(b)

password.extend(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(b-len(a_list)) )

for a in a_list : 
    i = random.randint(0, b-1)
    password.insert(i,a)

print(''.join(password))


# 배울점 
#for _ in range(5) :
#    print(random.choice(string.ascii_uppercase + string.digits) ) 
    
