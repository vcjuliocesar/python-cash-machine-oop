""" Module Value Objects
"""

import uuid

userId = uuid.UUID
_registered:bool = False

INITIALIZE_BALANCE_AMOUNT:int = 11000
INITIALIZE_CREDIT_BALANCE_AMOUNT:int = 500
EMPTY_BALANCE:int = 0
MAX_AMOUNT_AVAILABLE:int = 100000000
MIN_AMOUNT_AVAILABLE:int = 10

FEE:float = 0.05
LIMIT_CREDIT:int = 400000

    