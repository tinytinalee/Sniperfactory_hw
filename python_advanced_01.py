import csv
import time


# 모든 함수 호출 시간을 측정하는 데코레이터 적용
def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("실행 시간:", end - start, "초")
        return result

    return wrapper


# CSV 파일을 읽어 딕셔너리 리스트로 변환하는 함수 작성
@timing
def read_csv(filename):
    f = open(filename, newline="", encoding="utf-8")
    rows = list(csv.DictReader(f))
    f.close()
    return rows


# 학생 중 성적이 80점 이상인 학생만 필터링
@timing
def filter_students(students):
    return [s for s in students if int(s["score"]) >= 80]


# 필터링된 학생들의 평균 나이 계산
@timing
def average_age(students):
    ages = [int(s["age"]) for s in students]
    if ages:
        return sum(ages) / len(ages)
    else:
        return 0


students = read_csv("students.csv")
filtered = filter_students(students)
avg = average_age(filtered)
print("평균 나이:", avg)
