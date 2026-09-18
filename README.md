# 🚗 Vehicle Insurance Management System

A console-based **Vehicle Insurance Management System** developed using **Python and Object-Oriented Programming (OOP)**.

The project supports **Car Insurance** and **Bike Insurance** with policy purchase, premium payment, claim processing, policy details, authentication, premium tracking, and transaction receipts.

## ✨ Features

- 🔐 Policy authentication using Policy Number and PIN
- 🚗 Car Insurance
- 🏍️ Bike Insurance
- 📄 Buy Policy
- 💳 Pay Premium
- 🏥 Claim Policy
- 📋 Show Policy Details
- 💰 Show Current Premium
- 🧾 Generate Transaction Receipt
- 🔄 Track Last Transaction
- ❌ Input validation
- 🚪 Menu-driven console application

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python IDLE / any Python IDE

## 🧠 OOP Concepts Used

### Encapsulation

Sensitive policy information is kept inside the `Insurance` class using private attributes and private methods.

**Private attributes:**

```python
self.__policy_no
self.__pin
self.__sum_assured
self.__premium
self.__last_transaction
```

**Private methods:**

```python
__authenticate()
__generate_receipt()
__calculate_base_premium()
```

### Inheritance

`CarInsurance` and `BikeInsurance` inherit the common insurance functionality from the `Insurance` parent class.

```python
class CarInsurance(Insurance):
    ...

class BikeInsurance(Insurance):
    ...
```

### Method Overriding / Polymorphism

The child classes provide different premium calculation rates by overriding the parent's private premium-calculation method:

- 🚗 Car Insurance: **5% of Sum Assured**
- 🏍️ Bike Insurance: **2% of Sum Assured**
- 🛡️ Base Insurance: **3% of Sum Assured**

## 📂 Project Structure

```text
Vehicle-Insurance-Management-System/
│
├── src/
│   └── insurance_management.py
│
├── demo/
│   └── safedrive-insurance-demo.mp4
│
├── screenshots/
│   ├── 01-main-menu.png
│   ├── 02-buy-policy.png
│   ├── 03-claim-and-policy-details.png
│   ├── 04-last-transaction-receipt.png
│   └── 05-premium-and-exit.png
│
├── README.md
├── LICENSE
└── .gitignore
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/kirthika-2005/Vehicle-Insurance-Management-System.git
```

### 2. Open the project folder

```bash
cd Vehicle-Insurance-Management-System
```

### 3. Run the program

```bash
python src/insurance_management.py
```

No external Python packages are required.

## 🔑 Demo Accounts

### 🚗 Car Insurance

| Detail | Value |
|---|---|
| Policy Holder | Bablu |
| Policy Number | 630514 |
| PIN | 2255 |
| Sum Assured | ₹5,00,000 |
| Vehicle Number | TN01AB1234 |
| Category | Four Wheeler - Car |

### 🏍️ Bike Insurance

| Detail | Value |
|---|---|
| Policy Holder | Ramu |
| Policy Number | 720811 |
| PIN | 1122 |
| Sum Assured | ₹1,00,000 |
| Vehicle Number | TN02CD5678 |
| Category | Two Wheeler - Bike |

> These credentials are included only for project demonstration purposes.

## 💡 Main Operations

### 1. Buy Policy

Calculates the initial premium according to the selected vehicle type and stores the transaction receipt.

### 2. Pay Premium

Authenticates the policy holder and adds the entered amount to the current premium.

### 3. Claim Policy

Authenticates the policy holder and processes a claim when the amount is positive and does not exceed the available Sum Assured.

### 4. Show Policy Details

Displays company, head office, vehicle category, policy holder, policy number, remaining Sum Assured, and current premium.

### 5. Show Premium

Displays the current premium after successful authentication.

### 6. List Last Transaction

Displays the latest stored transaction receipt after successful authentication.

## 🧾 Transaction Receipt

The generated receipt contains:

- Company Name
- Head Office
- Vehicle Category
- Policy Holder
- Policy Number
- Transaction Type
- Transaction Amount
- Sum Assured
- Current Premium

## 🔐 Authentication

Protected operations verify:

```text
Policy Number + PIN
```

If authentication fails, the requested protected operation is not performed.

## 🎥 Project Running Video

A compressed screen recording of the project execution is included in the `demo` folder.

**[▶️ Watch / Open SafeDrive Project Demo](demo/safedrive-insurance-demo.mp4)**

> The included MP4 has been compressed to keep the GitHub upload package below 25 MB.

## 🖥️ Project Output Screenshots

### Main Menu

![Main Menu](screenshots/01-main-menu.png)

### Buy Policy

![Buy Policy](screenshots/02-buy-policy.png)

### Claim and Policy Details

![Claim and Policy Details](screenshots/03-claim-and-policy-details.png)

### Last Transaction Receipt

![Last Transaction Receipt](screenshots/04-last-transaction-receipt.png)

### Premium Details and Exit

![Premium Details and Exit](screenshots/05-premium-and-exit.png)

## 🎯 Project Objective

The objective of this project is to build a simple vehicle insurance application while applying **Python OOP concepts such as Encapsulation, Inheritance, and Method Overriding/Polymorphism** in a practical console-based system.

## 👩‍💻 Author

**Kirthika**

GitHub: https://github.com/kirthika-2005
