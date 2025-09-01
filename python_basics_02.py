# 주어진 데이터셋에서 튜플을 활용하여 다음 분석을 수행하세요

sales_data = [
    (2020, 1, "노트북", 1200, 100, "서울"),
    (2020, 1, "스마트폰", 800, 200, "부산"),
    (2020, 2, "노트북", 1200, 150, "서울"),
    (2020, 2, "스마트폰", 800, 250, "대구"),
    (2020, 3, "노트북", 1300, 120, "인천"),
    (2020, 3, "스마트폰", 850, 300, "서울"),
    (2020, 4, "노트북", 1300, 130, "부산"),
    (2020, 4, "스마트폰", 850, 350, "서울"),
    (2021, 1, "노트북", 1400, 110, "대구"),
    (2021, 1, "스마트폰", 900, 220, "서울"),
    (2021, 2, "노트북", 1400, 160, "인천"),
    (2021, 2, "스마트폰", 900, 270, "부산"),
    (2021, 3, "노트북", 1500, 130, "서울"),
    (2021, 3, "스마트폰", 950, 320, "대구"),
    (2021, 4, "노트북", 1500, 140, "부산"),
    (2021, 4, "스마트폰", 950, 370, "서울"),
]

# 연도별 판매량 계산
print("연도별 판매량")
years = []
for row in sales_data:
    year = row[0]
    qty = row[4]
    found = False
    for y in years:
        if y[0] == year:
            y[1] += qty
            found = True
    if not found:
        years.append([year, qty])
for y in years:
    print(f"{y[0]}: {y[1]}")

# 제품별 평균 가격 계산
print("\n제품별 평균 가격")
products = []
for row in sales_data:
    product = row[2]
    price = row[3]
    found = False
    for p in products:
        if p[0] == product:
            p[1] += price
            p[2] += 1
            found = True
    if not found:
        products.append([product, price, 1])
for p in products:
    print(f"{p[0]}: {p[1] / p[2]}")

# 최대 판매 지역 찾기
print("\n최대 판매 지역")
regions = []
for row in sales_data:
    region = row[5]
    qty = row[4]
    found = False
    for r in regions:
        if r[0] == region:
            r[1] += qty
            found = True
    if not found:
        regions.append([region, qty])
max_region = max(regions, key=lambda x: x[1])
print(f"{max_region[0]}: {max_region[1]}")

# 분기별 매출 분석
print("\n분기별 매출")
quarters = []
for row in sales_data:
    quarter = row[1]
    revenue = row[3] * row[4]
    found = False
    for q in quarters:
        if q[0] == quarter:
            q[1] += revenue
            found = True
    if not found:
        quarters.append([quarter, revenue])
for q in quarters:
    print(f"{q[0]}분기: {q[1]}")
