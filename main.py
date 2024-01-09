import wikipediaapi
import re

def add_korean_func(Eword_list, Eword_dic):
   with open('English-Korean_dic.txt', mode = 'r', encoding='utf-8') as file:
      for i in range(len(Eword_list)):
         found_word = Eword_list[i]

         for line in file:
            dic_word = line.split('/')[0].strip()
            if found_word == dic_word:
               Eword_dic[f'{found_word}'] = line.split('.')[1:].strip()
               break
            else:
               if found_word[0] != dic_word[0]:
                  Eword_dic[f'{found_word}'] = '단어검색실패'
                  break
               else:
                  continue
                  
                  


p = re.compile(r'\b[a-z]{3,30}\b')
#p는 패턴 객체
#3~30글자의 영단어와 일치

wiki_txt = wikipediaapi.Wikipedia(
   user_agent='page_englishWords_scrap (dndtm005646@gmail.com)',
      language = 'en',
      extract_format=wikipediaapi.ExtractFormat.WIKI
)

document_input = "Catherine, Princess of Wales"

p_wiki = wiki_txt.page(document_input)
#p_wiki는 wikipedia 객체.

arranged_Eword = list(set(re.findall(p, p_wiki.text)))
arranged_Eword.sort()

Eword_dic = {}
#리스트에 저장된 단어들 하나씩 불러와 한국어 단어 뜻 동봉시키기
add_korean_func(arranged_Eword, Eword_dic)


#긁어온 페이지의 영단어들을 정렬
#단어들이 어느 문서에서 왔는지도 로그 기록이 필요


with open('txtTemp.txt', mode='w', encoding='utf-8') as file:
   file.write(str(arranged_Eword))
   #정규식으로 단어들 추출
   #한국어 단어는 어떻게 동봉하지? 
   


   
