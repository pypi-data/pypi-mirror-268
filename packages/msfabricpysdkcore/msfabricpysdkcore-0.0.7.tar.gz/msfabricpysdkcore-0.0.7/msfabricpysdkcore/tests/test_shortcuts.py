import unittest
from msfabricpysdkcore.coreapi import FabricClientCore
from datetime import datetime
#from dotenv import load_dotenv

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        #load_dotenv()
        self.fc = FabricClientCore()
        self.workspace_id = "c3352d34-0b54-40f0-b204-cc964b1beb8d"

        self.lakehouse_target = "cb4ca0b5-b53b-4879-b206-a53c35cbff55"
        self.lakehouse_shortcut = "e2c09c89-bf97-4f71-bdeb-36338795ec36"

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        self.shortcutname = "shortcut" + datetime_str
        self.path_target = "Files/folder1"
        self.path_shortcut = "Files/shortcutfolder"

        self.target = {'oneLake': {'itemId': self.lakehouse_target,
                                   'path': self.path_target,        
                                   'workspaceId': self.workspace_id}}

    def test_shortcut_end_to_end(self):

        item = self.fc.create_shortcut(workspace_id=self.workspace_id,
                                       item_id=self.lakehouse_shortcut,
                                       path=self.path_shortcut,
                                       name=self.shortcutname,
                                       target=self.target)
        self.assertEqual(item.name, self.shortcutname)
        self.assertEqual(item.path, self.path_shortcut)
        self.assertEqual(item.target, self.target)

        item = self.fc.get_shortcut(workspace_id=self.workspace_id,
                                    item_id=self.lakehouse_shortcut,
                                    path=self.path_shortcut,
                                    name=self.shortcutname)
        self.assertEqual(item.name, self.shortcutname)
        self.assertEqual(item.path, self.path_shortcut)
        self.assertEqual(item.target, self.target)

        status_code = self.fc.delete_shortcut(workspace_id=self.workspace_id,
                                             item_id=self.lakehouse_shortcut,
                                             path=self.path_shortcut,
                                             name=self.shortcutname)
        
        self.assertAlmostEqual(status_code, 200)

if __name__ == "__main__":
    unittest.main()