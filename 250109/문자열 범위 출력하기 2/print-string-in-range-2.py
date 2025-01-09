given_str = input()
N = int(input())

if N <= 0:
    print(given_str)  # 음수나 0인 경우 전체 문자열 출력
elif N > len(given_str):
    print(given_str)  # N이 문자열 길이보다 큰 경우 전체 문자열 출력
else:
    print(given_str[-N:][::-1])  # 슬라이싱을 사용한 더 간단한 구현