import pytest
from pages.naver_page import NaverPage

def test_네이버_검색(page):
    naver = NaverPage(page)
    
    # 네이버 열기
    naver.열기()
    
    # 검색하기
    naver.검색하기("플레이라이트")
    
    # 검색 결과 확인
    결과 = naver.검색결과_확인("플레이라이트")
    assert 결과 == True, "❌ 검색 결과 없음!"
    print("✅ 네이버 검색 성공!")

def test_네이버_타이틀_확인(page):
    naver = NaverPage(page)
    
    naver.열기()
    
    타이틀 = page.title()
    assert "NAVER" in 타이틀, "❌ 네이버 타이틀 없음!"
    print(f"✅ 타이틀 확인: {타이틀}")