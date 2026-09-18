class Insurance:
    CompanyName = 'SafeDrive'
    HeadOffice = 'Chennai'

    def __init__(self, name, policy_no, pin, sum_assured):
        self.name = name
        self.__policy_no = policy_no
        self.__pin = pin
        self.__sum_assured = sum_assured
        self.__premium = 0
        self.__last_transaction = 'No transaction yet done'

    def __authenticate(self):
        Policy_no = int(input('🔑 Enter Policy Number: '))
        Pin = int(input('🔢 Enter PIN: '))
        return Policy_no == self.__policy_no and Pin == self.__pin

    def __generate_receipt(self, type, amount):
        return f'''
╔══════════════════════════════════════════════════╗
║          🧾 SAFEDRIVE TRANSACTION RECEIPT        ║
╠══════════════════════════════════════════════════╣
║ 🏢 Company          : {self.CompanyName}
║ 📍 Head Office      : {self.HeadOffice}
║ 🚗 Vehicle Category : {self.VehicleCategory}
║ 👤 Policy Holder    : {self.name}
║ 🔢 Policy Number    : {self.__policy_no}
║ 🔄 Transaction Type  : {type}
║ 💰 Transaction Amt  : ₹{amount:,.2f}
║ 🛡️ Sum Assured      : ₹{self.__sum_assured:,.2f}
║ 💳 Current Premium  : ₹{self.__premium:,.2f}
╚══════════════════════════════════════════════════╝
'''

    def __calculate_base_premium(self):
        return self.__sum_assured * 0.03

    def buy_policy(self):
        premium = self.__calculate_base_premium()
        self.__premium = premium
        self.__last_transaction = self.__generate_receipt('BUY POLICY', premium)
        print('\n✅ Policy purchased successfully!')
        print(f'💳 Initial Premium: ₹{premium:,.2f}')

    def pay_premium(self):
        if self.__authenticate():
            print('\n🔓 Authentication Successful!')
            amount = int(input('💰 Enter Premium Amount to Pay: ₹'))
            if amount > 0:
                self.__premium += amount
                self.__last_transaction = self.__generate_receipt('PAY PREMIUM', amount)
                print('\n✅ Premium paid successfully!')
                print(f'💰 Amount Paid   : ₹{amount:,.2f}')
                print(f'💳 Total Premium : ₹{self.__premium:,.2f}')
            else:
                print('❌ Invalid amount!')
        else:
            print('❌ Authentication Failed!')

    def claim_policy(self):
        if self.__authenticate():
            print('\n🔓 Authentication Successful!')
            amount = int(input('💰 Enter Claim Amount: ₹'))
            if amount > 0 and amount <= self.__sum_assured:
                self.__sum_assured -= amount
                self.__last_transaction = self.__generate_receipt('CLAIM', amount)
                print('\n✅ Claim processed successfully!')
                print(f'💰 Claim Amount     : ₹{amount:,.2f}')
                print(f'🛡️ Remaining Amount : ₹{self.__sum_assured:,.2f}')
            else:
                print('❌ Invalid claim or amount exceeds Sum Assured!')
        else:
            print('❌ Authentication Failed!')

    def show_policy_details(self):
        if self.__authenticate():
            print('''
╔══════════════════════════════════════════════════╗
║             📋 POLICY DETAILS                    ║
╠══════════════════════════════════════════════════╣
''')
            print(f'║ 🏢 Company          : {self.CompanyName}')
            print(f'║ 📍 Head Office      : {self.HeadOffice}')
            print(f'║ 🚗 Vehicle Category : {self.VehicleCategory}')
            print(f'║ 👤 Policy Holder    : {self.name}')
            print(f'║ 🔢 Policy Number    : {self.__policy_no}')
            print(f'║ 🛡️ Sum Assured      : ₹{self.__sum_assured:,.2f}')
            print(f'║ 💳 Current Premium  : ₹{self.__premium:,.2f}')
            print('''╚══════════════════════════════════════════════════╝
''')
        else:
            print('❌ Authentication Failed!')

    def show_premium(self):
        if self.__authenticate():
            print(f'''
╔════════════════════════════════════════════╗
║             💳 PREMIUM DETAILS             ║
╠════════════════════════════════════════════╣
║ 💰 Current Premium : ₹{self.__premium:,.2f}
╚════════════════════════════════════════════╝
''')
        else:
            print('❌ Authentication Failed!')

    def list_last_transaction(self):
        if self.__authenticate():
            print('\n🔓 Authentication Successful!')
            print(self.__last_transaction)
        else:
            print('❌ Authentication Failed!')


class CarInsurance(Insurance):
    VehicleCategory = 'Four Wheeler - Car'

    def __init__(self, name, policy_no, pin, sum_assured, car_number):
        super().__init__(name, policy_no, pin, sum_assured)
        self.__car_number = car_number

    def _Insurance__calculate_base_premium(self):
        return self._Insurance__sum_assured * 0.05


class BikeInsurance(Insurance):
    VehicleCategory = 'Two Wheeler - Bike'

    def __init__(self, name, policy_no, pin, sum_assured, bike_number):
        super().__init__(name, policy_no, pin, sum_assured)
        self.__bike_number = bike_number

    def _Insurance__calculate_base_premium(self):
        return self._Insurance__sum_assured * 0.02


car1 = CarInsurance('Bablu', 630514, 2255, 500000, 'TN01AB1234')
bike1 = BikeInsurance('Ramu', 720811, 1122, 100000, 'TN02CD5678')


while True:
    print('''
╔══════════════════════════════════════════════════╗
║          🚘 WELCOME TO SAFEDRIVE INSURANCE 🚘    ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  1️⃣  Buy Policy                                 ║
║  2️⃣  Pay Premium                                ║
║  3️⃣  Claim Policy                               ║
║  4️⃣  Show Policy Details                        ║
║  5️⃣  Show Premium                               ║
║  6️⃣  List Last Transaction                      ║
║  7️⃣  Exit                                       ║
║                                                  ║
╚══════════════════════════════════════════════════╝
''')

    try:
        choice = int(input('👉 Enter your choice: '))
    except ValueError:
        print('❌ Please enter a valid number!')
        continue

    if choice in range(1, 7):
        Vehicle_choice = input('🚗 Select Vehicle (car / bike): ').strip().lower()
        obj = car1 if Vehicle_choice == 'car' else bike1 if Vehicle_choice == 'bike' else None

        if obj is None:
            print('''
❌ Invalid Vehicle!

👉 Please type:
   🚗 car
   🏍️ bike
''')
            continue

    if choice == 1:
        obj.buy_policy()
    elif choice == 2:
        obj.pay_premium()
    elif choice == 3:
        obj.claim_policy()
    elif choice == 4:
        obj.show_policy_details()
    elif choice == 5:
        obj.show_premium()
    elif choice == 6:
        obj.list_last_transaction()
    elif choice == 7:
        print('''
╔══════════════════════════════════════════════════╗
║                                                  ║
║       🙏 THANK YOU FOR CHOOSING SAFEDRIVE       ║
║                                                  ║
║              🚘 DRIVE SAFE! 🛡️                  ║
║                                                  ║
╚══════════════════════════════════════════════════╝
''')
        break
    else:
        print('❌ Enter a valid choice number!')
