from pharmacy import Pharmacy
from clear import clear

p = Pharmacy()


# Execution function associated with pharmacy management classes
def run():
    while True:
        clear()
        # The primary page for user login
        choice = input("1.Login\n2.manager\n3.Exit\n")
        if choice == "1":
            clear()

            username = input("please enter username: ")
            password = input("please enter password")
            p.logoin(username, password)
            if username in p.pharmacist:
                while True:
                    clear()
                    # Pharmacy Attendant Page
                    choice = input(
                        "1.Adding medication\n2.See Medication Inventory\n3.See Prescriptions\n4.Prescription Payment\n5.Exit\n")
                    if choice == "1":
                        clear()
                        drug_name = input("enter drug name: ")
                        quantity = int(input("enter quantity: "))
                        price = int(input("enter price: "))
                        p.add_drugs(drug_name, quantity, price)
                    elif choice == "2":
                        clear()
                        p.view_inventory()
                    elif choice == "3":
                        clear()
                        p.view_prescriptions()
                    elif choice == "4":
                        clear()
                        patient_pharmacist = input("enter patient name: ")
                        if patient_pharmacist in p.patient:
                            clear()
                            p.Prescription_Payment(patient_pharmacist)
                        else:
                            clear()
                            print("The patient does not have the doctor's approval")
                    elif choice == "5":
                        break
                    else:
                        clear()
                        print("invalid chice!!")
            elif username in p.doctors:
                while True:
                    clear()
                    # Doctor's Plate
                    choice = input(
                        "1.Adding medication\n2.See Medication Inventory\n3.See Prescriptions\n4.create prescription\n5.Confirm\n6.Exit\n")
                    if choice == "1":
                        clear()
                        drug_name = input("enter drug name: ")
                        quantity = int(input("enter quantity: "))
                        price = int(input("enter price: "))
                        p.add_drugs(drug_name, quantity, price)
                    elif choice == "2":
                        clear()
                        p.view_inventory()
                    elif choice == "3":
                        clear()
                        p.view_prescriptions()
                    elif choice == "4":
                        clear()
                        patient_doctor = input("enter patiant name: ")
                        drug_name = input("enter drug name(,): ").split(",")
                        p.create_prescription(patient_doctor, drug_name)
                    elif choice == "5":
                        clear()
                        patient = input("enter patien: ")
                        p.Doctor_confirm(patient)
                    elif choice == "6":
                        break
                    else:
                        clear()
                        print("invalid chice!!")
        elif choice == "2":
            clear()
            # Pharmacy Manager Login Page
            x = input("enter password: ")
            if p.is_manager(x):
                while True:
                    clear()
                    choice = input("1.adding user\n2.See Inventory\n3.Logout\n")
                    if choice == "1":
                        clear()
                        us_name = input("enter user name: ")
                        psword = input("enter password: ")
                        rl = input("enter role: ")
                        p.add_user(us_name, psword, rl)
                    elif choice == "2":
                        clear()
                        p.view_inventory()
                    elif choice == "3":
                        clear()
                        p.logout(p.manager)
                    else:
                        clear()
                        print("invalid chice!!")
        # User logging out
        elif choice == "3":
            clear()
            print("goodbye!")
            break
        else:
            clear()
            print("invalid chice!!")


run()
