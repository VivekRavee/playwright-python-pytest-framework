from engine.runner_parser import RunnerParser
from engine.testdata_loader import TestDataLoader
from engine.flow_executor import FlowExecutor
class ExecutionEngine: 
    def __init__(self, page):
        self.page = page
    def start_execution(self):
        execution_list = (RunnerParser.get_execution_list())
        for testcase in execution_list:
            print("\n")
            print("=" * 50)
            print(f"Running : "f"{testcase['testcase_id']}")
            testdata = (TestDataLoader.load_testdata(testcase["testdata_file"],testcase["dataset"]))
            flow_executor = (FlowExecutor(self.page))
            flow_executor.execute(testcase["flow"],testdata)