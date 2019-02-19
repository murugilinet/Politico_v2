import json
from app.tests.base_test import BaseTest

class OfficeTest(BaseTest):

    def test_create_office(self):
        response = self.register_office()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Successfully saved')
        self.assertEqual(response.status_code,201)

    def test_no_name(self):
         response = self.missing_name_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Name input required')
         self.assertEqual(response.status_code,400)

    def test_short_office_name(self):
         response = self.short_name_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Name field too short')
         self.assertEqual(response.status_code,411)

    def test_missing_office_type(self):
         response = self.missing_type_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Office input required')
         self.assertEqual(response.status_code,400)

    def test_valid_office_type(self):
         response = self.invalid_type_registration()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Invalid Office_type')
         self.assertEqual(response.status_code,422)

    def test_remove_office_usingid(self):
        self.register_office()
        response = self.delete_by_id()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Office successfully deleted')
        self.assertEqual(response.status_code,200)

    def test_get_all_offices(self):
        self.register_office()
        response = self.get_all()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Returned successfully')
        self.assertEqual(response.status_code,200)

    def test_get_office_with_id(self):
        self.register_office()
        response = self.get_by_id()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'The office has been returned successfully')
        self.assertEqual(response.status_code,200)

        