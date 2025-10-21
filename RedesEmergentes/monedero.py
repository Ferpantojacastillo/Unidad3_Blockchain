import json
from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod
import os

# Configuración de la red (TestNet)
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN   = ""  # Algonode no necesita token
HEADERS       = {"User-Agent": "algod-python"}

algod_client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS, HEADERS)

WALLET_FILE = "wallet.json"


# Crear o cargar una cuenta persistente
def cargar_o_crear_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, "r") as f:
            data = json.load(f)
            private_key = mnemonic.to_private_key(data["mnemonic"])
            address = data["address"]
            print(f"Cuenta cargada: {address}")
            return private_key, address
    else:
        private_key, address = account.generate_account()
        passphrase = mnemonic.from_private_key(private_key)
        with open(WALLET_FILE, "w") as f:
            json.dump({"address": address, "mnemonic": passphrase}, f)
        print(f"Nueva cuenta creada: {address}")
        print(f"Frase mnemónica (guárdala bien):\n{passphrase}\n")
        return private_key, address

# Consultar saldo
def obtener_saldo(address):
    acct_info = algod_client.account_info(address)
    micro_algo = acct_info.get('amount', 0)
    algo = micro_algo / 1_000_000
    print(f"Saldo de {address[:6]}... : {algo} ALGO")
    return micro_algo


# Enviar ALGO
def enviar_algo(sender_sk, sender_addr, receiver_addr, amount_micro):
    params = algod_client.suggested_params()
    unsigned_txn = transaction.PaymentTxn(
        sender=sender_addr,
        sp=params,
        receiver=receiver_addr,
        amt=amount_micro,
        note=b"Envio desde monedero persistente"
    )
    signed_txn = unsigned_txn.sign(sender_sk)

    txid = algod_client.send_transaction(signed_txn)
    print(f"\nTransacción enviada, ID: {txid}")

    # Esperar confirmación
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 5)
        print("✅ Confirmada en el bloque:", confirmed_txn.get('confirmed-round'))
    except Exception as e:
        print("⚠️ Error esperando confirmación:", e)


if __name__ == "__main__":
    private_key, address = cargar_o_crear_wallet()
    obtener_saldo(address)

    receiver_addr = input("\nIntroduce la dirección de la wallet destino: ").strip()
    amount = float(input("Cantidad a enviar (en ALGO): "))
    amount_micro = int(amount * 1_000_000)

    enviar_algo(private_key, address, receiver_addr, amount_micro)

    print("\n=== Saldos finales ===")
    obtener_saldo(address)
    obtener_saldo(receiver_addr)