import random
rsp_random = ["가위","바위","보"]
ai_random = random.choice(rsp_random)
rsp_user = str(input("가위,바위,보 중에서 하나 고르세요."))
user = 0
while user < 10:
   if ai_random == "가위":
      if rsp_user == "가위":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("비겼습니다")
         user += 1
      elif rsp_user == "바위":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("이겼습니다")
         break
      elif rsp_user == "보":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("졌습니다.")
         user += 1
   elif ai_random == "바위":
      if rsp_user == "가위":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("졌습니다.")
         user += 1
      elif rsp_user == "바위":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("비겼습니다.")
         user += 1
      elif rsp_user == "보":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("이겼습니다.")
         break
   elif ai_random == "보":
      if rsp_user == "가위":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("이겼습니다.")
         break
      elif rsp_user == "바위":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("졌습니다.")
         user += 1
      elif rsp_user == "보":
         print("AI는 {}을 냈으므로,".format(ai_random))
         print("비겼습니다.")
         user += 1
   rsp_user = str(input("가위,바위,보 중에서 하나 고르세요."))
   ai_random = random.choice(rsp_random)
