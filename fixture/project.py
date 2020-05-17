from model.project import Project

class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        # click create
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill forms
        self.fill_project(project)
        # button add project
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        # error APPLICATION ERROR #701


    def fill_project(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()










