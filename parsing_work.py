import requests
from bs4 import BeautifulSoup

SITE_URL = "https://otus.ru/nest/python/"

def get_text_from_url(site_url):
    response = requests.get(site_url)
    if response.ok:
        return response.text
    else:
        return None

def get_all_url_set_from_text(text):
    all_url = set()
    soup = BeautifulSoup(text, 'lxml')
    all_a = soup.find_all('a')
    for a in all_a:
        href = a.get('href')
        if "http" in href:
            all_url.add(href)
    return all_url

def get_all_url_set_from_url(site_url):
    site_text = get_text_from_url(site_url)
    if site_text:
        return get_all_url_set_from_text(site_text)

# выводить результат в терминал, либо сохранять его в файл
if __name__ == '__main__':
    all_url_set = get_all_url_set_from_url(SITE_URL)
    print(all_url_set )

    for url in list(all_url_set):
        all_url_set.union(get_all_url_set_from_url(url))

    while True:
        choice = input("Сохранить в файл? (да/нет): ").lower()
        if choice in ['да', 'y', '']:
            print("Сохраняем в файл")
            break
        elif choice in ['нет', 'n']:
            print("Выводим в терминал")
            print(list(all_url_set))
            break
        else:
            print("Попробуйте ввести 'да' или 'нет'.")
