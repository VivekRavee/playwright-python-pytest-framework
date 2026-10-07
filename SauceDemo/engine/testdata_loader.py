from utilities.json_reader import JsonReader
class TestDataLoader:
    @staticmethod
    def load_testdata(file_name, dataset):
        path = f"testdata/{file_name}"
        data = JsonReader.read_json(path)
        return data[dataset]