!pip install googletrans==4.0.0-rc1

import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def search_news(keyword):
    base_url = "https://search.naver.com/search.naver?where=news&query="
    url = base_url + keyword

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # 기사 제목, 링크 가져오기
        news_titles = soup.find_all('a', {'class': 'news_tit'})

        print("검색된 뉴스 url:")
        for title in news_titles:
            news_title = title.get_text()
            news_link = title['href']
            print(news_title, ":", news_link)

    else:
        print("웹페이지 접속 오류")
        return None

def translate(text, lang):
  translator = Translator()
  translated = translator.translate(text, dest=lang)
  return translated.text

def translate_document(input_file, output_file, target_lang='en'):
    try:
        with open(input_file, 'r', encoding='utf-8') as input_f:
            document_text = input_f.read()
        
        translated_text = translate(document_text, target_lang)
        
        with open(output_file, 'w', encoding='utf-8') as output_f:
            output_f.write(translated_text)
        
        print("번역이 완료되어 새로운 파일에 저장되었습니다.")
    except FileNotFoundError:
        print("입력한 파일을 찾을 수 없습니다.")
    except Exception as e:
        print("번역 실패:", e)
