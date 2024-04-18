import unittest
from msfabricpysdkcore.coreapi import FabricClientCore
from datetime import datetime
#from dotenv import load_dotenv

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        #load_dotenv()
        self.fc = FabricClientCore()
        self.workspace_id = "fd3ba978-0b94-43e2-9f23-f65761e9ff34"
        
    def test_git(self):

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        ws2_name = "git" + datetime_str
        self.fc.create_workspace(display_name=ws2_name)
        ws2 = self.fc.get_workspace_by_name(name=ws2_name)
        self.fc.assign_to_capacity(workspace_id=ws2.id, capacity_id="a089a991-221c-49be-a41e-9020198cf7af")

        git_provider_details = {'organizationName': 'dasenf1860',
                        'projectName': 'fabrictest',
                        'gitProviderType': 'AzureDevOps',
                        'repositoryName': 'fabrictest',
                        'branchName': 'main',
                        'directoryName': '/folder1'}

        status_code = self.fc.git_connect(workspace_id=ws2.id, git_provider_details=git_provider_details)

        self.assertEqual(status_code, 204)

        initialization_strategy = "PreferWorkspace"

        status_code = self.fc.git_initialize_connection(workspace_id=ws2.id, initialization_strategy=initialization_strategy)
        self.assertEqual(status_code, 200)

        connection_details = self.fc.git_get_connection(workspace_id=ws2.id)
        self.assertEqual(connection_details['gitConnectionState'], 'ConnectedAndInitialized')

        status = self.fc.git_get_status(workspace_id=ws2.id)
        self.assertTrue(len(status["changes"]) > 0)

        status_code = self.fc.update_from_git(workspace_id=ws2.id, remote_commit_hash=status["remoteCommitHash"])

        self.assertEqual(status_code, 202)

        blubb_lakehouse = False
        for item in ws2.list_items():
            if item.type == "Lakehouse" and item.display_name == "blubb":
                blubb_lakehouse = True

        self.assertTrue(blubb_lakehouse)

        status_code = self.fc.git_disconnect(workspace_id=ws2.id)

        self.assertEqual(status_code, 204)

        ws2.delete()

if __name__ == "__main__":
    unittest.main()
