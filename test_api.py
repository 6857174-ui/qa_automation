import requests
import pytest

# 연습용 API 사이트 (https://jsonplaceholder.typicode.com)
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_게시글_가져오기():
    """게시글 1개 가져오기"""
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # ✅ 응답 코드 확인 (200 = 성공)
    assert response.status_code == 200, "❌ 응답 실패!"
    print(f"✅ 응답 코드: {response.status_code}")
    
    # ✅ 데이터 확인
    data = response.json()
    assert "title" in data, "❌ title 없음!"
    assert "body" in data, "❌ body 없음!"
    print(f"✅ 게시글 제목: {data['title']}")
     # ✅ 이거 추가!
    print(f"✅ 전체 응답 데이터: {response.json()}")
    print(f"✅ {response.status_code} OK")
    print(f"✅ GET {response.url}")

def test_게시글_목록():
    """게시글 전체 목록 가져오기"""
    response = requests.get(f"{BASE_URL}/posts")
    
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 100, "❌ 게시글 100개 아님!"
    print(f"✅ 게시글 총 개수: {len(data)}개")

def test_없는_게시글():
    """없는 게시글 요청"""
    response = requests.get(f"{BASE_URL}/posts/999999")
    
    # ✅ 없는 데이터는 404 떠야 함
    assert response.status_code == 404, "❌ 404 아님!"
    print("✅ 없는 게시글 404 확인!")