from pymongo import *
from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads
import urllib2
from LIHtmlParser import *


class LinkedInHandler:


    #htmlparser


    #2.
    #get function that returns name, title, current position, summary and skills with given parameter of linked in public profile

    def __init__(self):
        mongo = MongoClient()
        self.person_collection = mongo.gartner.persons
        
    
    def getPersonDetailsByURL(self, url):

        html = self.getURL(url)
        if(html != None):
            
            # parse the html
            self.htmlParser = LIHtmlParser(html)
            name = self.htmlParser.getName()
            title = self.htmlParser.getTitle()
            position = self.htmlParser.getPosition()
            summary = self.htmlParser.getSummary()
            skills = self.htmlParser.getSkills()


            # save / update the person in DB
            self.person_collection.insert_one({"name":name, "title":title, "position":position,"summary": summary, "skills": skills})

            # return the json
            return dumps({"name":name, "title":title, "position":position,"summary": summary, "skills": skills})

    #3
    def getPersonDetailsByName(self,name):
        return dumps(self.person_collection.find({"name": name},{"_id":0}))        
        
     #4       
    def getSkillsOfPeopleDict(self):
        personList = loads(dumps(self.person_collection.find()))
        skillsOfPeople = dict()
        for p in personList:
            skills = p.get("skills")
            if(skills):
                for skill in skills:
                    skill = str(skill)
                    if(skill in skillsOfPeople):
                        skillsOfPeople[skill] = skillsOfPeople[skill]+1
                    else:
                        skillsOfPeople[skill] = 1
        return dumps(skillsOfPeople)


    def getURL(self, url):
        userAgent= "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64)"
        headers = {"User-Agent": userAgent }
        url = "https://" + url
        req = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(req)
        return response.read()

