from typing import Union

from pydantic import BaseModel


class Transaction(BaseModel):
	"""Payok API transaction model"""

	transaction: int
	email: str
	amount: float
	currency: str
	currency_amount: float
	comission_percent: float
	comission_fixed: float
	amount_profit: float
	method: Union[str, None]
	payment_id: Union[int, str]
	description: str
	date: str
	pay_date: str
	transaction_status: int
	custom_fields: str
	webhook_status: int
	webhook_amount: int


class Balance(BaseModel):
	"""Payok API balance model"""

	balance: float
	ref_balance: float


class Payout(BaseModel):
	"""Payok API payout model"""

	payout_id: int
	method: Union[str, None]
	amount: float
	comission_percent: float
	comission_fixed: float
	amount_profit: float
	date_create: str
	date_pay: str
	status: str


class DataPayout(BaseModel):
	"""Payok API payout model"""
	payout_id: int
	method: str
	amount: float
	comission_percent: float
	comission_fixed: float
	amount_profit: float
	date: str
	payout_status_code: int
	payout_status_text: str


class CreatedPayout(BaseModel):
	"""Payok API created payout model"""

	status: str
	remain_balance: float
	data: DataPayout
