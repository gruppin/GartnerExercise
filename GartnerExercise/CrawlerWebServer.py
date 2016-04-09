import web
from LinkedInHandler import *
    
urls = (
    '/person_by_url/(.*)', 'get_person_by_url',
    '/person_by_name/(.*)', 'get_person_by_name',
    '/skills_statistics', 'get_skills_statistics'
)

app = web.application(urls, globals())

linkedInHandler = LinkedInHandler()

class get_person_by_url:        
    def GET(self, url):
        return linkedInHandler.getPersonDetailsByURL(url)


class get_person_by_name:
    def GET(self, person):
        return linkedInHandler.getPersonDetailsByName(person)

class get_skills_statistics:
    def GET(self):
        return linkedInHandler.getSkillsOfPeopleDict()
    
if __name__ == "__main__":
    app.run()


