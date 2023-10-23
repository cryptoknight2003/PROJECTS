from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

visited_urls = set()

def get_valid_urls(base_url, soup):
    urls = []
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        if href and href != "#":
            url = urljoin(base_url, href)
            urls.append(url)
    return urls

def spider_url(url, keyword):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        urls = get_valid_urls(url, soup)

        for url_to_visit in urls:
            if url_to_visit not in visited_urls:
                visited_urls.add(url_to_visit)
                if keyword in url_to_visit:
                    print(url_to_visit)
                    spider_url(url_to_visit, keyword)

if __name__ == "__main":
    start_url = input("Enter the URL you want to scrape: ")
    keyword = input("Enter the keyword to search for in the URL provided: ")
    spider_url(start_url, keyword)


'''n this improved version:

The code is organized into functions for better readability and maintainability.
The get_valid_urls function extracts valid URLs from the HTML content.
Error handling for requests and exceptions is added.
The script now checks for response.raise_for_status() to ensure the HTTP request is successful.
The main part of the script is enclosed in the if __name__ == "__main__": block to ensure it's only executed when the script is run directly.
Clear variable names and proper indentation make the code neater and more organized.
This version of the code is easier to read and understand, making it more maintainable and efficient.'''
