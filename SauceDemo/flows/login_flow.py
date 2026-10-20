import allure

from pages.login_page import LoginPage
from utilities.evidence_manager import EvidenceManager
from utilities.execution_evidence import ExecutionEvidence


class LoginFlow:

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

        login_page = LoginPage(
            self.page
        )

        #
        # Step 1 - Login Page
        #
        login_page_shot = (
            EvidenceManager.capture_screenshot(
                self.page,
                self.testcase_id,
                "login_page"
            )
        )

        ExecutionEvidence.add_step(
            step_name="Login Page Displayed",

            description=
            "Navigate to Login Page",

            validation=
            "Verify Login Page is displayed successfully",

            screenshot=login_page_shot
        )

        #
        # Step 2 - Enter Credentials
        #
        login_page.login_creds(
            testdata["username"],testdata["password"]
        )

        credentials_shot = (
            EvidenceManager.capture_screenshot(
                self.page,
                self.testcase_id,
                "credentials_entered"
            )
        )

        ExecutionEvidence.add_step(
            step_name="Credentials Entered",

            description=
            "Enter valid username and password",

            validation=
            "Verify credentials are entered successfully",

            screenshot=credentials_shot
        )

        #
        # Step 3 - Click Login
        #
        login_page.loginSubmit()

        #
        # Step 4 - Login Validation
        #
        login_page.verify_login_success()

        success_shot = (
                EvidenceManager.capture_screenshot(
                    self.page,
                    self.testcase_id,
                    "login_success"
                )
        )

        ExecutionEvidence.add_step(
                step_name="Login Successful",

                description=
                "Click Login button",

                validation=
                "Verify user is successfully navigated to Inventory page",

                screenshot=success_shot
        )

        with allure.step(
                "Login Successful"
            ):
                allure.attach.file(
                    success_shot,
                    name="Login Success",
                    attachment_type=
                    allure.attachment_type.PNG
        )

        