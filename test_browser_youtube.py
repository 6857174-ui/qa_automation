import pytest
import time
from playwright.sync_api import sync_playwright

BROWSERS = ["chromium", "firefox", "msedge"]
TIME_LIMIT = 15

def get_browser(p, browser_name):
    if browser_name == "chromium":
        return p.chromium.launch(headless=True)   # False → True
    elif browser_name == "firefox":
        return p.firefox.launch(headless=True)     # False → True
    elif browser_name == "msedge":
        return p.chromium.launch(headless=True, channel="msedge")  # False → True

@pytest.mark.parametrize("browser_name", BROWSERS)
def test_naver_youtube(browser_name):
    with sync_playwright() as p:
        browser = get_browser(p, browser_name)
        context = browser.new_context()
        page = context.new_page()

        print(f"\n[{browser_name}] 테스트 시작!")

        # 1. 네이버 접근
        start = time.time()
        page.goto("https://www.naver.com")
        page.wait_for_load_state("networkidle")
        elapsed = round(time.time() - start, 2)

        print(f"[{browser_name}] 네이버 접근: {elapsed}초")
        assert elapsed < TIME_LIMIT, f"[{browser_name}] FAIL - 네이버 {elapsed}초 초과"
        assert "NAVER" in page.title(), f"[{browser_name}] FAIL - 네이버 접근 실패"
        print(f"[{browser_name}] 네이버 접근 PASS ({elapsed}초)")

        # 2. 유튜브 검색
        start = time.time()
        page.fill("input[name='query']", "유튜브")
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        elapsed = round(time.time() - start, 2)

        print(f"[{browser_name}] 유튜브 검색: {elapsed}초")
        assert elapsed < TIME_LIMIT, f"[{browser_name}] FAIL - 검색 {elapsed}초 초과"
        print(f"[{browser_name}] 유튜브 검색 PASS ({elapsed}초)")

        # 3. 유튜브 접근
        start = time.time()
        try:
            with context.expect_page() as new_page_info:
                page.click("a[href*='youtube.com']")
            new_page = new_page_info.value
            new_page.wait_for_load_state("networkidle")
        except Exception:
            page.click("a[href*='youtube.com']")
            page.wait_for_load_state("networkidle")
            new_page = page

        elapsed = round(time.time() - start, 2)

        print(f"[{browser_name}] 유튜브 접근: {elapsed}초")
        assert elapsed < TIME_LIMIT, f"[{browser_name}] FAIL - 유튜브 {elapsed}초 초과"
        assert "youtube.com" in new_page.url, f"[{browser_name}] FAIL - 유튜브 URL 확인 실패"
        print(f"[{browser_name}] 유튜브 접근 PASS ({elapsed}초)")

        print(f"[{browser_name}] 모든 구간 PASS!")
        browser.close()