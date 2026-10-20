from flows.login_flow import LoginFlow
from flows.home_flow import HomeFlow

from utilities.evidence_manager import EvidenceManager
from utilities.execution_evidence import ExecutionEvidence


class FlowExecutor:

    FLOW_MAP = {
        "LOGIN": LoginFlow,
        "HOME": HomeFlow
    }

    def __init__(
        self,
        page,
        testcase_id
    ):
        self.page = page
        self.testcase_id = testcase_id

    def execute(
        self,
        flow_name,
        testdata
    ):

        flow_steps = flow_name.split(">")

        for step in flow_steps:

            step = step.strip().upper()

            print(
                f"Executing Flow Step : {step}"
            )

            flow_class = self.FLOW_MAP.get(
                step
            )

            if not flow_class:

                raise Exception(
                    f"Unknown Flow Step : {step}"
                )

            try:

                flow_instance = flow_class(
                    self.page,
                    self.testcase_id
                )

                flow_instance.execute(
                    testdata
                )

            except Exception as e:

                failure_shot = (
                    EvidenceManager.capture_screenshot(
                        self.page,
                        self.testcase_id,
                        f"{step.lower()}_failure"
                    )
                )

                ExecutionEvidence.add_step(
                    step_name=f"{step} Failed",
                    description=f"Failure during {step}",
                    validation=str(e),
                    screenshot=failure_shot
                )

                # Re-throw
                raise