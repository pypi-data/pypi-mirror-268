# asyncio_payok

## Quickstart

Here's a quick example of using `asyncio_payok` to get your current balance:

```python
import asyncio
from asyncio_payok import PayOk

async def main():
    client = PayOk('your_api_id', 'your_api_key', 'your_secret_key', 'your_shop_id')
    balance = await client.get_balance()
    print(balance)

asyncio.run(main())
```

## Features

- Asynchronous requests
- Easy to use with Python's asyncio
- Support for payment creation, balance checks, transaction retrieval, and payouts

## Usage

### Initializing the Client

Create an instance of the `PayOk` client with your API credentials:

```python
from asyncio_payok import PayOk

client = PayOk(api_id='your_api_id', api_key='your_api_key', secret_key='your_secret_key', shop='your_shop_id')
```

### Get Balance

Retrieve your current balance as follows:

```python
balance = await client.get_balance()
```

### Create Payment

Initiate a payment with the required details:

```python
payment = await client.create_payment(amount='10.00', currency='USD', description='Payment Description', ...)
```

### Transaction History

Fetch the transaction history by payment ID or offset:

```python
transactions = await client.get_transactions(payment_id='123', offset=10)
```

### Create Payout

Send a payout to a specified recipient:

```python
payout = await client.create_payout(amount='10.00', receiver='receiver_info', ...)
```

### Handling Exceptions

Handle API and network exceptions gracefully:

```python
try:
    balance = await client.get_balance()
except Exception as e:
    print(f'Error occurred: {e}')
```

## Dependencies

- Python 3.6 or higher
- `aiohttp`

## Contributing

Contributions are welcome! Please open a pull request or issue to propose changes or additions.

## License

This project is licensed under the MIT License.