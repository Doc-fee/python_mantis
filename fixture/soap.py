from model.project import Project
from suds.client import Client
from suds import WebFault


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost:8080/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects(self, username, password, url):
        client = Client("%sapi/soap/mantisconnect.php?wsdl" % url)
        projects = []
        try:
            client_projects = client.service.mc_projects_get_user_accessible(username, password)
            for pr in client_projects:
                project = Project(name=pr.name, description=pr.description, id=pr.id)
                projects.append(project)
            return projects
        except WebFault:
            return projects