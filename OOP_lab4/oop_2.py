class Employee:

    def __init__(self, first_name, last_name, email, gross_salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__gross_salary = gross_salary
        self.__ssm_signed = False

    def sign_ssm(self):
        self.__ssm_signed = True

    def sign_presence(self):
        pass

    def get_net_salary(self):
        return self.__gross_salary

    def pay(self):
        print(
            f'Amount to transfer {self.__first_name} {self.__last_name} {self.get_net_salary()} Ron')


class FullTimeEmployee(Employee):
    pass


class Contractor(Employee):
    pass


class NoTaxEmployee(Employee):
    pass


class PartTimeEmployee(Employee):
    def pay(self):
        return super().pay()


employees = [FullTimeEmployee('Ionut', 'Sergiu', 'Test@tes.com', 3000),
             Contractor('Ionut', 'Zmeu', 'Test@tes.com', 6000),
             PartTimeEmployee('Alex', 'Grigore', 'Test@tes.com', 4000),
             NoTaxEmployee('Elena', 'Sergiu', 'Test@tes.com', 5000)
             ]

for emp in employees:
    emp.pay()

# MRO = Method resolution order
