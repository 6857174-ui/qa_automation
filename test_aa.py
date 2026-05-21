from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 네이버 접속
    page.goto("https://www.naver.com")
    print("네이버 접속 성공!")
    
    # 검색창에 글자 입력
    page.fill("input[name='query']", "플레이라이트 자동화")
    print("검색어 입력 완료!")
    
    # 검색 버튼 클릭
    page.click("button[type='submit']")
    print("검색 클릭 완료!")
    
    # 결과 3초 보기
    page.wait_for_timeout(3000)
    
    browser.close()
    print("완료!")