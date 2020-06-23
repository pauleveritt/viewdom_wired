"""
Different kinds of customers to act as the context.
"""
from dataclasses import dataclass


@dataclass
class Customer:
    name: str


@dataclass
class FrenchCustomer:
    name: str
