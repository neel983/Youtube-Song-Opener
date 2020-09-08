import sys
import bs4
import os
import requests
import json

str = sys.argv[1]

sub_url = str.replace(' ', '+')
sub_url = sub_url.replace('"', '')

url = "https://www.youtube.com/results?search_query="+sub_url
page = requests.get(url)

file = open('html.html', 'w')
file.write(page.text.encode('ascii', 'ignore').decode('utf-8'))
file.close()

soup = bs4.BeautifulSoup(page.text, 'html.parser')

vids = soup.findAll('script')

res = vids[-3]
res = res.text.replace(" ", "")
res = res[25:]
res = res[:-94]
data = json.loads(res)
# try:
#     final_href = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
#         "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["videoRenderer"]["videoId"]
# except Exception:
#     try:
#         final_href = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
#             "sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][1]["videoRenderer"]["videoId"]
#         print(final_href)
#     except Exception:
#         final_href = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
#             "sectionListRenderer"]["contents"][1]["itemSectionRenderer"]["contents"][1]["videoRenderer"]["videoId"]
#         print(final_href)
outer_contents = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"]
flag = False
for i in outer_contents:
    if flag == True:
        break
    try:
        inner_contents = i["itemSectionRenderer"]["contents"]
        for j in inner_contents:
            try:
                final_href = j["videoRenderer"]["videoId"]
                flag = True
                break
            except Exception:
                print("")
    except Exception:
        print("")


tmp = 'https://www.youtube.com/watch?v=' + final_href
os.system('start firefox.exe ' + tmp)
