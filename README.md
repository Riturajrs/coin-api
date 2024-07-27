
## Documentation for the Coin Market REST API

  

### Introduction

  

Welcome to the Coin Market REST API documentation. This API provides endpoints to manage and retrieve data related to various cryptocurrencies and their market data. This documentation outlines the available endpoints, their usage, and specifications.

  

### Version
  

Current API Version: 1.0


### Base URL

  

```
/api/
```

  

### Authentication

  

This API is protected using your favorite authentication mechanism. Ensure you include the necessary authentication headers in your requests.

  

### Endpoints


#### 1. Signup

**Endpoint:**  `/api/new-user`


**Method:**  `POST`


**Description:** Creates a new user, when requested with a valid username, email and password. Returns a ```<AUTH_TOKEN>``` on successful creation of a user


**Request:**

*URL*: ``localhost:8000/api/new-user``

*Body*:
```json
{
    "email": "newuser@gmail.com",
    "username": "newuser3",
    "password": "securepassword123"
}
```

**Response:**

```json
{
    "token": "82a6cbba2cef45ebc7e3d7d41af29d595091282d",
    "user": {
        "id": 4,
        "username": "newuser3",
        "email": "newuser@gmail.com",
        "password": "securepassword123"
    }
}
```

#### 2. Login

**Endpoint:**  `/api/login`

**Method:**  `POST`

**Description:** Logs in a user, when requested with correct credentials. Returns a ```<AUTH_TOKEN>``` on successful login of a user

**Request:**

*URL*: ``localhost:8000/api/login``

*Body*:
```json
{
    "email": "newuser@gmail.com",
    "username": "newuser_1",
    "password": "securepassword123"
}
```

**Response:**

```json
{
    "token": "4b8ad9cd1b42ae7c6eead1e0c97567f031a47a9a",
    "user": {
        "id": 3,
        "username": "newuser_1",
        "email": "newuser@gmail.com",
        "password": "pbkdf2_sha256$600000$OpChvgLN21RJisQZxjnWCg$TggRD+qjSlileTYT1RejPgIhpIuCvJcnSrczCqe/ow4="
    }
}
```


#### 3. Logout

**Endpoint:**  `/api/logout`


**Method:**  `POST`


**Description:** Logs out a user, and the previously issued ```<AUTH_TOKEN>``` gets invalidated

**Request:**

*URL*: ``localhost:8000/api/logout``

*Headers*:
```json
Authorization: token <AUTH_TOKEN>
```

**Response:**
```json
"User newuser@gmail.com has been logged out!"
```

  

#### 4. List All Coins

  

**Endpoint:**  `/api/coins`


**Method:**  `GET`


**Description:** Retrieves a paginated list of all available coins, including their IDs. This is a protected endpoint, you need to set authorization header as  ```token <AUTH_TOKEN> ```, after login or signup has been done


**Query Parameters:**
-  `page_num` (optional, default: 1): The page number to retrieve.
-  `per_page` (optional, default: 10): The number of items per page.

**Request:**

*URL*: ``localhost:8000/api/coins?page_num=10&per_page=8``

*Headers*:
```json
Authorization: token <AUTH_TOKEN>
```

**Response:**

```json
[
    {
        "id": "3-kingdoms-multiverse",
        "symbol": "3km",
        "name": "3 Kingdoms Multiverse"
    },
    {
        "id": "3space-art",
        "symbol": "pace",
        "name": "3SPACE ART"
    },
    {
        "id": "4",
        "symbol": "four",
        "name": "4"
    },
    {
        "id": "404aliens",
        "symbol": "404a",
        "name": "404Aliens"
    },
    {
        "id": "404-bakery",
        "symbol": "bake",
        "name": "404 Bakery"
    },
    {
        "id": "404blocks",
        "symbol": "404blocks",
        "name": "404Blocks"
    },
    {
        "id": "404ver",
        "symbol": "top",
        "name": "404ver"
    },
    {
        "id": "404wheels",
        "symbol": "404wheels",
        "name": "404WHEELS"
    }
]
```

  

#### 5. List Coin Categories

**Endpoint:**  `/api/categories`


**Method:**  `GET`


**Query Parameters:**
-  `page_num` (optional, default: 1): The page number to retrieve.
-  `per_page` (optional, default: 10): The number of items per page.  

**Description:** Retrieves a list of all available coin categories. This is a protected endpoint, you need to set authorization header as  ```token <AUTH_TOKEN> ```, after login or signup has been done

**Request:**

*URL*: ```localhost:8000/api/categories?page_num=10&per_page=5``` 

*Headers*:
```json
Authorization: token <AUTH_TOKEN>
```

**Response:**

```json
[
    {
        "category_id": "beamprivacy-ecosystem",
        "name": "BeamPrivacy Ecosystem"
    },
    {
        "category_id": "berachain-ecosystem",
        "name": "Berachain Ecosystem"
    },
    {
        "category_id": "bevm-ecosystem",
        "name": "BEVM Ecosystem"
    },
    {
        "category_id": "big-data",
        "name": "Big Data"
    },
    {
        "category_id": "binance-hodler-airdrops",
        "name": "Binance HODLer Airdrops"
    }
]
```

  

#### 6. Market Data for a Specific Coin

**Endpoint:**  `/api/market-data`

**Method:**  `GET`


**Query Parameters:**
-  `page_num` (optional, default: 1): The page number to retrieve.
-  `per_page` (optional, default: 10): The number of items per page.  

**Description:** Retrieves market data for a specific coin, including data against the Canadian Dollar (CAD).  This is a protected endpoint, you need to set authorization header as  ```token <AUTH_TOKEN> ```, after login or signup has been done

**JSON Parameters:**
Either the `id` or the `category` parameter must have a valid value, both can also be set.
-  `id` (optional): The ID of the coin.

-  `category` (optional): The ID of the coin category.

**Request:**

*URL*: `localhost:8000/api/market-data?page_num=1&per_page=3`  

*Body*:
```json
{
	"id":  "0xgasless-2",
	"category":  "account-abstraction"
}
```

*Headers*:
```json
Authorization: token <AUTH_TOKEN>
```

**Response:**

```json

[
    {
        "id": "iotex",
        "symbol": "iotx",
        "name": "IoTeX",
        "image": "https://coin-images.coingecko.com/coins/images/3334/large/iotex-logo.png?1696504041",
        "current_price": 0.064553,
        "market_cap": 608714599,
        "market_cap_rank": 156,
        "fully_diluted_valuation": 612253390,
        "total_volume": 27684668,
        "high_24h": 0.065171,
        "low_24h": 0.060975,
        "price_change_24h": 0.00280911,
        "price_change_percentage_24h": 4.54962,
        "market_cap_change_24h": 24875532,
        "market_cap_change_percentage_24h": 4.26068,
        "circulating_supply": 9441378929.0,
        "total_supply": 9496266827.32,
        "max_supply": 9496266827.32,
        "ath": 0.320799,
        "ath_change_percentage": -79.90831,
        "ath_date": "2021-11-13T16:54:18.643Z",
        "atl": 0.00169309,
        "atl_change_percentage": 3706.88892,
        "atl_date": "2020-03-13T02:29:47.597Z",
        "roi": null,
        "last_updated": "2024-07-27T11:47:25.329Z"
    },
    {
        "id": "trust-wallet-token",
        "symbol": "twt",
        "name": "Trust Wallet",
        "image": "https://coin-images.coingecko.com/coins/images/11085/large/Trust.png?1696511026",
        "current_price": 1.42,
        "market_cap": 592192145,
        "market_cap_rank": 159,
        "fully_diluted_valuation": 1421318342,
        "total_volume": 13078168,
        "high_24h": 1.43,
        "low_24h": 1.39,
        "price_change_24h": 0.0261608,
        "price_change_percentage_24h": 1.87549,
        "market_cap_change_24h": 10952943,
        "market_cap_change_percentage_24h": 1.88441,
        "circulating_supply": 416649900.0,
        "total_supply": 1000000000.0,
        "max_supply": null,
        "ath": 3.72,
        "ath_change_percentage": -61.75336,
        "ath_date": "2022-12-11T23:25:46.205Z",
        "atl": 0.00374143,
        "atl_change_percentage": 37881.52797,
        "atl_date": "2020-06-09T09:15:06.983Z",
        "roi": null,
        "last_updated": "2024-07-27T11:47:20.177Z"
    },
    {
        "id": "biconomy",
        "symbol": "bico",
        "name": "Biconomy",
        "image": "https://coin-images.coingecko.com/coins/images/21061/large/biconomy_logo.jpg?1696520444",
        "current_price": 0.421047,
        "market_cap": 349799846,
        "market_cap_rank": 230,
        "fully_diluted_valuation": 421048222,
        "total_volume": 7450861,
        "high_24h": 0.427787,
        "low_24h": 0.408432,
        "price_change_24h": 0.00882686,
        "price_change_percentage_24h": 2.1413,
        "market_cap_change_24h": 7424310,
        "market_cap_change_percentage_24h": 2.16847,
        "circulating_supply": 830783335.880957,
        "total_supply": 1000000000.0,
        "max_supply": 1000000000.0,
        "ath": 27.46,
        "ath_change_percentage": -98.46688,
        "ath_date": "2021-12-02T02:18:45.254Z",
        "atl": 0.257867,
        "atl_change_percentage": 63.28464,
        "atl_date": "2023-09-11T19:42:03.355Z",
        "roi": null,
        "last_updated": "2024-07-27T11:47:35.117Z"
    }
]
```


#### 7. Health

**Endpoint:**  `/api/health`

**Method:**  `GET`


**Description:** Gives information about versioning and health of the api along with the health of it's 3rd party applications

**Request:**

*URL*: ``localhost:8000/api/health``

**Response:**

```json
{
    "version": 1.0,
    "status": "online",
    "3rd party api response": "{'gecko_says': '(V3) To the Moon!'}"
}
```


### Pagination

All list endpoints support pagination. Use the `page_num` and `per_page` query parameters to control the pagination of the response. By default, `page_num` is set to 1, and `per_page` is set to 10.

  

### Error Handling

The API uses standard HTTP status codes to indicate the success or failure of an API request. Responses with a status code in the 2xx range indicate success, while codes in the 4xx and 5xx ranges indicate errors. Error responses include a JSON object with an `error` field containing a message describing the error.

  

**Example Error Response:**

```json
{
"detail": "Authentication credentials were not provided."
}
```

### Unit Tests
The application is thoroughly covered by unit tests to ensure the reliability and correctness of the API functionality. Currently test coverage is ~90%
