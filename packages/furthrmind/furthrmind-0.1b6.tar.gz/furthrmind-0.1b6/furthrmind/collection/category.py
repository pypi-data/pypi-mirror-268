from inspect import isclass
from furthrmind.collection.baseclass import BaseClass
from typing_extensions import TYPE_CHECKING, List, Self

class Category(BaseClass):
    id = ""
    name = ""
    description = ""
    project = ""

    _attr_definition = {
        "project": {"class": "Project"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def _get_url_instance(self, project_id=None):
        project_url = Category.fm.get_project_url(project_id)
        url = f"{project_url}/researchcategory/{self.id}"
        return url

    @classmethod
    def _get_url_class(cls, id, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchcategory/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchcategory"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/researchcategory"
        return url

    @classmethod
    def get(cls, id=None) -> Self:
        """
        Method to get all one category by it's id
        If called on an instance of the class, the id of the class is used
        :param str id: id of requested category 
        :return Self: Instance of category class
        """

        if isclass(cls):
            return cls._get_class_method(id)
        else:
            self = cls
            data = self._get_instance_method()
            return data
    
    @classmethod
    def get_all(cls, project_id=None) -> List[Self]:
        """
        Method to get all categories belonging to one project
        :param str project_id: Optionally to get categories from another project as the furthrmind sdk was initiated with, defaults to None
        :return List[Self]: List with instances of category class
        """
        return super().get_all(project_id)
    
    @staticmethod
    def create():
        pass




