from brownie import OurToken, config, network
from scripts.helpful_scripts import get_account
from web3 import Web3

intial_supply = Web3.toWei(1000, "ether")


def deploy_token():
    account = get_account()
    our_token = OurToken.deploy(
        intial_supply,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("{} has been deployed!".format(our_token.name()))
    return our_token


def show_token_balance():
    account = get_account()
    our_token = OurToken[-1]
    print(our_token.balanceOf(account))


def main():
    deploy_token()
    show_token_balance()
