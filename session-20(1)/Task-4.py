# Design a simple abstract class PaymentMethod with an abstract method pay(amount). Then, create two subclasses: Paytm and PhonePe, each implementing pay(amount) to print a different message. Instantiate both and call their pay methods with any amount.

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Paytm(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Paytm")

class PhonePe(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PhonePe")

my_paytm = Paytm()
my_phonepe = PhonePe()
my_paytm.pay(100)
my_phonepe.pay(200)