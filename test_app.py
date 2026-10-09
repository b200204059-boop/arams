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

    def test_update_order_status_changes_status(self):
        connection = sqlite3.connect(app.app.config["DATABASE"])
        try:
            connection.execute("DELETE FROM orders WHERE reference = 'AR-TEST-UPDATE'")
            created_at = datetime.now(timezone.utc).isoformat()
            connection.execute(
                """
                INSERT INTO orders (
                    reference, customer_name, customer_phone, customer_email,
                    delivery_notes, items_json, total, status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "AR-TEST-UPDATE",
                    "Status User",
                    "01711111111",
                    "status@example.com",
                    "Call before delivery",
                    '[{"id":"sola-frames","quantity":1}]',
                    1850,
                    "awaiting_whatsapp",
                    created_at,
                ),
            )
            connection.commit()
        finally:
            connection.close()

        updated = app.update_order_status("AR-TEST-UPDATE", "paid")

        self.assertTrue(updated)
        self.assertEqual(app.get_order_by_reference("AR-TEST-UPDATE")["status"], "paid")

    def test_get_order_by_reference_returns_order(self):
        connection = sqlite3.connect(app.app.config["DATABASE"])
        try:
            connection.execute("DELETE FROM orders WHERE reference = 'AR-TEST-DETAILS'")
            created_at = datetime.now(timezone.utc).isoformat()
            connection.execute(
                """
                INSERT INTO orders (
                    reference, customer_name, customer_phone, customer_email,
                    delivery_notes, items_json, total, status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "AR-TEST-DETAILS",
                    "Details User",
                    "01722222222",
                    "details@example.com",
                    "Please call first",
                    '[{"id":"sola-frames","quantity":2}]',
                    3700,
                    "paid",
                    created_at,
                ),
            )
            connection.commit()
        finally:
            connection.close()

        order = app.get_order_by_reference("AR-TEST-DETAILS")

        self.assertIsNotNone(order)
        self.assertEqual(order["reference"], "AR-TEST-DETAILS")
        self.assertEqual(order["status"], "paid")

    def test_update_order_status_rejects_invalid_status(self):
        with self.assertRaises(ValueError):
            app.update_order_status("AR-TEST-UPDATE", "unknown_state")

    def test_cancel_order_marks_order_cancelled(self):
        connection = sqlite3.connect(app.app.config["DATABASE"])
        try:
            connection.execute("DELETE FROM orders WHERE reference = 'AR-TEST-CANCEL'")
            created_at = datetime.now(timezone.utc).isoformat()
            connection.execute(
                """
                INSERT INTO orders (
                    reference, customer_name, customer_phone, customer_email,
                    delivery_notes, items_json, total, status, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    "AR-TEST-CANCEL",
                    "Cancel User",
                    "01733333333",
                    "cancel@example.com",
                    "Cancel if needed",
                    '[{"id":"sola-frames","quantity":1}]',
                    1850,
                    "awaiting_whatsapp",
                    created_at,
                ),
            )
            connection.commit()
        finally:
            connection.close()

        cancelled = app.cancel_order("AR-TEST-CANCEL")

        self.assertTrue(cancelled)
        self.assertEqual(app.get_order_by_reference("AR-TEST-CANCEL")["status"], "cancelled")

    def test_best_seller_perfume_catalog_includes_reference_products(self):
        names = [name for _, name, _ in app.PERFUME_PRODUCTS]

        self.assertIn("Rasasi Hawas Ice EDP for Men 100ml", names)
        self.assertIn("Rasasi Hawas Fire EDP 100ml", names)
        self.assertIn("Lattafa Atlas Eau De Parfum 55ml", names)
        self.assertIn("Al Rehab Choco Musk - Eau De Spray Perfume (50 ml)", names)
        self.assertNotIn("Rasasi Fattan Men 50ml EDP", names)
        self.assertEqual(app.perfume_details("perfume-007"), ("Rayhaan Aquatica EDP 100ml", 2650))
        self.assertIsNone(app.perfume_details("perfume-006"))

    def test_admin_can_add_custom_product_to_catalog(self):
        custom_id = "portal-led-product"
        app.add_custom_product(
            product_id=custom_id,
            name="Portal LED Product",
            price=1299,
            description="Added from portal",
            color="Black",
            image="https://example.com/portal-led-product.jpg",
        )

        product = app.get_catalog_product(custom_id)
        self.assertIsNotNone(product)
        self.assertEqual(product["name"], "Portal LED Product")
        self.assertEqual(product["price"], 1299)

    def test_admin_can_update_and_delete_custom_product(self):
        custom_id = "portal-update-product"
        app.add_custom_product(
            product_id=custom_id,
            name="Portal Update Product",
            price=1199,
            description="Old description",
            color="Gold",
            image="https://example.com/portal-update-product.jpg",
        )

        updated = app.update_custom_product(
            custom_id,
            name="Portal Updated Product",
            price=1399,
            description="New description",
            color="Black",
            image="https://example.com/portal-updated-product.jpg",
        )
        self.assertIsNotNone(updated)
        self.assertEqual(updated["name"], "Portal Updated Product")
        self.assertEqual(updated["price"], 1399)

        removed = app.delete_custom_product(custom_id)
        self.assertTrue(removed)
        self.assertIsNone(app.get_catalog_product(custom_id))

    def test_custom_product_stock_is_tracked_and_deducted_on_order(self):
        custom_id = "portal-stock-product"
        app.add_custom_product(
            product_id=custom_id,
            name="Portal Stock Product",
            price=1500,
            description="Inventory tracked",
            color="Cream",
            image="https://example.com/portal-stock-product.jpg",
            stock=8,
        )

        product = app.get_catalog_product(custom_id)
        self.assertEqual(product["stock"], 8)

        app.reserve_stock_for_order([{"id": custom_id, "quantity": 3}])
        updated = app.get_catalog_product(custom_id)
        self.assertEqual(updated["stock"], 5)

        app.delete_custom_product(custom_id)

    def test_admin_login_route_accepts_default_credentials(self):
        client = app.app.test_client()
        response = client.post(
            "/admin/login",
            data={"username": app.ADMIN_USERNAME, "password": app.ADMIN_PASSWORD},
            follow_redirects=False,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.headers.get("Location"), "/admin")

    def test_track_order_endpoint_by_reference_and_phone(self):
        client = app.app.test_client()
        # Track by reference
        response = client.get("/api/orders/track?reference=AR-TEST-ORDER")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["found"])
        self.assertEqual(data["order"]["reference"], "AR-TEST-ORDER")
        self.assertIn("****", data["order"]["customer_phone_masked"])

        # Track by phone
        response_phone = client.get("/api/orders/track?phone=01700000000")
        self.assertEqual(response_phone.status_code, 200)
        data_phone = response_phone.get_json()
        self.assertTrue(data_phone["found"])
        self.assertTrue(any(o["reference"] == "AR-TEST-ORDER" for o in data_phone["orders"]))

    def test_coupon_validation_and_order_discount(self):
        client = app.app.test_client()
        # Validate 10% coupon
        res = client.post("/api/coupons/validate", json={"code": "ARAMS10", "subtotal": 2000})
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(data["valid"])
        self.assertEqual(data["discount"], 200)
        self.assertEqual(data["final_total"], 1800)

        # Inactive or invalid coupon
        res_invalid = client.post("/api/coupons/validate", json={"code": "NONEXISTENT", "subtotal": 2000})
        self.assertEqual(res_invalid.status_code, 400)

        # Minimum spend requirement
        res_min = client.post("/api/coupons/validate", json={"code": "ARAMS10", "subtotal": 500})
        self.assertEqual(res_min.status_code, 400)

    def test_admin_analytics_endpoint(self):
        client = app.app.test_client()
        with client.session_transaction() as sess:
            sess["admin_logged_in"] = True

        res = client.get("/api/admin/analytics")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertIn("metrics", data)
        self.assertIn("total_revenue", data["metrics"])
        self.assertIn("status_breakdown", data)
        self.assertIn("top_products", data)

    def test_admin_export_orders_csv(self):
        client = app.app.test_client()
        with client.session_transaction() as sess:
            sess["admin_logged_in"] = True

        res = client.get("/api/admin/orders/export?format=steadfast")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.mimetype, "text/csv")
        self.assertIn("Invoice,Recipient Name,Recipient Phone", res.text)

    def test_unified_catalog_endpoint(self):
        client = app.app.test_client()
        res = client.get("/api/catalog?search=sola")
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertTrue(any("Sola Frames" in p["name"] for p in data["products"]))

    def test_verify_admin_password_supports_plain_and_hash(self):
        self.assertTrue(app.verify_admin_password("admin123"))
        self.assertFalse(app.verify_admin_password("wrong-password"))


if __name__ == "__main__":
    unittest.main()

