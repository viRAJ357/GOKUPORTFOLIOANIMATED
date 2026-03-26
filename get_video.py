import urllib.request
import re
import traceback

try:
  req = urllib.request.Request('https://pin.it/706YepTHW', headers={'User-Agent': 'Mozilla/5.0'})
  html = urllib.request.urlopen(req).read().decode('utf-8')
  
  videos = re.findall(r'https://v1\.pinimg\.com/videos/.*?\.mp4', html)
  if not videos:
    videos = re.findall(r'https://[^"\'<>]+?\.mp4', html)
    
  if videos:
    vid_url = videos[0].replace('\\/', '/')
    print('Found video:', vid_url)
    urllib.request.urlretrieve(vid_url, 'app/public/hero-bg.mp4')
    print('Downloaded hero-bg.mp4')
  else:
    print('No video found in HTML')
except Exception as e:
  traceback.print_exc()
