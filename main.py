s = input()
compressed = []

for slice_index in range(1, len(s) + 1):
    sliced = [s[j:j + slice_index] for j in range(0, len(s), slice_index)]  # 슬라이스 된 문자열
    result = []
    index = 1

    for k in range(1, len(sliced)):
        if sliced[k - 1] == sliced[k]:
            index += 1
        else:
            if index > 1:
                result.append(str(index) + sliced[k - 1])
            else:
                result.append(sliced[k - 1])
            index = 1

    # 마지막 남은 패턴 추가
    if index > 1:
        result.append(str(index) + sliced[-1])
    else:
        result.append(sliced[-1])

    compressed.append("".join(result))

print(compressed)