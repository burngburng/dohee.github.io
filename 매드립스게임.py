#1. 매드립스게임

sentense1 = "I shoudn't {} you, but i {} you."
sentense2 = "I just can't {}"
sentense3 = "I shoudn't {} you, but i can't {}. i can't {}"

s1 = input("동사(영어) : ")
s2 = input("동사(영어) : ")
s3 = input("동사(영어) : ")
s4 = input("동사(영어) : ")
s5 = input("동사(영어) : ")
s6 = input("동사(영어) : ")

sentense1 = sentense1.format(s1,s2)
sentense2 = sentense2.format(s3)
sentense3 = sentense3.format(s4, s5, s6)

print(sentense1)
print(sentense2)
print(sentense3)



