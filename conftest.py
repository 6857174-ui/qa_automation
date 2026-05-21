import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        yield page  # 테스트에서 page를 사용할 수 있게 넘겨줌
        
        browser.close()  # 테스트 끝나면 자동으로 브라우저 닫기