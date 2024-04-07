# Модуль 3. Beautiful Soap

import requests
from bs4 import BeautifulSoup

import json


def main():
    url_base = "https://quotes.toscrape.com/page/"

    # Парсінг авторів і відомостей про них
    author_recocrds = []

    for i in range(1, 11):
        url = url_base + str(i) + "/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")
        authors = soup.find_all("small", class_="author")

        for author in authors:

            href = author.find_next_sibling("a")["href"]
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
                "description": description.text.strip(),
            }
            author_recocrds.append(author_bio)

    with open("authors.json", "w", encoding="utf-8") as f:
        json.dump(author_recocrds, f)

    # Парсінг цитат
    url_base = "https://quotes.toscrape.com/page/"
    quote_records = []

    for i in range(1, 11):

        url = url_base + str(i) + "/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "lxml")

        quotes = soup.find_all("span", class_="text")
        tags = soup.find_all("div", class_="tags")
        authors = soup.find_all("small", class_="author")

        for i in range(0, len(quotes)):
            tagsforquotes = []
            tagsforquote = tags[i].find_all("a", class_="tag")
            for tagforquote in tagsforquote:
                tagforquote = tagforquote.text
                tagsforquotes.append(tagforquote)

            quote_record = {
                "tags": tagsforquotes,
                "author": authors[i].text,
                "quote": quotes[i].text,
            }
            quote_records.append(quote_record)

    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quote_records, f)


if __name__ == "__main__":
    main()
