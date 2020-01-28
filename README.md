# Cashfree Cashgram Integration Kit for Python

Below is an integration flow on how to use Cashfree's Payout sdk.
Please go through the payout docs [here](https://docs.cashfree.com/docs/payout/guide/)
<br/>
This kit is linked to the Cashgram flow. Go [here](https://dev.cashfree.com/payouts/integrations/cashgram) to get a better understanding.
<br/>

## Functionalities

The following kit contains the following functionalities:
    <ol>
    <li> init(https://dev.cashfree.com/api-reference/payouts-api#authorise): to get auth token to be used in all following calls.
    <li> Cashgram.create_cashgram: to create a cashgram.
    <li> Cashgram.get_cashgram_status: get the status of the created cashgram.
    </ol>

## Build Steps

follow the following build steps to compile the Integration kit:
  1. Download the code and cd into the directory containing the code.
  2. install the following dependancy Cashfree python sdk
  ```
  pip3 install git+https://github.com/cashfree/cashfree-sdk-python.git
  ```
 
## Set Up

### Pre Requisites:
The following kit uses information stored in the app.py file. Before running the code for the first time open the app.py file
and add the relevant details:
  1. ClientId: This is a unique Identifier that identifies the merchant. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#credentials).
  2. ClientSecret: Corresponding secret key for the given ClientId that helps Cashfree indentify the merchant. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#credentials).
  3. Environment: Enviornment to be hit. The following values are accepted prod: for production, test: for test enviornment.

### IP Whitelisting:

Your IP has to be whitelisted to hit Cashfree's server. For more information please go [here](https://dev.cashfree.com/payouts/integrations/pre-requisites#ip).

### Cashgram

The following kit needs Cashgram details to create a cashgram. To know more information on how to create cashgrams please go [here](https://dev.cashfree.com/api-reference/payouts-api#create-cashgram-request).

The kit picks up the cashgram details from the app.py file, params sent to the create_cashgram function .
Required Fields are:
  1. cashgramId: unique Id of the created cashgram.
  2. amount: amount to be transferred.
  3. name: name of the contact.
  4. phone: phone number of the contact.

## Usage

Once the app.py file is setup you can run the executable, to run the entire flow. Authorise, create a cashgram 
and check the status of the created cashgram.

run the following command in the terminal to run the script:
```
  python app.py
```

You can change the necessary values in the app.py file as per your requirements and re run the script whenever needed.

## Doubts

Reach out to techsupport@cashfree.com in case of doubts.
 


