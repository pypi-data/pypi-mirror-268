
import requests
from bs4 import BeautifulSoup

def search_news(keyword):
    base_url = "https://search.naver.com/search.naver?where=news&query="
    url = base_url + keyword

    # URL에서 페이지 가져오기
    response = requests.get(url)

    # 응답이 성공적인지 확인
    if response.status_code == 200:
        # BeautifulSoup를 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 기사 제목과 링크 가져오기
        news_titles = soup.find_all('a', {'class': 'news_tit'})

        # 결과 출력
        print("검색된 뉴스 url:")
        for title in news_titles:
            news_title = title.get_text()
            news_link = title['href']
            print(news_title, ":", news_link)

    else:
        print("웹페이지 접속 오류")
        return None

# 키워드 입력
#keyword = input("검색할 키워드를 입력하세요: ")

# 뉴스 검색 및 결과 출력
#search_news(keyword)
