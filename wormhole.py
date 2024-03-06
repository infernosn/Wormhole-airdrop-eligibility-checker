import argparse
import requests

def get_allocation(address, blockchain):
    id = {
      "sol": 1,
      "eth": 2,
      "sui": 21,
      "aptos": 22,
      "inj": 19,
      "terra": 3,
      "algorand": 8,
      "osmosis": 20,
    }[blockchain]
    url = f"https://prod-flat-files-min.wormhole.com/{address}_{id}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        allocation = data['amount'] * 1e-9
        print(f"{address}: {allocation}")
    else:
        print(f"{address}: 0")

def main():
    parser = argparse.ArgumentParser(description="""
      Fetch allocation for addresses from a file in a blockchain.
      Put files in addresses.txt (one per line).
      Usage: python wormhole.py addresses.txt eth
    """)
    parser.add_argument("address_file", help="Path to the file containing addresses (.txt).")
    parser.add_argument("blockchain", help="Blockchain (sol/eth/sui/aptos/inj/terra/algorand/osmosis).")
    args = parser.parse_args()

    assert args.blockchain in ["sol", "eth"], "Only support sol/eth"

    with open(args.address_file, 'r') as file:
        addresses = file.readlines()

    for address in addresses:
        address = address.strip()
        get_allocation(address, args.blockchain)

if __name__ == "__main__":
    main()
