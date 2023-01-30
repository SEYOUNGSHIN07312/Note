scores = [('eng', 88), ('sci', 90), ('math', 80)]

def check(x):
    return x[1]

# scores.sort(key = check)
# check 함수에서 return된 값(성적)을 기준으로 정렬.

scores.sort(key = lambda x : x[1])
# 한번 쓰고 안 쓸 함수면 lambda 함수 이용

print(scores)