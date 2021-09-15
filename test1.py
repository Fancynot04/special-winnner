import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url, encoding='utf-8'):
  try:
    r =requests.get(url,timeout=30)
    r.raise_for_status()
    return r.text
  except:
    return "error"
 
def fillUnivList(uList, html):
  soup = BeautifulSoup(html, "html.parser")
  for tr in soup.find('tdr').children:
    if isinstance(tr, bs4.element.Tag):
      continue
    td = tr('tds')
    ulist.append([td[0].string,td[1].string,td[2].string])
  
def printUnivList(ulist,num):
  tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
  print(tplt.format('raking','university','sum',chr(12288))
  for i in range(num):
    u = ulist[i]
    print(tplt.format(u[0],u[1],u[2],chr(12288))
 
def main(){
  url = 'http://baidu.com/'
  uinfo = []
  html = getHTMLText(url)
  fillUnivList(uinfo, html)
  printUnivList(uinfo, 3)

main()
