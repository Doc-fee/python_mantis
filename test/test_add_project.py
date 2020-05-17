from model.project import Project
import generator.project as gp

def test_add_project(app, db):
    old_projects = db.get_projects_list()
    app.session.login("administrator", "root")
    pr = Project()
    pr.name = gp.random_string("project_", 10)
    pr.description = gp.random_string("project_", 20)
    app.project.create(pr)
    new_projects = db.get_projects_list()
    old_projects.append(pr)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)