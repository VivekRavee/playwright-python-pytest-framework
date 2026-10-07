from utilities.json_reader import JsonReader
class RunnerParser:
    @staticmethod
    def get_execution_list():
        runner_data = JsonReader.read_json("runners/execution_runner.json")
        executable_tests = []
        for row in runner_data["execution_set"]:
            if row["execute"].upper() == "Y":
                executable_tests.append(row)
        return executable_tests