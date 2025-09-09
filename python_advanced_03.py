"""
다음 클래스를 구현하세요:
    `Book`: 도서 정보(제목, 저자, ISBN, 출판연도 등)를 관리
    `Library`: 도서 컬렉션을 관리하고 대출/반납 기능 제공
    `Member`: 도서관 회원 정보와 대출 목록 관리

다음 기능을 구현하세요:
    도서 추가/삭제
    도서 검색(제목, 저자, ISBN으로)
    도서 대출/반납
    회원 등록/관리
    회원별 대출 현황 확인

객체 지향 설계 원칙(SOLmember_id)을 최소한 2가지 이상 적용하세요.
적절한 캡슐화를 통해 데이터를 보호하세요.
"""


class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.borrowed = False


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.loans = []


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    # 도서 추가
    def add_book(self, book):
        self.books[book.isbn] = book
        print(f"{book.isbn}: {book.title} 도서가 등록되었습니다.")

    # 도서 삭제
    def remove_book(self, isbn):
        book = self.books[isbn]
        del self.books[isbn]
        print(f"{book.isbn}: {book.title} 도서가 삭제되었습니다.")

    # 회원 등록
    def register_member(self, member):
        self.members[member.member_id] = member
        print(f"{member.member_id}: {member.name} 이 등록되었습니다.")

    # 제목으로 검색
    def search_by_title(self, keyword):
        return [b for b in self.books.values() if keyword in b.title]

    # 저자로 검색
    def search_by_author(self, keyword):
        return [b for b in self.books.values() if keyword in b.author]

    # ISBN으로 검색
    def search_by_isbn(self, isbn):
        return self.books.get(isbn)

    # 도서 대출
    def borrow(self, member_id, isbn):
        book = self.books[isbn]
        member = self.members[member_id]
        book.borrowed = True
        member.loans.append(isbn)
        print(
            f"{member.member_id}: {member.name} 님, {book.isbn}: {book.title} 도서가 대출되었습니다."
        )

    # 도서 반납
    def return_book(self, member_id, isbn):
        book = self.books[isbn]
        member = self.members[member_id]
        book.borrowed = False
        member.loans.remove(isbn)
        print(
            f"{member.member_id}: {member.name} 님, {book.isbn}: {book.title} 도서가 반납되었습니다."
        )

    # 회원별 대출 현황
    def loans_of(self, member_id):
        member = self.members[member_id]
        return [self.books[i] for i in member.loans]
