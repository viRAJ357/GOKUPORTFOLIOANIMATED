import urllib.request
import re

try:
    req = urllib.request.Request('https://prankushgiri.netlify.app/', headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    links = re.findall(r'href="([^"]+\.css)"', html)
    print("CSS links:", links)

    for link in links:
        if not link.startswith('http'):
            if not link.startswith('/'):
                link = '/' + link
            link = 'https://prankushgiri.netlify.app' + link
        print("Fetching", link)
        css_req = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0'})
        css_content = urllib.request.urlopen(css_req).read().decode('utf-8')
        with open('prankush.css', 'w', encoding='utf-8') as f:
            f.write(css_content)
        print("CSS written to prankush.css")
except Exception as e:
    print("Error:", e)
