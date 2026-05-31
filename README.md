# QA 자동화 포트폴리오

## 소개
Python + Playwright 기반 웹 자동화 테스트 프로젝트입니다.
QA 실무 경험을 바탕으로 다양한 자동화 테스트를 구축했습니다.

---

## 기술 스택
- **언어**: Python
- **자동화**: Playwright
- **테스트**: pytest
- **CI/CD**: GitHub Actions
- **리포트**: pytest-html

---

## 테스트 항목

| 파일 | 내용 |
|------|------|
| test_login.py | 로그인 자동화 테스트 |
| test_api.py | API 자동화 테스트 |
| test_shop.py | 쇼핑몰 실전 테스트 |
| test_coverage.py | 테스트 커버리지 |
| test_mobile.py | 모바일 화면 테스트 |
| test_performance.py | 성능 테스트 |
| test_multi_browser.py | 멀티 브라우저 테스트 |
| test_pom.py | Page Object Model |

---

## 주요 기능

- ✅ 로그인/로그아웃 자동화
- ✅ 정상/비정상/경계값 테스트 케이스
- ✅ API 자동화 테스트 (requests)
- ✅ Chrome/Firefox 멀티 브라우저 테스트
- ✅ iPhone/Galaxy 모바일 화면 테스트
- ✅ 페이지 로딩 성능 측정
- ✅ GitHub Actions CI/CD 파이프라인
- ✅ HTML 테스트 리포트 자동 생성
- ✅ Page Object Model 패턴 적용

---

## 실행 방법

### 1. 저장소 클론
```bash
git clone https://github.com/6857174-ui/qa_automation.git
cd qa_automation
```

### 2. 패키지 설치
```bash
pip install playwright pytest pytest-html requests
playwright install
```

### 3. 전체 테스트 실행
```bash
pytest --html=report.html
```

### 4. 개별 테스트 실행 예시
```bash
pytest test_login.py        # 로그인 테스트
pytest test_api.py          # API 테스트
pytest test_mobile.py       # 모바일 테스트
pytest test_multi_browser.py # 멀티브라우저 테스트
```

### 5. HTML 리포트 확인
테스트 완료 후 `report.html` 파일을 브라우저로 열어서 확인
```bash
