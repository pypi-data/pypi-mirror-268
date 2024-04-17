import requests
from furthrmind.collection.project import Project
import os
from furthrmind import collection


class Furthrmind:
    Experiment = collection.Experiment
    File = collection.File
    FieldData = collection.FieldData
    ResearchItem = collection.ResearchItem
    Sample = collection.Sample
    Unit = collection.Unit
    ComboBoxEntry = collection.ComboBoxEntry
    Field = collection.Field
    DataTable = collection.DataTable
    Group = collection.Group
    Column = collection.Column
    Project = collection.Project
    Category = collection.Category

    def __init__(self, host, api_key=None, api_key_file=None, project_id=None, project_name=None):

        if not host.startswith("http"):
            host = f"https://{host}"
        self.host = host
        self.base_url = f"{host}/api2"
        self.session = requests.session()



        assert api_key is not None or api_key_file is not None, "Either api_key or api_key_file must be specified"

        if api_key_file:
            assert os.path.isfile(api_key_file), "Api key file is not a valid file"
            with open(api_key_file, "r") as f:
                api_key = f.read()

        self.session.headers.update({"X-API-KEY": api_key})

        self.api_key = api_key
        self.project_id = project_id
        self._write_fm_to_base_class()

        # write project_url with wrong project_id to enable get request if name is provided
        self.project_url = f"{self.base_url}/projects/{self.project_id}"

        if project_name is not None:
            project = Project.get(name=project_name)
            if project:
                self.project_id = project.id

            assert self.project_id is not None, f"Project '{project_name} was not found. Check the spelling"

        # rewrite project_url after project is successully found
        self.project_url = f"{self.base_url}/projects/{self.project_id}"

    def get_project_url(self, project_id=None):
        if project_id is None:
            return self.project_url
        else:
            project_url = self.project_url.replace(str(self.project_id), project_id)
            return project_url

    def get_projects(self):
        return self.get.project()

    def _write_fm_to_base_class(self):
        from furthrmind.collection.baseclass import BaseClass
        BaseClass.fm = self



