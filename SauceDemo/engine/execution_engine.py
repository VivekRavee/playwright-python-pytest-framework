from utilities.config_reader import ConfigReader
from engine.runner_parser import RunnerParser
from engine.testdata_loader import TestDataLoader
from engine.flow_executor import FlowExecutor

from utilities.execution_evidence import ExecutionEvidence
from utilities.business_report import BusinessReport

from pathlib import Path
import allure
import json
import time


class ExecutionEngine:

    def __init__(self, browser):
        self.browser = browser

    def start_execution(self):

        Path(
            "screenshots"
        ).mkdir(
            exist_ok=True
        )

        Path(
            "reports/traces"
        ).mkdir(
            parents=True,
            exist_ok=True
        )

        execution_start_time = time.time()

        execution_list = (
            RunnerParser.get_execution_list()
        )

        for testcase in execution_list:

            print("\n")
            print("=" * 50)
            print(
                f"Running : "
                f"{testcase['testcase_id']}"
            )

            context = (
                self.browser.new_context()
            )

            page = None

            context.tracing.start(
                screenshots=True,
                snapshots=True,
                sources=True
            )

            try:

                # Start Evidence Collection
                ExecutionEvidence.start_testcase(
                    testcase
                )

                # Allure Title
                allure.dynamic.title(
                    f"{testcase['testcase_id']} - "
                    f"{testcase['testcase_name']}"
                )

                # Allure Description
                allure.dynamic.description(
                    f"""
Description : {testcase['description']}

Flow : {testcase['flow']}

Environment : {testcase['environment']}

Test Data File : {testcase['testdata_file']}

Dataset : {testcase['dataset']}
"""
                )

                page = context.new_page()

                url = (
                    ConfigReader.get_config(
                        testcase["environment"]
                    )["base_url"]
                )

                page.goto(url)

                testdata = (
                    TestDataLoader.load_testdata(
                        testcase["testdata_file"],
                        testcase["dataset"]
                    )
                )

                # Attach Test Data
                allure.attach(
                    json.dumps(
                        testdata,
                        indent=4
                    ),
                    name="Test Data",
                    attachment_type=
                    allure.attachment_type.JSON
                )

                flow_executor = (
                    FlowExecutor(
                        page=page,
                        testcase_id=
                        testcase["testcase_id"]
                    )
                )

                flow_executor.execute(
                    testcase["flow"],
                    testdata
                )

                # Mark PASS
                ExecutionEvidence.end_testcase(
                    status="PASS"
                )

                print(
                    f"{testcase['testcase_id']} "
                    f": PASS"
                )

            except Exception as e:

                screenshot_path = (
                    f"screenshots/"
                    f"{testcase['testcase_id']}"
                    f"_failure.png"
                )

                if page:

                    page.screenshot(
                        path=screenshot_path,
                        full_page=True
                    )

                    allure.attach.file(
                        screenshot_path,
                        name="Failure Screenshot",
                        attachment_type=
                        allure.attachment_type.PNG
                    )

                # Attach Exception Details
                allure.attach(
                    str(e),
                    name="Failure Reason",
                    attachment_type=
                    allure.attachment_type.TEXT
                )

                # Mark FAIL
                ExecutionEvidence.end_testcase(
                    status="FAIL",
                    failure_reason=str(e)
                )

                print(
                    f"Screenshot captured : "
                    f"{screenshot_path}"
                )

                print(
                    f"{testcase['testcase_id']} "
                    f": FAIL"
                )

                print(
                    f"Reason : "
                    f"{str(e)}"
                )

                continue

            finally:

                trace_file = (
                    f"reports/traces/"
                    f"{testcase['testcase_id']}.zip"
                )

                try:

                    context.tracing.stop(
                        path=trace_file
                    )

                    print(
                        f"Trace saved : "
                        f"{trace_file}"
                    )

                except Exception as trace_error:

                    print(
                        f"Trace generation failed : "
                        f"{trace_error}"
                    )

                context.close()

        execution_end_time = time.time()

        total_execution_time = round(
            execution_end_time -
            execution_start_time,
            2
        )

        # Generate Business Reports
        BusinessReport.generate_reports(
            ExecutionEvidence.execution_results,
            total_execution_time
        )

        print("\n")
        print("=" * 50)
        print(
            "Business Reports Generated"
        )
        print(
            f"Total Execution Time : "
            f"{total_execution_time} sec"
        )
        print(
            "Location : reports/business"
        )
        print(
            "Trace Location : reports/traces"
        )
        print("=" * 50)