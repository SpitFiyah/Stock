import urllib.request
from bs4 import BeautifulSoup

url = "https://midnighttdreamerr.blogspot.com"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    with open('/home/ZeroDay/kamraan_report/blogger_raw_text.txt', 'w') as f:
        f.write(soup.get_text(separator='\n', strip=True))
    print("Blogger raw text saved.")
except Exception as e:
    print(f"Error: {e}")

