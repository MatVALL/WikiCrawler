from urllib.request import urlopen
from bs4 import BeautifulSoup

class WikiCrawler():
    def __init__(self,max_depth=5,root='https://en.wikipedia.org/wiki/Special:Random'):
        self.root = root
        self.html = urlopen(self.root)
        self.max_depth = max_depth
    def getName(self):
        soup=BeautifulSoup(self.html,'html.parser')
        return soup.find_all('h1',{"id":"firstHeading"})
    def getLinks(self):
        links = []
        soup = BeautifulSoup(self.html,'html.parser')
        soup_body = soup.find('div',{"id":"bodyContent"})
        for link in soup_body.find_all('a', href=True):
            ref = link['href']
            if 'File' in ref or 'Category' in ref or 'Special' in ref or 'wikidata' in ref:
                continue
            if '/wiki/' in ref:
                links.append(ref)
        return ['https://en.wikipedia.org'+ref for ref in links]
    def crawlDepths(self):
        related = [[[self.root]]]
        for depth in range(self.max_depth):
            print(depth,related[-1])
            related.append([WikiCrawler(root=r).getLinks() for r in related[-1][0]])
        return related
if __name__=='__main__':
    wc=WikiCrawler()
    print(wc.crawlDepths())
