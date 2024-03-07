#!/usr/bin/python3
"""Base class model"""
from datetime import datetime
from uuid import uuid4
from __init__ import storage


class BaseModel:
    """Base class for models"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key in kwargs:
                format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == '__class__':
                    continue
                if key == 'created_at':
                    conv1 = kwargs['created_at']
                    self.created_at = datetime.strptime(conv1, format)
                if key == 'updated_at':
                    conv2 = kwargs['updated_at']
                    self.updated_at = datetime.strptime(conv2, format)
                setattr(self, key, kwargs[key])

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """print representation"""
        return (f"[{self.__class__.__name__}] {self.id} {self.__dict__}")

    def save(self):
        """update modification time"""
        self.updated_at = datetime.now()
        storage.save

    def to_dict(self):
        """convert to dictionary"""
        dict_cp = self.__dict__.copy()
        dict_cp['created_at'] = self.created_at.isoformat()
        dict_cp['updated_at'] = self.updated_at.isoformat()
        dict_cp['__class__'] = self.__class__.__name__
        return dict_cp
    def save(self):
        """Save to JSON file"""
        self.updated_at = datetime.now()
        storage.save()
    
    
if __name__ == "__main__":
    all_objs = storage.all()
    print("-- Reloaded objects --")
    for obj_id in all_objs.keys():
        obj = all_objs[obj_id]
        print(obj)

    print("-- Create a new object --")
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()
    print(my_model)
