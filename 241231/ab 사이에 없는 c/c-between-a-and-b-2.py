# 변수 선언 및 입력
inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])
satisfied = True

for i in range(a, b + 1):
	# a에서 b사이의 값 중 c의 배수가 있는지 확인합니다.
	if i % c == 0:
		satisfied = False


# 출력
if satisfied == True:
	print("YES")
else:
	print("NO")