import pytest
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"

def test_로그인_정상():
    """커버리지 1: 정상 로그인"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        assert "inventory" in page.url
        print("✅ 정상 로그인 커버")
        browser.close()

def test_로그인_실패():
    """커버리지 2: 로그인 실패"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "wrong_user")
        page.fill("input[name='password']", "wrong_pass")
        page.click("input[name='login-button']")
        
        assert "Epic sadface" in page.content()
        print("✅ 로그인 실패 커버")
        browser.close()

def test_상품목록_노출():
    """커버리지 3: 상품 목록 노출 확인"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        # 상품 개수 확인
        items = page.locator(".inventory_item").count()
        assert items > 0, "❌ 상품 없음!"
        print(f"✅ 상품 목록 커버: {items}개 노출 확인")
        browser.close()

def test_장바구니_담기():
    """커버리지 4: 장바구니 담기"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        page.click("text=Add to cart")
        page.wait_for_timeout(1000)
        
        cart = page.locator(".shopping_cart_badge").text_content()
        assert cart == "1"
        print(f"✅ 장바구니 커버: {cart}개 담김")
        browser.close()

def test_로그아웃():
    """커버리지 5: 로그아웃"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        # 메뉴 열고 로그아웃
        page.click("#react-burger-menu-btn")
        page.wait_for_timeout(1000)
        page.click("#logout_sidebar_link")
        page.wait_for_load_state("networkidle")
        
        assert page.url == BASE_URL + "/"
        print("✅ 로그아웃 커버")
        browser.close()