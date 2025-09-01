# 학생들의 이름과 점수 정보를 리스트로 관리하는 코드 구현

# 리스트 생성
students = []


# 학생 추가
def add_student(name, score):
    students.append([name, score])
    print(f"{name} 학생이 추가되었습니다")


# 학생 삭제
def remove_student(name):
    for student in students:
        if name in student:
            students.remove(student)
            print(f"{name} 학생이 삭제되었습니다")
            return
    print("존재하지 않는 학생입니다")


# 성적 수정
def update_student(name, new_score):
    for student in students:
        if name in student:
            student[1] = new_score
            print(f"{name} 학생 점수가 수정되었습니다")
            return
    print("존재하지 않는 학생입니다")


# 전체 목록 출력
def print_all():
    if not students:
        print("등록된 학생이 없습니다")
        return
    for student in students:
        print(student[0], student[1])


# 통계 출력
def print_stats():
    if not students:
        print("등록된 학생이 없습니다")
        return
    scores = [int(student[1]) for student in students]
    최고 = max(scores)
    최저 = min(scores)
    평균 = sum(scores) / len(scores)
    print("최고점수", 최고, "최저점수", 최저, "평균점수", 평균)
