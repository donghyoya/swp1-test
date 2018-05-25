original = str(input("문자열을 입력하시오:"))
vowels = "aeiouAEIOU"
result = ""
for letter in original:
   if letter not in vowels:
      result += letter
print("모음(소문자,대문자)를 제외한 문자를 출력:{}".format(result))

word = original.lower() #.lower()은 소문자로 변화한다
vowels2 = 0
consonants = 0
if len(original) > 0 and original.isalpha(): #문자가 하나라도 있고 알파벳이면
   for char in word:
      if char in "aeiou": #자음갯수
         vowels2 += 1
      else:               #모음갯수
         consonants += 1
print("자음의 갯수:{}".format(vowels2))
print("모음의 갯수:{}".format(consonants)) #왜 띄어쓰기 하면 안되나?
