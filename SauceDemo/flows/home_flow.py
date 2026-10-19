import allure

from pages.home_page import HomePage
from utilities.evidence_manager import EvidenceManager
from utilities.execution_evidence import ExecutionEvidence


class HomeFlow:

    def __init__(
        self,
        page,
        testcase_id
    ):
        self.page = page
        self.testcase_id = testcase_id

    def execute(
        self,
        testdata
    ):

        home_page = HomePage(
            self.page
        )

        with allure.step(
            "Verify Products Page"
        ):

            if home_page.verify_home_page():

                screenshot = (
                    EvidenceManager.capture_screenshot(
                        self.page,
                        self.testcase_id,
                        "products_page"
                    )
                )

                ExecutionEvidence.add_step(
                    step_name=
                    "Products Page Displayed",

                    description=
                    "User successfully navigated to Products page after login.",

                    validation=
                    "Verify Products page is displayed successfully.",

                    screenshot=screenshot
                )

            else:

                screenshot = (
                    EvidenceManager.capture_screenshot(
                        self.page,
                        self.testcase_id,
                        "products_page_failure"
                    )
                )

                ExecutionEvidence.add_step(
                    step_name=
                    "Products Page Validation Failed",

                    description=
                    "Products page was not displayed.",

                    validation=
                    "Verify Products page is displayed successfully.",

                    screenshot=screenshot
                )

                raise Exception(
                    "Products Page not displayed"
                )
