from model.project import Project
import generator.project as gp

def test_add_project(app):
    web_config = app.config['web']
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_projects = app.soap.get_projects(username, password, web_config["baseUrl"])
    pr = Project()
    pr.name = gp.random_string("project_", 10)
    pr.description = gp.random_string("project_", 20)
    app.project.create(pr)
    new_projects = app.soap.get_projects(username, password, web_config["baseUrl"])
    old_projects.append(pr)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)