from form import getSiteForm
from href import Href
from database import WorkDatabase

getForm = getSiteForm()

def createHref():
    href = Href()
    href.setHref(getForm.getHrefFromInput())
    href.setHexHref()
    return href

def checkSrcInDatabaseAndCreate(href):
    if WorkDatabase.checkSrcInDatabase(href.getHexHref()):
        WorkDatabase.createSrcInDatabase(href.getHexHref(), getForm.getHrefFromInput())

def returnHex(href):
    hex_, src = WorkDatabase.getHexAndSrc(href.getHexHref())
    return hex_