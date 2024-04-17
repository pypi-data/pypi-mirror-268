import asyncio
from aiohttp import ClientSession
from enum import Enum as enum
from asyncio_payok.const import Ty, Method
import functools
import time
from typing import Optional


class BaseSession:
	STATIC_URL = 'https://payok.io/'


	@staticmethod
	async def _check_response(response: dict) -> dict:
		"""
        A static method to check the response dictionary for errors and raise an exception if 'status' is 'error'.

        Parameters:
            response (dict): The response dictionary to be checked.

        Returns:
            dict: The input response dictionary.
            :param response:
            :return:
        """
		if response.get('status') == 'error':
			raise Exception(response.get('error_text'))
		return response

	async def _send_req(self, method: enum, url: enum, **kwargs) -> dict:
		"""
        An asynchronous function to send a request using the specified method, URL, and additional keyword arguments.
        :param method: The HTTP method to be used for the request
        :param url: The URL to which the request will be sent
        :param kwargs: Additional keyword arguments to be passed to the request
        :return: The result of checking the response after sending the request
        """
		url = f'{self.STATIC_URL}{url.value}'
		async with ClientSession() as session:
			async with session.request(method.value, url, **kwargs) as response:
				response = await response.json(content_type="text/plain")
				return await self._check_response(response)

