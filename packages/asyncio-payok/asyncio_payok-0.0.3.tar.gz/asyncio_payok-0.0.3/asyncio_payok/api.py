from asyncio_payok.payok_base import BaseSession
from typing import Optional, Union
from asyncio_payok.const import *
from urllib.parse import urlencode
from urllib.parse import quote
from hashlib import md5


class PayOk(BaseSession):
	def __init__(
			self,
			api_id: int,
			api_key: str,
			secret_key: Optional[str] = None,
			shop: Optional[int] = None,
			*args, **kwargs
	) -> None:
		self.__api_id = api_id
		self.__api_key = api_key
		self.__secret_key = secret_key
		self.__shop = shop

	async def get_balance(self) -> Balance:
		"""
		get_balance function retrieves the balance for the user.

		Parameters:None

		Returns:
			Balance: An object representing the user's balance."""
		method = Method.POST
		data = {
			'API_ID': self.__api_id,
			'API_KEY': self.__api_key,
		}
		req = await self._send_req(method, Ty.BALANCE, data=data)
		return Balance(**req)

	async def get_transactions(self, payment_id: Optional[int] = None, offset: Optional[int] = None) -> Union[
		Transaction, list[Transaction]]:
		"""
		Async function to retrieve transactions based on payment ID and offset.

		:param payment_id: Optional[int] - The payment ID to filter transactions by.
		:param offset: Optional[int] - The offset for paginating through transactions.
		:return: Union[Transaction, list[Transaction]] - A single transaction or a list of transactions.
		"""
		method = Method.POST
		if shop is None:
			raise ValueError('Shop ID is required')
		data = {
			'API_ID': self.__api_id,
			'API_KEY': self.__api_key,
			'shop': self.__shop,
		}
		if payment_id:
			data['payment_id'] = payment_id
		if offset:
			data['offset'] = offset

		res = list((await self._send_req(method, Ty.TRANSACTIONS, data=data)).values())
		transactions = [Transaction(**x) for x in res if isinstance(x, dict)]
		return transactions[0] if len(transactions) == 1 else transactions

	@staticmethod
	async def __sign(params: list) -> str:
		sign = '|'.join(map(str, params)).encode('utf-8')
		return md5(sign).hexdigest()

	async def create_pay(
			self,
			amount: float,
			payment: Union[int, str],
			currency: Optional[str] = Currencies.RUB.value,
			desc: Optional[str] = 'Description',
			email: Optional[str] = None,
			success_url: Optional[str] = None,
			method: Optional[str] = None,
			lang: Optional[str] = None,
			custom: Optional[str] = None
	) -> str:
		"""
		Generate the payment URL for a given amount, payment method, and other optional parameters.

		Parameters:
		    amount (float): The amount of the payment.
		    payment (Union[int, str]): The payment method.
		    currency (Optional[str]): The currency for the payment (default is RUB).
		    desc (Optional[str]): Description of the payment (default is 'Description').
		    email (Optional[str]): Email associated with the payment.
		    success_url (Optional[str]): URL to redirect to after successful payment.
		    method (Optional[str]): Payment method.
		    lang (Optional[str]): Language for the payment.
		    custom (Optional[str]): Custom parameter for the payment.

		Returns:
		    str: The payment URL.
		"""
		url = self.STATIC_URL + Ty.PAY.value + '?'
		if self.__secret_key:
			data = {
				'amount': amount,
				'payment': payment,
				'shop': self.__shop,
				'currency': currency,
				'desc': desc,
				'email': email,
				'success_url': success_url,
				'method': method,
				'lang': lang,
				'custom': custom
			}
			for key, value in list(data.items()):
				if value is None:
					del data[key]
			data['sign'] = await self.__sign([*list(data.values())[:5], self.__secret_key])
		else:
			raise Exception('Secret key is required')

		return url + urlencode(data)

	async def get_payout(
			self,
	        payout: Optional[int] = None,
	        offset: Optional[int] = None) -> Union[Payout, list[Payout]]:
		"""
		A description of the entire function, its parameters, and its return types.
		    :param payout: Optional[int] = None
		    :param offset: Optional[int] = None
		    :return: Union[Payout, list[Payout]]
		"""
		method = Method.POST
		data = {
			'API_ID': self.__api_id,
			'API_KEY': self.__api_key,
		}
		if payout:
			data['payout'] = payout
		if offset:
			data['offset'] = offset
		res = list((await self._send_req(method, Ty.PAYOUT, data=data)).values())
		payouts = [Payout(**x) for x in res if isinstance(x, dict)]
		return payouts[0] if len(payouts) == 1 else payouts

	async def create_payout(
			self,
			amount: float,
			receiver: str,
			sbp_bank: Optional[str] = None,
			commission_type: str = 'balance',
			webhook_url: Optional[str] = None,
			method: str = 'card',
	) -> CreatedPayout:
		"""
		Asynchronously creates a payout with the given amount, receiver, and optional parameters.

		:param amount: The amount to be paid out.
		:param receiver: The recipient of the payout.
		:param sbp_bank: The SBP bank for the payout (optional).
		:param commission_type: The type of commission for the payout (default is 'balance').
		:param webhook_url: The URL for webhook notifications (optional).
		:param method: The method of payout (default is 'card').
		:return: An instance of CreatedPayout representing the created payout.
		"""

		method_http = Method.POST
		data = {
			'API_ID': self.__api_id,
			'API_KEY': self.__api_key,
			'amount': amount,
			'receiver': receiver,
			'sbp_bank': sbp_bank if sbp_bank else None,
			'commission_type': commission_type,
			'webhook_url': webhook_url if webhook_url else None,
			'method': method
		}
		data = {key: value for key, value in data.items() if value is not None}

		req = await self._send_req(method_http, Ty.PAYOUT_CREATE, data=data)

		return CreatedPayout(**req)
