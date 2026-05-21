import pytest

def test_네이버_검색(page):  # page를 따로 만들지 않고 그냥 받아요!
    page.goto("https://www.naver.com")
    page.fill("input[name='query']", "플레이라이트")
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")
    
    assert "플레이라이트" in page.content(), "❌ 검색 결과 없음!"
    print("✅ 네이버 검색 성공!")

def test_구글_접속(page):  # 여기도 page 그냥 받아요!
    page.goto("https://www.google.com")
    page.wait_for_load_state("networkidle")
    
    assert "Google" in page.title(), "❌ 구글 접속 실패!"
    print("✅ 구글 접속 성공!")