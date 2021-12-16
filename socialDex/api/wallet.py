from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/a2da908a72014f4a952f2b18d58f0ecb'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"Your address: {address}\nYour key: {privateKey}")