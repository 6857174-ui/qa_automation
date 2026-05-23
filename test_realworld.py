import pytest
from playwright.sync_api import sync_playwright

# 연습용 사이트 사용 (https://the-internet.herokuapp.com)

def test_정상_로그인():
    """정상 케이스: 맞는 아이디/비밀번호"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("input[name='username']", "tomsmith")
        page.fill("input[name='password']", "SuperSecretPassword!")
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        
        # ✅ 로그인 성공 확인
        assert "You logged into a secure area!" in page.content()
        print("✅ 정상 로그인 성공!")
        
        browser.close()

def test_틀린_비밀번호_로그인():
    """비정상 케이스: 틀린 비밀번호"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://the-internet.herokuapp.com/login")
        page.fill("input[name='username']", "tomsmith")
        page.fill("input[name='password']", "틀린비밀번호123!")
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        
        # ✅ 로그인 실패 메시지 확인
        assert "Your password is invalid!" in page.content()
        print("✅ 틀린 비밀번호 오류 메시지 확인!")
        
        browser.close()

def test_빈칸_로그인():
    """경계값 케이스: 아무것도 입력 안 하고 로그인"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://the-internet.herokuapp.com/login")
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        
        # ✅ 오류 메시지 확인
        assert "Your username is invalid!" in page.content()
        print("✅ 빈칸 로그인 오류 메시지 확인!")
        
        browser.close()