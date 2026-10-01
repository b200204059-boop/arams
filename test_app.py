import sqlite3
import unittest
from datetime import datetime, timezone

import app


class BuildOrderTests(unittest.TestCase):
    def test_optional_email_allows_null(self):
        payload = {
            "customer": {
                "name": "Test User",
                "phone": "123",
                "email": None,
                "notes": "Pickup at front desk",
            },
            "items": [{"id": "sola-frames", "quantity": 1}],
        }

        customer, items, total = app.build_order(payload)

        self.assertEqual(customer["email"], "")
        self.assertEqual(items[0]["id"], "sola-frames")
        self.assertEqual(total, 1850)

    def test_list_orders_returns_recent_orders(self):
        connection = sqlite3.connect(app.app.config["DATABASE"])
        try:
            connection.execute("DELETE FROM orders WHERE reference = 'AR-TEST-ORDER'")
            created_at = datetime.now(timezone.utc).isoformat()
            connection.execute(
                """
                INSERT INTO orders (
                    reference, customer_name, customer_phone, customer_email,
                    delivery_notes, items_json, total, status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "AR-TEST-ORDER",
                    "Test Admin",
                    "01700000000",
                    "admin@example.com",
                    "Front desk",
                    '[{"id":"sola-frames","quantity":2}]',
                    3700,
                    "awaiting_whatsapp",
                    created_at,
                ),
            )
            connection.commit()
        finally:
            connection.close()

        orders = app.list_orders(limit=10)

        self.assertTrue(any(order["reference"] == "AR-TEST-ORDER" for order in orders))
        self.assertEqual(orders[0]["reference"], "AR-TEST-ORDER")


if __name__ == "__main__":
    unittest.main()
