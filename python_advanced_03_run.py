from python_advanced_03 import Book, Library, Member


def main():
    lib = Library()

    while True:
        print("\n===== 도서관 시스템 =====")
        print("1. 도서 생성 후 등록")
        print("2. 회원 생성 후 등록")
        print("3. 도서 대출")
        print("4. 도서 반납")
        print("5. 회원별 대출 현황 보기")
        print("6. 도서 삭제")
        print("0. 종료")

        choice = input("메뉴를 선택하세요: ").strip()

        if choice == "1":
            title = input("도서 제목: ").strip()
            author = input("저자: ").strip()
            isbn = input("ISBN: ").strip()
            year = int(input("출판 연도: ").strip())
            b = Book(title, author, isbn, year)
            lib.add_book(b)

        elif choice == "2":
            member_id = input("회원 ID: ").strip()
            name = input("회원 이름: ").strip()
            m = Member(member_id, name)
            lib.register_member(m)

        elif choice == "3":
            member_id = input("회원 ID: ").strip()
            isbn = input("대출할 도서 ISBN: ").strip()
            lib.borrow(member_id, isbn)

        elif choice == "4":
            member_id = input("회원 ID: ").strip()
            isbn = input("반납할 도서 ISBN: ").strip()
            lib.return_book(member_id, isbn)

        elif choice == "5":
            member_id = input("회원 ID: ").strip()
            loans = lib.loans_of(member_id)
            print(f"{member_id} 회원의 대출 현황:")
            for bk in loans:
                print(f"- {bk.isbn}: {bk.title}")

        elif choice == "6":
            isbn = input("삭제할 도서 ISBN: ").strip()
            lib.remove_book(isbn)

        elif choice == "0":
            print("프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
