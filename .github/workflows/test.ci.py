import pytest
from playwright.sync_api import sync_playwright

def test_네이버_접속():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # ← True!
        page = browser.new_page()
        
        page.goto("https://www.naver.com")
        page.wait_for_load_state("networkidle")
        
        assert "NAVER" in page.title(), "❌ 네이버 접속 실패!"
        print("✅ 네이버 접속 성공!")
        
        browser.close()