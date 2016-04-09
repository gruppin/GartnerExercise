from bs4 import BeautifulSoup

class LIHtmlParser:


    def __init__(self,html):
        self.html = html
        self.parser = BeautifulSoup(html, 'html5lib')

    def getName(self):
        return self.parser.find(id="name").string


    def getTitle(self):
        return self.parser.find('p',class_='headline').string

    def getPosition(self):
        return self.parser.find('span',class_='org').string

    def getSummary(self):
        if(self.parser.find(id="summary")):
            return str(self.parser.find(id="summary").div.p.contents)

    def getSkills(self):
        if(self.parser.find(id="skills")):
            return [li.string for li in self.parser.find(id="skills").find_all('li') ]
    
