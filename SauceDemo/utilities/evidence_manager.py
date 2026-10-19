import allure
from pathlib import Path


class EvidenceManager:

    @staticmethod
    def capture_screenshot(
            page,
            testcase_id,
            step_name):

        Path(
            "screenshots/steps"
        ).mkdir(
            parents=True,
            exist_ok=True
        )

        screenshot_path = (
            f"screenshots/steps/"
            f"{testcase_id}_{step_name}.png"
        )

        page.screenshot(
            path=screenshot_path,
            full_page=True
        )

        allure.attach.file(
            screenshot_path,
            name=step_name,
            attachment_type=
            allure.attachment_type.PNG
        )

        return screenshot_path
