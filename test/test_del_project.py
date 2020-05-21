import random
from model.project import Project

def test_del_project(app, db):
    web_config = app.config['web']

    username = "administrator"
    password = "root"
    app.session.login(username, password)

    if len(db.get_projects_list()) == 0:
        app.project.create(Project(name='testik'))

    old_projects = app.soap.get_projects(username, password, web_config["baseUrl"])
    project = random.choice(old_projects)
    app.project.del_project_by_id(project.id)
    new_projects = app.soap.get_projects(username, password, web_config["baseUrl"])

    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
