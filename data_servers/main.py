import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

# Kullanıcı verisi (örnek JSON)
credit_data = {
    "user_id": "1414141",
    "name": "Ahmet Yılmaz",
    "age": 32,
    "gender": "M",
    "language": "tr",
    "income": 27000,
    "employment_status": "full_time",
    "credit_score": 710,
    "applications": [
        {
            "application_id": "app_001",
            "application_date": "2025-04-10",
            "loan_amount": 150000,
            "loan_type": "mortgage",
            "is_fraudulent": False,
            "agent_routed": "ProductAgent",
            "system_action": "Present mortgage options based on credit score"
        },
        {
            "application_id": "app_002",
            "application_date": "2025-04-25",
            "loan_amount": 30000,
            "loan_type": "personal",
            "is_fraudulent": False,
            "agent_routed": "MoneyAgent",
            "system_action": "Notify user about credit utilization and budgeting advice"
        },
        {
            "application_id": "app_003",
            "application_date": "2025-05-05",
            "loan_amount": 75000,
            "loan_type": "auto",
            "is_fraudulent": True,
            "agent_routed": "FraudAgent",
            "system_action": "Trigger fraud alert due to suspicious login pattern"
        },
        {
            "application_id": "app_004",
            "application_date": "2025-05-21",
            "loan_amount": 10000,
            "loan_type": "personal",
            "is_fraudulent": False,
            "agent_routed": "ProductAgent",
            "system_action": "Offer short-term personal loan with flexible payment plan"
        },
        {
            "application_id": "app_005",
            "application_date": "2025-06-03",
            "loan_amount": 200000,
            "loan_type": "mortgage",
            "is_fraudulent": True,
            "agent_routed": "FraudAgent",
            "system_action": "Block application due to mismatch in declared income"
        },
        {
            "application_id": "app_006",
            "application_date": "2025-06-20",
            "loan_amount": 50000,
            "loan_type": "education",
            "is_fraudulent": False,
            "agent_routed": "ProductAgent",
            "system_action": "Approve education loan with student-friendly rate"
        }
    ]
}

balance_data = {
  "user_id": "1414141",
  "name": "Ahmet Yılmaz",
  "cards": [
    {
      "card_id": "cc_001",
      "card_type": "credit",
      "card_number_masked": "**** **** **** 1234",
      "currency": "TRY",
      "credit_limit": 20000,
      "current_balance": 5400.75,
      "available_credit": 14600.25,
      "due_date": "2025-07-25",
      "minimum_payment": 750.00,
      "status": "active"
    },
    {
      "card_id": "dc_001",
      "card_type": "debit",
      "card_number_masked": "**** **** **** 5678",
      "currency": "TRY",
      "current_balance": 8950.20,
      "linked_account": "TR12 0006 2000 1234 0000 5678 90",
      "status": "active"
    }
  ],
  "last_updated": "2025-07-11T18:45:00+03:00"
}

transaction_data = {
  "user_id": "1414141",
  "name": "Ahmet Yılmaz",
  "spending_history": [
    {
      "transaction_id": "txn_001",
      "date": "2025-04-07T13:23:00Z",
      "category": "restaurant",
      "merchant": "McDonald's",
      "location": "Antalya",
      "amount": 1693.13,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_002",
      "date": "2025-04-07T15:46:00Z",
      "category": "entertainment",
      "merchant": "Netflix",
      "location": "Istanbul",
      "amount": 4334.67,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_003",
      "date": "2025-04-08T14:36:00Z",
      "category": "entertainment",
      "merchant": "YouTube Premium",
      "location": "Ankara",
      "amount": 4837.44,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_004",
      "date": "2025-04-10T12:29:00Z",
      "category": "transportation",
      "merchant": "BiTaksi",
      "location": "Ankara",
      "amount": 1582.84,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_005",
      "date": "2025-04-12T09:50:00Z",
      "category": "electronics",
      "merchant": "Vatan Computer",
      "location": "Bursa",
      "amount": 4970.75,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_006",
      "date": "2025-04-14T10:26:00Z",
      "category": "utilities",
      "merchant": "İGDAŞ",
      "location": "Bursa",
      "amount": 2510.91,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_007",
      "date": "2025-04-14T16:17:00Z",
      "category": "restaurant",
      "merchant": "Happy Moon’s",
      "location": "Ankara",
      "amount": 2424.73,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_008",
      "date": "2025-04-15T17:29:00Z",
      "category": "transportation",
      "merchant": "BiTaksi",
      "location": "Ankara",
      "amount": 2034.78,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_009",
      "date": "2025-04-19T10:01:00Z",
      "category": "restaurant",
      "merchant": "BigChefs",
      "location": "Izmir",
      "amount": 4577.1,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_010",
      "date": "2025-04-19T17:00:00Z",
      "category": "utilities",
      "merchant": "ASKİ",
      "location": "Izmir",
      "amount": 265.9,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_011",
      "date": "2025-04-22T08:36:00Z",
      "category": "subscription",
      "merchant": "Amazon Prime",
      "location": "Antalya",
      "amount": 2967.56,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_012",
      "date": "2025-04-22T14:43:00Z",
      "category": "groceries",
      "merchant": "Migros",
      "location": "Bursa",
      "amount": 750.95,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "groceries"
      ]
    },
    {
      "transaction_id": "txn_013",
      "date": "2025-04-22T16:44:00Z",
      "category": "transportation",
      "merchant": "Uber",
      "location": "Istanbul",
      "amount": 3935.09,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_014",
      "date": "2025-04-22T22:24:00Z",
      "category": "clothing",
      "merchant": "LC Waikiki",
      "location": "Antalya",
      "amount": 65.3,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "clothing"
      ]
    },
    {
      "transaction_id": "txn_015",
      "date": "2025-04-24T16:21:00Z",
      "category": "electronics",
      "merchant": "MediaMarkt",
      "location": "Istanbul",
      "amount": 1263.67,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_016",
      "date": "2025-04-29T19:09:00Z",
      "category": "electronics",
      "merchant": "MediaMarkt",
      "location": "Bursa",
      "amount": 4358.74,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_017",
      "date": "2025-04-30T11:43:00Z",
      "category": "subscription",
      "merchant": "Amazon Prime",
      "location": "Ankara",
      "amount": 492.25,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_018",
      "date": "2025-05-01T09:52:00Z",
      "category": "clothing",
      "merchant": "Zara",
      "location": "Antalya",
      "amount": 4359.78,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "clothing"
      ]
    },
    {
      "transaction_id": "txn_019",
      "date": "2025-05-01T20:53:00Z",
      "category": "electronics",
      "merchant": "Teknosa",
      "location": "Antalya",
      "amount": 3675.9,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_020",
      "date": "2025-05-02T18:20:00Z",
      "category": "clothing",
      "merchant": "Zara",
      "location": "Istanbul",
      "amount": 3915.54,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "clothing"
      ]
    },
    {
      "transaction_id": "txn_021",
      "date": "2025-05-04T20:28:00Z",
      "category": "electronics",
      "merchant": "MediaMarkt",
      "location": "Antalya",
      "amount": 4516.19,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_022",
      "date": "2025-05-04T22:49:00Z",
      "category": "transportation",
      "merchant": "Havaist",
      "location": "Istanbul",
      "amount": 3787.63,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_023",
      "date": "2025-05-05T21:44:00Z",
      "category": "transportation",
      "merchant": "BiTaksi",
      "location": "Istanbul",
      "amount": 2123.33,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_024",
      "date": "2025-05-10T19:38:00Z",
      "category": "health",
      "merchant": "Private Clinic",
      "location": "Ankara",
      "amount": 2104.5,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "health"
      ]
    },
    {
      "transaction_id": "txn_025",
      "date": "2025-05-10T20:20:00Z",
      "category": "subscription",
      "merchant": "Apple Music",
      "location": "Istanbul",
      "amount": 3874.18,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_026",
      "date": "2025-05-11T14:24:00Z",
      "category": "restaurant",
      "merchant": "BigChefs",
      "location": "Ankara",
      "amount": 4956.74,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_027",
      "date": "2025-05-13T20:44:00Z",
      "category": "entertainment",
      "merchant": "Spotify",
      "location": "Bursa",
      "amount": 4998.21,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_028",
      "date": "2025-05-13T22:40:00Z",
      "category": "clothing",
      "merchant": "Zara",
      "location": "Bursa",
      "amount": 3195.73,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "clothing"
      ]
    },
    {
      "transaction_id": "txn_029",
      "date": "2025-05-14T11:28:00Z",
      "category": "health",
      "merchant": "Pharmacy",
      "location": "Ankara",
      "amount": 1819.59,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "health"
      ]
    },
    {
      "transaction_id": "txn_030",
      "date": "2025-05-16T08:24:00Z",
      "category": "transportation",
      "merchant": "Havaist",
      "location": "Izmir",
      "amount": 2773.01,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_031",
      "date": "2025-05-18T11:12:00Z",
      "category": "electronics",
      "merchant": "MediaMarkt",
      "location": "Istanbul",
      "amount": 3245.76,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_032",
      "date": "2025-05-18T19:48:00Z",
      "category": "restaurant",
      "merchant": "McDonald's",
      "location": "Izmir",
      "amount": 594.41,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_033",
      "date": "2025-05-21T09:28:00Z",
      "category": "subscription",
      "merchant": "Amazon Prime",
      "location": "Antalya",
      "amount": 1285.84,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_034",
      "date": "2025-05-22T08:29:00Z",
      "category": "utilities",
      "merchant": "CLK Boğaziçi",
      "location": "Izmir",
      "amount": 1697.1,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_035",
      "date": "2025-05-23T16:29:00Z",
      "category": "entertainment",
      "merchant": "Spotify",
      "location": "Antalya",
      "amount": 267.51,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_036",
      "date": "2025-05-25T20:12:00Z",
      "category": "entertainment",
      "merchant": "YouTube Premium",
      "location": "Izmir",
      "amount": 1729.83,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_037",
      "date": "2025-05-30T10:19:00Z",
      "category": "transportation",
      "merchant": "BiTaksi",
      "location": "Bursa",
      "amount": 379.7,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_038",
      "date": "2025-05-31T12:59:00Z",
      "category": "entertainment",
      "merchant": "Spotify",
      "location": "Izmir",
      "amount": 3131.54,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_039",
      "date": "2025-05-31T14:09:00Z",
      "category": "groceries",
      "merchant": "Migros",
      "location": "Ankara",
      "amount": 4014.37,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "groceries"
      ]
    },
    {
      "transaction_id": "txn_040",
      "date": "2025-05-31T22:29:00Z",
      "category": "electronics",
      "merchant": "MediaMarkt",
      "location": "Izmir",
      "amount": 488.97,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_041",
      "date": "2025-06-01T08:24:00Z",
      "category": "electronics",
      "merchant": "Vatan Computer",
      "location": "Ankara",
      "amount": 3821.44,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_042",
      "date": "2025-06-01T09:29:00Z",
      "category": "utilities",
      "merchant": "ASKİ",
      "location": "Istanbul",
      "amount": 1605.89,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_043",
      "date": "2025-06-03T16:19:00Z",
      "category": "subscription",
      "merchant": "Apple Music",
      "location": "Antalya",
      "amount": 489.38,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_044",
      "date": "2025-06-04T09:51:00Z",
      "category": "utilities",
      "merchant": "CLK Boğaziçi",
      "location": "Izmir",
      "amount": 1556.19,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_045",
      "date": "2025-06-07T16:57:00Z",
      "category": "utilities",
      "merchant": "İGDAŞ",
      "location": "Istanbul",
      "amount": 1672.78,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_046",
      "date": "2025-06-08T08:40:00Z",
      "category": "electronics",
      "merchant": "Teknosa",
      "location": "Izmir",
      "amount": 1095.36,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "electronics"
      ]
    },
    {
      "transaction_id": "txn_047",
      "date": "2025-06-08T20:47:00Z",
      "category": "clothing",
      "merchant": "Mavi",
      "location": "Bursa",
      "amount": 4122.08,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "clothing"
      ]
    },
    {
      "transaction_id": "txn_048",
      "date": "2025-06-09T13:52:00Z",
      "category": "utilities",
      "merchant": "İGDAŞ",
      "location": "Istanbul",
      "amount": 1248.39,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "utilities"
      ]
    },
    {
      "transaction_id": "txn_049",
      "date": "2025-06-09T14:42:00Z",
      "category": "restaurant",
      "merchant": "KFC",
      "location": "Izmir",
      "amount": 795.64,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_050",
      "date": "2025-06-11T19:01:00Z",
      "category": "transportation",
      "merchant": "Havaist",
      "location": "Izmir",
      "amount": 4907.92,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_051",
      "date": "2025-06-15T17:46:00Z",
      "category": "restaurant",
      "merchant": "Nusr-Et",
      "location": "Antalya",
      "amount": 1797.55,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_052",
      "date": "2025-06-16T20:38:00Z",
      "category": "subscription",
      "merchant": "Apple Music",
      "location": "Antalya",
      "amount": 1168.85,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_053",
      "date": "2025-06-19T11:49:00Z",
      "category": "clothing",
      "merchant": "Mavi",
      "location": "Bursa",
      "amount": 3509.34,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "clothing"
      ]
    },
    {
      "transaction_id": "txn_054",
      "date": "2025-06-21T09:40:00Z",
      "category": "entertainment",
      "merchant": "Netflix",
      "location": "Izmir",
      "amount": 2563.38,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_055",
      "date": "2025-06-21T21:43:00Z",
      "category": "transportation",
      "merchant": "Havaist",
      "location": "Izmir",
      "amount": 1430.02,
      "currency": "TRY",
      "payment_method": "debit_card",
      "card_last4": "3821",
      "tags": [
        "transportation"
      ]
    },
    {
      "transaction_id": "txn_056",
      "date": "2025-06-22T12:04:00Z",
      "category": "subscription",
      "merchant": "Apple Music",
      "location": "Antalya",
      "amount": 172.34,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "subscription"
      ]
    },
    {
      "transaction_id": "txn_057",
      "date": "2025-06-22T20:10:00Z",
      "category": "entertainment",
      "merchant": "Spotify",
      "location": "Antalya",
      "amount": 4812.9,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "entertainment"
      ]
    },
    {
      "transaction_id": "txn_058",
      "date": "2025-06-25T22:33:00Z",
      "category": "restaurant",
      "merchant": "McDonald's",
      "location": "Istanbul",
      "amount": 2002.91,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_059",
      "date": "2025-06-26T17:46:00Z",
      "category": "restaurant",
      "merchant": "Nusr-Et",
      "location": "Istanbul",
      "amount": 1147.04,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "restaurant"
      ]
    },
    {
      "transaction_id": "txn_060",
      "date": "2025-06-28T16:40:00Z",
      "category": "electronics",
      "merchant": "Vatan Computer",
      "location": "Antalya",
      "amount": 630.47,
      "currency": "TRY",
      "payment_method": "credit_card",
      "card_last4": "9476",
      "tags": [
        "electronics"
      ]
    }
  ]
}

@app.get("/credit/{user_id}")
def get_user_info(user_id: str):
    if user_id == credit_data["user_id"]:
        return JSONResponse(content=credit_data)
    return JSONResponse(status_code=404, content={"error": "User not found"})

@app.get("/balance/{user_id}")
def get_user_info(user_id: str):
    if user_id == balance_data["user_id"]:
        return JSONResponse(content=balance_data)
    return JSONResponse(status_code=404, content={"error": "User not found"})

@app.get("/transaction/{user_id}")
def get_user_info(user_id: str):
    if user_id == transaction_data["user_id"]:
        return JSONResponse(content=transaction_data)
    return JSONResponse(status_code=404, content={"error": "User not found"})

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)