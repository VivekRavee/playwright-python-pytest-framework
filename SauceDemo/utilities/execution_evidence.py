import time


class ExecutionEvidence:

    execution_results = []

    current_testcase = None

    @classmethod
    def start_testcase(
            cls,
            testcase):

        cls.current_testcase = {
            "testcase_id":
                testcase["testcase_id"],

            "testcase_name":
                testcase["testcase_name"],

            "description":
                testcase["description"],

            "environment":
                testcase["environment"],

            "steps": [],

            "start_time":
                time.time()
        }

    @classmethod
    def add_step(
            cls,
            step_name,
            description,
            validation,
            screenshot):

        cls.current_testcase["steps"].append(
            {
                "step_name": step_name,
                "description": description,
                "validation": validation,
                "screenshot": screenshot
            }
        )

    @classmethod
    def end_testcase(
            cls,
            status,
            failure_reason=""):

        end_time = time.time()

        cls.current_testcase[
            "duration"
        ] = round(
            end_time -
            cls.current_testcase[
                "start_time"
            ],
            2
        )

        cls.current_testcase[
            "status"
        ] = status

        cls.current_testcase[
            "failure_reason"
        ] = failure_reason

        cls.execution_results.append(
            cls.current_testcase
        )