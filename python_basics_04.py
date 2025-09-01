# 소셜 네트워크에서 사용자 간의 관계와 추천 시스템을 구현하는 프로그램을 작성

# 사용자 데이터 (딕셔너리)
interests = {
    "Alice": ["음악", "영화", "독서"],
    "Bob": ["스포츠", "여행", "음악"],
    "Charlie": ["프로그래밍", "게임", "영화"],
    "David": ["요리", "여행", "사진"],
    "Eve": ["프로그래밍", "독서", "음악"],
    "Frank": ["스포츠", "게임", "요리"],
    "Grace": ["영화", "여행", "독서"],
}


def find_friends(user):
    user_interests = set(interests[user])
    common = []
    not_common = []

    for friend, friend_interests in interests.items():
        if friend == user:
            continue
        # 교집합 확인
        if user_interests & set(friend_interests):
            common.append(friend)
        else:
            not_common.append(friend)

    return common, not_common


# 예시 실행
user = "Alice"
common_friends, not_common_friends = find_friends(user)

print(f"[{user}]와 공통 관심사가 있는 친구들:", common_friends)
print(f"[{user}]와 공통 관심사가 없는 친구들:", not_common_friends)
