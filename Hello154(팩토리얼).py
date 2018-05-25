import time
user_num = int(input("정수를 입력하세요:"))
start1_time = time.time()
fact1 = 1
for i in range(1,user_num+1):
   fact1 = fact1 * i
print("첫번째 것은 for문으로 구한 팩토리얼입니다.")
print("fact ={}".format(fact1))
print("{}초 걸렸습니다.".format(time.time() - start1_time))

user_range = int(input("몇까지 곱할지 정수를 입력하세요:"))
start2_time = time.time()
fact2 = 1
i = 1
while i <= user_range:
   fact2 = fact2 * i
   i += 1
print("두번째 것은 while문으로 구한 팩토리얼입니다.")
print("fact ={}".format(fact2))
print("{}초 걸렸습니다.".format(time.time() - start2_time))
