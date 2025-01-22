array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  if len(array)<=1:
    return array
  
  pivot = array[0]
  tail = array[1:]
  left_side = [i for i in tail if i<= pivot]
  right_side = [j for j in tail if j> pivot]
  
  return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))


#2
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    # 종료 조건: 배열 크기가 1 이하일 때
    if start >= end:
        return

    # 피봇은 첫 번째 원소
    pivot = start
    left = start + 1
    right = end

    # 왼쪽과 오른쪽이 엇갈릴 때까지 반복
    while True:
        # 왼쪽 포인터 이동 (피봇보다 큰 값 찾기)
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 오른쪽 포인터 이동 (피봇보다 작은 값 찾기)
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸을 경우
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
            break
        # 엇갈리지 않았을 경우
        else:
            array[right], array[left] = array[left], array[right]

    # 피봇을 기준으로 왼쪽과 오른쪽 부분 배열을 재귀적으로 정렬
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# 정렬 실행
quick_sort(array, 0, len(array) - 1)
print(array)

#3
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    #종료조건: 배열크기가 1일 때
    if start == end:
        return

    #피봇은 첫번째 원소
    pivot = start
    left = start+1
    right = end
    
    #교차할때까지
    while left <= right:
        #왼쪽은 피봇보다 커질때까지 증가
        while array[left] < array[pivot]:
            left+=1
        #오른쪽은 피봇보다 작아질때까지 감소
        while array[right] > array[pivot]:
            right-=1
        #엇갈릴 경우 작은 데이터인 오른쪽과 피봇 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        #엇갈리지 않았을 경우 작은 데이터와 큰 데이터 교체
        else: 
            array[right], array[left] = array[left], array[right]
    
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
        
        


quick_sort(array,0,len(array)-1)

#4
array =  
        #[2(pivot),4,1,3,6,7,5,8(right),9(left),10]
        
        #[2(pivot),4(left),1(right),3,6,7,5,8,9,10]
        #[2(pivot),1(left),4(right),3,6,7,5,8,9,10]

def quick_sort(array, start, end):
    #종료 조건: 배열 크기가 1이하일때
    if start >= end:
        return
    
    #변수 초기화
    pivot = start
    left = start + 1
    right = end
    
    #엇갈리기 전까지
    while left <= right:
        #왼쪽 숫자가 피봇보다 작은 동안은 계속 증가
        while left <= end and array[pivot] > array[left]:
            left += 1
        #오른쪽 숫자가 피봇보다 큰 동안은 계속 감소
        while right >= start and array[pivot] < array[right]:
            right -= 1
        #엇갈렸다면 오른쪽과 피봇을 교체하고 끝
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
            break
        #엇갈리지 않았다면 왼쪽과 오른쪽 바꾸기만
        else:
            array[left], array[right] = array[right], array[left]
    #바뀐 피봇을 기준으로 왼쪽과 오른쪽 부분 배열을 재귀적으로 정렬
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array,0,len(array)-1)
print(array)