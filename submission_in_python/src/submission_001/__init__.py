"""
submission_001.py

What is the hash of block 654,321?
"""
from bitcoinrpc.authproxy import AuthServiceProxy
from bitcoinrpc.authproxy import JSONRPCException
from src import bitcoinconf  # pylint: disable=import-error


def submission_getblockhash(blockheight: int) -> str | None:
    try:
        # get bitcoin.conf
        p = bitcoinconf.get_path()
        config = bitcoinconf.get_conf(filepath=p)

        # Connect to server
        ip = config["rpcconnect"]
        user = config["rpcuser"]
        passwd = config["rpcpassword"]
        rpc = AuthServiceProxy(f"http://{user}:{passwd}@{ip}:8332")

        # -----------------------------------
        # now extract hash from desired block
        # -----------------------------------
        return rpc.getblockhash(blockheight)

    except JSONRPCException as exc:
        print(f"Failed connection: {exc}")
        return None

    # pylint: disable=broad-exception-caught
    except Exception as exc:
        print(exc)
        return None
