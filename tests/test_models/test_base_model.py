import unittest
import uuid
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.BaseModel = BaseModel()
        super().setUp()

    def tearDown(self):
        # Clean up code
        ... 

    def test_id_uniqueness(self):
        id1 = self.BaseModel.id
        id2 = BaseModel().id
        self.assertNotEqual(id1, id2)

    def test_save_method_updates_updated_at(self):
        prev_updated_at = self.BaseModel.updated_at
        self.BaseModel.save()
        self.assertNotEqual(prev_updated_at, self.BaseModel.updated_at)

    def test_to_dict_method_returns_dictionary(self):
        BaseModel_dict = self.BaseModel.to_dict()
        self.assertIsInstance(BaseModel_dict, dict)

    def test_instance_str(self):
        inst = self.BaseModel
        id = inst.id
        string = "[{}] ({}) {}".format(inst.__class__.__name__,
                                       id, inst.__dict__)
        self.assertEqual(inst.__str__(), string)

    def test_str_method_returns_string_representation(self):
        string_representation = str(self.BaseModel)
        self.assertIsInstance(string_representation, str)



if __name__ == '__main__':
    unittest.main()
