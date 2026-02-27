import urllib.request
from bs4 import BeautifulSoup
import re

url = "https://midnighttdreamerr.blogspot.com"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    posts = soup.find_all('div', class_=re.compile(r'post-body'))
    
    with open('/home/ZeroDay/kamraan_report/blogger_writings.txt', 'w') as f:
        if not posts:
            f.write("No blog posts found or blog is empty.\n")
        else:
            for i, post in enumerate(posts):
                f.write(f"--- Post {i+1} ---\n")
                f.write(post.get_text(separator='\n', strip=True))
                f.write("\n\n")
    print("Blogger content saved successfully.")
except Exception as e:
    print(f"Error fetching Blogger: {e}")

