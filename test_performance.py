import pytest
import time
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.saucedemo.com"

def test_페이지_로딩_속도():
    """페이지 로딩 시간 측정"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 시작 시간 기록
        start = time.time()
        
        page.goto(BASE_URL)
        page.wait_for_load_state("networkidle")
        
        # 끝 시간 기록
        end = time.time()
        
        # 로딩 시간 계산
        load_time = end - start
        print(f"✅ 페이지 로딩 시간: {load_time:.2f}초")
        
        # 3초 이내면 성공!
        assert load_time < 3, f"❌ 로딩 너무 느림: {load_time:.2f}초"
        
        browser.close()

def test_로그인_속도():
    """로그인 처리 시간 측정"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto(BASE_URL)
        
        # 로그인 시작 시간
        start = time.time()
        
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        page.wait_for_load_state("networkidle")
        
        # 로그인 끝 시간
        end = time.time()
        
        login_time = end - start
        print(f"✅ 로그인 처리 시간: {login_time:.2f}초")
        
        # 5초 이내면 성공!
        assert login_time < 5, f"❌ 로그인 너무 느림: {login_time:.2f}초"
        
        browser.close()

def test_상품목록_로딩_속도():
    """상품 목록 로딩 시간 측정"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # 로그인
        page.goto(BASE_URL)
        page.fill("input[name='user-name']", "standard_user")
        page.fill("input[name='password']", "secret_sauce")
        page.click("input[name='login-button']")
        
        # 상품목록 로딩 시작
        start = time.time()
        page.wait_for_load_state("networkidle")
        end = time.time()
        
        load_time = end - start
        print(f"✅ 상품목록 로딩 시간: {load_time:.2f}초")
        
        assert load_time < 3, f"❌ 상품목록 너무 느림: {load_time:.2f}초"
        
        browser.close()