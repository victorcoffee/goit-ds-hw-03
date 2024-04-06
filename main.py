# Модуль 3. Beautiful Soap

import requests
from bs4 import BeautifulSoup

import json


# Парсінг авторів і відомостей про них
def parsing_author(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")

    authors = soup.find_all("small", class_="author")
    for author in authors:
        print(author.text)

    href = soup.find("small", class_="author").find_next_sibling("a")["href"]
    url_about = "https://quotes.toscrape.com" + href

    response = requests.get(url_about)
    soup = BeautifulSoup(response.text, "lxml")

    fullname = soup.find("h3", class_="author-title")
    born_date = soup.find("span", class_="author-born-date")
    born_location = soup.find("span", class_="author-born-location")
    description = soup.find("div", class_="author-description")

    author_bio = {
        "fullname": fullname.text,
        "born_date": born_date.text,
        "born_location": born_location.text,
        # "description": description.text.strip(),
    }
    return author_bio


# Парсінг цитат
def parsing_quote(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.find_all("span", class_="text")
    tags = soup.find_all("div", class_="tags")

    authors = soup.find_all("small", class_="author")
    for author in authors:
        print(author.text)

    quote_records = []
    for i in range(0, len(quotes)):
        print(quotes[i].text)
        print("--" + authors[i].text)
        tagsforquotes = []
        tagsforquote = tags[i].find_all("a", class_="tag")
        for tagforquote in tagsforquote:
            tagforquote = tagforquote.text
            tagsforquotes.append(tagforquote)
            print(tagforquote)

        quote_record = {
            "tags": tagsforquotes,
            "author": author.text,
            "quote": quotes[i].text,
        }
        quote_records.append(quote_record)

    return quote_records


# def save_to_json(data, filename):
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(data, f)


def main():
    url_base = "https://quotes.toscrape.com/page/"
    authors = []

    with open("authors.json", "w", encoding="utf-8") as f:

        for i in range(1, 11):
            url = url_base + str(i) + "/"
            author_bio = parsing_author(url)
            authors.append(author_bio)

        json.dump(authors, f)

    url_base = "https://quotes.toscrape.com/page/"
    quotes = []
    with open("quotes.json", "w", encoding="utf-8") as f:

        for i in range(1, 11):
            url = url_base + str(i) + "/"
            quote_records = parsing_quote(url)
            quotes.extend(quote_records)

        json.dump(quotes, f)


if __name__ == "__main__":
    main()
