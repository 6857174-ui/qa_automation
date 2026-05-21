class NaverPage:
    def __init__(self, page):
        self.page = page
    
    # 네이버 접속
    def 열기(self):
        self.page.goto("https://www.naver.com")
        self.page.wait_for_load_state("networkidle")
    
    # 검색하기
    def 검색하기(self, 검색어):
        self.page.fill("input[name='query']", 검색어)
        self.page.click("button[type='submit']")
        self.page.wait_for_load_state("networkidle")
    
    # 검색 결과 확인
    def 검색결과_확인(self, 검색어):
        if 검색어 in self.page.content():
            return True
        return False