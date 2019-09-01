L = list(map(int, input().split()))
answerList = list(filter(lambda element: element % 2 != 0, L))
num_min = min(answerList) if len(answerList) > 0 else 0
print(num_min)
