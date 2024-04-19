import unittest
from datetime import datetime
#from dotenv import load_dotenv
from time import sleep
from msfabricpysdkcore.coreapi import FabricClientCore

class TestFabricClientCore(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFabricClientCore, self).__init__(*args, **kwargs)
        #load_dotenv()
        self.fc = FabricClientCore()
        self.workspace_id = "c3352d34-0b54-40f0-b204-cc964b1beb8d"

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        self.item_name = "testitem" + datetime_str
        self.item_type = "Notebook"
    
    def test_item_end_to_end(self):

        item = self.fc.create_item(display_name=self.item_name, type=self.item_type, workspace_id=self.workspace_id) 
        self.assertEqual(item.display_name, self.item_name)
        self.assertEqual(item.type, self.item_type)
        self.assertEqual(item.workspace_id, self.workspace_id)
        self.assertEqual(item.description, "")

        item = self.fc.get_item(workspace_id=self.workspace_id, item_id=item.id)
        item_ = self.fc.get_item(workspace_id=self.workspace_id,
                                  item_name=self.item_name, item_type=self.item_type)
        self.assertEqual(item.id, item_.id)
        self.assertEqual(item.display_name, self.item_name)
        self.assertEqual(item.type, self.item_type)
        self.assertEqual(item.workspace_id, self.workspace_id)
        self.assertEqual(item.description, "")

        item_list = self.fc.list_items(workspace_id=self.workspace_id)
        self.assertTrue(len(item_list) > 0)

        item_ids = [item_.id for item_ in item_list]
        self.assertIn(item.id, item_ids)

        self.fc.update_item(workspace_id=self.workspace_id, item_id=item.id, display_name=f"u{self.item_name}")
        item = self.fc.get_item(workspace_id=self.workspace_id, item_id=item.id)
        self.assertEqual(item.display_name, f"u{self.item_name}")

        status_code = self.fc.delete_item(workspace_id=self.workspace_id, item_id=item.id)

        self.assertAlmostEqual(status_code, 200)

    def test_item_definition(self):

        sjd = self.fc.get_item(workspace_id=self.workspace_id, item_name="blubb", item_type="SparkJobDefinition")
        self.assertIsNotNone(sjd.definition)
        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        blubb2 = "blubb2" + datetime_str
        blubb3 = "blubb3" + datetime_str
        blubb2 = self.fc.create_item(display_name=blubb2, type="SparkJobDefinition", workspace_id=self.workspace_id,
                                   definition=sjd.definition)

        blubb3 =  self.fc.create_item(display_name=blubb3, type="SparkJobDefinition", workspace_id=self.workspace_id)

        blubb3 = self.fc.update_item_definition(workspace_id=self.workspace_id,
                                                item_id=blubb3.id, definition=sjd.definition)
        
        self.assertEqual(blubb3.definition, sjd.definition)
        
        self.assertNotEqual(blubb2.id, sjd.id)
        self.assertEqual(blubb2.definition, sjd.definition)
        self.assertNotEqual(blubb2.id, blubb3.id)
        
        blubb2.delete()
        blubb3.delete()


    def test_list_other_items(self):

        fc = self.fc

        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        list_dashboards = fc.list_dashboards(workspace_id)
        dashboard_names = [dashboard.display_name for dashboard in list_dashboards]
        self.assertGreater(len(list_dashboards), 0)
        self.assertIn("dashboard1", dashboard_names)

        list_datamarts = fc.list_datamarts(workspace_id)
        datamart_names = [datamart.display_name for datamart in list_datamarts]
        self.assertGreater(len(list_datamarts), 0)
        self.assertIn("datamart1", datamart_names)

        list_sql_endpoints = fc.list_sql_endpoints(workspace_id)
        sqlendpoint_names = [sqlendpoint.display_name for sqlendpoint in list_sql_endpoints]
        self.assertGreater(len(list_sql_endpoints), 0)
        self.assertIn("sqlendpointlakehouse", sqlendpoint_names)

        # list_mirrored_warehouses = fc.list_mirrored_warehouses(self.workspace_id)
        # self.assertGreater(len(list_mirrored_warehouses), 0)

        # list_paginated_reports = fc.list_paginated_reports(self.workspace_id)
        # self.assertGreater(len(list_paginated_reports), 0)

    def test_lakehouse(self):

        lakehouse = self.fc.get_item(workspace_id=self.workspace_id, item_name="lakehouse1", item_type="Lakehouse")
        self.assertIsNotNone(lakehouse.properties)
        item_id = lakehouse.id
        date_str = datetime.now().strftime("%Y%m%d%H%M%S")
        table_name = f"table{date_str}"


        status_code = self.fc.load_table(workspace_id=self.workspace_id, item_id=item_id, table_name=table_name, 
                                         path_type="File", relative_path="Files/folder1/titanic.csv")

        self.assertEqual(status_code, 202)

        table_list = self.fc.list_tables(workspace_id=self.workspace_id, item_id=item_id)
        table_names = [table["name"] for table in table_list]

        self.assertIn(table_name, table_names)

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        lakehouse = fc.create_lakehouse(workspace_id=workspace_id, display_name="lakehouse2")
        self.assertIsNotNone(lakehouse.id)

        lakehouses = fc.list_lakehouses(workspace_id)
        lakehouse_names = [lh.display_name for lh in lakehouses]
        self.assertGreater(len(lakehouse_names), 0)
        self.assertIn("lakehouse2", lakehouse_names)

        lakehouse2 = fc.get_lakehouse(workspace_id=workspace_id, lakehouse_id=lakehouse.id)
        self.assertEqual(lakehouse.id, lakehouse2.id)

        sleep(20)
        lakehouse2 = fc.update_lakehouse(workspace_id=workspace_id, lakehouse_id=lakehouse.id, display_name="lakehouse3")
        self.assertEqual(lakehouse2.display_name, "lakehouse3")

        id = lakehouse2.id

        lakehouse2 = fc.get_lakehouse(workspace_id=workspace_id, lakehouse_name="lakehouse3")
        self.assertEqual(lakehouse2.id, id)

        status_code = fc.delete_lakehouse(workspace_id=workspace_id, lakehouse_id=lakehouse.id)
        self.assertEqual(status_code, 200)


    def test_data_pipelines(self):

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id
        
        dps = fc.list_data_pipelines(workspace_id)
        dp_names = [dp.display_name for dp in dps]
        self.assertGreater(len(dps), 0)
        self.assertIn("pipeline1", dp_names)

        dp = fc.get_data_pipeline(workspace_id, data_pipeline_name="pipeline1")
        self.assertIsNotNone(dp.id)
        self.assertIsNotNone(dp.definition)
        self.assertEqual(dp.display_name, "pipeline1")

        dp2 = fc.update_data_pipeline(workspace_id, dp.id, display_name="pipeline2")

        dp = fc.get_data_pipeline(workspace_id, data_pipeline_id=dp.id)
        self.assertEqual(dp.display_name, "pipeline2")
        self.assertEqual(dp.id, dp2.id)

        dp2 = fc.update_data_pipeline(workspace_id, dp.id, display_name="pipeline1")

        dp = fc.get_data_pipeline(workspace_id, data_pipeline_id=dp.id)
        self.assertEqual(dp.display_name, "pipeline1")
        self.assertEqual(dp.id, dp2.id)
        # status_code = fc.delete_data_pipeline(workspace_id, dp.id)
        # self.assertEqual(status_code, 200)

    def test_eventstreams(self):

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        es_name = "es" + datetime_str

        eventstream = fc.create_eventstream(workspace_id, display_name=es_name)
        self.assertEqual(eventstream.display_name, es_name)

        eventstreams = fc.list_eventstreams(workspace_id)
        eventstream_names = [es.display_name for es in eventstreams]
        self.assertGreater(len(eventstreams), 0)
        self.assertIn(es_name, eventstream_names)

        
        es = fc.get_eventstream(workspace_id, eventstream_name=es_name)
        self.assertIsNotNone(es.id)
        self.assertEqual(es.display_name, es_name)

        es2 = fc.update_eventstream(workspace_id, es.id, display_name=f"{es_name}2")

        es = fc.get_eventstream(workspace_id, eventstream_id=es.id)
        self.assertEqual(es.display_name, f"{es_name}2")
        self.assertEqual(es.id, es2.id)

        status_code = fc.delete_eventstream(workspace_id, es.id)
        self.assertEqual(status_code, 200)

    def test_kql_database(self):

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        kql_databases = fc.list_kql_databases(workspace_id)
        kql_database_names = [kqldb.display_name for kqldb in kql_databases]
        self.assertGreater(len(kql_databases), 0)
        self.assertIn("kqldatabase1", kql_database_names)

        kqldb = fc.get_kql_database(workspace_id, kql_database_name="kqldatabase1")
        self.assertIsNotNone(kqldb.id)
        self.assertEqual(kqldb.display_name, "kqldatabase1")

        kqldb2 = fc.update_kql_database(workspace_id, kqldb.id, display_name="kqldb2")

        kqldb = fc.get_kql_database(workspace_id, kql_database_id=kqldb.id)
        self.assertEqual(kqldb.display_name, "kqldb2")
        self.assertEqual(kqldb.id, kqldb2.id)
        
        kqldb2 = fc.update_kql_database(workspace_id, kqldb.id, display_name="kqldatabase1")

        kqldb = fc.get_kql_database(workspace_id, kql_database_id=kqldb.id)
        self.assertEqual(kqldb.display_name, "kqldatabase1")
        self.assertEqual(kqldb.id, kqldb2.id)
        # status_code = fc.delete_kql_database(workspace_id, kqldb.id)
        # self.assertEqual(status_code, 200)

    def test_kql_querysets(self):

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        kql_queryset_name = "kqlqueryset1"

        kql_querysets = fc.list_kql_querysets(workspace_id)
        kql_queryset_names = [kqlq.display_name for kqlq in kql_querysets]
        self.assertGreater(len(kql_querysets), 0)
        self.assertIn(kql_queryset_name, kql_queryset_names)

        kqlq = fc.get_kql_queryset(workspace_id, kql_queryset_name=kql_queryset_name)
        self.assertIsNotNone(kqlq.id)
        self.assertEqual(kqlq.display_name, kql_queryset_name)

        kqlq2 = fc.update_kql_queryset(workspace_id, kqlq.id, display_name=f"{kql_queryset_name}2")

        kqlq = fc.get_kql_queryset(workspace_id, kql_queryset_id=kqlq.id)
        self.assertEqual(kqlq.display_name, f"{kql_queryset_name}2")
        self.assertEqual(kqlq.id, kqlq2.id)

        kqlq2 = fc.update_kql_queryset(workspace_id, kqlq.id, display_name=kql_queryset_name)

        kqlq = fc.get_kql_queryset(workspace_id, kql_queryset_id=kqlq.id)
        self.assertEqual(kqlq.display_name, kql_queryset_name)
        self.assertEqual(kqlq.id, kqlq2.id)

        # status_code = fc.delete_kql_queryset(workspace_id, kqlq.id)
        # self.assertEqual(status_code, 200)

    
    def test_ml_experiments(self):
            
        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        ml_experiment = fc.create_ml_experiment(workspace_id, display_name="mlexperiment1")
        self.assertEqual(ml_experiment.display_name, "mlexperiment1")
        
        ml_experiments = fc.list_ml_experiments(workspace_id)
        ml_experiment_names = [mle.display_name for mle in ml_experiments]
        self.assertGreater(len(ml_experiments), 0)
        self.assertIn("mlexperiment1", ml_experiment_names)

        mle = fc.get_ml_experiment(workspace_id, ml_experiment_name="mlexperiment1")
        self.assertIsNotNone(mle.id)
        self.assertEqual(mle.display_name, "mlexperiment1")

        mle2 = fc.update_ml_experiment(workspace_id, mle.id, display_name="mlexperiment2")

        mle = fc.get_ml_experiment(workspace_id, ml_experiment_id=mle.id)
        self.assertEqual(mle.display_name, "mlexperiment2")
        self.assertEqual(mle.id, mle2.id)

        status_code = fc.delete_ml_experiment(workspace_id, mle.id)
        self.assertEqual(status_code, 200)

    def test_ml_models(self):

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id
        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        model_name = "mlm" + datetime_str

        ml_model = fc.create_ml_model(workspace_id, display_name=model_name)
        self.assertEqual(ml_model.display_name, model_name)
        
        ml_models = fc.list_ml_models(workspace_id)
        ml_model_names = [ml.display_name for ml in ml_models]
        self.assertGreater(len(ml_models), 0)
        self.assertIn(model_name, ml_model_names)

        mlm = fc.get_ml_model(workspace_id, ml_model_name=model_name)
        self.assertIsNotNone(mlm.id)
        self.assertEqual(mlm.display_name, model_name)

        # mlm2 = fc.update_ml_model(workspace_id=workspace_id,ml_model_id= mlm.id,  description=model_name)

        # mlm = fc.get_ml_model(workspace_id, ml_model_id=mlm.id)
        # self.assertEqual(mlm.description, model_name)
        # self.assertEqual(mlm.id, mlm2.id)

        status_code = fc.delete_ml_model(workspace_id, mlm.id)
        self.assertEqual(status_code, 200)

    def test_notebooks(self):
            
        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        notebook_name = "notebook125"

        notebook_w_content = fc.get_notebook(workspace_id, notebook_name="HelloWorld")
        definition = notebook_w_content.definition

        notebook = fc.create_notebook(workspace_id, definition=definition, display_name=notebook_name)
        fc.update_notebook_definition(workspace_id, notebook.id, definition=definition)
        notebook = fc.get_notebook(workspace_id, notebook_id=notebook.id)
        self.assertEqual(notebook.display_name, notebook_name)
        self.assertIsNotNone(notebook.definition)
        
        notebooks = fc.list_notebooks(workspace_id)
        notebook_names = [nb.display_name for nb in notebooks]
        self.assertGreater(len(notebooks), 0)
        self.assertIn(notebook_name, notebook_names)

        nb = fc.get_notebook(workspace_id, notebook_name=notebook_name)
        self.assertIsNotNone(nb.id)
        self.assertEqual(nb.display_name, notebook_name)

        nb2 = fc.update_notebook(workspace_id, notebook_id=nb.id, display_name=f"{notebook_name}2")

        nb = fc.get_notebook(workspace_id, notebook_id=nb.id)
        self.assertEqual(nb.display_name, f"{notebook_name}2")
        self.assertEqual(nb.id, nb2.id)

        status_code = fc.delete_notebook(workspace_id, nb.id)
        self.assertEqual(status_code, 200)

    def test_reports(self):
                
        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        report_name = "report1234"

        report_w_content = fc.get_report(workspace_id, report_name="HelloWorldReport")
        definition = report_w_content.definition
        report = fc.create_report(workspace_id, display_name=report_name, definition=definition)
        fc.update_report_definition(workspace_id, report.id, definition=definition)
        report = fc.get_report(workspace_id, report_id=report.id)
        self.assertEqual(report.display_name, report_name)
        self.assertIsNotNone(report.definition)
        
        reports = fc.list_reports(workspace_id)
        report_names = [r.display_name for r in reports]
        self.assertGreater(len(reports), 0)
        self.assertIn(report_name, report_names)

        r = fc.get_report(workspace_id, report_name=report_name)
        self.assertIsNotNone(r.id)
        self.assertEqual(r.display_name, report_name)

        status_code = fc.delete_report(workspace_id, r.id)
        self.assertEqual(status_code, 200)

    def test_semantic_models(self):
                    
        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        semantic_model_name = "semanticmodel1234"

        semantic_model_w_content = fc.get_semantic_model(workspace_id, semantic_model_name="Table")
        definition = semantic_model_w_content.definition
        semantic_model = fc.create_semantic_model(workspace_id, display_name=semantic_model_name, definition=definition)
        fc.update_semantic_model_definition(workspace_id, semantic_model.id, definition=definition)
        semantic_model = fc.get_semantic_model(workspace_id, semantic_model_id=semantic_model.id)
        self.assertEqual(semantic_model.display_name, semantic_model_name)
        self.assertIsNotNone(semantic_model.definition)
        
        semantic_models = fc.list_semantic_models(workspace_id)
        semantic_model_names = [sm.display_name for sm in semantic_models]
        self.assertGreater(len(semantic_models), 0)
        self.assertIn(semantic_model_name, semantic_model_names)

        sm = fc.get_semantic_model(workspace_id, semantic_model_name=semantic_model_name)
        self.assertIsNotNone(sm.id)
        self.assertEqual(sm.display_name, semantic_model_name)

        status_code = fc.delete_semantic_model(workspace_id, sm.id)
        self.assertEqual(status_code, 200)


    def test_spark_job_definitions(self):
        
        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        spark_job_definition_name = f"sjd{datetime_str}"

        spark_job_definition_w_content = fc.get_spark_job_definition(workspace_id, spark_job_definition_name="helloworld")
        definition = spark_job_definition_w_content.definition
        spark_job_definition = fc.create_spark_job_definition(workspace_id, display_name=spark_job_definition_name)
        fc.update_spark_job_definition_definition(workspace_id, spark_job_definition.id, definition=definition)
        spark_job_definition = fc.get_spark_job_definition(workspace_id, spark_job_definition_id=spark_job_definition.id)
        self.assertEqual(spark_job_definition.display_name, spark_job_definition_name)
        self.assertIsNotNone(spark_job_definition.definition)

        spark_job_definitions = fc.list_spark_job_definitions(workspace_id)
        spark_job_definition_names = [sjd.display_name for sjd in spark_job_definitions]
        self.assertGreater(len(spark_job_definitions), 0)
        self.assertIn(spark_job_definition_name, spark_job_definition_names)

        sjd = fc.get_spark_job_definition(workspace_id, spark_job_definition_name=spark_job_definition_name)
        self.assertIsNotNone(sjd.id)
        self.assertEqual(sjd.display_name, spark_job_definition_name)

        sjd = fc.update_spark_job_definition(workspace_id, sjd.id, display_name=f"{spark_job_definition_name}2")
        sjd = fc.get_spark_job_definition(workspace_id, spark_job_definition_id=sjd.id)
        self.assertEqual(sjd.display_name, f"{spark_job_definition_name}2")

        status_code = fc.delete_spark_job_definition(workspace_id, sjd.id)
        self.assertEqual(status_code, 200)

    def test_warehouses(self):

        fc = self.fc
        workspace = fc.get_workspace_by_name("testitems")
        workspace_id = workspace.id

        datetime_str = datetime.now().strftime("%Y%m%d%H%M%S")
        warehouse1 = f"wh{datetime_str}"
        warehouse = fc.create_warehouse(workspace_id, display_name=warehouse1)
        self.assertIsNotNone(warehouse.id)

        warehouses = fc.list_warehouses(workspace_id)
        warehouse_names = [wh.display_name for wh in warehouses]
        self.assertGreater(len(warehouses), 0)
        self.assertIn(warehouse1, warehouse_names)

        warehouse = fc.get_warehouse(workspace_id, warehouse_name=warehouse1)
        self.assertIsNotNone(warehouse.id)
        self.assertEqual(warehouse.display_name, warehouse1)

        warehouse2 = fc.update_warehouse(workspace_id, warehouse.id, display_name=f"{warehouse1}2")
        warehouse = fc.get_warehouse(workspace_id, warehouse_id=warehouse.id)
        self.assertEqual(warehouse.display_name, f"{warehouse1}2")
        self.assertEqual(warehouse.id, warehouse2.id)

        status_code = fc.delete_warehouse(workspace_id, warehouse.id)
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()