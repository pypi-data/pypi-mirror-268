import unittest
from dotenv import load_dotenv
from datetime import datetime
from msfabricpysdkcore.coreapi import FabricClientCore

load_dotenv()

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        self.fc = FabricClientCore()
        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        self.display_name = "testws" + datetime_str
        self.workspace_id = None
    
    def test_end_to_end_workspace(self):

        ws_created = self.fc.create_workspace(display_name=self.display_name,
                                              description="test workspace", 
                                              exists_ok=False)
        # Add assertions here to verify the result
        self.assertEqual(ws_created.display_name, self.display_name)
        self.workspace_id = ws_created.id
        ws = self.fc.get_workspace_by_id(id = self.workspace_id)
        self.assertEqual(ws.display_name, self.display_name)
        self.assertEqual(ws.description, "test workspace")

#   def test_assign_to_capacity(self):
        
        result_status_code = self.fc.assign_to_capacity(workspace_id=ws.id, 
                                                        capacity_id="41cb829c-c231-4e9f-b4fc-f9042a6f9840")
        self.assertEqual(result_status_code, 202)
      

#    def test_list_workspaces(self):
        
        result = self.fc.list_workspaces()
        display_names = [ws.display_name for ws in result]
        self.assertIn(self.display_name, display_names)

        for ws in result:
            if ws.display_name == self.display_name:
                self.assertEqual(ws.capacity_id, "41cb829c-c231-4e9f-b4fc-f9042a6f9840")


  #  def test_get_workspace_by_name(self):

        workspace_name = self.display_name
        ws = self.fc.get_workspace_by_name(name = workspace_name)
        self.assertEqual(ws.display_name, self.display_name)

 #   def test_get_workspace_by_id(self):
        ws = self.fc.get_workspace_by_id(id = self.workspace_id)
        self.assertEqual(self.display_name, ws.display_name)


#    def test_get_workspace(self):
        result = self.fc.get_workspace_by_id(id = self.workspace_id)
        self.assertEqual(result.display_name, self.display_name)
    
 #   def test_add_role_assignment(self):
        result_status = self.fc.add_workspace_role_assignment(workspace_id = ws.id,
                                                              principal = {"id" : "fe9dee5d-d244-4c93-8ea1-d5e6a2225c69",
                                                                           "type" : "ServicePrincipal"},
                                                              role = 'Member')
        
        self.assertEqual(result_status, 200)

 #   def test_get_workspace_role_assignments(self):
        result = self.fc.get_workspace_role_assignments(workspace_id = ws.id)
        self.assertTrue("value" in result)
        self.assertTrue(len(result["value"]) == 2)
        for user in result["value"]:
            if user["principal"]["displayName"] == "fabrictestuser":
                self.assertTrue(user["role"] == "Member")

#    def test_update_workspace_role_assignment(self):

        result_status_code = self.fc.update_workspace_role_assignment(workspace_id = ws.id, 
                                                                      role = "Contributor", 
                                                                      principal_id = "fe9dee5d-d244-4c93-8ea1-d5e6a2225c69")
        
        self.assertEqual(result_status_code, 200)

        result = self.fc.get_workspace_role_assignments(workspace_id = ws.id)
        self.assertTrue("value" in result)
        self.assertTrue(len(result["value"]) == 2)
        for user in result["value"]:
            if user["principal"]["displayName"] == "fabrictestuser":
                self.assertTrue(user["role"] == "Contributor")

#   def test_delete_role_assignment(self):
        result_status_code = self.fc.delete_workspace_role_assignment(workspace_id = ws.id,
                                                                      principal_id = "fe9dee5d-d244-4c93-8ea1-d5e6a2225c69")
        self.assertEqual(result_status_code, 200)

 #   def test_get_workspace_role_assignments(self):
        result = self.fc.get_workspace_role_assignments(workspace_id = ws.id)
        self.assertTrue("value" in result)
        self.assertTrue(len(result["value"]) == 1)
        user = result["value"][0]
#        self.assertTrue(user["principal"]["displayName"] == "fabricapi")
        self.assertTrue(user["role"] == "Admin")

#    def test_update_workspace(self):
        ws_updated = self.fc.update_workspace(workspace_id=ws.id, 
                                              display_name="newname8912389u1293", 
                                              description="new description")
        self.assertEqual(ws_updated.display_name, "newname8912389u1293")
        self.assertEqual(ws_updated.description, "new description")
        ws = self.fc.get_workspace_by_id(id = ws.id)
        self.assertEqual(ws.display_name, "newname8912389u1293")
        self.assertEqual(ws.description, "new description")

#    def test_unassign_from_capacity(self):

        result_status_code = self.fc.unassign_from_capacity(workspace_id=ws.id)
        self.assertEqual(result_status_code, 202)
        ws = self.fc.get_workspace_by_id(ws.id)
        self.assertEqual(ws.capacity_id, None)

#    def test_delete_workspace(self):
        result_status = self.fc.delete_workspace(display_name="newname8912389u1293")
        self.assertEqual(result_status, 200)

    def test_list_capacities(self):
        result = self.fc.list_capacities()
        self.assertTrue(len(result) > 0)
        cap_ids = [cap.id for cap in result]
        self.assertIn("41cb829c-c231-4e9f-b4fc-f9042a6f9840", cap_ids)

    def test_get_capacity(self):
        capacity = self.fc.get_capacity(capacity_id = "41cb829c-c231-4e9f-b4fc-f9042a6f9840")
        self.assertEqual(capacity.id, "41cb829c-c231-4e9f-b4fc-f9042a6f9840")

        cap = self.fc.get_capacity(capacity_name= capacity.display_name)

        self.assertEqual(capacity.id, cap.id)
        self.assertIsNotNone(cap.state)
        self.assertIsNotNone(cap.sku)
        self.assertIsNotNone(cap.region)


if __name__ == "__main__":
    unittest.main()