import pytest
import csv
from playwright.sync_api import sync_playwright

def csv_데이터_읽기():
    데이터 = []
    with open("test_data.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            데이터.append((row["검색어"], row["기대결과"]))
    return 데이터

@pytest.mark.parametrize("검색어,기대결과", csv_데이터_읽기())
def test_네이버_CSV_검색(검색어, 기대결과):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.naver.com")
        page.wait_for_load_state("networkidle")
        
        page.fill("input[name='query']", 검색어)
        page.click("button[type='submit']")
        page.wait_for_load_state("networkidle")
        
        assert 기대결과 in page.content(), f"❌ '{기대결과}' 검색 결과 없음!"
        print(f"✅ '{검색어}' 검색 성공!")
        
        page.screenshot(path=f"search_{검색어}.png")
        
        browser.close()