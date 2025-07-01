# 점수 정의
korean, english, mathematics, science = map(int,input().split())

def get_average(**kwargs):
    return sum(kwargs.values()) / len(kwargs)

def get_min_max_score(*args):
    return min(args), max(args)

# 전체 과목에 대해
min_score, max_score = get_min_max_score(korean=korean, english=english, mathematics=mathematics, science=science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

# 일부 과목에 대해
min_score, max_score = get_min_max_score(english=english, science=science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
