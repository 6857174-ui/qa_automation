from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 연습용 로그인 사이트 접속
    page.goto("https://the-internet.herokuapp.com/login")
    print("로그인 페이지 접속 성공!")
    
    # 아이디 입력
    page.fill("input[name='username']", "tomsmith")
    print("아이디 입력 완료!")
    
    # 비밀번호 입력
    page.fill("input[name='password']", "SuperSecretPassword!")
    print("비밀번호 입력 완료!")
    
    # 로그인 버튼 클릭
    page.click("button[type='submit']")
    print("로그인 버튼 클릭!")
    
    # 로그인 성공 검증
    page.wait_for_load_state("networkidle")
    
    if "You logged into a secure area!" in page.content():
        print("✅ 로그인 성공 확인!")
    else:
        print("❌ 로그인 실패!")
    
    # 스크린샷 저장
    page.screenshot(path="login_result.png")
    print("📸 스크린샷 저장 완료!")
    
    page.wait_for_timeout(3000)
    browser.close()
    print("완료!")