import unittest
from msfabricpysdkcore.coreapi import FabricClientCore

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        #load_dotenv()
        self.fc = FabricClientCore()
        self.workspace_id = "c3352d34-0b54-40f0-b204-cc964b1beb8d"
        self.item_id = "7e38f344-81df-4805-83b6-b9cc16830500"


    def test_jobs_end_to_end(self):
        job = self.fc.run_on_demand_item_job(workspace_id=self.workspace_id,
                                            item_id=self.item_id,
                                            job_type="RunNotebook")
        
        self.assertEqual(job.item_id, self.item_id)
        self.assertEqual(job.workspace_id, self.workspace_id)
        self.assertEqual(job.job_type, "RunNotebook")
        self.assertIn(job.status, ["NotStarted", "InProgress"])
        self.assertEqual(job.invoke_type, "Manual")

        job2 = self.fc.get_item_job_instance(workspace_id=self.workspace_id,
                                        item_id=self.item_id,
                                        job_instance_id=job.id)
        
        self.assertEqual(job.id, job2.id)

        status_code = self.fc.cancel_item_job_instance(workspace_id=self.workspace_id,
                                                  item_id=self.item_id,
                                                  job_instance_id=job.id)

        self.assertEqual(status_code, 202)

if __name__ == "__main__":
    unittest.main()

