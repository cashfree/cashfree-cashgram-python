from cashfree_sdk.payouts import Payouts
from cashfree_sdk.payouts.cashgram import Cashgram

clientId = "clientId"
clientSecret = "clientSecret"
env = "TEST"

try:
    Payouts.init(clientId, clientSecret, env)

    create_cashgram_response = Cashgram.create_cashgram(
    cashgramId="cf111",
    amount= "1.00",
    name= "sameera",
    email= "sameera@cashfree.com",
    phone= "9000000001",
    linkExpiry= "2020/01/19",
    remarks= "sample cashgram",
    notifyCustomer= 1
    )
    print("create cashgram response")
    print(create_cashgram_response.content)

    get_cashgram_status_response = Cashgram.get_cashgram_status("cf111")
    print("get cashgram status")
    print(get_cashgram_status_response.content)
except Exception as err:
    print("err in cashgram")
    print(err)