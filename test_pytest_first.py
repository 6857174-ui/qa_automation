import pytest
from playwright.sync_api import sync_playwright, expect

def test_naver_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 네이버 접속
        page.goto("https://www.naver.com")
        
        # 검색어 입력
        page.fill("input[name='query']", "플레이라이트")
        page.click("button[type='submit']")
        
        page.wait_for_load_state("networkidle")
        
        # ✅ 검증
        assert "플레이라이트" in page.content(), "❌ 검색 결과 없음!"
        print("✅ 검색 성공!")
        
        browser.close()

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 구글 접속
        page.goto("https://www.google.com")
        
        # 검색어 입력
        page.fill("textarea[name='q']", "playwright")
        page.keyboard.press("Enter")
        
        page.wait_for_load_state("networkidle")
        
        # ✅ 검증
        assert "playwright" in page.content(), "❌ 검색 결과 없음!"
        print("✅ 구글 검색 성공!")
        
        browser.close()