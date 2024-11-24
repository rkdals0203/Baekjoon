#정확성 100점, 효율성 0점인 코드
def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    original_len = len(food_times)
    food_times.insert(0,-1)
    answer = 0
    eaten = 0
    eatens = []
    
    i = 1
    end_count = 0
    while True:
        #다음 번째 아이템 추가
        food_times.append(food_times[i]-1)
        
        #해당 아이템이 먹을 수 있으면 먹은 회수 증가
        if food_times[i] > 0:
            eaten += 1
        
        if not eaten in eatens:
            eatens = []
        eatens.append(eaten)
    
   
        #먹은 횟수가 한 싸이클 이상 변하지 않으면 -1 리턴
        if len(eatens) > original_len:
            return -1
            
        #먹은 횟수가 k보다 커지면 해당 인덱스 저장
        if eaten > k:
            answer = i
            break
        #i 증가
        i += 1
    
    if answer % (original_len) == 0:
        answer = (original_len)
    else:
        answer = answer % (original_len)

    return answer
