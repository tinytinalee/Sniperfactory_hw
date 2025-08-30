# 딕셔너리를 활용하여 간단한 주소록 프로그램 작성

infos = {}


# 연락처 추가
def add_info(name, phone, email, address):
    infos[name] = {"phone": phone, "email": email, "address": address}
    print(f"{name}님의 연락처가 추가되었습니다.")


# 연락처 삭제
def delete_info(name):
    if name in infos:
        del infos[name]
        print(f"{name}님의 연락처가 삭제되었습니다.")
    else:
        print("존재하지 않는 연락처입니다.")


# 연락처 검색
def search_info(name):
    if name in infos:
        info = infos[name]
        print(
            f"[{name}] 전화: {info['phone']}, 이메일: {info['email']}, 주소: {info['address']}"
        )
    else:
        print("존재하지 않는 연락처입니다.")


# 연락처 수정
def update_info(name, phone=None, email=None, address=None):
    if name in infos:
        if phone:
            infos[name]["phone"] = phone
        if email:
            infos[name]["email"] = email
        if address:
            infos[name]["address"] = address
        print(f"{name}님의 연락처가 수정되었습니다.")
    else:
        print("존재하지 않는 연락처입니다.")


# 모든 연락처 보기
def list_infos():
    if not infos:
        print("등록된 연락처가 없습니다.")
    else:
        for name, info in infos.items():
            print(
                f"[{name}] 전화: {info['phone']}, 이메일: {info['email']}, 주소: {info['address']}"
            )
