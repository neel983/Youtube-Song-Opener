import sys
import bs4
import os
import requests
import json

str= sys.argv[1]

sub_url=str.replace(' ','+')
sub_url=sub_url.replace('"','')

url="https://www.youtube.com/results?search_query="+sub_url
page = requests.get(url)

soup= bs4.BeautifulSoup(page.text,'html.parser')

vids = soup.findAll('script')

res = vids[-3]
res = res.text.replace(" ","")
res = res[25:]
res = res[:-94]
data = json.loads(res)
final_href = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["videoRenderer"]["videoId"]
tmp = 'https://www.youtube.com/watch?v=' + final_href
os.system('start firefox.exe '+ tmp)
