given_str = input().strip()
ee_count = 0
eb_count = 0

# 겹치는 경우를 포함해서 세기 위해 인덱스를 한 칸씩 이동하며 확인
for i in range(len(given_str)-1):
    if given_str[i:i+2] == 'ee':
        ee_count += 1
    if given_str[i:i+2] == 'eb':
        eb_count += 1

print(ee_count, eb_count)