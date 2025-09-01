# 여러 개의 숫자를 입력받아 합계를 계산하는 함수를 작성
# 사용자가 'q'를 입력하면 입력을 중단하고 지금까지 입력한 숫자의 합을 출력

sum = 0

while True:
    x = input("숫자를 입력하세요 (끝내려면 q): ")
    if x == "q":
        break
    sum += int(x)

print("합계:", sum)
