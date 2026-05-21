import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
def test_네이버_멀티브라우저(browser_name):
    with sync_playwright() as p:
        # 브라우저 이름에 따라 자동으로 선택
        browser_type = getattr(p, browser_name)
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        
        # 네이버 접속
        page.goto("https://www.naver.com")
        page.wait_for_load_state("networkidle")
        
        # 검증
        assert "NAVER" in page.title(), f"❌ {browser_name} 에서 네이버 접속 실패!"
        print(f"✅ {browser_name} 에서 네이버 접속 성공!")
        
        page.screenshot(path=f"naver_{browser_name}.png")
        print(f"📸 {browser_name} 스크린샷 저장!")
        
        page.wait_for_timeout(2000)
        browser.close()