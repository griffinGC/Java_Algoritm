# 블루레이의 순서가 바뀌면 안됨...
# i번과 j사이의 모든 레슨도 같은 블루 레이에 녹화 해야함
# m개의 블루레이에 모든 기타 레슨 동영상 녹화
# m개의 블루레이는 모두 같은 크기
# 블루레이의 크기 중 최소를 구하는 프로그램
n, m = map(int, input().split())
blueray = list(map(int, input().split()))
# 블루레이의 크기를 찾는 것이 문제
# 최소 m개를 만족 시켜야 하니까
# m의 갯수가 블루레이의 갯수를 뜻함
# 블루레이의 갯수를 카운터 하는데, 
# 그 갯수가 m을 초과한다면 => 크기가 작다는 것이므로 => 블루레이 한장의 크기를 늘려줘야 함
# 그 갯수가 m보다 작다면 => 크기가 크다는 것이므로 => 블루레이의 한장의 크기를 줄여줘야 함
# 예를 들어 블루레이 한장의 크기가 10이라면, 크기를 초과하기 전까지 블루레이에 넣어줌
# 만약 크기를 초과한다면 거기서부터 다시 0으로 초기화 하고 넣어줘야함

# 왼쪽, 오른쪽 
# => 왼쪽은 가장 작은 경우 => 영상 하나의 크기를 쪼갤 수 없기때문에 => 영상들이 무조건 하나씩은 들어가야 하므로 영상중 가장 큰 크기를 최소 블루레이 크기로 정함
# => 오른쪽은 가장 큰 경우 => 블루레이 갯수를 1개만 사용하는 경우 => 모두 넣는 경우 => 모든 영상을 한장에 넣는 것이므로 => 한장에 넣을 수 있는 크기
left = max(blueray)
right = sum(blueray)

while left <= right:
    # 합을 저장하기 위한 temp
    temp = 0
    # 블루레이의 갯수를 다시 0부터 카운트 하는 변수
    cnt = 0
    # 중간 값
    mid = (left + right) // 2
    for vol in blueray:
        if temp + vol > mid:
            temp = 0
            cnt += 1
        temp += vol
    # temp에는 값이 계속 남아있다는 것은 블루레이 디스크를 추가로 필요하다는 것 의미
    if temp != 0:
        cnt += 1
    # m보다 카운트한 갯수가 작다는 것은 블루레이 한장의 크기가 너무 크다는 것 의미 => 크기를 줄여야 함 => max인 right 변경
    # if cnt <= m:
        # right = mid - 1
        # left 출력 
        # => m과 동일할경우에 right는 mid - 1이니까 right말고 left 출력
        # cnt는 m보다 큰 경우는 원하는 것보다 블루레이의 갯수가 많이 생성된 것을 뜻함 => 볼륨이 너무 작다는 것을 의미, 하지만 left > right보다 커지는 순간이 오면 그게 이제 만들 수 있는 볼륨중 최소 값
    if cnt > m:
        left = mid + 1
        print("cnt", cnt, "left", left)
    # m보다 카운트한 갯수가 크다는 것은 블루레이 한장의 크기가 너무 작다는 것 의미 => 크기를 늘려야 함 => min인 left 변경
    else:
        # left = mid + 1
        right = mid - 1
print(left)





