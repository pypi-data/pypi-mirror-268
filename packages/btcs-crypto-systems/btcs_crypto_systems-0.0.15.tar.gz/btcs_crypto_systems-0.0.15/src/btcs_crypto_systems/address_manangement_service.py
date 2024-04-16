import requests
from dataclasses import dataclass, field
import json
import curlify


@dataclass
class AMS:
    env:str = "test"
    base_url:str = field(init=False)
    cookie_value:str = None
    log_requests:bool = False
    log_reponses:bool = False
    log_results:bool = False
    cookie_string:str = field(init=False, default=None)
    read_only:bool = field(init=False, default=True)
    
    
    def __post_init__(self):
        self.base_url = f"https://ams.btcs{self.env}.net/api/AddressManagement"
        self.cookie_string = f".AspNetCore.Cookies={self.cookie_value}; Path=/; Secure; HttpOnly;" 
        if self.cookie_value:
            self.read_only = False

    def get_addresses(self, blockchain_id=None, include_balances=None, limit=99999999999999, account_ref=None, include_balance_groups=None, is_pay=None, is_active=None, is_contract=None, is_deposit=None, ownership=None, account_asset_id=None, customer_id=None, addresses=None, tags=None):
        page = 0
        page_size = 100
        total = 0
        take_now = page_size
        addresses = []

        while True:
            try:
                # respect the limit
                if limit - (total + page_size*page) <= 0:
                    break
                elif limit - (total + page_size*page) < page_size:
                    take_now = limit - (total + page_size*page)
                url = ""
                params = AMS.remove_none_fields({
                    "Skip": page*take_now,
                    "Take": take_now,
                    "AccountRef": account_ref,
                    "BlockchainId": blockchain_id,
                    "IncludeBalances": include_balances,
                    "IncludeBalanceGroups": include_balance_groups,
                    "IsPay": is_pay,
                    "IsActive": is_active,
                    "IsContract": is_contract,
                    "IsDeposit": is_deposit,
                    "Ownership": ownership,
                    "AccountAssetId": account_asset_id,
                    "CustomerId": customer_id,
                    "Addresses": addresses,
                    "Tags": tags
                })

                r = requests.request("GET", f"{self.base_url}/addresses", params=params)
                addresses_res = r.json()
                if self.log_reponses:
                    print(f"{r.status_code}: {r.text}")
                addresses.extend(addresses_res)
                page += 1
                total += take_now

                if self.log_results:
                    print(f"collected {total} addresses...")
                if len(addresses_res) == 0:
                    break

            except:
                print("Error with URL: {}".format(url))
        
        return addresses
    
    def tag_address(self, address, blockchain_id, tag):
        if self.read_only:
            raise Exception("No cookie provided.")

        data = json.dumps({
            "addresses": [
                {
                "blockchainId": blockchain_id,
                "address": address
                }
            ],
            "tags": [
                {
                "tagName": tag
                }
            ]
        })

        headers = {
            'cookie': self.cookie_string,
            'Content-Type': 'application/json'
        }

        r = requests.patch(url=f"{self.base_url}/tag-address", data=data, headers=headers)
        
        if self.log_requests:
            print(curlify.to_curl(r.request))
        
        return r

    def attach_address(self, address:str, blockchain_id:int, account_ref:str):
        if self.read_only:
            raise Exception("No cookie provided.")
        
        data = json.dumps({
            "blockchainId": blockchain_id,
            "accountRef": account_ref,
            "addresses": [
                address
            ]
        })

        headers = {
            'cookie': self.cookie_string,
            'Content-Type': 'application/json'
        }

        r = requests.patch(url=f"{self.base_url}/attach-addresses", data=data, headers=headers)
        if self.log_requests:
            print(curlify.to_curl(r.request))
        return r
    
    def detach_address(self, address:str, blockchain_id:int, account_ref:str):
        if self.read_only:
            raise Exception("No cookie provided.")
        
        data = json.dumps({
            "blockchainId": blockchain_id,
            "accountRef": account_ref,
            "address": address
        })

        headers = {
            'cookie': self.cookie_string,
            'Content-Type': 'application/json'
        }

        r = requests.patch(url=f"{self.base_url}/detach-address", data=data, headers=headers)

        if self.log_requests:
            print(curlify.to_curl(r.request))

        return r

    def upsert_address(self, blockchain_id:int, address:str, ownership:str=None, is_active:bool=None, is_deposit:bool=None, is_contract:bool=None, vault_account_ref:str=None, location:str=None, fee_booking_mode:str=None, fee_booking_height:bool=None, is_pay:bool=None, passphrase:str=None, account_ref:str=None, tags:list[str]=None):
        if self.read_only:
            raise Exception("No cookie provided.")
        
        data_dict = AMS.remove_none_fields({
            "ownership": ownership,
            "blockchainId": blockchain_id,
            "address": address,
            "isActive": is_active,
            "isDeposit": is_deposit,
            "isContract": is_contract,
            "vaultAccountRef": vault_account_ref,
            "location": location,
            "feeBookingMode": fee_booking_mode,
            "feeBookingStartHeight": fee_booking_height,
            "isPay": is_pay,
            "passPhrase": passphrase,
            "tags": tags,
            "accountRef": account_ref
        })

        data = json.dumps(data_dict)

        headers = {
            'cookie': self.cookie_string,
            'Content-Type': 'application/json'
        }
        
        r = None

        if self.is_detached(address=address, blockchain_id=blockchain_id):
            r = requests.patch(url=f"{self.base_url}/detached-address", data=data, headers=headers)
            if self.log_requests:  
                print("\nAddress is detached, PATCH /detached-address")
        else:
            account_refs = self.get_account_refs(address, blockchain_id)
            data_dict["accountRef"] = account_refs[0]
            data = json.dumps(data_dict)
            r = requests.patch(url=f"{self.base_url}/address", data=data, headers=headers)
            if self.log_requests:  
                print("\nAddress is already attached, PATCH /address")
        
        if self.log_requests:
            print(f"\nRequest:\n{curlify.to_curl(r.request)}")

        if self.log_reponses:
            print(f"\nResponse:\n{r.text}")
        return r

    def is_detached(self, address:str, blockchain_id:int):
        if self.log_results:
            print("\nChecking whether address is detached.")
        r = requests.request("GET", f"{self.base_url}/addresses/{blockchain_id}/{address}")

        if self.log_requests:
            print(curlify.to_curl(r.request))

        if self.log_reponses:
            print(f"{r.status_code}: {r.text}")

        try:
            j = r.json()
            return j["isDetached"]
        except:
            print(f"{self.base_url}/addresses/{blockchain_id}/{address} failed")

    def get_account_refs(self, address, blockchain_id):
        r = requests.request("GET", f"{self.base_url}/addresses/{blockchain_id}/{address}?includeAccountRefs=true")

        if self.log_requests:
            print(curlify.to_curl(r.request))

        if self.log_reponses:
            print(f"{r.status_code}: {r.text}")
        
        j = r.json()

        return j['accountRefs']

    def remove_none_fields(my_dict):
        return {
            key: value for key, value in my_dict.items()
            if value is not None
        }

if __name__ == "__main__":
    # COOKIE_VALUE = ""    
    # ams = AMS("test", cookie_value=COOKIE_VALUE)
    # print(json.dumps(ams.get_addresses(is_deposit=True, include_balances=True, limit=10, tags=["siba"]), indent=2))

    # print(ams.upsert_address(
    #         blockchain_id=2, 
    #         address="addr1q8034em76n4qyhfrexv8j349gpcr5904cc4fm9vf7le59wxlrtnha482qfwj8jvc09r22srs8g2lt332nk2cnalng2uqnnqh77", 
    #         is_pay=True
    #         # tags=["siba_loves_python"]
    #     ).text)
    # print(ams.get_addresses(account="1065010", limit=10))
    # print(ams.tag_address(address="addr1q8034em76n4qyhfrexv8j349gpcr5904cc4fm9vf7le59wxlrtnha482qfwj8jvc09r22srs8g2lt332nk2cnalng2uqnnqh77", blockchain_id=2, tag="HW🔥").text)
    # print(ams.detach_address(address="addr1q8034em76n4qyhfrexv8j349gpcr5904cc4fm9vf7le59wxlrtnha482qfwj8jvc09r22srs8g2lt332nk2cnalng2uqnnqh77", blockchain_id=2, account_ref="200064921008").text)
    
    # addresses = [
    #     "0xa05b8dd67114bedac493c8e79b8de6bc09b43d126f39b2a9e5e64401d7ea8fa3f24f06a766f37893314e7a8d89eed3c9"
    # ]
    # for address in addresses:
    #     r = ams.tag_address(address=address, blockchain_id=19, tag="stk-slashed")
    #     print(r.text)
    addresses = [
    ("8a7c403e-8f6e-4cbb-afbf-5fa51a3c0171",1,"21rZRqJpsH77jNqqDZ2DxFdaTFTQrM5XfAhCkdJTW5v8cTKT","EXOTIC")
    ]

    ENV = "test"
    LOCATION = "VAULT"
    COOKIE = "CfDJ8BE_qDCocmZHnuek5KbKK72RZwfEhZGFKJfPpHWnLb4lnJZN0ufkRBBKl3fjuWZGkwoT625cehHm4VBhOgqVngKOTcx5KW7o1QLLmDKs7T9p7paa0leg2HqbPNgrif7fyXNOGlev7ai3DBHoct2CW0TWPY50T8XR8qZ9VkrqK297OW0BwsdjGUlY696wENYVLUtCMn7fFfXGVJEFzBtJl9fVsWCWb9SDqpgYHNY2-8p_tB8-X-0Td_d7GuncCHHgQJE9CQEkVogQzCkKxw5y5QzyogCR6Ejux7wUbnzHBZvE2GzaSbJA8AD7tou9cBLyXLv_sigU_S6u6iFcUOeg9OwjpdUXpvF8zxGJW-Q90Ot0FmGNtiGlZC0wvawbItsv__eYxuvXLedgijDGwAjeKUv7o3UMJVNDFyqUwAstY4Y5Uo1LZa2Sb8GFDSI87fLH-N3Tty9pRDArnUWvM-Fi80UfilAjAvVDb9hEpEclc3nY5RYQHfVvsh6JbwvpFzovS3aRjb9qTQOuUWwCJ7pzbyMsZu3yVCkeVJVbbHhNgc_5ZNRt_iKx2oV50TjloZjBauZEjkNrC1trbLlXPxXwtp0MDUgJAGpdEkknexK8pyqCYRD8jeqmBKMWYjSXXOHJKiCro0aSdMGHPZD7SChfii52Ha5in8wBnSky8RtlM1WC7rbpoL2ZJnXmGkbwPb0PAIsJ9mFYURQKjz_vjB9MvuglxVvbsM37Wqw6W4Tre7ClpxZGnsWsT8ndYvlxMMgsTpVEgCDCicAkkrSDtqfRUxPCHIYOtnhbGBfcrbHabWsLPl0qxrjxLrdr0we9vMQlYFvTaPFTfGp4g-qHWhYsvqSijfvmFTQTti4xTwN68PtWsSBMPFH5Ru3xF0JFkBYz6UbUQvycPWLCU0Ggcl3A-88Sym7v8UwQCyGN-4_VQnO1zczMvN1A-ytllfGQch71sjwRlm66kEf6DSpzlv5eZ-k4CpwnIEC26MVJ-LaUJWb-FaQLf_mKh-N05zNYDc8lZtaJepRWXMX_47nbAxu21S4Z8h_UXJA9EzCyWrWgZdQXJUMxLHwVmluouMhAvdnTf5CfwZLmZcKRbW2D1xzb1V1HcVRFwgUETUwNQv_Fhh2kMv8jP_dQ_YAVdr_uek_3fQiqEsilC6UPbmH6SiNruPrPD0T9qLQPYUyuO87H75RyhKREBf0scWeqHEtjwqhO4nI_G8YFJ2fZzwd4t6fhgN3drf_9SS6z0_pkuk_Ro5DiliCDX65zVqCjwjOJOelBn3bjqJ05CKWLNlKWsO-kqbLfGx90eO7enVIVVwCLet_pit8NByLFthZIze8ER91Q8Q2C67MotK3BiIqn34y2anoO5rBqwzOo_JfcbYI9kH5uPa-e4-MvMXdOFzalcUkcWG36WvXQbcEvhtYNrHA8H-9FzKRT9Oll3WTQU9R4moUjz0VRbQDaIAsyQ8wlIRYkjZ0hqIBEthsRNsWS6DK5mtvtsEeqWg4RRoLHgtOus054kMnMZhxix9Key4fLBTyv9zLZhZAu09xG_A2PupfImCG2ryR5YquqfMLb0zqA5uhFj4f0OnA2ZzEQD5ZOFwfmmeD7MjEQyulf0S3PRp8nfgQbcMLh5tpc6anhU8_ugOg02clW5vbN6yaOyf3QZzfjdBDAy8QCW0iBSivadN3ifBg6CYCUkKXd8iLTjOdkt9ldn0sBwM9AXxv9-wnBbRbdv2rRHgPLRLXvlT9yBUNDSd7GvFCGy3jmNkZOvnV8fGR2csXvPKgX-51T4tYBC-zkS-gHFmaOgw-6BHNQ7qpTFRRWUXJ2Y9yvZNN_cqkCnFJbTgT8EJ17e3HZILqgso8jEQZj57LPx-cDR2tSOVb_rAWTe46CH2kBHbTT466JHQGSA3tU8CfM3qpPHMUxJMxGFqCu0D1ZzS5VnCPbVlzV6iNVOR6OjMHx0t9vvu79zx4iXsvECYNs2QoBZM5nvGw82Mf0_MJPTw94aqq5o7aMUpuMA2xI21lrbKmkTeKm1hHU0kdwgDNfQiPEfH1grUvNUJPXh6F4K_59f-ity78u8HD4AUHe9SrWmjotZ7ixLcPmp2-xgxzK00bre6pwCXTjg5YxUrIJFf19BX7jRt5HtiWcQ8-ajL-KCGiZuYG9cW3r6C_Jul3XD9wdndOb_NmDI9SoKonkqXoIbvApBNvsCBfUIgvHjdiaf0db2pVfGgeDZcDTM8XDG04YGj-XLivW05IeFLbBwdXwrL_trScaRsA5nrsrtQrX9FkvOzsRXYRXtEedBJkfI0raawjqvma0HcllfOfCWOw_R4HgdoX3kkmg-KnERsF_ohArm8e9MPxSY61lzonU-TIVhgGJbq3sf29a3TntDzmABEWLT5BAvtC42-IuWpZJq4JKAAB__nAsMr_PTqComuzjNFikwS6jucbl4i3Kjm1p0I4Aj9TE8klxoR_xgLIp8Teymxke4hOk_p0Cb-1a01o2-mP_AdZlNb699dXZbtkS6LSKnp5FHYPiQ1hTrri3jN-FW4uPpkHtimtQhNSyB8_JqdQWhLOAMcupgYLw5h62eZncA5HvtEqsddju9Vkyy43d-GX58wQljMsvLxF6QQJc4dAThfhiJbv8e4qIBUYCFN-CA0joAmaaX39qa_sAIg9Y10CU1dejbPeAMOhTXDe6t_Q6Zsg5CrFiwuFtWrDgFaclayAJDHNsKbbxqrGIuCQdxQIBS5D4"
    TOTAL = len(addresses)
    ams = AMS(ENV, cookie_value=COOKIE, log_requests=True, log_reponses=True, log_results=True)

    for i,t in enumerate(addresses):
        vault_acc_ref, blockchain_id, address, _ = t
        print(f"{i+1}/{TOTAL}: {address}")
        print(ams.upsert_address(address=address, blockchain_id=blockchain_id, location=LOCATION, vault_account_ref=vault_acc_ref).text)
    # ams.upsert_address(address="addr1q8094sq8l0j78a2usnx25xq4vpsdaj7jznsazxz08e7c3cmzvvxwngql5fcygxejpc6l8mha2m2xqny42693lrhvlyasua4nl3", blockchain_id=2, is_active=True)



