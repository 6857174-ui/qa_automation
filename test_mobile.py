import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"

def test_PC_화면_로그인():
    """일반 PC 화면으로 테스트"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        
        # PC 화면 크기 확인
        size = page.viewport_size
        print(f"✅ PC 화면 크기: {size['width']}x{size['height']}")
        
        page.screenshot(path="pc_screen.png")
        print("📸 PC 스크린샷 저장!")
        browser.close()

def test_아이폰_화면_로그인():
    """아이폰 13 화면으로 테스트"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # 아이폰 13 설정
        iphone = p.devices["iPhone 13"]
        context = browser.new_context(**iphone)
        page = context.new_page()
        
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        
        # 모바일 화면 크기 확인
        size = page.viewport_size
        print(f"✅ 아이폰 화면 크기: {size['width']}x{size['height']}")
        
        page.screenshot(path="iphone_screen.png")
        print("📸 아이폰 스크린샷 저장!")
        
        context.close()
        browser.close()

def test_갤럭시_화면_로그인():
    """갤럭시 S23 화면으로 테스트"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        # 갤럭시 S23 설정
        galaxy = p.devices["Galaxy S9+"]
        context = browser.new_context(**galaxy)
        page = context.new_page()
        
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        
        # 모바일 화면 크기 확인
        size = page.viewport_size
        print(f"✅ 갤럭시 화면 크기: {size['width']}x{size['height']}")
        
        page.screenshot(path="galaxy_screen.png")
        print("📸 갤럭시 스크린샷 저장!")
        
        context.close()
        browser.close()