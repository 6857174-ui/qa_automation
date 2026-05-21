from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # 네이버 접속
    page.goto("https://www.naver.com")
    
    # 검색어 입력 후 검색
    page.fill("input[name='query']", "플레이라이트")
    page.click("button[type='submit']")
    
    # 검색 결과 페이지 로딩 기다리기
    page.wait_for_load_state("networkidle")
    
    # ✅ 검증 1: 페이지 제목 확인
    title = page.title()
    print(f"페이지 제목: {title}")
    
    # ✅ 검증 2: 특정 글자가 화면에 있는지 확인
    if "플레이라이트" in page.content():
        print("✅ 성공: '플레이라이트' 글자 화면에 있음!")
    else:
        print("❌ 실패: '플레이라이트' 글자 없음!")
    
    # ✅ 검증 3: 스크린샷 저장
    page.screenshot(path="result.png")
    print("📸 스크린샷 저장 완료! (result.png)")
    
    page.wait_for_timeout(3000)
    browser.close()
    print("완료!")