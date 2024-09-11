from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# Playwright를 사용하여 브라우저를 열고 페이지를 로드합니다.
with sync_playwright() as p:
    # 브라우저 및 페이지 객체 생성
    browser = p.chromium.launch(headless=False)  # headless=True로 설정하면 GUI가 없이 실행됩니다.
    page = browser.new_page()

    # 웹 페이지 열기
    url = "https://www.yna.co.kr/"
    page.goto(url)

    # 페이지 로딩을 기다립니다.
    page.wait_for_timeout(5000)  # 5초 대기 (네트워크 요청이나 자바스크립트 로딩에 따라 조정 가능)

    # 페이지의 HTML을 가져옵니다.
    html = page.content()

    # BeautifulSoup으로 HTML 파싱하기
    soup = BeautifulSoup(html, 'html.parser')

    # 필요한 데이터 추출하기
    products = soup.find_all('div', class_='item-box01')

    for product in products:
        title_tag = product.find('strong', class_='tit-news')
        contents1_tag = product.find('span', class_='tit')
        contents2_tag = product.find('span', class_='tit')

        if title_tag and contents1_tag and contents2_tag:
            title = title_tag.text.strip()
            contents1 = contents1_tag.text.strip()
            contents2 = contents2_tag.text.strip()
            print(f"Product: {title}, Contents1: {contents1}, Contents2: {contents2}")
        else:
            print("Tag not found")

    # 브라우저를 닫습니다.
    browser.close()
