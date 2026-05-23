import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"

def test_정상_로그인():
    """정상 계정으로 로그인"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        # ✅ 로그인 성공 확인
        assert "inventory" in page.url, "❌ 로그인 실패!"
        print("✅ 정상 로그인 성공!")
        
        page.screenshot(path="shop_login.png")
        browser.close()

def test_잠긴계정_로그인():
    """잠긴 계정으로 로그인 시도"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "locked_out_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        # ✅ 잠긴 계정 오류 메시지 확인
        assert "Epic sadface" in page.content(), "❌ 오류 메시지 없음!"
        print("✅ 잠긴 계정 오류 메시지 확인!")
        
        page.screenshot(path="shop_locked.png")
        browser.close()

def test_상품_장바구니_담기():
    """로그인 후 상품 장바구니 담기"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 로그인
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        # 첫번째 상품 장바구니 담기
        page.click("text=Add to cart")
        page.wait_for_timeout(1000)
        print("✅ 장바구니 담기 완료!")
        
        # 장바구니 확인
        cart = page.locator(".shopping_cart_badge").text_content()
        assert cart == "1", "❌ 장바구니 개수 오류!"
        print(f"✅ 장바구니 상품 개수: {cart}개")
        
        # 스크린샷 먼저 찍고 닫기!
        page.screenshot(path="shop_cart.png")
        print("📸 스크린샷 저장!")
        
        browser.close()