from functools import wraps

from furthrmind.utils import furthr_wrap, instance_overload
from typing_extensions import List, Self, Any, Dict, TYPE_CHECKING
from inspect import isclass
import os

if TYPE_CHECKING:
    from furthrmind.collection import File, FieldData, Experiment

class BaseClass:
    _data = {}
    _fetched = False
    _id = None
    fm = None

    _attr_definition = {}

    def __init__(self, id=None, data=None):
        if data:
            self._update_attributes(data)

        if id:
            self._id = id
        else:
            if "id" in self._data:
                self._id = self._data["id"]
        if not self._id:
            raise ValueError("No id provided")

        # create instance methods for certain class_methods
        instance_methods = ["get", "get_all", "post"]
        instance_overload(self, instance_methods)

    def __getitem__(self, item):
        if hasattr(self, item):
            return getattr(self, item)
        else:
            raise ValueError("No such attribute")


    def _get_url_instance(self, project_id=None):
        return ""

    @classmethod
    def _get_url_class(cls, id, project_id=None):
        return ""

    @classmethod
    def _get_all_url(cls, project_id=None):
        return ""

    @classmethod
    def _post_url(cls, project_id=None):
        return ""

    @staticmethod
    def _update_instance_decorator(f):
        @wraps(f)
        def decorated(*args, **kws):
            results = f(*args, **kws)
            self = args[0]
            self._update_attributes(results)
            return self

        return decorated

    @staticmethod
    def _create_instances_decorator(f):
        @wraps(f)
        def decorated(*args, **kws):
            results = f(*args, **kws)
            if results is None:
                return
            if isclass(args[0]):
                cls = args[0]
            else:
                self = args[0]
                cls = self.__class__

            if isinstance(results, list):
                item_list = []
                for r in results:
                    item = cls(data=r)
                    item_list.append(item)
                return item_list
            else:
                item = cls(data=results)
                return item

        return decorated

    def _update_attributes(self, data):
        from furthrmind.collection import get_collection_class
        self._data = data

        def _create_instance(classname, _data):
            cls = get_collection_class(classname)
            if isinstance(_data, list):
                item_list = []
                for item in _data:
                    item = cls(self.fm, data=item)
                    item_list.append(item)
                item = item_list
            else:
                item = cls(self.fm, data=_data)
            return item

        for key in data:
            if hasattr(self, key):
                item = data[key]
                if key in self._attr_definition:
                    attr_definition = self._attr_definition[key]
                    if "class" in attr_definition:
                        if "nested_dict" in attr_definition:
                            item = {}
                            for item_key in data[key]:
                                item[item_key] = _create_instance(attr_definition["class"],
                                                                  data[key][item_key])
                        else:
                            if data[key]:
                                item = _create_instance(attr_definition["class"], data[key])
                            else:
                                pass

                setattr(self, key, item)
            else:
                for attr_definition in self._attr_definition.items():
                    definition_key = attr_definition[0]
                    definition_value = attr_definition[1]
                    if "data_key" in definition_value:
                        if definition_value["data_key"] == key:
                            item = data[key]
                            if "class" in definition_value:
                                item = _create_instance(definition_value["class"], data[key])
                            setattr(self, definition_key, item)
                            break

    @classmethod
    def get(cls, id=None):
        if isclass(cls):
            return cls._get_class_method(id)
        else:
            self = cls
            data = self._get_instance_method()
            return data

    @_update_instance_decorator
    @furthr_wrap(force_list=False)
    def _get_instance_method(self):
        url = self._get_url_instance()
        data = self.fm.session.get(url)
        return data

    @classmethod
    @_create_instances_decorator
    @furthr_wrap(force_list=False)
    def _get_class_method(cls, id):
        url = cls._get_url_class(id)
        return cls.fm.session.get(url)

    @classmethod
    def get_all(cls, project_id=None) -> List[Self]:
        if isclass(cls):
            return cls._get_all_class_method(project_id)
        else:
            self = cls
            return self._get_all_instance_method(project_id)

    @_create_instances_decorator
    @furthr_wrap(force_list=True)
    def _get_all_instance_method(self, project_id):
        from .project import Project
        if isinstance(self, Project):
            url = self.__class__._get_all_url()
        else:
            url = self.__class__._get_all_url(project_id)
        return self.fm.session.get(url)

    @classmethod
    @_create_instances_decorator
    @furthr_wrap(force_list=True)
    def _get_all_class_method(cls, project_id):
        from .project import Project
        if cls in [Project]:
            url = cls._get_all_url()
        else:
            url = cls._get_all_url(project_id)
        return BaseClass.fm.session.get(url)
      

    @classmethod
    def post(cls, data, project_id=None):
        if isclass(cls):
            return cls._post_class_method(data, project_id)
        else:
            self = cls
            return self._post_instance_method(data, project_id)


    @furthr_wrap(force_list=False)
    def _post_instance_method(self, data,  project_id=None):
        url = self.__class__._post_url(project_id)
        return self.fm.session.post(url, json=data)

    @classmethod
    @furthr_wrap(force_list=False)
    def _post_class_method(cls, data, project_id=None):
        url = cls._post_url(project_id)
        return cls.fm.session.post(url, json=data)

class BaseClassWithFieldData(BaseClass):
    id = None
    fielddata = []


    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def update_field_value(self, value, fieldname=None, fieldid=None):
        """
        :param value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        :param field_name: Name of field that should be updated. Either field_name or field_id must be specified
        :param field_id: id of field that should be updated. Either field_name or field_id must be specified
        :return: id
        """

        fielddata = None
        for fielddata in self.fielddata:
            if fielddata:
                break
            if fieldid:
                if fielddata.fieldid == fieldid:
                    fielddata = fielddata
            elif fieldname:
                if fielddata.fieldname == fieldname:
                    fielddata = fielddata

        if not fielddata:
            raise ValueError("No field found with the given fieldid or fieldname")

        return fielddata.update_value(value)

    def update_field_unit(self, unit, field_name=None, field_id=None):
        """
        :param value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        :param field_name: Name of field that should be updated. Either field_name or field_id must be specified
        :param field_id: id of field that should be updated. Either field_name or field_id must be specified
        :return: id
        """

        fielddata = None
        for fielddata in self.fielddata:
            if field_id:
                if fielddata.fieldid == field_id:
                    fielddata = fielddata
            elif field_name:
                if fielddata.fieldname == field_name:
                    fielddata = fielddata

        if not fielddata:
            raise ValueError("No field found with the given fieldid or fieldname")

        return fielddata.update_unit(unit)

    def add_field(self, field_name=None, field_type=None, field_id=None,
                  value=None, unit=None) -> "FieldData":
        """
        :param field_name: Name of field that should be added. If fieldname provided,
                            also fieldtype must be specified. Either fieldname and fieldtype or field_id must be specified
        :param field_type: Type of field: Must be out of: Numeric, Date, SingleLine
                                                        ComboBoxEntry, MultiLine, CheckBox
        :param field_id: id of field that should be added.
        :param value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        :param unit: dict with id or name, or name as string, or id as string
        :return: fielddata object
        """

        from .fielddata import FieldData

        fielddata = FieldData.create(field_name, field_type, field_id, value, unit)
        self.fielddata.append(fielddata)
        data = {"id": self.id, "fielddata": [{"id": f.id} for f in self.fielddata]}
        self.post(data)
        return fielddata

    def add_many_fields(self, data_list: List[Dict] ) -> List["FieldData"]:
        """
        Method to add many fields to an item. Each field is defined by and dict in the data_list parameter

        :param data_list: dict with the following key
        - field_name: Name of field that should be added. If fieldname provided, also fieldtype must be specified. Either fieldname and fieldtype or field_id must be specified
        - field_type: Type of field: Must be out of: Numeric, Date, SingleLine
            ComboBoxEntry, MultiLine, CheckBox
        - field_id: id of field that should be added.
        - value:
            - Numeric: float or int, or a string convertable to a float
            - Date: datetime, or date object, or unix timestamp or string with iso format
            - SingleLine: string
            - ComboBoxEntry: dict with id or name as key, or string with name, or string with id
            - MultiLine: dict with content as key, or string
            - CheckBox: boolean
        - unit: dict with id or name, or name as string, or id as string

        :return: list with fielddata object

        """

        from .fielddata import FieldData

        fielddata_list = FieldData.create_many(data_list)
        self.fielddata.extend(fielddata_list)
        data = {"id": self.id, "fielddata": [{"id": f.id} for f in self.fielddata]}
        self.post(data)
        return fielddata_list


    def remove_field(self, fieldname=None, fieldid=None):
        """

        :param fieldname: Name of field that should be removed. Either id or fieldname must be specified
        :param fieldid: id of field that should be removed.
        :return id of item

        """

        new_fielddata_list = []
        fielddata_to_be_removed = None
        for fielddata in self.fielddata:
            found = False
            if fieldid:
                found = True
                if fielddata.fieldid == fieldid:
                    fielddata_to_be_removed = fielddata
            elif fieldname:
                found = True
                if fielddata.fieldname == fieldname:
                    fielddata_to_be_removed = fielddata
            if not found:
                new_fielddata_list.append(fielddata)


        if not fielddata_to_be_removed:
            raise ValueError("No field found with the given fieldid or fieldname")

        self.fielddata = new_fielddata_list
        fielddata_list = [{"id": fd.id} for fd in new_fielddata_list]
        post_data = {"id": self.id, "fielddata": fielddata_list}
        id = self.post(post_data)
        return id

class BaseClassWithFiles(BaseClass):
    id = None
    files = []

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    def add_file(self, file_path, file_name=None) -> "File":
        """

        :param file_path: file path of the file that should be uploaded
        :param file_name: Optionally specify the file name if not the original file name should be used

        :return: file object
        """

        from furthrmind.file_loader import FileLoader
        from .file import File

        if not os.path.isfile(file_path):
            raise ValueError("File does not exist")

        fl = FileLoader(self.fm.host, self.fm.api_key)
        file_id, file_name = fl.uploadFile(file_path, file_name)
        file_data = {"id": file_id,
                     "name": file_name}
        file_list = [{"id": f.id} for f in self.files]
        file_list.append(file_data)
        post_data = {"id": self.id, "files": file_list}

        id = self.post(post_data)
        file = File(data=file_data)
        self.files.append(file)
        return file

    def remove_file(self, file_id=None, file_name=None):
        """

        :param file_id: id of file that should be removed, either file_name or file_id must be specified
        :param file_name: file name of file to be removed

        :return: file object
        """

        new_file_list = []
        file_to_be_removed = None
        for file in self.files:
            found = False
            if file_id:
                found = True
                if file.id == file_id:
                    file_to_be_removed = file
            elif file_name:
                found = True
                if file.name == file_name:
                    file_to_be_removed = file
            if not found:
                new_file_list.append(file)

        if not file_to_be_removed:
            raise ValueError("No file found with the given file_id or file_name")

        self.files = new_file_list
        file_list = [{"id": f.id} for f in new_file_list]
        post_data = {"id": self.id, "files": file_list}
        id = self.post(post_data)
        return id

class BaseClassWithGroup(BaseClass):
    id = None
    groups = []

    def __init__(self, id=None, data=None):
        super().__init__(id, data)

    @classmethod
    def _create(cls, name, group_name = None, group_id=None, project_id=None):
        """
        Method to create a new item (sample, experiment)
        :param name: the name of the item to be created
        :param group_name: The name of the group where the new item will belong to. group name can be only considered
                            for groups that are not subgroups. Either group_name or group_id must be specified
        : param group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
        : param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        : return: instance of the item class: experiment, or sample
        """
        data = cls._prepare_data_for_create(name, group_name, group_id, project_id)
        id = cls.post(data, project_id)
        data["id"] = id
        return data

    @classmethod
    def _create_many(cls, data_list: List[Dict], project_id=None):
        """
        Method to create multiple items (sample, experiment)
        :param data_list: dict with the following keys:
            - name: the name of the item to be created
            - group_name: The name of the group where the new item will belong to. group name can be only considered
                            for groups that are not subgroups. Either group_name or group_id must be specified
            - group_id: the id of the group where the new item will belong to. Either group_name or group_id must be specified
        :param project_id: Optionally to create an item in another project as the furthrmind sdk was initiated with
        : return list with instances of the item class: experiment, or sample
        """
        from furthrmind.collection import Group

        new_list = []
        groups = Group.get_all()
        for data in data_list:
            new_list.append(cls._prepare_data_for_create(name=data.get("name"), group_name=data.get("group_name"),
                                                         group_id=data.get("group_id"), project_id=project_id,
                                                         groups=groups))

        id_list = cls.post(new_list, project_id)
        for data, id in zip(new_list, id_list):
            data["id"] = id
        return new_list

    @classmethod
    def _prepare_data_for_create(cls, name, group_name = None, group_id=None, project_id=None, groups=None):
        from furthrmind.collection import Group
        if not name:
            raise ValueError("Name must be specified")
        if not group_name and not group_id:
            raise ValueError("Either group_name or group_id must be specified")

        if group_name:
            if not groups:
                groups = Group.get_all(project_id)
            for group in groups:
                if group.parent_group:
                    continue
                if group.name == group_name:
                    group_id = group.id
                    break

            if not group_id:
                raise ValueError("No group with Name was found")

        data = {"name": name, "groups": [{"id": group_id}]}

        return data