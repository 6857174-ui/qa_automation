import pytest
import time
from playwright.sync_api import sync_playwright

# 테스트할 브라우저 목록
BROWSERS = ["chromium", "firefox", "msedge"]
# 검색어 목록
SEARCH_TERMS = ["삼성전자", "하이닉스"]
# 반복 횟수
REPEAT = 3

def search_naver(page, keyword):
    """네이버에서 키워드 검색"""
    page.goto("https://www.naver.com")
    page.wait_for_load_state("networkidle")
    page.fill("input[name='query']", keyword)
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")
    assert keyword in page.content(), f"❌ {keyword} 검색 결과 없음!"

@pytest.mark.parametrize("browser_name", BROWSERS)
def test_멀티브라우저_검색(browser_name):
    """크롬/파이어폭스/엣지로 삼성전자→하이닉스 검색 3번 반복"""
    with sync_playwright() as p:

        # 브라우저 선택
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=False)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=False)
        elif browser_name == "msedge":
            browser = p.chromium.launch(
                headless=False,
                channel="msedge"
            )

        print(f"\n🌐 {browser_name} 브라우저 시작!")

        for repeat in range(1, REPEAT + 1):
            print(f"\n🔄 {repeat}번째 반복 시작!")
            page = browser.new_page()

            for keyword in SEARCH_TERMS:
                # 시작 시간
                start = time.time()

                try:
                    search_naver(page, keyword)
                    end = time.time()
                    elapsed = end - start
                    print(f"✅ [{browser_name}] {repeat}번째 "
                          f"'{keyword}' 검색 성공! "
                          f"({elapsed:.2f}초)")

                except Exception as e:
                    end = time.time()
                    elapsed = end - start
                    print(f"❌ [{browser_name}] {repeat}번째 "
                          f"'{keyword}' 검색 실패! "
                          f"({elapsed:.2f}초)")
                    print(f"   오류: {e}")

            page.close()
            print(f"✅ {repeat}번째 반복 완료!")

        browser.close()
        print(f"\n✅ {browser_name} 모든 테스트 완료!")