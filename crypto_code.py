import requests
coins_name = ['Bitcoin', 'Ethereum']
for coin in coins_name:
    api = f"https://api.diadata.org/v1/assetQuotation/{coin}/0x0000000000000000000000000000000000000000"
    response = requests.get(api)
    print(response)
    print(response.json())
    response_body = response.json()
    coin_price = round(response_body.get("Price"), 2)
    print(f'the {coin} price is {coin_price} $')

import requests
import streamlit as st
with st.sidebar:
    st.write('cyrptocurrency app')
    st.image('ea5dd497244e411bf013f0ddad660f72.jpg')
# coins_name = ['Bitcoin', 'Ethereum']
# for coin in coins_name:
#     api = f"https://api.diadata.org/v1/assetQuotation/{coin}/0x0000000000000000000000000000000000000000"
#     response = requests.get(api)
#     print(response)
#     print(response.json())
#     response_body = response.json()
#     coin_price = round(response_body.get("Price"), 2)
#     print(f'the {coin} price is {coin_price} $')
coin = st.selectbox(label="select coin", options = ['Ethereum', 'Bitcoin'])
btn = st.button("get coin price")
if btn:
    api = f"https://api.diadata.org/v1/assetQuotation/{coin}/0x0000000000000000000000000000000000000000"
    response = requests.get(api)
    print(response)
    response_body = response.json()
    coin_price = round(response_body.get("Price"), 2)
    st.write(f'the {coin} price is {coin_price} $')