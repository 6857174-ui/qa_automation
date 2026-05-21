from playwright.sync_api import sync_playwright

# 아이디/비밀번호는 여기서만 관리
USERNAME = "kcs850408"
PASSWORD = "여기에_비밀번호_직접_입력하세요"  # 본인만 보이는 곳에 입력

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 네이버 로그인 페이지 접속
    page.goto("https://nid.naver.com/nidlogin.login")
    print("네이버 로그인 페이지 접속!")
    
    # 아이디 입력
    page.fill("input[name='id']", USERNAME)
    print("아이디 입력 완료!")
    
    # 비밀번호 입력
    page.fill("input[name='pw']", PASSWORD)
    print("비밀번호 입력 완료!")
    
    # 로그인 버튼 클릭
    page.click("button[type='submit']")
    print("로그인 버튼 클릭!")
    
    page.wait_for_load_state("networkidle")
    
    # 로그인 성공 검증
    if "https://www.naver.com" in page.url:
        print("✅ 네이버 로그인 성공!")
    else:
        print("❌ 로그인 실패 - 캡챠 또는 보안 문자 확인 필요!")
    
    page.screenshot(path="naver_login.png")
    print("📸 스크린샷 저장 완료!")
    
    page.wait_for_timeout(3000)
    browser.close()