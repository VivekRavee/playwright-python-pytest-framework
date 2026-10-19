from flows.login_flow import LoginFlow
from flows.home_flow import HomeFlow



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

            flow_instance = flow_class(
                self.page,
                self.testcase_id
            )

            flow_instance.execute(
                testdata
            )