# 문자열을 구현하여 입력받습니다.
string = input()

# 정수를 입력받습니다.
a = int(input())

# 문자열의 길이를 구합니다.
# cnt : 지금까지 출력한 문자의 개수
leng = len(string)
cnt = 0

# 문자열의 맨 뒤에서부터 주어진 개수만큼 출력합니다.
for i in range(leng - 1, -1, -1):
	# 주어진 개수만큼 출력했을 경우 for문을 나갑니다.
	if cnt >= a:
		break
	print(string[i], end="")
	cnt += 1