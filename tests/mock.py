from dataclasses import dataclass


@dataclass
class Context:
    environment: list[dict]


URL_TAGOIO = "https://api.tago.io/"

EDIT_SUBSCRIPTION = {
    "status": True,
    "result": "Subscription Successfully Updated"
}

EDIT_SUBSCRIPTION_FAIL = {
    "status": False,
    "message": "Cannot subscribe without payment method",
}

ENVIRONMENT = [
    {"key": "account_token", "value": "00000000-0000-0000-0000-000000000000"},
    {"key": "input", "value": "95"},
    {"key": "output", "value": "95"},
    {"key": "data_records", "value": "95"},
    {"key": "sms", "value": "95"},
    {"key": "email", "value": "95"},
    {"key": "push_notification", "value": "95"},
    {"key": "file_storage", "value": "95"},
    {"key": "analysis", "value": "95"},
]

MOCK_TOKEN = "00000000-0000-0000-0000-000000000000"

PROFILE_LIST = {
    "status": True,
    "result": [
        {
            "id": "fake_id",
            "name": "tago.io",
            "logo_url": None,
        }
    ],
}

TOKEN_LIST = {
    "status": True,
    "result": [
        {
            "name": "Generated automatically by Tago (admin)",
            "permission": "full",
            "token": "00000000-0000-0000-0000-000000000001",
            "expire_time": "2023-06-07T01:43:45.951Z",
            "created_at": "2023-03-07T01:43:45.952Z",
        },
        {
            "name": "Token #",
            "permission": "full",
            "token": "00000000-0000-0000-0000-000000000000",
            "expire_time": None,
            "created_at": "2023-02-24T18:09:33.731Z",
        },
    ],
}

TOKEN_LIST_FAIL = {
    "status": True,
    "result": [
        {
            "name": "Generated automatically by Tago (admin)",
            "permission": "full",
            "token": "00000000-0000-0000-0000-000000000001",
            "expire_time": "2023-06-07T01:43:45.951Z",
            "created_at": "2023-03-07T01:43:45.952Z",
        },
        {
            "name": "Token #",
            "permission": "full",
            "token": "00000000-0000-0000-0000-000000000002",
            "expire_time": None,
            "created_at": "2023-02-24T18:09:33.731Z",
        },
    ],
}

PROFILE_SUMMARY = {
    "status": True,
    "result": {
        "limit": {
            "analysis": 100,
            "data_records": 100,
            "email": 100,
            "input": 100,
            "output": 100,
            "sms": 100,
            "run_users": 100,
            "push_notification": 100,
            "file_storage": 100,
        },
        "limit_used": {
            "input": 0,
            "output": 0,
            "analysis": 0,
            "sms": 0,
            "email": 0,
            "data_records": 0,
            "run_users": 0,
            "push_notification": 0,
            "file_storage": 0,
        },
    },
}

SUBSCRIPTION = {
    "status": True,
    "result": {
        "services": {
            "analysis": {"limit": 3000},
            "data_records": {"limit": 800000},
            "email": {"limit": 100},
            "input": {"limit": 1000000},
            "output": {"limit": 3000000},
            "sms": {"limit": 10},
            "run_users": {"limit": 10},
            "push_notification": {"limit": 100},
            "file_storage": {"limit": 200},
        }
    },
}

BILLING = {
    "status": True,
    "result": {
        "analysis": [
            {"price": 0, "amount": 3000},
            {"price": 3000, "amount": 6000},
            {"price": 5500, "amount": 12000},
            {"price": 15000, "amount": 36000},
            {"price": 22000, "amount": 60000},
            {"price": 40000, "amount": 120000},
            {"price": 70000, "amount": 240000},
            {"price": 100000, "amount": 360000},
            {"price": 150000, "amount": 600000},
            {"price": 200000, "amount": 900000},
            {"price": 240000, "amount": 1200000},
            {"price": 400000, "amount": 2400000},
            {"price": 560000, "amount": 3600000},
            {"price": 700000, "amount": 7000000},
        ],
        "data_records": [
            {"price": 0, "amount": 800000},
            {"price": 1500, "amount": 1500000},
            {"price": 4000, "amount": 5000000},
            {"price": 6000, "amount": 10000000},
            {"price": 10000, "amount": 20000000},
            {"price": 20000, "amount": 50000000},
            {"price": 35000, "amount": 100000000},
            {"price": 50000, "amount": 150000000},
            {"price": 75000, "amount": 250000000},
            {"price": 100000, "amount": 350000000},
            {"price": 140000, "amount": 500000000},
            {"price": 170000, "amount": 750000000},
            {"price": 200000, "amount": 1000000000},
            {"price": 280000, "amount": 1500000000},
            {"price": 360000, "amount": 2000000000},
        ],
        "email": [
            {"price": 0, "amount": 100},
            {"price": 250, "amount": 1000},
            {"price": 500, "amount": 2000},
            {"price": 1000, "amount": 5000},
            {"price": 1500, "amount": 10000},
            {"price": 5000, "amount": 50000},
            {"price": 7500, "amount": 100000},
            {"price": 15000, "amount": 500000},
        ],
        "file_storage": [
            {"price": 0, "amount": 200},
            {"price": 2000, "amount": 10000},
            {"price": 3000, "amount": 25000},
            {"price": 8000, "amount": 100000},
            {"price": 10000, "amount": 250000},
            {"price": 20000, "amount": 1000000},
            {"price": 40000, "amount": 5000000},
            {"price": 50000, "amount": 15000000},
        ],
        "input": [
            {"price": 0, "amount": 1000000},
            {"price": 2000, "amount": 3000000},
            {"price": 5500, "amount": 10000000},
            {"price": 9000, "amount": 20000000},
            {"price": 17000, "amount": 50000000},
            {"price": 33000, "amount": 100000000},
            {"price": 48000, "amount": 150000000},
            {"price": 75000, "amount": 250000000},
            {"price": 100000, "amount": 500000000},
            {"price": 125000, "amount": 750000000},
            {"price": 150000, "amount": 1000000000},
            {"price": 200000, "amount": 1500000000},
            {"price": 250000, "amount": 2500000000},
            {"price": 300000, "amount": 4000000000},
        ],
        "output": [
            {"price": 0, "amount": 3000000},
            {"price": 2000, "amount": 18000000},
            {"price": 5500, "amount": 54000000},
            {"price": 9000, "amount": 90000000},
            {"price": 17000, "amount": 180000000},
            {"price": 33000, "amount": 360000000},
            {"price": 48000, "amount": 540000000},
            {"price": 75000, "amount": 900000000},
            {"price": 100000, "amount": 1350000000},
            {"price": 120000, "amount": 1800000000},
            {"price": 180000, "amount": 3600000000},
            {"price": 220000, "amount": 5400000000},
            {"price": 250000, "amount": 7200000000},
            {"price": 290000, "amount": 9000000000},
        ],
        "push_notification": [
            {"price": 0, "amount": 100},
            {"price": 250, "amount": 1000},
            {"price": 500, "amount": 2000},
            {"price": 1000, "amount": 5000},
            {"price": 1500, "amount": 10000},
            {"price": 5000, "amount": 50000},
            {"price": 7500, "amount": 100000},
            {"price": 25000, "amount": 500000},
        ],
        "sms": [
            {"price": 0, "amount": 10},
            {"price": 250, "amount": 100},
            {"price": 500, "amount": 200},
            {"price": 1250, "amount": 500},
            {"price": 2500, "amount": 1000},
            {"price": 10000, "amount": 5000},
            {"price": 18000, "amount": 10000},
            {"price": 35000, "amount": 20000},
            {"price": 50000, "amount": 30000},
            {"price": 65000, "amount": 40000},
            {"price": 85000, "amount": 50000},
        ],
        "run_users": [
            {"price": 0, "amount": 10},
            {"price": 1000, "amount": 100},
            {"price": 4000, "amount": 500},
            {"price": 6000, "amount": 1000},
            {"price": 15000, "amount": 5000},
            {"price": 25000, "amount": 10000},
            {"price": 60000, "amount": 50000},
            {"price": 100000, "amount": 100000},
        ],
        "addons": [
            {"name": "custom_dns", "price": 9900},
            {"name": "mobile", "price": 9900},
        ],
        "plans": [
            {"name": "free", "price": 0},
            {"name": "starter", "price": 4900},
            {"name": "scale", "price": 19900},
        ],
    },
}
