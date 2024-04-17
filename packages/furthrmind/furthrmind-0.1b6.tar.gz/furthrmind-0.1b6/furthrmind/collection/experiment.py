from furthrmind.collection.baseclass import BaseClassWithFieldData, BaseClassWithFiles, BaseClassWithGroup, BaseClass
from typing_extensions import Self, List, Dict, TYPE_CHECKING
from inspect import isclass
if TYPE_CHECKING:
    from furthrmind.collection import FieldData, Sample, Group, ResearchItem, DataTable, File

class Experiment(BaseClassWithFieldData, BaseClassWithFiles, BaseClassWithGroup):
    id = ""
    name = ""
    neglect = False
    shortid = ""
    files: List["File"] = []
    fielddata: List["FieldData"] = []
    linked_samples: List["Sample"] = []
    linked_experiments: List[Self] = []
    groups: List["Group"] = []
    linked_researchitems: Dict[str, List["ResearchItem"]] = []
    datatables: List["DataTable"] = []


    _attr_definition = {
        "files": {"class": "File"},
        "fielddata": {"class": "FieldData"},
        "linked_samples": {"class": "Sample"},
        "linked_experiments": {"class": "Experiment"},
        "groups": {"class": "Group"},
        "linked_researchitems": {"class": "ResearchItem", "nested_dict": True},
        "datatables": {"class": "DataTable"}
    }

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def _get_url_instance(self, project_id=None):
        project_url = Experiment.fm.get_project_url(project_id)
        url = f"{project_url}/experiments/{self.id}"
        return url

    @classmethod
    def _get_url_class(cls, id, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/experiments/{id}"
        return url

    @classmethod
    def _get_all_url(cls, project_id:str = None) -> str:
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/experiments"
        return url

    @classmethod
    def _post_url(cls, project_id=None):
        project_url = cls.fm.get_project_url(project_id)
        url = f"{project_url}/experiments"
        return url

    @classmethod
    def get(cls, id=None, name=None) -> Self:
        """
        Method to get all one experiment by it's id or short_id
        If called on an instance of the class, the id of the class is used
        :param str id: id or short_id of requested experiment 
        :param str name: name of requested experiment 
        :return Self: Instance of experiment class
        """
        
        if isclass(cls):
            if id is None:
                id = name
            assert id is not None or name is not None, "Either id or name must be specified"
            return cls._get_class_method(id)
        else:
            self = cls
            data = self._get_instance_method()
            return data
    
    @classmethod
    def get_all(cls, project_id=None) -> List[Self]:
        """
        Method to get all experiment belonging to one project
        :param str project_id: Optionally to get experiments from another project as the furthrmind sdk was initiated with, defaults to None
        :return List[Self]: List with instances of experiment class
        """
        return super().get_all(project_id)

    @classmethod
    @BaseClass._create_instances_decorator
    def create(cls, name, group_name = None, group_id=None, project_id=None) -> Self:
        """
        Method to create a new experiment

        :param name: the name of the item to be created
        :param group_name: The name of the group where the new item will belong to. group name can be only considered
            for groups that are not subgroups. Either group_name or group_id must be specified
        :param group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return instance of the experiment class

        """

        return Experiment._create(name, group_name, group_id, project_id)

    @classmethod
    @BaseClass._create_instances_decorator
    def create_many(cls, data_list: List[Dict], project_id=None) -> Self:
        """
        Method to create multiple experiments

        :param data_list: dict with the following keys:
            - name: the name of the item to be created
            - group_name: The name of the group where the new item will belong to. group name can be only considered
            for groups that are not subgroups. Either group_name or group_id must be specified
            - group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified

        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return list with instance of the experiment class

        """

        return Experiment._create_many(data_list, project_id)

    def add_datatable(self, name: str, columns: List[Dict], project_id=None ) -> "DataTable":
        """
        Method to create a new datatable within this experiment

        :param name: name of the datatable
        :param columns: a list of columns that should be added to the datatable. List with dicts with the following keys:
            - name: name of the column
            - type: Type of the column, Either "Text" or "Numeric". Data must fit to type, for Text all data
            will be converted to string and for Numeric all data is converted to float (if possible)
            - data: List of column values, must fit to column_type
            - unit: dict with id or name, or name as string, or id as string

        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        :return: instance of column datatable class

        """

        from furthrmind.collection import DataTable
        datatable = DataTable.create(name, experiment_id=self.id, columns=columns, project_id=project_id)
        return datatable

