from enum import Enum


class Ty(Enum):
	PAY = 'pay'
	BALANCE = 'api/balance'
	TRANSACTIONS = 'api/transaction'
	PAYOUT = 'api/payout'
	PAYOUT_CREATE = 'api/payout_create'


class Method(Enum):
	GET = 'GET'
	POST = 'POST'
	ANY = 'ANY'


class Currencies(str, Enum):
	RUB = 'RUB'
	UAH = 'UAH'
	USD = 'USD'
	EUR = 'EUR'
	RUB2 = 'RUB2'
