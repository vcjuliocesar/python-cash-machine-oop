"""This module has definition of the Debit entity
"""

from src.domain.entities.user import User
from src.domain.value_objects import INITIALIZE_BALANCE_AMOUNT, INITIALIZE_CREDIT_BALANCE_AMOUNT, MAX_AMOUNT_AVAILABLE, MIN_AMOUNT_AVAILABLE
from src.domain.entities.interfaces.debit_account_interface import DebitAccountInterface


class Debit(DebitAccountInterface):

    def __init__(self, user: User) -> None:

        self.user = user

        self.init_balance = INITIALIZE_BALANCE_AMOUNT - INITIALIZE_CREDIT_BALANCE_AMOUNT

    def balance(self):

        return self.init_balance

    def with_draw(self, amount):

        if amount == 0:

            raise Exception(f"Indica una cantidad mayor a {amount}")

        if amount > self.init_balance:

            raise Exception(f"La cantidad es mayor al saldo disponible")

        if self.init_balance == 0:

            raise Exception("La cuenta esta vacia")

        Debit.update_balance(self.init_balance + amount)

    def saving(amount):

        if amount >= MAX_AMOUNT_AVAILABLE:

            raise Exception(
                f"No se permiten transacciones superiores o iguales a {MAX_AMOUNT_AVAILABLE}")

        if amount < MIN_AMOUNT_AVAILABLE:

            raise Exception(f"No se permiten transacciones menores a {MIN_AMOUNT_AVAILABLE}")
    
    @staticmethod
    def update_balance(self, new_balance):

        self.init_balance = new_balance
