# Creating a Logger
import logging
import sys
import random
from datetime import datetime


# logger = logging.getLogger(__name__)
# stream_handler = logging.StreamHandler(sys.stdout)
# logger.addHandler(stream_handler)
#
# # Print logging levels (0 - 50)
# print(logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
#
# logger.setLevel(logging.DEBUG)
#
#
# def division():
#     logger.debug("Starting Division!")
#     try:
#         dividend = float(input("Enter the dividend: "))
#         logger.info(dividend)
#         divisor = float(input("Enter the divisor: "))
#         logger.info(divisor)
#     except SyntaxError:
#         logger.log(logging.CRITICAL, 'No dividend or divisor value entered!')
#         return
#     if divisor == 0:
#         logger.error('Attempting to divide by 0!')
#         return
#     else:
#         return dividend / divisor
#
#
# result = division()
#
# if result is None:
#     logger.warning('The result value is None!')

# _________________________________________________________________________________
# Logging to a file and console

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('output.log')
# stream_handler = logging.StreamHandler(sys.stdout)
#
# formatter1 = logging.Formatter("[%(asctime)s] {%(levelname)s} %(name)s: #%(lineno)d - %(message)s")
# file_handler.setFormatter(formatter1)
#
# formatter2 = logging.Formatter("[%(asctime)s] {%(levelname)s} - %(message)s")
# stream_handler.setFormatter(formatter2)
#
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
#
#
#
# def division():
#     logger.debug("Starting Division!")
#     try:
#         dividend = float(input("Enter the dividend: "))
#         logger.info(dividend)
#         divisor = float(input("Enter the divisor: "))
#         logger.info(divisor)
#     except SyntaxError:
#         logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
#         return
#     if divisor == 0:
#         logger.error("Attempting to divide by 0!")
#         return
#     else:
#         return dividend / divisor
#
#
# result = division()
# if result == None:
#     logger.warning("The result value is None!")

# _________________________________________________________________________________
# Using basicConfig()
# logger = logging.getLogger(__name__)
#
# logging.basicConfig(filename='basic_config.log', level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')
#
#
# def division():
#     logger.debug("Starting Division!")
#     try:
#         dividend = float(input("Enter the dividend: "))
#         logger.info(dividend)
#         divisor = float(input("Enter the divisor: "))
#         logger.info(divisor)
#     except SyntaxError:
#         logger.log(logging.CRITICAL, "No dividend or divisor value entered!")
#         return
#     if divisor == 0:
#         logger.error("Attempting to divide by 0!")
#         return
#     else:
#         return dividend / divisor
#
#
# result = division()
# if result == None:
#     logger.warning("The result value is None!")

# ____________________________________________________________________
# ATM Logging project

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('formatted.log')

formatter = logging.Formatter("[%(asctime)s] - %(message)s")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

logger.setLevel(logging.INFO)


class BankAccount:
    def __init__(self):
        self.balance = 100
        print("Hello! Welcome to the ATM Depot!")

    def authenticate(self):
        while True:
            pin = int(input("Enter account pin: "))
            if pin != 1234:
                logger.error("Error! Invalid pin. Try again.")
            else:
                return None

    def deposit(self):
        try:
            amount = float(input("Enter amount to be deposited: "))
            if amount < 0:
                logger.warning("Warning! You entered a negative number to deposit.")
            self.balance += amount
            logger.info("Amount Deposited: ${amount}".format(amount=amount))
            logger.info("Transaction Info:")
            logger.info("Status: Successful")
            logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
        except ValueError:
            logger.error("Error! You entered a non-number value to deposit.")
            logger.info("Transaction Info:")
            logger.info("Status: Failed")
            logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))

    def withdraw(self):
        try:
            amount = float(input("Enter amount to be withdrawn: "))
            if self.balance >= amount:
                self.balance -= amount
                logger.info("You withdrew: ${amount}".format(amount=amount))
                logger.info("Transaction Info:")
                logger.info("Status: Successful")
                logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
            else:
                logger.error("Error! Insufficient balance to complete withdraw.")
                logger.info("Transaction Info:")
                logger.info("Status: Failed")
                logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
        except ValueError:
            logger.error("Error! You entered a non-number value to withdraw.")
            logger.info("Transaction Info:")
            logger.info("Status: Failed")
            logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))

    def display(self):
        print("Available Balance = ${balance}".format(balance=self.balance))


acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
