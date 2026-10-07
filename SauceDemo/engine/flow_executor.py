class FlowExecutor:
    def __init__(self, page):
        self.page = page
    def execute(self, flow_name, testdata):
        flow_steps = flow_name.split(">")
        for step in flow_steps:
            step = step.strip().upper()
            print(f"Executing Flow Step : {step}")
            if step == "LOGIN":
                self.execute_login(testdata)
            elif step == "HOME":
                self.execute_home()
            elif step == "CATALOG":
                self.execute_catalog()
            elif step == "CART":
                self.execute_cart()
            elif step == "CHECKOUT":
                self.execute_checkout()
            else:
                raise Exception(f"Unknown Flow Step : {step}")
    def execute_login(self, testdata):
        print("Login Flow")
    def execute_home(self):
        print("Home Flow")
    def execute_catalog(self):
        print("Catalog Flow")
    def execute_cart(self):
        print("Cart Flow")
    def execute_checkout(self):
        print("Checkout Flow")