from user import User
from functools import wraps


# Class for pharmacy management that is related to the class of users
class Pharmacy:
    # Necessary Attributions for Pharmacy Management
    def __init__(self):
        self.pharmacist = {}
        self.doctors = {}
        self.drogs = {}
        self.manager = ""
        self.patient = []
        self.current_user = {}
        self.prescription = {}

    # A decorator that allows access to different methods
    def role_required(roles=[]):
        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                for r in roles:
                    if list(self.current_user.values())[0] == r:
                        func(self, *args, **kwargs)

            return wrapper

        return decorator

    # A method for adding users and allowing access to them
    @role_required(["manager"])
    def add_user(self, username: str, password: str, role: str):
        user = User(username, password, role)
        if role == "pharmacist":
            self.pharmacist[user.username] = [user.password, user.role]
        elif role == "doctor":
            self.pharmacist[user.username] = [user.password, user.role]

    # A method for logging in users who have access
    def logoin(self, username: str, password: str):
        if type(username) and type(password) != str:
            raise TypeError
        if (username in self.pharmacist) and (password == self.pharmacist.get(username)[0]):
            print(f"welcame {username}")
            self.current_user = {username: "pharmacist"}

        elif (username in self.doctors) and (password == self.doctors.get(username)[0]):
            print(f"welcame {username}")
            self.current_user = {username: "doctor"}

        else:
            print("user not found")

    # A method for logging out the user
    def logout(self, username: str):
        print(f"goodbye {username}")
        self.current_user = None

    # Method for adding medication
    @role_required(["pharmacist", "doctor"])
    def add_drugs(self, drug_name: str, quantity: int, price: float):
        if type(drug_name) == str:
            raise TypeError
        if drug_name in self.drogs:
            self.drogs[drug_name][0] += quantity
            self.drogs[drug_name][1] = price
        else:
            self.drogs[drug_name] = [quantity, price]
        print(f" added {quantity} of {drug_name}")

    # A method for seeing medications and their quantity
    @role_required(["pharmacist", "doctor", "manager"])
    def view_inventory(self):
        for d, q in self.drogs.items():
            print(f"{d}:{q}")
        else:
            print('There are no medications')

    # A Method for Writing a Prescription by a Doctor
    @role_required(["doctor"])
    def create_prescription(self, patient: str, drug_neme: list):
        for drug in drug_neme:
            if drug in self.drogs:
                print(self.drogs.get(drug)[0])
                if self.drogs.get(drug)[0] != 0:
                    self.prescription[patient] = list(drug)
                    print(f"prescription created for {patient}")
                else:
                    print("Not enough inventory")
            elif drug == '':
                pass

            else:
                print(f"{drug} not available")

    # A method for seeing written versions
    @role_required(["pharmacist", "doctor"])
    def view_prescriptions(self):
        print("current prescription")
        print("patient\tdrugs")
        for i in range(0, len(self.prescription)):
            print(f"patiet: {list(self.prescription.keys())[i]}\tdrugs:{list(self.prescription.values())[i]}")

    # Method for Prescription Approval by a Doctor
    @role_required(["doctor"])
    def Doctor_confirm(self, patient: str):
        print(self.prescription[patient])
        ok = input(" ok or no? ")
        if ok.upper() == "OK":
            self.patient.append(patient.upper())
        else:
            print('The medicine is wrong')

    # Method to pay for the prescription and see the cost of the prescription
    @role_required(["pharmacist"])
    def Prescription_Payment(self, patient: str):
        price = 0
        for d in self.prescription[patient]:
            price += self.drogs[d][1]
        print(f"Amount Payable: {price}")

    # Method that manages the entry of the pharmacy manager
    def is_manager(self, x):
        if x == "abc123defg456hijk789":
            self.current_user = {"manager": "manager"}
            return True
        else:
            print("You're not the manager")
