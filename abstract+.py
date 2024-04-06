# Модуль 3. Beautiful Soap

import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

authors = soup.find_all("small", class_="author")
# print(authors)
# for i in range(0, len(authors)):
#     print(authors[i].text)

# next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
# print(next_sibling)

# Looking for:
# fullname
# born_date
# born_location
# description

href = soup.find("small", class_="author").find_next_sibling("a")["href"]
print(href)

url_about = "https://quotes.toscrape.com" + href

response = requests.get(url_about)
soup = BeautifulSoup(response.text, "lxml")

fullname = soup.find("h3", class_="author-title")
print(fullname.text)

born_date = soup.find("span", class_="author-born-date")
print(born_date.text)

born_location = soup.find("span", class_="author-born-location")
print(born_location.text)

description = soup.find("div", class_="author-description")
print(description.text.strip())


# quotes = soup.find_all("span", class_="text")
# tags = soup.find_all("div", class_="tags")

# for i in range(0, len(quotes)):
#     print(quotes[i].text)
#     print("--" + authors[i].text)
#     tagsforquote = tags[i].find_all("a", class_="tag")
#     for tagforquote in tagsforquote:
#         print(tagforquote.text)
#     # break

# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")

# знайти перший тег <p> на сторінці
# first_paragraph = soup.find("p")


# print(first_paragraph)
# print(first_paragraph.text)

# знайти всі теги <p> на сторінці
# all_paragraphs = soup.find_all("p")

# print(all_paragraphs)


# отримати текст першого тега <p> на сторінці
# first_paragraph = soup.find("p")
# first_paragraph_text = first_paragraph.get_text()
# print(first_paragraph_text.strip())  # 'Login'


# отримати значення атрибута "href" першого тегу <a> на сторінці
# first_link = soup.find("a")
# first_link_href = first_link["href"]
# print(first_link_href)  # '/'


# Дочірні елементи
# body_children = list(first_paragraph.children)
# print(body_children)


# знайти перший тег <a> всередині першого тегу <div> на сторінці
# first_div = soup.find("div")
# first_div_link = first_div.find("a")
# print(first_div_link)


# Батьківські елементи
# first_paragraph_parent = first_paragraph.parent
# print(first_paragraph_parent)


# container = soup.find("div", attrs={"class": "quote"}).find_parent(
#     "div", class_="col-md-8"
# )
# print(container)


# Сусідні елементи
# next_sibling = soup.find("span", attrs={"class": "tag-item"}).find_next_sibling("span")
# print(next_sibling)

# previous_sibling = next_sibling.find_previous_sibling("span")
# print(previous_sibling)


# Пошук за CSS-селекторами

# Прості селектори

# Всі теги <p> на сторінці
# p = soup.select("p")
# print(p)

# Знайдемо всі елементи з класом "text"
# text = soup.select(".text")
# print(text)


# Знайдемо всі елементи з ідентифікатором "header". Ідентифікатор - це спеціальний атрибут тегу id.
# header = soup.select("#header")
# print(header)

# Комбіновані селектори
# a = soup.select("div.container a")
# print(a)

# Атрибути

# Знайдемо всі елементи, у яких атрибут href починається з "https://"
# href = soup.select("[href^='https://']")
# print(href)

# Знайдемо всі елементи, у яких атрибут class містить слово "text":
# ctext = soup.select("[class*='text']")
# print(ctext)
