from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.naver.com")
    print("네이버 접속 성공!")
    page.wait_for_timeout(3000)
    browser.close()
    print("완료!")