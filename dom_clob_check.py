import requests
from bs4 import BeautifulSoup
import re

def detect_dom_clobbering(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    clobbering_patterns = [
        re.compile(r'<form.*id=.*><.*id=.*>', re.I),
        re.compile(r'<a.*id=.*name=.*href=.*>', re.I),
        re.compile(r'<iframe.*name=.*srcdoc=.*>', re.I),
        re.compile(r'<form.*id=.*name=.*><input.*id=.*>', re.I),
        re.compile(r'<base.*href=.*>', re.I)
    ]

    sink_patterns = [
        re.compile(r'alert\(.*\)', re.I),
        re.compile(r'document.getElementById\(.*\)', re.I),
    ]

    for pattern in clobbering_patterns:
        for tag in soup.find_all(string=pattern):
            print(f"[Potential Clobbering]: {tag}")

    for pattern in sink_patterns:
        for tag in soup.find_all(string=pattern):
            print(f"[Sink Detected]: {tag}")

if __name__ == '__main__':
    url = input("Enter the URL to check: ")
    detect_dom_clobbering(url)
