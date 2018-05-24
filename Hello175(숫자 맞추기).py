import random
num_selected = int(input("AI의 범위를 정하세요:"))
ai_random = random.randrange(1,num_selected)
try_number = 1
while try_number < 10:
   try_number += 1
   num_player = int(input("AI가 생각하는 수를 추측해보세요:"))
   if ai_random < num_player:
      print("당신은 AI보다 높은수를 생각하고 있습니다.")
   if ai_random > num_player:
      print("당신은 AI보다 낮은수를 생각하고 있습니다.")
   else:
      break;
print("{}번 만에 찾으셧습니다!".format(try_number))
