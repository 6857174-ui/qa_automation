import pytest
from playwright.sync_api import sync_playwright

def test_성공하는_테스트():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.naver.com")
        page.wait_for_load_state("networkidle")
        
        # 실패시 스크린샷 저장
        try:
            assert "NAVER" in page.title(), "네이버 타이틀 없음!"
            print("✅ 성공!")
        except AssertionError as e:
            page.screenshot(path="fail_naver.png")
            print("📸 실패 스크린샷 저장!")
            raise e
        finally:
            browser.close()

def test_실패하는_테스트():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.naver.com")
        page.wait_for_load_state("networkidle")
        
        # 일부러 틀린 검증 (네이버에 "구글"이 있을리 없음)
        try:
            assert "구글" in page.title(), "구글 타이틀 없음!"
            print("✅ 성공!")
        except AssertionError as e:
            page.screenshot(path="fail_screenshot.png")
            print("📸 실패 스크린샷 저장됨!")
            raise e
        finally:
            browser.close()