import csv
import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("실행 시간:", end - start, "초")
        return result

    return wrapper


@timing
def read_csv(filename):
    f = open(filename, newline="", encoding="utf-8")
    rows = list(csv.DictReader(f))
    f.close()
    return rows


@timing
def filter_students(students):
    return [s for s in students if int(s["score"]) >= 80]


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
