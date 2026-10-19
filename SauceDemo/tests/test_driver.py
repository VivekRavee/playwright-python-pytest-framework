from engine.execution_engine import ExecutionEngine


def test_execution_driver(browser):

    engine = ExecutionEngine(browser)

    engine.start_execution()