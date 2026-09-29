from utilities.json_reader import JsonReader
class ConfigReader:
    @staticmethod
    def get_config(environment):
        file_path = f"config/{environment.lower()}.json"
        return JsonReader.read_json(file_path)