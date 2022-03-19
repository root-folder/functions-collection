import requests
import bs4
try:
    from googlesearch import search
except importError:
    print("There is no module named google. \nTry pip3 install google")

#test papers marking function
def marking(paper, score):
    result = (score / paper) * 100
    return round(result)

#scraping a website
def web_scrapper(website):
    story_list_holder = []
    page = requests.get(website)
    page = bs4.BeautifulSoup(page.content, 'html.parser')
    for story in page.find_all('p'):
        story_list_holder.append(story.get_text())
    return story_list_holder

#searching for urls based on the key word
def terminal_search(key_words):
    url_list = []
    for url in search(key_words, stop=5):
        url_list.append(url)
    return url_list
