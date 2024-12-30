array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    #종료조건: 배열크기가 1일 때
    if start == end:
        return

    #피봇은 첫번째 원소
    pivot = start
    left = start+1
    right = end
    
    #왼쪽이 오른쪽보다 작아질 때까지
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