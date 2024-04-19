# Covalent SDK for Python

The Covalent SDK is the fastest way to integrate the Covalent Unified API for working with blockchain data. The SDK works with all [supported chains](https://www.covalenthq.com/docs/networks/) including Mainnets and Testnets. 

Note - use `Python 3.7` and above for best results.

> **Sign up for an API Key**
>
> To create your own API key, **[sign up for an Covalent account here](https://www.covalenthq.com/platform/auth/register/)** and use the key created under the [API Keys](https://www.covalenthq.com/platform/apikey/) tab.

## Getting started

```
pip3 install covalent-api-sdk
```

## How to use the Covalent SDK

After installing the app, you can then import and use the SDK:

```py
from covalent import CovalentClient
```
```py
def main():
    c = CovalentClient("YOUR_KEY")

    balance_resp = c.balance_service.get_token_balances_for_wallet_address("eth-mainnet", "demo.eth")
    if not balance_resp.error:
        print(balance_resp.data.chain_name)
    else:
        print(balance_resp.error_message)
```

> **Name Resolution**
>
> The Covalent SDK natively supports ENS domains (e.g. `demo.eth`), Lens Handles (e.g. `@demo.lens`) and Unstoppable Domains (e.g. `demo.x`) which automatically resolve to the underlying user address (e.g. `0xfC43f5F9dd45258b3AFf31Bdbe6561D97e8B71de`)

> **ℹ️ BREAKING CHANGE**
>
> Please change 
```py
from covalent import Client
```
to 
```py
from covalent import CovalentClient
```

### How to apply supported query parameters to endpoints

Query parameters serve as optional fields for an API endpoint. Developers can utilize the pydocs associated with the function parameters to receive autocomplete suggestions for supported parameters when sending them. These supported parameters can be defined in any order. For instance, if a developer wishes to assign the `quote_currency` parameter to `CAD` and `no_spam` to `True`.

```py
b = c.balance_service.get_token_balances_for_wallet_address("eth-mainnet", "demo.eth", no_spam=True, quote_currency="CAD")
```

### Different ways to input chains in chain fields
We offer users three options for specifying a chain in the designated field:
1. String literal - directly inputting the chain name, such as `eth-mainnet`, with auto-completion functionality as the user types.
2. Chain Enum - utilizing the Chain enum `Chains.ETH_MAINNET`, which provides auto-suggestions as the user types in the chain field.
3. Chain Id - entering the ChainId as a numerical value.

Example with string literal
```py
resp_with_string_literal = c.balance_service.get_token_balances_for_wallet_address("eth-mainnet", "WALLET_ADDRESS")
```
Example with Chain Enum
```py
resp_with_enum = c.balance_service.get_token_balances_for_wallet_address(Chains.ETH_MAINNET, "WALLET_ADDRESS")
```
Example with Chain Id
```py
resp_with_chain_id = c.balance_service.get_token_balances_for_wallet_address(1, "WALLET_ADDRESS")
```

## Supported Endpoints

The Covalent Python SDK provides comprehensive support for all Class A, Class B, and Pricing endpoints grouped under various Services, offering a wide range of functionalities and capabilities:

- `security_service`: Access to the Covalent's getApprovals endpoint
- `balance_service`: Access to the Covalent's balances endpoints
- `base_service`: Access to the Covalent's log events, chain, and block endpoints
- `nft_service`: Access to the Covalent's NFT endpoints
- `pricing_service`: Access to the Covalent's get historical token prices endpoint
- `transaction_service`: Access to the Covalent's transactions endpoints
- `xyk_service`: Access to the Covalent's Xy=k endpoints

### security_service

The `security_service` class contains the get_approvals() endpoint, refer to the [get_approvals endpoint on our API docs](https://www.covalenthq.com/docs/api/security/get-token-approvals-for-address/).

- `get_approvals()`: Get a list of approvals across all token contracts categorized by spenders for a wallet’s assets.
- `get_nft_approvals()`: Get a list of NFT approvals across all token contracts categorized by spenders for a wallet’s assets.

### balance_service

The `balance_service` class contains the balances endpoints. Listed below are the supported endpoints, also refer to our api docs under the Balances section in our class A endpoints.

- `get_token_balances_for_wallet_address()`: Fetch the native, fungible (ERC20), and non-fungible (ERC721 & ERC1155) tokens held by an address. Response includes spot prices and other metadata.
- `get_historical_token_balances_for_wallet_address()`: Fetch the historical native, fungible (ERC20), and non-fungible (ERC721 & ERC1155) tokens held by an address at a given block height or date. Response includes daily prices and other metadata.
- `get_historical_portfolio_for_wallet_address()`: Render a daily portfolio balance for an address broken down by the token. The timeframe is user-configurable, defaults to 30 days.
- `get_erc20_transfers_for_wallet_address()`: Render the transfer-in and transfer-out of a token along with historical prices from an address. (Paginated)
- `get_erc20_transfers_for_wallet_address_by_page()`: Render the transfer-in and transfer-out of a token along with historical prices from an address. (Nonpaginated)
- `get_token_holders_v2_for_token_address()`: Get a list of all the token holders for a specified ERC20 or ERC721 token. Returns historic token holders when block-height is set (defaults to latest). Useful for building pie charts of token holders. (Paginated)
- `get_token_holders_v2_for_token_address_by_page()`: Get a list of all the token holders for a specified ERC20 or ERC721 token. Returns historic token holders when block-height is set (defaults to latest). Useful for building pie charts of token holders. (Nonpaginated)
- `get_native_token_balance()`: Get the native token balance for an address. This endpoint is required because native tokens are usually not ERC20 tokens and sometimes you want something lightweight.

### base_service

The `base_service` class contains the log events, chain, and block endpoints. Listed below are the supported endpoints, also refer to our api docs under the Base section in our class A endpoints.

- `get_block()`: Fetch and render a single block for a block explorer.
- `get_logs()`: Get all the event logs of the latest block, or for a range of blocks. Includes sender contract metadata as well as decoded logs.
- `get_resolved_address()`: Used to resolve ENS, RNS and Unstoppable Domains addresses.
- `get_block_heights()`: Get all the block heights within a particular date range. Useful for rendering a display where you sort blocks by day (Paginated).
- `get_block_heights_by_page()`: Get all the block heights within a particular date range. Useful for rendering a display where you sort blocks by day. (Nonpaginated)
- `get_log_events_by_address()`: Get all the event logs emitted from a particular contract address. Useful for building dashboards that examine on-chain interactions. (Paginated)
- `get_log_events_by_address_by_page()`: Get all the event logs emitted from a particular contract address. Useful for building dashboards that examine on-chain interactions. (Nonpaginated)
- `get_log_events_by_topic_hash()`: Get all event logs of the same topic hash across all contracts within a particular chain. Useful for cross-sectional analysis of event logs that are emitted on-chain. (Paginated)
- `get_log_events_by_topic_hash_by_page()`: Get all event logs of the same topic hash across all contracts within a particular chain. Useful for cross-sectional analysis of event logs that are emitted on-chain. (Nonpaginated)
- `get_all_chains()`: Used to build internal dashboards for all supported chains on Covalent.
- `get_all_chain_status()`: Used to build internal status dashboards of all supported chains.
- `get_address_activity()`: Locate chains where an address is active on with a single API call.
- `get_gas_prices()`: Get real-time gas estimates for different transaction speeds on a specific network, enabling users to optimize transaction costs and confirmation times.

### nft_service

The `NftService` class contains the NFT endpoints. Listed below are the supported endpoints, also refer to our api docs under the NFT section in our class A endpoints.

- `get_chain_collections()`: Used to fetch the list of NFT collections with downloaded and cached off chain data like token metadata and asset files. (Paginated)
- `get_chain_collections_by_page()`: Used to fetch the list of NFT collections with downloaded and cached off chain data like token metadata and asset files. (Nonpaginated)
- `get_nfts_for_address()`: Used to render the NFTs (including ERC721 and ERC1155) held by an address.
- `get_token_ids_for_contract_with_metadata()`: Get NFT token IDs with metadata from a collection. Useful for building NFT card displays. (Paginated)
- `get_token_ids_for_contract_with_metadata_by_page()`: Get NFT token IDs with metadata from a collection. Useful for building NFT card displays. (Nonpaginated)
- `get_nft_metadata_for_given_token_id_for_contract()`: Get a single NFT metadata by token ID from a collection. Useful for building NFT card displays.
- `get_nft_transactions_for_contract_token_id()`: Get all transactions of an NFT token. Useful for building a transaction history table or price chart.
- `get_traits_for_collection()`: Used to fetch and render the traits of a collection as seen in rarity calculators.
- `get_attributes_for_trait_in_collection()`: Used to get the count of unique values for traits within an NFT collection.
- `get_collection_traits_summary()`: Used to calculate rarity scores for a collection based on its traits.
- `check_ownership_in_nft()`: Used to verify ownership of NFTs (including ERC-721 and ERC-1155) within a collection.
- `check_ownership_in_nft_for_specific_token_id()`: Used to verify ownership of a specific token (ERC-721 or ERC-1155) within a collection.
- `get_nft_market_sale_count()`: Used to build a time-series chart of the sales count of an NFT collection.
- `get_nft_market_volume()`: Used to build a time-series chart of the transaction volume of an NFT collection.
- `get_nft_market_floor_price()`: Used to render a price floor chart for an NFT collection.

### pricing_service

The `pricing_service` class contains the get_token_prices() endpoint. Refer to the [get_token_prices endpoint on our API docs](https://www.covalenthq.com/docs/api/pricing/get-historical-token-prices/).

- `get_token_prices()`: Get historic prices of a token between date ranges. Supports native tokens.

### transaction_service

The `transaction_service` class contains the transactions endpoint. Listed below are the supported endpoints, also refer to our api docs under the Transactions section in our class A endpoints.

- `get_all_transactions_for_address()`: Fetch and render the most recent transactions involving an address. Frequently seen in wallet applications. (Paginated)
- `get_all_transactions_for_address_by_page()`: Fetch and render the most recent transactions involving an address. Frequently seen in wallet applications. (Nonpaginated)
- `get_transactions_for_address_v3()`: Fetch and render the most recent transactions involving an address. Frequently seen in wallet applications.
- `get_transaction()`: Fetch and render a single transaction including its decoded log events. Additionally return semantically decoded information for DEX trades, lending and NFT sales.
- `get_transactions_for_block()`: Fetch all transactions including their decoded log events in a block and further flag interesting wallets or transactions.
- `get_transaction_summary()`: Fetch the earliest and latest transactions, and the transaction count for a wallet. Calculate the age of the wallet and the time it has been idle and quickly gain insights into their engagement with web3.
- `get_time_bucket_transactions_for_address()`: Fetch all transactions including their decoded log events in a 15-minute time bucket interval.
- `get_transactions_for_block_hash_by_page()`: Fetch all transactions including their decoded log events in a block and further flag interesting wallets or transactions.
- `get_transactions_for_block_hash()`: Fetch all transactions including their decoded log events in a block and further flag interesting wallets or transactions.


The functions `get_all_transactions_for_address_by_page()`, `get_transactions_for_address_v3()`, and `get_time_bucket_transactions_for_address()` have been enhanced with the introduction of `next()` and `prev()` support functions. These functions facilitate a smoother transition for developers navigating through our links object, which includes `prev` and `next` fields. Instead of requiring developers to manually extract values from these fields and create Python API fetch calls for the URL values, the new `next()` and `prev()` functions provide a streamlined approach, allowing developers to simulate this behavior more efficiently.

```py
from covalent import CovalentClient

def main():
    c = CovalentClient("YOUR_KEY", debug=True)
    b = c.transaction_service.get_all_transactions_for_address_by_page("eth-mainnet", "demo.eth")
    if not b.error:
        prev_page = b.data.prev() ## will retrieve page 9
        print(prev_page.data)
    else:
        print(b.error_message)

main()
```

### xyk_service

The `xyk_service` class contains the Xy=k endpoints. Listed below are the supported endpoints, also refer to our api docs under the XY=K section in our class B endpoints.

- `get_pools()`: Get all the pools of a particular DEX. Supports most common DEXs (Uniswap, SushiSwap, etc), and returns detailed trading data (volume, liquidity, swap counts, fees, LP token prices).
- `get_pool_by_address()`: Get the 7 day and 30 day time-series data (volume, liquidity, price) of a particular liquidity pool in a DEX. Useful for building time-series charts on DEX trading activity.
- `get_pools_for_token_address()`: Get all pools and the supported DEX for a token. Useful for building a table of top pairs across all supported DEXes that the token is trading on.
`get_pools_for_wallet_address()`: Get all pools and supported DEX for a wallet. Useful for building a personal DEX UI showcasing pairs and supported DEXes associated to the wallet.
- `get_address_exchange_balances()`: Return balance of a wallet/contract address on a specific DEX.
- `get_network_exchange_tokens()`: Retrieve all network exchange tokens for a specific DEX. Useful for building a top tokens table by total liquidity within a particular DEX.
- `get_lp_token_view()`: Get a detailed view for a single liquidity pool token. Includes time series data.
- `get_supported_dexes()`: Get all the supported DEXs available for the xy=k endpoints, along with the swap fees and factory addresses.
- `get_dex_for_pool_address()`: Get the supported DEX given a pool address, along with the swap fees, DEX's logo url, and factory addresses. Useful to identifying the specific DEX to which a pair address is associated.
- `get_single_network_exchange_token()`: Get historical daily swap count for a single network exchange token.
- `get_transactions_for_account_address()`: Get all the DEX transactions of a wallet. Useful for building tables of DEX activity segmented by wallet.
- `get_transactions_for_token_address()`: Get all the transactions of a token within a particular DEX. Useful for getting a per-token view of DEX activity.
- `get_transactions_for_exchange()`: Get all the transactions of a particular DEX liquidity pool. Useful for building a transactions history table for an individual pool.
- `get_transactions_for_dex()`: Get all the the transactions for a given DEX. Useful for building DEX activity views.
- `get_ecosystem_chart_data()`: Get a 7d and 30d time-series chart of DEX activity. Includes volume and swap count.
- `get_health_data()`: Ping the health of xy=k endpoints to get the synced block height per chain.

## Additional Helper Functions
### calculate_pretty_balance
The `calculate_pretty_balance` function is designed to take up to 4 inputs: the `balance` field obtained from the `token_balances` endpoint and the `contract_decimals`. The function also includes two optional fields, `round_off` and `precision`, to allow developers to round the unscaled balance to a certain decimal precision. The primary purpose of this function is to convert the scaled token balance (the balance parameter) into its unscaled, human-readable form. The scaled balance needs to be divided by 10^(contractDecimals) to remove the scaling factor.

```py
from covalent import CovalentClient, calculate_pretty_balance

c = CovalentClient("YOUR_KEY")
b = c.balance_service.get_token_balances_for_wallet_address("eth-mainnet", "demo.eth")
pretty_balance = calculate_pretty_balance(b.data.items[0].balance, b.data.items[0].contract_decimals)
```
### prettify_currency
The `prettify_currency` function refines the presentation of a monetary value, accepting a numerical amount and a fiat currency code as parameters (with USD as the default currency). It simplifies currency formatting for developers, ensuring visually polished representations of financial information in user interfaces for an enhanced user experience.

```py
from covalent import CovalentClient, prettify_currency

c = CovalentClient("YOUR_KEY")
b = c.balance_service.get_token_balances_for_wallet_address("eth-mainnet", "demo.eth")
pretty_currency = prettify_currency(b.data.items[0].quote_rate)
```

## Built-in SDK Features
### Explaining Pagination Mechanism Within the SDK

#### Endpoints supporting pagination

- `get_erc20_transfers_for_wallet_address()`
- `get_token_holders_v2_for_token_address()`
- `get_block_heights()`
- `get_log_events_by_address()`
- `get_log_events_by_topic_hash()`
- `get_chain_collections()`
- `get_token_ids_for_contract_with_metadata()`
- `get_all_transactions_for_address()`

Using the Covalent API, paginated supported endpoints return only 100 items, such as transactions or log events, per page. However, the Covalent SDK leverages generators to *seamlessly fetch all items without the user having to deal with pagination*.

```py
from covalent import CovalentClient
import asyncio

async def main():
    c = CovalentClient("YOUR_KEY")
    try:
        async for res in c.transaction_service.get_all_transactions_for_address("eth-mainnet", "demo.eth"):
            print(res)
    except Exception as e:
        print(e)

asyncio.run(main())
```
The paginated endpoints exclusively returns their response items without the response wrapper, enabling developers to access the list seamlessly, ensuring efficient and straightforward item retrieval.

### HTTP_PROXY and HTTPS_PROXY

The `requests` library in Python automatically respects the `HTTP_PROXY` and `HTTPS_PROXY` environment variables if they are set. This means that if your system has these environment variables configured for proxy settings, the SDK's HTTP requests will use these proxies without requiring additional configuration within the SDK code itself.

To utilize `HTTP_PROXY` and `HTTPS_PROXY` environment variables with the requests library in Python, ensure these variables are set in your environment. Then, when you make a request using requests.get or any other method from the requests library, it will automatically detect and use these proxy settings. Here's a simple demonstration:

```py
import requests
import os

# Optionally set proxies directly in code (if not already set as environment variables)
os.environ['HTTP_PROXY'] = 'http://your_http_proxy:port'
os.environ['HTTPS_PROXY'] = 'https://your_https_proxy:port'

response = requests.get('http://example.com')
print(response.status_code)
```

Read more on how to use [Proxy](https://www.zenrows.com/blog/python-requests-proxy#prerequisites) with Python Requests.

### Debugger Mode

Developers have the option to enable a debugger mode that provides response times, the URLs of called endpoints, and the HTTP statuses of those endpoints. This feature helps users identify which endpoints may have encountered failures. The default is `debug = False` if no input is provided.

```py
from covalent import CovalentClient

def main():
    c = CovalentClient("YOUR_KEY", debug=True)
    b = c.balance_service.get_token_balances_for_wallet_address("eth-mainnet", "demo.eth")
    if not b.error:
        print(b.data.chain_name)
    else:
        print(b.error_message)
```

![example result image](https://github.com/covalenthq/covalent-api-sdk-ts/assets/58843979/a4f6b024-2663-4820-9ac1-204c668da399)

### Retry Mechanism

Each endpoint is equipped with an exponential backoff algorithm that exponentially extends the wait time between retries, up to a `maximum of 5` retry attempts.

### Error Handling
The paginated endpoints will throw an error message in this format: `An error occurred {error_code}: {error_message}`, when an error occurs. The developer would need to make sure to `catch` those errors if any. This endpoint does not follow our default response format unlike our other endpoints, shown below.
```py
❴ 
    "data": ...,
    "error": false,
    "error_message": null,
    "error_code": null
❵
```

### Error codes
Covalent uses standard HTTP response codes to indicate the success or failure of an API request. In general: codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.). Codes in the 5xx range indicate an error with Covalent's servers (these are rare).

| Code      | Description |
| ----------- | ----------- |
| 200      | OK	Everything worked as expected.       |
| 400   | Bad Request	The request could not be accepted, usually due to a missing required parameter.        |
| 401   | Unauthorized	No valid API key was provided.        |
| 404   | Not Found	The request path does not exist.        |
| 429   | Too Many Requests	You are being rate-limited. Please see the rate limiting section for more information.        |
| 500, 502, 503   | Server Errors	Something went wrong on Covalent's servers. These are rare.        |

## Tests

Ensure you are at the root directory before running any tests

install `pytest-env` first if you do not have it already

```
pip install pytest-env
```
then go to the `pytest.ini` file in the root director and enter your covalent api key in the `COVALENT_API_KEY` field
then to run all tests, run
```
pytest
```
OR run individual tests

```
pytest tests/test_security_service.py
```

## Documentation

The Covalent API Python SDK documentation is integrated within the source code through `pydoc` comments. When utilizing an Integrated Development Environment (IDE), the SDK provides generated types and accompanying documentation for seamless reference and usage.
