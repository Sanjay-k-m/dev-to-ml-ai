import re
from bs4 import BeautifulSoup
import requests


URL = 'https://expertzlab.com/contact'

def fetch_page(url):
    r = requests.get(url,timeout=15)
    r.raise_for_status()
    return r.text

def extract_data(text):
    # return text.splitlines()

    lines =  [item.strip() for item in text.splitlines() if item.strip()]

    joined = "\n".join(lines)

    email =sorted(set(re.findall(r'[\w\.-]+@[\w\.-]+\.\w+',joined)))

    # print(joined)

    phones = re.findall(r'(?<!\d)(?:\+?\(?\d{1,3}\)?[\s-]*)?\d(?:[\s-]*\d){9,12}(?!\d)', joined)


    return {
        "email" :email,
        "phone" :phones
    }



if __name__ == "__main__":
    html = fetch_page(URL)
    # print(html)

    # with open("page_raw.txt","w",encoding="utf-8") as f:
    #     f.write(html)
    # print("HTML saved to page_raw.txt")

    soup  = BeautifulSoup(html,"html.parser")

    # print("|||||||||||||||||||||||||||||")

    # print(soup)

    page_text = soup.get_text('\n',strip=True)

    # print("|||||||||||||||||||||||||||||")

    # print(page_text)
    
    # print("|||||||||||||||||||||||||||||")
 

    print(extract_data(page_text))