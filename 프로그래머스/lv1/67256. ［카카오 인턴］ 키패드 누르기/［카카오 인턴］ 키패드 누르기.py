def solution(numbers, hand):
    result = ""
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    left = [3,0]
    right = [3,2]
    for i in range(len(numbers)):
        for j in range(4):
            for k in range(3):
                if numbers[i] == keypad[j][k]:
                    if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
                        result += "L"
                        left = [j,k]
                    elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
                        result += "R"
                        right = [j,k]
                    else:
                        r = abs(right[0]-j)+abs(right[1]-k)
                        l = abs(left[0]-j)+abs(left[1]-k)
                        if r == l:
                            if hand == "right":
                                result += "R"
                                right = [j,k]
                            else:
                                result += "L"
                                left = [j,k]
                        elif r > l:                         
                            result += "L"
                            left = [j,k]
                        else:
                            result += "R"
                            right = [j,k]
    return result