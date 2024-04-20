import requests
from bs4 import BeautifulSoup


to_check = []
work = []
url = 'https://ogladajanime.pl/anime_list/34881' # LINK DO LISTY
szukany_tag = "Isekai"                            # POSZUKIWANY GATUNEK (dostepne: https://ogladajanime.pl/search/custom) upewnij sie co do wielkosci liter (bardzo wazne), wprowadz tylko jeden pls
x = 0

# getting html info
response = requests.get(url)
html_content = response.text

# analizing html with bs
soup = BeautifulSoup(html_content, 'html.parser')
anime_links = soup.find_all('a')

# scanning for hrefs
for link in anime_links:
    href = link.get('href')
    if href and href.startswith('/anime/') and href not in to_check:
        to_check.append(href)

# overriding old variables
for link in to_check:
    response = requests.get("https://ogladajanime.pl" + str(link))
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    tags = soup.find_all('span')
    for i in tags:
        href = i.get('href')

        if href and href.startswith('/search/name/'):
            if szukany_tag in href:
                work.append(to_check[x])
    x += 1

print(work)
print('\n\n\nczy chcesz wyeksportować nazwy do pliku .txt? (y/n)')

input = input()
if input == "y":
    with open(r"C:lista.txt", 'w') as file:
        for element in work:
            file.write(str(element) + '\n')

print('Gotowe!')

while True:
    pass
