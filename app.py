import json
import os
import re
import secrets
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

from flask import Flask, abort, jsonify, redirect, request, send_from_directory, session


BASE_DIR = Path(__file__).resolve().parent
PRODUCTS = {
    "sola-frames": ("Sola Frames", 1850),
    "atlas-aviators": ("Atlas Aviators", 2100),
    "noir-square-sunglasses": ("Noir Square Sunglasses", 1950),
    "coast-round-sunglasses": ("Coast Round Sunglasses", 1750),
    "summit-sport-shades": ("Summit Sport Shades", 2250),
    "sunset-metal-shades": ("Sunset Metal Shades", 2400),
    "gulshan-cat-eye": ("Gulshan Cat-Eye Shades", 2150),
    "riverline-aviators": ("Riverline Aviators", 2350),
    "padma-polarized-shades": ("Padma Polarized Shades", 2600),
    "banani-soft-square": ("Banani Soft Square Shades", 2050),
    "field-watch": ("Field Watch", 3450),
    "luna-watch": ("Luna Watch", 3200),
    "metro-steel-watch": ("Metro Steel Watch", 2850),
    "heritage-leather-watch": ("Heritage Leather Watch", 2950),
    "noor-mini-watch": ("Noor Mini Watch", 2750),
    "apex-chronograph": ("Apex Chronograph", 4250),
    "rally-sport-watch": ("Rally Sport Watch", 2450),
    "sundarban-field-watch": ("Sundarban Field Watch", 3050),
    "dhaka-dial-watch": ("Dhaka Dial Watch", 3650),
    "meghna-mesh-watch": ("Meghna Mesh Watch", 3350),
    "uttara-classic-watch": ("Uttara Classic Watch", 3500),
    "motijheel-steel-watch": ("Motijheel Steel Watch", 3900),
    "casio-a159wa": ("Casio A-159WA Digital Watch", 990),
    "everyday-shirt": ("Everyday Shirt", 2250),
    "city-layer": ("City Layer", 3850),
    "mens-shorts": ("Everyday Shorts", 1850),
    "mens-trousers": ("Daily Trousers", 2650),
    "relaxed-cargo-trousers": ("Relaxed Cargo Trousers", 3150),
    "linen-wide-leg-trousers": ("Linen Wide-Leg Trousers", 2950),
    "city-pleat-trousers": ("City Pleat Trousers", 3250),
    "utility-denim-trousers": ("Utility Denim Trousers", 3050),
    "linen-straight-trousers": ("Linen Straight Trousers", 2850),
    "workday-twill-trousers": ("Workday Twill Trousers", 2950),
    "gulshan-wide-leg-trousers": ("Gulshan Wide-Leg Trousers", 3100),
    "uttara-cord-trousers": ("Uttara Cord Trousers", 3200),
    "weekend-tote": ("Weekend Tote", 2950),
    "soft-form": ("Soft Form Top", 2400),
}
PREMIUM_BAG_NAMES = [
    "Dhaka Carryall", "Jamuna Leather Satchel", "Bengal Work Tote",
    "Gulshan Shoulder Bag",
]
MARKET_SUNGLASSES = [
    ("Trendsetter Black Sunglasses", 897),
    ("White Metal Frame Sunglasses", 997),
    ("Unisex Plastic Summer Sunglasses", 977),
    ("RIDERACE Sports Cycling Goggles", 407),
    ("Popular Women's Punk Oval Y2K Sunglasses", 349),
    ("UV400 Windproof Cycling Goggles", 474),
    ("Y2K UV400 Sports Sunglasses", 402),
    ("Black to White UV400 Sunglasses", 339),
    ("White Frame Sunglasses for Men", 996),
    ("Transparent Frame Sunglasses for Men", 996),
    ("Wayfarer Sunglasses for Men", 996),
    ("SCVCN Outdoor MTB UV400 Glasses", 662),
    ("Polarized Round UV400 Sunglasses", 922),
    ("Vintage Cat Eye Sunglasses for Women", 277),
    ("ONEVAN 2023 Square Sunglasses", 995),
    ("DKS04694 Flexible Polycarbonate Sunglasses", 254),
    ("Unisex Metal UV Protection Sunglasses", 376),
    ("Roza Retro Sunglasses for Men", 219),
    ("Rectangular Black MC Stan Sunglasses", 998),
    ("OMEKOL Photochromic Cycling Glasses", 415),
]
PRONOUN_WATCHES = [
    ("Fastrack Urban Crest FT-UC-242", 999),
    ("Fastrack Meridian FT-MD-241", 1120),
    ("Universe Point Royal Noir UP-RN427", 999),
    ("Fastrack Groove 3321SM01 Men's Watch", 800),
    ("Fastrack PRN-SQ17 Modern Edge", 999),
    ("Mark M6278 Ultra Thin Watch", 1299),
    ("OMEGA ZQ98 Triple Calendar Watch", 1599),
    ("Fastrack 9947 Mens Watch", 750),
    ("Hublot Gang Sang Spider Dial Watch", 1050),
    ("Forest F-740", 1399),
    ("Titan Chain Man's Watch", 899),
    ("TOMI T077A Elegant Narrative", 899),
    ("Fastrack ES-214 Men's Watch", 850),
    ("Hublot Obsidian Prime", 999),
    ("Forest F-1035 Urban Drift Men's Watch", 1150),
]
KATUA_PRODUCTS = [
    ("Henley Katua Wooden | Lavender Blush", 1125),
    ("Henley Katua Wooden | Dark Olive", 1250),
    ("V-Neck Katua | Graphite Grey", 1350),
    ("V-Neck Katua | Black", 1350),
    ("V-Neck Katua | Mocha", 1350),
    ("V-Neck Katua | Grey", 1350),
    ("Henley Katua Wooden | Black", 1250),
    ("Henley Katua Wooden | Graphite Grey", 1250),
    ("Henley Katua Wooden | Mocha", 1250),
    ("V-Neck Katua | Dark Navy", 1350),
    ("V-Neck Katua | Sage", 1350),
    ("Henley Katua Wooden | Lime Green", 1125),
    ("Hooded Katua | Beige", 945),
    ("Hooded Katua | Black", 945),
    ("Henley Katua | Pastel Pink", 1125),
    ("Henley Katua Wooden | Brown", 1250),
    ("Henley Katua | Sage", 1125),
    ("Henley Katua | Grey", 1125),
    ("Henley Katua | Oasis Sandstone", 1250),
    ("Henley Katua | Mushroom Brown", 1062),
    ("Henley Katua | Printed Desert Sands", 1250),
    ("Henley Katua | Plum Wine", 1250),
    ("Henley Katua | Mocha", 1250),
]
PANTS_PRODUCTS = [
    ("Baggy Fit Cargo Pants in Off-White", 1500),
    ("Baggy Fit Cargo Pants in Dark Jungle Green", 1300),
    ("Baggy Fit Cargo Pants in Deep Blue", 1300),
    ("Baggy Fit Cargo Pants in Black", 1300),
    ("Men's Straight Fit Carpenter Pants in Black", 1300),
    ("Men's Straight Fit Carpenter Pants in Brown", 1300),
    ("Men's Baggy Cord Pants in Green", 1400),
    ("Men's Baggy Cord Pants in Off-White", 1400),
    ("Men's Baggy Cord Pants in Brown", 1400),
    ("Men's Baggy Cord Pants in Black", 1400),
    ("Unisex Baggy Jeans in Light Blue", 1850),
    ("Unisex Bootcut Jeans in Blue", 1850),
    ("Unisex Bootcut Jeans in Black", 1850),
    ("Unisex Baggy Jeans in Navy", 1850),
    ("Men's White Pleated Relaxed Gurkha Pants", 1800),
    ("Men's Light Grey Classic Pleated Gurkha Pants with New Belt", 1800),
    ("Men's Dark Brown Classic Pleated Gurkha Pants with New Belt", 1800),
    ("Men's Cream Classic Pleated Gurkha Pants with New Belt", 1800),
    ("Men's White Formal Pleated Pants", 1700),
    ("Men's Black Formal Pleated Pants", 1700),
    ("Men's Black Classic Pleated Gurkha Pants with New Belt", 1800),
    ("Men's White Straight Fit Pleated Formal Gurkha Pants", 1800),
    ("Men's Pinstripe High Waisted Relaxed Pants in Navy Blue", 1800),
    ("Men's Pinstripe High Waisted Relaxed Pants in Grey", 1800),
    ("Men's Barrel Pants in Black", 1500),
    ("Men's Classic Relaxed Fit Pants in White", 1700),
    ("Men's Classic Relaxed Fit Pants in Black", 1700),
    ("Pleated Summer Shorts in Cream", 800),
    ("Pleated Summer Shorts in Black", 800),
]
PERFUME_PRODUCTS = [
    ("perfume-001", "Rasasi Hawas Ice EDP for Men 100ml", 3100),
    ("perfume-002", "Karus Gold Absolu by Khadlaj EDP 100ml", 3150),
    ("perfume-003", "Al Rehab Choco Musk - Eau De Spray Perfume (50 ml)", 850),
    ("perfume-004", "Rasasi Hawas Fire EDP 100ml", 3999),
    ("perfume-005", "Lattafa Atlas Eau De Parfum 55ml", 3150),
    ("perfume-007", "Rayhaan Aquatica EDP 100ml", 2650),
    ("perfume-008", "Our Moment by One Direction For Women 50ml", 999),
]


def premium_bag_details(product_id):
    match = re.fullmatch(r"premium-bag-(\d{3})", product_id)
    if not match:
        return None
    index = int(match.group(1)) - 1
    if index < 0 or index >= len(PREMIUM_BAG_NAMES):
        return None
    return (
        f"{PREMIUM_BAG_NAMES[index % len(PREMIUM_BAG_NAMES)]} {index + 1:03d}",
        3850 + ((index * 375) % 12151),
    )


def market_sunglasses_details(product_id):
    match = re.fullmatch(r"market-sunglasses-(\d{3})", product_id)
    if not match:
        return None
    index = int(match.group(1)) - 1
    if index < 0 or index >= len(MARKET_SUNGLASSES):
        return None
    return MARKET_SUNGLASSES[index]


def pronoun_watch_details(product_id):
    match = re.fullmatch(r"pronoun-watch-(\d{3})", product_id)
    if not match:
        return None
    index = int(match.group(1)) - 1
    if index < 0 or index >= len(PRONOUN_WATCHES):
        return None
    return PRONOUN_WATCHES[index]


def katua_details(product_id):
    match = re.fullmatch(r"katua-(\d{3})", product_id)
    if not match:
        return None
    index = int(match.group(1)) - 1
    if index < 0 or index >= len(KATUA_PRODUCTS):
        return None
    return KATUA_PRODUCTS[index]


def pants_details(product_id):
    match = re.fullmatch(r"gorur-pants-(\d{3})", product_id)
    if not match:
        return None
    index = int(match.group(1)) - 1
    if index < 0 or index >= len(PANTS_PRODUCTS):
        return None
    return PANTS_PRODUCTS[index]


def perfume_details(product_id):
    for catalog_id, name, price in PERFUME_PRODUCTS:
        if catalog_id == product_id:
            return name, price
    return None

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024
app.secret_key = os.environ.get("ARAMS_SECRET_KEY", "arams-admin-secret-key")
default_database = "/tmp/orders.sqlite3" if os.environ.get("VERCEL") else str(Path(app.instance_path) / "orders.sqlite3")
app.config["DATABASE"] = os.environ.get(
    "ARAMS_DATABASE", default_database
)
WHATSAPP_NUMBER = re.sub(r"\D", "", os.environ.get("ARAMS_WHATSAPP", "8801815653564"))
ADMIN_USERNAME = os.environ.get("ARAMS_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ARAMS_ADMIN_PASSWORD", "admin123")


def require_admin_auth():
    if session.get("admin_logged_in"):
        return None
    if not ADMIN_PASSWORD:
        return None

    auth = request.authorization
    if auth is None or auth.username != ADMIN_USERNAME or auth.password != ADMIN_PASSWORD:
        response = jsonify({"error": "Admin authentication required."})
        response.status_code = 401
        response.headers["WWW-Authenticate"] = 'Basic realm="Admin"'
        return response
    return None


@app.before_request
def enforce_admin_access():
    admin_api_patterns = (
        request.path == "/api/orders" and request.method == "GET",
        request.path.startswith("/api/orders/") and request.method in {"PATCH", "DELETE"},
    )
    is_admin_page = request.path.startswith("/admin") and request.path not in {"/admin/login", "/admin/logout"}
    if is_admin_page or any(admin_api_patterns):
        auth_error = require_admin_auth()
        if auth_error is not None:
            return auth_error


def initialize_database():
    database_path = Path(app.config["DATABASE"])
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path, timeout=30)
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                reference TEXT PRIMARY KEY,
                customer_name TEXT NOT NULL,
                customer_phone TEXT NOT NULL,
                delivery_notes TEXT NOT NULL,
                customer_email TEXT NOT NULL DEFAULT '',
                items_json TEXT NOT NULL,
                total INTEGER NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                description TEXT NOT NULL DEFAULT '',
                color TEXT NOT NULL DEFAULT '',
                image TEXT NOT NULL DEFAULT '',
                stock INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            "SELECT COUNT(*) FROM pragma_table_info('products') WHERE name = 'stock'"
        )
        stock_exists = connection.execute(
            "SELECT COUNT(*) FROM pragma_table_info('products') WHERE name = 'stock'"
        ).fetchone()[0]
        if stock_exists == 0:
            connection.execute("ALTER TABLE products ADD COLUMN stock INTEGER NOT NULL DEFAULT 0")
        connection.commit()
    finally:
        connection.close()


def sanitize_product_id(product_id):
    if not isinstance(product_id, str):
        raise ValueError("Product ID is required.")
    cleaned = re.sub(r"[^a-z0-9-]+", "-", product_id.strip().lower())
    cleaned = cleaned.strip("-")
    if not cleaned:
        raise ValueError("Product ID is required.")
    return cleaned


def add_custom_product(product_id, name, price, description="", color="", image="", stock=0):
    normalized_id = sanitize_product_id(product_id)
    safe_name = clean_field(name, "Product name", 200)
    if not isinstance(price, int):
        raise ValueError("Price must be a whole number.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    if not isinstance(stock, int):
        raise ValueError("Stock must be a whole number.")
    if stock < 0:
        raise ValueError("Stock cannot be negative.")
    safe_description = clean_field(description or "", "Description", 500, required=False)
    safe_color = clean_field(color or "", "Color", 80, required=False)
    safe_image = clean_field(image or "", "Image URL", 500, required=False)
    created_at = datetime.now(timezone.utc).isoformat()

    connection = sqlite3.connect(app.config["DATABASE"], timeout=30)
    try:
        connection.execute(
            """
            INSERT INTO products (id, name, price, description, color, image, stock, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                name = excluded.name,
                price = excluded.price,
                description = excluded.description,
                color = excluded.color,
                image = excluded.image,
                stock = excluded.stock,
                created_at = excluded.created_at
            """,
            (
                normalized_id,
                safe_name,
                price,
                safe_description,
                safe_color,
                safe_image,
                stock,
                created_at,
            ),
        )
        connection.commit()
    finally:
        connection.close()

    return get_catalog_product(normalized_id)


def update_custom_product(product_id, **updates):
    normalized_id = sanitize_product_id(product_id)
    if not updates:
        return get_catalog_product(normalized_id)

    safe_updates = {}
    if "name" in updates:
        safe_updates["name"] = clean_field(updates["name"], "Product name", 200)
    if "price" in updates:
        price = updates["price"]
        if not isinstance(price, int):
            raise ValueError("Price must be a whole number.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        safe_updates["price"] = price
    if "description" in updates:
        safe_updates["description"] = clean_field(updates.get("description", "") or "", "Description", 500, required=False)
    if "color" in updates:
        safe_updates["color"] = clean_field(updates.get("color", "") or "", "Color", 80, required=False)
    if "image" in updates:
        safe_updates["image"] = clean_field(updates.get("image", "") or "", "Image URL", 500, required=False)
    if "stock" in updates:
        stock = updates.get("stock")
        if stock is None:
            safe_updates["stock"] = 0
        else:
            if not isinstance(stock, int):
                raise ValueError("Stock must be a whole number.")
            if stock < 0:
                raise ValueError("Stock cannot be negative.")
            safe_updates["stock"] = stock

    connection = sqlite3.connect(app.config["DATABASE"], timeout=30)
    try:
        existing = connection.execute(
            "SELECT 1 FROM products WHERE id = ? LIMIT 1",
            (normalized_id,),
        ).fetchone()
        if existing is None:
            return None
        assignments = ", ".join(f"{key} = ?" for key in safe_updates)
        values = list(safe_updates.values()) + [normalized_id]
        connection.execute(
            f"UPDATE products SET {assignments} WHERE id = ?",
            tuple(values),
        )
        connection.commit()
    finally:
        connection.close()
    return get_catalog_product(normalized_id)


def delete_custom_product(product_id):
    normalized_id = sanitize_product_id(product_id)
    connection = sqlite3.connect(app.config["DATABASE"], timeout=30)
    try:
        cursor = connection.execute(
            "DELETE FROM products WHERE id = ?",
            (normalized_id,),
        )
        connection.commit()
    finally:
        connection.close()
    return cursor.rowcount > 0


def list_custom_products(limit=100):
    connection = sqlite3.connect(app.config["DATABASE"])
    try:
        rows = connection.execute(
            """
            SELECT id, name, price, description, color, image, stock
            FROM products
            ORDER BY created_at DESC, rowid DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        connection.close()
    return [
        {
            "id": product_id,
            "name": name,
            "price": price,
            "description": description,
            "color": color,
            "image": image,
            "stock": stock,
        }
        for product_id, name, price, description, color, image, stock in rows
    ]


def get_catalog_product(product_id):
    if not isinstance(product_id, str):
        return None
    normalized_id = sanitize_product_id(product_id)
    connection = sqlite3.connect(app.config["DATABASE"])
    try:
        row = connection.execute(
            """
            SELECT id, name, price, description, color, image, stock
            FROM products
            WHERE id = ?
            LIMIT 1
            """,
            (normalized_id,),
        ).fetchone()
    finally:
        connection.close()

    if row is not None:
        product_id, name, price, description, color, image, stock = row
        return {"id": product_id, "name": name, "price": price, "description": description, "color": color, "image": image, "stock": stock}

    if product_id in PRODUCTS:
        name, price = PRODUCTS[product_id]
        return {"id": product_id, "name": name, "price": price, "description": "In stock", "color": "Standard", "image": "", "stock": 999}

    for matcher in (premium_bag_details, market_sunglasses_details, pronoun_watch_details, katua_details, pants_details, perfume_details):
        details = matcher(product_id)
        if details is not None:
            if isinstance(details, tuple) and len(details) == 2:
                name, price = details
                return {"id": product_id, "name": name, "price": price, "description": "In stock", "color": "Standard", "image": "", "stock": 999}
    return None


VALID_ORDER_STATUSES = {
    "awaiting_whatsapp",
    "awaiting_payment",
    "paid",
    "packed",
    "shipped",
    "completed",
    "cancelled",
}


def _deserialize_order_row(row):
    if row is None:
        return None
    (
        reference,
        customer_name,
        customer_phone,
        customer_email,
        delivery_notes,
        items_json,
        total,
        status,
        created_at,
    ) = row
    return {
        "reference": reference,
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "customer_email": customer_email,
        "delivery_notes": delivery_notes,
        "items": json.loads(items_json or "[]"),
        "total": total,
        "status": status,
        "created_at": created_at,
    }


def get_order_by_reference(reference):
    if not isinstance(reference, str) or not reference.strip():
        return None
    connection = sqlite3.connect(app.config["DATABASE"])
    try:
        row = connection.execute(
            """
            SELECT reference, customer_name, customer_phone, customer_email,
                   delivery_notes, items_json, total, status, created_at
            FROM orders
            WHERE reference = ?
            LIMIT 1
            """,
            (reference.strip(),),
        ).fetchone()
    finally:
        connection.close()
    return _deserialize_order_row(row)


def list_orders(limit=50):
    connection = sqlite3.connect(app.config["DATABASE"])
    try:
        rows = connection.execute(
            """
            SELECT reference, customer_name, customer_phone, customer_email,
                   delivery_notes, items_json, total, status, created_at
            FROM orders
            ORDER BY created_at DESC, rowid DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        connection.close()

    return [_deserialize_order_row(row) for row in rows]


def update_order_status(reference, status):
    if not isinstance(reference, str) or not reference.strip():
        raise ValueError("Order reference is required.")
    if not isinstance(status, str):
        raise ValueError("Order status is required.")
    normalized_status = status.strip().lower()
    if normalized_status not in VALID_ORDER_STATUSES:
        allowed = ", ".join(sorted(VALID_ORDER_STATUSES))
        raise ValueError(f"Status must be one of: {allowed}.")

    existing_order = get_order_by_reference(reference)
    if existing_order is None:
        return False

    connection = sqlite3.connect(app.config["DATABASE"], timeout=30)
    try:
        cursor = connection.execute(
            "UPDATE orders SET status = ? WHERE reference = ?",
            (normalized_status, reference.strip()),
        )
        connection.commit()
    finally:
        connection.close()
    return cursor.rowcount > 0


def cancel_order(reference):
    return update_order_status(reference, "cancelled")


def reserve_stock_for_order(items):
    if not isinstance(items, list):
        return

    connection = sqlite3.connect(app.config["DATABASE"], timeout=30)
    try:
        for item in items:
            if not isinstance(item, dict):
                continue
            product_id = item.get("id")
            quantity = item.get("quantity", 0)
            if not isinstance(product_id, str) or not isinstance(quantity, int) or quantity < 1:
                continue
            row = connection.execute(
                "SELECT id, name, stock FROM products WHERE id = ? LIMIT 1",
                (sanitize_product_id(product_id),),
            ).fetchone()
            if row is None:
                continue
            _, _, stock = row
            if quantity > stock:
                raise ValueError(f"Only {stock} units left for {product_id}.")
            connection.execute(
                "UPDATE products SET stock = stock - ? WHERE id = ?",
                (quantity, sanitize_product_id(product_id)),
            )
        connection.commit()
    finally:
        connection.close()


def clean_field(value, field, maximum, required=True):
    if value is None:
        if required:
            raise ValueError(f"{field} is required.")
        return ""
    if not isinstance(value, str):
        raise ValueError(f"{field} must be text.")
    value = value.strip()
    if required and not value:
        raise ValueError(f"{field} is required.")
    if len(value) > maximum:
        raise ValueError(f"{field} is too long.")
    return value


def build_order(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("customer"), dict):
        raise ValueError("Order details are missing.")

    customer_data = payload["customer"]
    customer = {
        "name": clean_field(customer_data.get("name"), "Name", 120),
        "phone": clean_field(customer_data.get("phone"), "Phone", 40),
        "email": clean_field(customer_data.get("email", ""), "Email", 254, required=False),
        "notes": clean_field(customer_data.get("notes"), "Delivery or pickup details", 1000),
    }
    requested_items = payload.get("items")
    if not isinstance(requested_items, list) or not requested_items or len(requested_items) > 50:
        raise ValueError("Add at least one product to your order.")

    items = []
    for requested_item in requested_items:
        if not isinstance(requested_item, dict):
            raise ValueError("An order item is invalid.")
        product_id = requested_item.get("id")
        quantity = requested_item.get("quantity")
        product_details = PRODUCTS.get(product_id) if isinstance(product_id, str) else None
        if product_details is None and isinstance(product_id, str):
            product_details = premium_bag_details(product_id)
        if product_details is None and isinstance(product_id, str):
            product_details = market_sunglasses_details(product_id)
        if product_details is None and isinstance(product_id, str):
            product_details = pronoun_watch_details(product_id)
        if product_details is None and isinstance(product_id, str):
            product_details = katua_details(product_id)
        if product_details is None and isinstance(product_id, str):
            product_details = pants_details(product_id)
        if product_details is None and isinstance(product_id, str):
            product_details = perfume_details(product_id)
        if product_details is None:
            raise ValueError("A selected product is unavailable.")
        if type(quantity) is not int or quantity < 1 or quantity > 99:
            raise ValueError("Product quantity must be between 1 and 99.")
        product_name, unit_price = product_details
        items.append({
            "id": product_id,
            "name": product_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": unit_price * quantity,
        })

    return customer, items, sum(item["line_total"] for item in items)


def make_whatsapp_url(reference, customer, items, total):
    message_lines = [f"ARAMS order {reference}", ""]
    message_lines.extend(
        f"{item['name']} x {item['quantity']} — ৳{item['line_total']:,}" for item in items
    )
    message_lines.extend([
        "",
        f"Total: ৳{total:,}",
        f"Name: {customer['name']}",
        f"Customer phone: {customer['phone']}",
    ])
    if customer["email"]:
        message_lines.append(f"Email: {customer['email']}")
    message_lines.append(f"Delivery / pickup: {customer['notes']}")
    return f"https://wa.me/{WHATSAPP_NUMBER}?{urlencode({'text': chr(10).join(message_lines)})}"


@app.get("/api/health")
def health_check():
    return jsonify({
        "status": "ok",
        "database": app.config["DATABASE"],
        "products": len(PRODUCTS),
    })


@app.get("/api/products")
def list_products_endpoint():
    query = (request.args.get("search") or "").strip().lower()
    category = (request.args.get("category") or "").strip().lower()
    products = list_custom_products(limit=200)

    if query:
        products = [
            product for product in products
            if query in product["name"].lower()
            or query in (product.get("description") or "").lower()
        ]
    if category:
        products = [
            product for product in products
            if category in product["name"].lower()
            or category in (product.get("description") or "").lower()
        ]
    return jsonify({"products": products, "count": len(products)})


@app.get("/api/products/<product_id>")
def get_single_product_endpoint(product_id):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    product = get_catalog_product(product_id)
    if product is None:
        return jsonify({"error": "Product not found."}), 404
    return jsonify({"product": product})


@app.patch("/api/products/<product_id>")
def update_product_endpoint(product_id):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    try:
        product = update_custom_product(
            product_id,
            name=payload.get("name"),
            price=int(payload.get("price", 0)) if payload.get("price") not in (None, "") else None,
            description=payload.get("description"),
            color=payload.get("color"),
            image=payload.get("image"),
            stock=int(payload.get("stock", 0) or 0) if payload.get("stock") not in (None, "") else None,
        )
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    if product is None:
        return jsonify({"error": "Product not found."}), 404
    return jsonify({"product": product, "success": True})


@app.delete("/api/products/<product_id>")
def delete_product_endpoint(product_id):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    deleted = delete_custom_product(product_id)
    if not deleted:
        return jsonify({"error": "Product not found."}), 404
    return jsonify({"success": True, "deleted": True})


@app.post("/api/products")
def create_product_endpoint():
    if not session.get("admin_logged_in"):
        auth_error = require_admin_auth()
        if auth_error is not None:
            return auth_error

    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    try:
        product = add_custom_product(
            product_id=payload.get("id", payload.get("product_id")),
            name=payload.get("name"),
            price=int(payload.get("price", 0)),
            description=payload.get("description", ""),
            color=payload.get("color", ""),
            image=payload.get("image", ""),
            stock=int(payload.get("stock", 0) or 0),
        )
    except ValueError as error:
        return jsonify({"error": str(error)}), 400
    return jsonify({"product": product, "success": True}), 201


@app.get("/api/orders")
def list_orders_endpoint():
    orders = list_orders(limit=100)
    return jsonify({"orders": orders})


@app.get("/api/orders/<reference>")
def get_order_endpoint(reference):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    order = get_order_by_reference(reference)
    if order is None:
        return jsonify({"error": "Order not found."}), 404
    return jsonify({"order": order})


@app.patch("/api/orders/<reference>/status")
def update_order_status_endpoint(reference):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    payload = request.get_json(silent=True) or {}
    status = payload.get("status")
    try:
        updated = update_order_status(reference, status)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    if not updated:
        return jsonify({"error": "Order not found."}), 404

    normalized_status = status.strip().lower() if isinstance(status, str) else status
    return jsonify({"reference": reference, "status": normalized_status, "updated": True})


@app.delete("/api/orders/<reference>")
def delete_order_endpoint(reference):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    updated = cancel_order(reference)
    if not updated:
        return jsonify({"error": "Order not found."}), 404
    return jsonify({"reference": reference, "status": "cancelled", "deleted": True})


@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "Not found."}), 404
    return error


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/buy")
def buy_page():
    return send_from_directory(BASE_DIR, "buy.html")


@app.get("/admin")
@app.get("/admin/orders")
def admin_orders_page():
    if not session.get("admin_logged_in"):
        return send_from_directory(BASE_DIR, "admin_login.html")
    return send_from_directory(BASE_DIR, "admin_orders.html")


@app.get("/admin/login")
def admin_login_page():
    if session.get("admin_logged_in"):
        return redirect("/admin")
    return send_from_directory(BASE_DIR, "admin_login.html")


@app.post("/admin/login")
def admin_login_submit():
    payload = request.form.to_dict()
    username = payload.get("username", "")
    password = payload.get("password", "")
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        session["admin_logged_in"] = True
        return redirect("/admin")
    return send_from_directory(BASE_DIR, "admin_login.html")


@app.get("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    return redirect("/admin/login")


@app.get("/watch/casio-a159wa")
def casio_product_page():
    return send_from_directory(BASE_DIR, "casio.html")


@app.get("/product/<product_id>")
def product_page(product_id):
    if product_id == "casio-a159wa":
        return send_from_directory(BASE_DIR, "casio.html")
    return send_from_directory(BASE_DIR, "product.html")


@app.get("/<path:filename>")
def frontend_asset(filename):
    if filename not in {"app.js", "buy.js", "styles.css", "buy.html", "casio.html", "product.html", "product.js"}:
        abort(404)
    return send_from_directory(BASE_DIR, filename)


@app.post("/api/orders")
def create_order():
    payload = request.get_json(silent=True)
    try:
        customer, items, total = build_order(payload)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    reference = f"AR-{secrets.token_hex(4).upper()}"
    created_at = datetime.now(timezone.utc).isoformat()
    reserve_stock_for_order(items)
    connection = sqlite3.connect(app.config["DATABASE"])
    try:
        connection.execute(
            """
            INSERT INTO orders (
                reference, customer_name, customer_phone, customer_email,
                delivery_notes, items_json, total, status, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                reference,
                customer["name"],
                customer["phone"],
                customer["email"],
                customer["notes"],
                json.dumps(items),
                total,
                "awaiting_whatsapp",
                created_at,
            ),
        )
        connection.commit()
    finally:
        connection.close()

    return jsonify({
        "reference": reference,
        "total": total,
        "whatsapp_url": make_whatsapp_url(reference, customer, items, total),
    }), 201


initialize_database()


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )