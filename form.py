from flask import request

class getSiteForm:
    def __init__(self):
        self.formName = "input-src"

    def getHrefFromInput(self):
        href = request.form[self.formName]
        return href