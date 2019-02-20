import json
from app.tests.base_test import BaseTest

class PartyTest(BaseTest):

    def test_create_party(self):
         response = self.register_party()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'You have succesfully created a party')
         self.assertEqual(response.status_code,201)
    
    def test_party_exists(self):
         self.register_party()
         response = self.existing_party()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Party already exists')
         self.assertEqual(response.status_code,401)

    def test_find_party_usingid(self):
        self.register_party()
        response  = self.get_party_by_id()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'The party has been returned successfully')
        self.assertEqual(response.status_code,200)


    def test_remove_party_usingid(self):
        self.register_party()
        response = self.delete_party_by_id()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'You have successfully deleted the party')
        self.assertEqual(response.status_code,200)

    def test_missing_name(self):
         response = self.register_missing_partyname()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Name input required')
         self.assertEqual(response.status_code,400)

    def test_short_party_name(self):
         response = self.register_short_partyname()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'Name field too short')
         self.assertEqual(response.status_code,411)

    def test_long_abbreviations(self):
         response = self.register_long_abbreviations()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'abbreviations too long')
         self.assertEqual(response.status_code,411)

    def test_missing_logoUrl(self):
         response = self.register_missing_logo()
         result = json.loads(response.data)
         self.assertEqual(result['Message'],'logo input required')
         self.assertEqual(response.status_code,400)

    def test_find_all_parties(self):
        self.register_party()
        response = self.get_all_parties()
        result = json.loads(response.data)
        self.assertEqual(result['Message'],'Parties successfully returned')
        self.assertEqual(response.status_code,200)


