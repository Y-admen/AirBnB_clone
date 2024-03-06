#!/usr/bin/python3
"""Base class model"""
from datetime import datetime
from uuid import uuid4

class BaseModel:
    """Base class for models"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == '__class__':
                    continue
                if key == 'created_at':
                    self.created_at = datetime.strptime(kwargs['created_at'], format )
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(kwargs['updated_at'], format )
                setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """print representation"""
        return (f"[{self.__class__.__name__}] {self.id} {self.__dict__}")

    def save(self):
        """update modification time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """convert to dictionary"""
        dict_cp = self.__dict__.copy()
        dict_cp['created_at'] = self.created_at.isoformat()
        dict_cp['updated_at'] = self.updated_at.isoformat()
        dict_cp['__class__'] = self.__class__.__name__
        return dict_cp
    

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
