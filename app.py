import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass
import csv
import io
import json
import os
import re
import secrets
import sqlite3
import psycopg2
import psycopg2.extras
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

from flask import Flask, Response, abort, jsonify, redirect, request, send_from_directory, session
from werkzeug.security import check_password_hash, generate_password_hash


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
    ("perfume-001", "Arabiyat Oud al Layl Midnight Edition EDP 100ml", 1850),
    ("perfume-002", "Tad Angel Attractive EDP Men 100ml", 1650),
    ("perfume-003", "Vampire Blood Perfume Oil (Euro Valley)", 850),
    ("perfume-004", "Brandy Perfumes Sunset EDP 100ml", 1450),
    ("perfume-005", "Jean Lowe Azure by Maison Alhambra EDP 100ml", 3500),
    ("perfume-006", "Swiss Arabian Shaghaf Oud Ahmar 75ml", 4200),
    ("perfume-007", "Rasasi Hawas Ice EDP for Men 100ml", 3100),
    ("perfume-008", "Maison Francis Kurkdjian Baccarat Rouge 540 EDP", 32500),
    ("perfume-009", "Parfums de Marly Layton EDP for Men 125ml", 24500),
    ("perfume-010", "Xerjoff Erba Pura EDP Unisex 100ml", 21000),
    ("perfume-011", "Amouage Interlude Man EDP 100ml", 28000),
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
app.secret_key = os.environ.get("ARAMS_SECRET_KEY") or secrets.token_hex(32)
default_database = "/tmp/orders.sqlite3" if os.environ.get("VERCEL") else str(Path(app.instance_path) / "orders.sqlite3")
app.config["DATABASE"] = os.environ.get(
    "ARAMS_DATABASE", default_database
)
WHATSAPP_NUMBER = re.sub(r"\D", "", os.environ.get("ARAMS_WHATSAPP", "8801815653564"))
ADMIN_USERNAME = os.environ.get("ARAMS_ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ARAMS_ADMIN_PASSWORD")

if not ADMIN_PASSWORD:
    ADMIN_PASSWORD = secrets.token_urlsafe(16)
    print(f"\n[SECURITY WARNING] No ARAMS_ADMIN_PASSWORD set. Generated random admin password: {ADMIN_PASSWORD}\n", flush=True)


def verify_admin_password(provided_password):
    if not isinstance(provided_password, str) or not provided_password:
        return False
    if ADMIN_PASSWORD.startswith(("scrypt:", "pbkdf2:", "argon2:")):
        return check_password_hash(ADMIN_PASSWORD, provided_password)
    return secrets.compare_digest(ADMIN_PASSWORD, provided_password)


def require_admin_auth():
    if session.get("admin_logged_in"):
        return None

    auth = request.authorization
    if auth is None or auth.username != ADMIN_USERNAME or not verify_admin_password(auth.password):
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
        request.path.startswith("/api/admin/"),
    )
    is_admin_page = request.path.startswith("/admin") and request.path not in {"/admin/login", "/admin/logout"}
    if is_admin_page or any(admin_api_patterns):
        auth_error = require_admin_auth()
        if auth_error is not None:
            return auth_error


@app.errorhandler(400)
def bad_request_error(e):
    return jsonify({"error": "Bad request", "message": str(e)}), 400

@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Not found", "message": "The requested resource could not be found."}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error", "message": "An unexpected error occurred."}), 500



class PostgresCursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor
        
    def fetchone(self):
        return self.cursor.fetchone()
        
    def fetchall(self):
        return self.cursor.fetchall()
        
    @property
    def rowcount(self):
        return self.cursor.rowcount

class PostgresConnectionWrapper:
    def __init__(self, dsn):
        self.conn = psycopg2.connect(dsn)
        self.conn.autocommit = False
    
    def execute(self, query, params=()):
        query = query.replace("?", "%s")
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return PostgresCursorWrapper(cursor)
        
    def executemany(self, query, params_list):
        query = query.replace("?", "%s")
        cursor = self.conn.cursor()
        cursor.executemany(query, params_list)
        return PostgresCursorWrapper(cursor)
        
    def commit(self):
        self.conn.commit()
        
    def close(self):
        self.conn.close()

def get_db_connection(database_path=None):
    dsn = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
    if dsn:
        return PostgresConnectionWrapper(dsn)
    if database_path:
        return sqlite3.connect(database_path, timeout=30)
    return sqlite3.connect(app.config["DATABASE"], timeout=30)

def initialize_database():
    database_path = Path(app.config["DATABASE"])
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = get_db_connection(database_path)
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
            """
            CREATE TABLE IF NOT EXISTS coupons (
                code TEXT PRIMARY KEY,
                discount_type TEXT NOT NULL,
                discount_value INTEGER NOT NULL,
                min_spend INTEGER NOT NULL DEFAULT 0,
                max_uses INTEGER NOT NULL DEFAULT 0,
                used_count INTEGER NOT NULL DEFAULT 0,
                expires_at TEXT NOT NULL DEFAULT '',
                active INTEGER NOT NULL DEFAULT 1,
                created_at TEXT NOT NULL DEFAULT ''
            )
            """
        )

        dsn = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
        if dsn:
            order_cols = {row[0] for row in connection.execute("SELECT column_name FROM information_schema.columns WHERE table_name='orders'").fetchall()}
        else:
            order_cols = {row[1] for row in connection.execute("PRAGMA table_info('orders')").fetchall()}
        if "courier_name" not in order_cols:
            connection.execute("ALTER TABLE orders ADD COLUMN courier_name TEXT NOT NULL DEFAULT ''")
        if "tracking_code" not in order_cols:
            connection.execute("ALTER TABLE orders ADD COLUMN tracking_code TEXT NOT NULL DEFAULT ''")
        if "discount" not in order_cols:
            connection.execute("ALTER TABLE orders ADD COLUMN discount INTEGER NOT NULL DEFAULT 0")
        if "coupon_code" not in order_cols:
            connection.execute("ALTER TABLE orders ADD COLUMN coupon_code TEXT NOT NULL DEFAULT ''")

        dsn = os.environ.get("DATABASE_URL") or os.environ.get("POSTGRES_URL")
        if dsn:
            product_cols = {row[0] for row in connection.execute("SELECT column_name FROM information_schema.columns WHERE table_name='products'").fetchall()}
        else:
            product_cols = {row[1] for row in connection.execute("PRAGMA table_info('products')").fetchall()}
        if "stock" not in product_cols:
            connection.execute("ALTER TABLE products ADD COLUMN stock INTEGER NOT NULL DEFAULT 0")

        coupon_count = connection.execute("SELECT COUNT(*) FROM coupons").fetchone()[0]
        if coupon_count == 0:
            now_iso = datetime.now(timezone.utc).isoformat()
            default_coupons = [
                ("ARAMS10", "percent", 10, 1500, 0, 0, "", 1, now_iso),
                ("EID2026", "fixed", 500, 3000, 0, 0, "", 1, now_iso),
                ("WELCOME", "fixed", 200, 1000, 0, 0, "", 1, now_iso),
            ]
            connection.executemany(
                """
                INSERT INTO coupons (code, discount_type, discount_value, min_spend, max_uses, used_count, expires_at, active, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                default_coupons,
            )

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
    safe_image = clean_field(image or "", "Image URL", 2000, required=False)
    created_at = datetime.now(timezone.utc).isoformat()

    connection = get_db_connection()
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
        safe_updates["image"] = clean_field(updates.get("image", "") or "", "Image URL", 2000, required=False)
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

    connection = get_db_connection()
    try:
        existing = connection.execute(
            "SELECT 1 FROM products WHERE id = ? LIMIT 1",
            (normalized_id,),
        ).fetchone()
        if existing is None:
            return None
        if not safe_updates:
            return get_catalog_product(normalized_id)
            
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
    connection = get_db_connection()
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
    connection = get_db_connection()
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
    connection = get_db_connection()
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
    reference = row[0]
    customer_name = row[1]
    customer_phone = row[2]
    customer_email = row[3]
    delivery_notes = row[4]
    items_json = row[5]
    total = row[6]
    status = row[7]
    created_at = row[8]
    courier_name = row[9] if len(row) > 9 else ""
    tracking_code = row[10] if len(row) > 10 else ""
    discount = row[11] if len(row) > 11 else 0
    coupon_code = row[12] if len(row) > 12 else ""

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
        "courier_name": courier_name,
        "tracking_code": tracking_code,
        "discount": discount,
        "coupon_code": coupon_code,
    }


def get_order_by_reference(reference):
    if not isinstance(reference, str) or not reference.strip():
        return None
    connection = get_db_connection()
    try:
        row = connection.execute(
            """
            SELECT reference, customer_name, customer_phone, customer_email,
                   delivery_notes, items_json, total, status, created_at,
                   courier_name, tracking_code, discount, coupon_code
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
    connection = get_db_connection()
    try:
        rows = connection.execute(
            """
            SELECT reference, customer_name, customer_phone, customer_email,
                   delivery_notes, items_json, total, status, created_at,
                   courier_name, tracking_code, discount, coupon_code
            FROM orders
            ORDER BY created_at DESC, rowid DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
    finally:
        connection.close()

    return [_deserialize_order_row(row) for row in rows]


def update_order_status(reference, status, courier_name=None, tracking_code=None):
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

    connection = get_db_connection()
    try:
        if courier_name is not None or tracking_code is not None:
            cursor = connection.execute(
                """
                UPDATE orders
                SET status = ?,
                    courier_name = COALESCE(?, courier_name),
                    tracking_code = COALESCE(?, tracking_code)
                WHERE reference = ?
                """,
                (normalized_status, courier_name, tracking_code, reference.strip()),
            )
        else:
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

    connection = get_db_connection()
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


def validate_coupon(code, subtotal):
    if not isinstance(code, str) or not code.strip():
        raise ValueError("Coupon code is required.")
    if not isinstance(subtotal, int) or subtotal <= 0:
        raise ValueError("Subtotal must be greater than zero.")

    normalized_code = code.strip().upper()
    connection = get_db_connection()
    try:
        row = connection.execute(
            """
            SELECT code, discount_type, discount_value, min_spend, max_uses, used_count, expires_at, active
            FROM coupons
            WHERE code = ?
            LIMIT 1
            """,
            (normalized_code,),
        ).fetchone()
    finally:
        connection.close()

    if row is None:
        raise ValueError(f"Coupon '{normalized_code}' does not exist.")

    code, discount_type, discount_value, min_spend, max_uses, used_count, expires_at, active = row
    if not active:
        raise ValueError(f"Coupon '{normalized_code}' is currently inactive.")

    if expires_at:
        try:
            exp_date = datetime.fromisoformat(expires_at)
            if datetime.now(timezone.utc) > exp_date:
                raise ValueError(f"Coupon '{normalized_code}' has expired.")
        except (ValueError, TypeError):
            pass

    if max_uses > 0 and used_count >= max_uses:
        raise ValueError(f"Coupon '{normalized_code}' has reached its maximum usage limit.")

    if subtotal < min_spend:
        raise ValueError(f"Coupon '{normalized_code}' requires a minimum spend of ৳{min_spend:,}.")

    if discount_type == "percent":
        discount = int(subtotal * discount_value / 100)
    elif discount_type == "fixed":
        discount = min(discount_value, subtotal)
    else:
        raise ValueError("Invalid coupon configuration.")

    final_total = max(0, subtotal - discount)
    return {
        "valid": True,
        "code": normalized_code,
        "discount_type": discount_type,
        "discount_value": discount_value,
        "discount": discount,
        "final_total": final_total,
        "message": f"Coupon applied: ৳{discount:,} off!",
    }


def record_coupon_usage(code):
    if not code:
        return
    normalized_code = code.strip().upper()
    connection = get_db_connection()
    try:
        connection.execute(
            "UPDATE coupons SET used_count = used_count + 1 WHERE code = ?",
            (normalized_code,),
        )
        connection.commit()
    finally:
        connection.close()


def build_order(payload, coupon_code=None):
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
        if product_details is None and isinstance(product_id, str):
            custom_product = get_catalog_product(product_id)
            if custom_product is not None:
                product_details = (custom_product["name"], custom_product["price"])
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

    subtotal = sum(item["line_total"] for item in items)
    discount = 0
    coupon = coupon_code or payload.get("coupon_code") or (payload.get("customer") or {}).get("coupon_code")
    if coupon and isinstance(coupon, str) and coupon.strip():
        coupon_res = validate_coupon(coupon, subtotal)
        discount = coupon_res["discount"]

    final_total = max(0, subtotal - discount)
    return customer, items, final_total


def make_whatsapp_url(reference, customer, items, total, discount=0, coupon_code=""):
    message_lines = [f"ARAMS order {reference}", ""]
    message_lines.extend(
        f"{item['name']} x {item['quantity']} — ৳{item['line_total']:,}" for item in items
    )
    if discount > 0 and coupon_code:
        subtotal = total + discount
        message_lines.append("")
        message_lines.append(f"Subtotal: ৳{subtotal:,}")
        message_lines.append(f"Coupon ({coupon_code}): -৳{discount:,}")
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
    
    # Start with custom products from the database
    products = list_custom_products(limit=200)
    
    # Merge hardcoded PERFUME_PRODUCTS
    for p_id, p_name, p_price in PERFUME_PRODUCTS:
        products.append({"id": p_id, "name": p_name, "price": p_price, "description": "Premium Fragrance", "color": "Full bottle", "image": "", "stock": 999})
        
    # Merge PANTS_PRODUCTS
    for i, (p_name, p_price) in enumerate(PANTS_PRODUCTS):
        products.append({"id": f"gorur-pants-{i+1:03d}", "name": p_name, "price": p_price, "description": "Apparel", "color": "Standard", "image": "", "stock": 999})
        
    # Merge KATUA_PRODUCTS
    for i, (p_name, p_price) in enumerate(KATUA_PRODUCTS):
        products.append({"id": f"katua-{i+1:03d}", "name": p_name, "price": p_price, "description": "Katua Apparel", "color": "Standard", "image": "", "stock": 999})
        
    # Merge MARKET_SUNGLASSES
    for i, (p_name, p_price) in enumerate(MARKET_SUNGLASSES):
        products.append({"id": f"market-sunglasses-{i+1:03d}", "name": p_name, "price": p_price, "description": "Sunglasses", "color": "Standard", "image": "", "stock": 999})
        
    # Merge PRONOUN_WATCHES
    for i, (p_name, p_price) in enumerate(PRONOUN_WATCHES):
        products.append({"id": f"pronoun-watch-{i+1:03d}", "name": p_name, "price": p_price, "description": "Watches", "color": "Standard", "image": "", "stock": 999})
        
    # Merge PREMIUM_BAG_NAMES
    for i, p_name in enumerate(PREMIUM_BAG_NAMES):
        bag_name, bag_price = premium_bag_details(f"premium-bag-{i+1:03d}")
        products.append({"id": f"premium-bag-{i+1:03d}", "name": bag_name, "price": bag_price, "description": "Premium Bag", "color": "Standard", "image": "", "stock": 999})
        
    # Merge base PRODUCTS
    for p_id, (p_name, p_price) in PRODUCTS.items():
        products.append({"id": p_id, "name": p_name, "price": p_price, "description": "In stock", "color": "Standard", "image": "", "stock": 999})

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
    courier_name = payload.get("courier_name")
    tracking_code = payload.get("tracking_code")
    try:
        updated = update_order_status(reference, status, courier_name=courier_name, tracking_code=tracking_code)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    if not updated:
        return jsonify({"error": "Order not found."}), 404

    normalized_status = status.strip().lower() if isinstance(status, str) else status
    return jsonify({
        "reference": reference,
        "status": normalized_status,
        "courier_name": courier_name,
        "tracking_code": tracking_code,
        "updated": True,
    })


@app.delete("/api/orders/<reference>")
def delete_order_endpoint(reference):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    updated = cancel_order(reference)
    if not updated:
        return jsonify({"error": "Order not found."}), 404
    return jsonify({"reference": reference, "status": "cancelled", "deleted": True})


STATUS_MESSAGES = {
    "awaiting_whatsapp": {
        "badge": "Awaiting WhatsApp",
        "description": "Order registered in system. Awaiting customer confirmation via WhatsApp.",
        "step": 1,
    },
    "awaiting_payment": {
        "badge": "Payment Pending",
        "description": "Order confirmed. Awaiting payment or COD validation.",
        "step": 2,
    },
    "paid": {
        "badge": "Confirmed & Paid",
        "description": "Payment received or COD approved. Preparing for dispatch.",
        "step": 3,
    },
    "packed": {
        "badge": "Packed & Ready",
        "description": "Your items are carefully packed and ready for courier pickup.",
        "step": 3,
    },
    "shipped": {
        "badge": "Shipped / In Transit",
        "description": "Parcel handed over to courier for delivery. Expect arrival in 24-48 hours.",
        "step": 4,
    },
    "completed": {
        "badge": "Delivered",
        "description": "Order delivered successfully. Thank you for shopping with ARAMS!",
        "step": 5,
    },
    "cancelled": {
        "badge": "Cancelled",
        "description": "This order has been cancelled.",
        "step": 0,
    },
}


def mask_string(val, is_email=False):
    if not val:
        return ""
    if is_email and "@" in val:
        user, domain = val.split("@", 1)
        masked_user = user[0] + "***" if len(user) > 1 else user + "***"
        return f"{masked_user}@{domain}"
    if len(val) >= 7:
        return val[:3] + "****" + val[-3:]
    return val[:2] + "****"


@app.get("/api/orders/track")
def track_order_endpoint():
    reference = (request.args.get("reference") or "").strip()
    phone = (request.args.get("phone") or "").strip()

    if not reference and not phone:
        return jsonify({"error": "Please provide an order reference or phone number."}), 400

    connection = get_db_connection()
    try:
        if reference:
            row = connection.execute(
                """
                SELECT reference, customer_name, customer_phone, customer_email,
                       delivery_notes, items_json, total, status, created_at,
                       courier_name, tracking_code, discount, coupon_code
                FROM orders
                WHERE reference = ?
                LIMIT 1
                """,
                (reference,),
            ).fetchone()

            if row is None:
                return jsonify({"found": False, "error": f"No order found with reference '{reference}'."}), 404

            order = _deserialize_order_row(row)
            status_info = STATUS_MESSAGES.get(order["status"], {
                "badge": order["status"].replace("_", " ").title(),
                "description": "Order is being processed.",
                "step": 1,
            })

            return jsonify({
                "found": True,
                "order": {
                    "reference": order["reference"],
                    "customer_name": order["customer_name"],
                    "customer_phone_masked": mask_string(order["customer_phone"]),
                    "customer_email_masked": mask_string(order["customer_email"], is_email=True),
                    "items": order["items"],
                    "total": order["total"],
                    "discount": order["discount"],
                    "status": order["status"],
                    "status_badge": status_info["badge"],
                    "status_description": status_info["description"],
                    "step": status_info["step"],
                    "courier_name": order["courier_name"],
                    "tracking_code": order["tracking_code"],
                    "created_at": order["created_at"],
                },
            })

        cleaned_phone = re.sub(r"\D", "", phone)
        if len(cleaned_phone) >= 10 and cleaned_phone.startswith("88"):
            cleaned_phone = cleaned_phone[2:]

        rows = connection.execute(
            """
            SELECT reference, customer_name, customer_phone, customer_email,
                   delivery_notes, items_json, total, status, created_at,
                   courier_name, tracking_code, discount, coupon_code
            FROM orders
            WHERE customer_phone LIKE ? OR customer_phone LIKE ?
            ORDER BY created_at DESC
            LIMIT 10
            """,
            (f"%{cleaned_phone}%", f"%{phone}%"),
        ).fetchall()

        if not rows:
            return jsonify({"found": False, "error": f"No orders found for phone number '{phone}'."}), 404

        orders = []
        for r in rows:
            ord_dict = _deserialize_order_row(r)
            s_info = STATUS_MESSAGES.get(ord_dict["status"], {"badge": ord_dict["status"].title(), "description": "", "step": 1})
            orders.append({
                "reference": ord_dict["reference"],
                "total": ord_dict["total"],
                "status": ord_dict["status"],
                "status_badge": s_info["badge"],
                "created_at": ord_dict["created_at"],
                "items_count": len(ord_dict["items"]),
                "courier_name": ord_dict["courier_name"],
                "tracking_code": ord_dict["tracking_code"],
            })

        return jsonify({"found": True, "count": len(orders), "orders": orders})

    finally:
        connection.close()


@app.get("/api/admin/analytics")
def admin_analytics_endpoint():
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    connection = get_db_connection()
    try:
        orders_row = connection.execute(
            """
            SELECT 
                COUNT(*) as total_orders,
                COALESCE(SUM(CASE WHEN status != 'cancelled' THEN total ELSE 0 END), 0) as total_revenue,
                COALESCE(SUM(CASE WHEN status != 'cancelled' THEN discount ELSE 0 END), 0) as total_discounts
            FROM orders
            """
        ).fetchone()
        total_orders, total_revenue, total_discounts = orders_row

        status_rows = connection.execute(
            "SELECT status, COUNT(*) FROM orders GROUP BY status"
        ).fetchall()
        status_breakdown = {status: count for status, count in status_rows}

        valid_orders_count = total_orders - status_breakdown.get("cancelled", 0)
        avg_order_value = int(total_revenue / valid_orders_count) if valid_orders_count > 0 else 0

        all_items_rows = connection.execute(
            "SELECT items_json FROM orders WHERE status != 'cancelled'"
        ).fetchall()
        item_counter = {}
        for (item_json,) in all_items_rows:
            try:
                for it in json.loads(item_json or "[]"):
                    it_id = it.get("id", "unknown")
                    it_name = it.get("name", it_id)
                    it_qty = it.get("quantity", 1)
                    it_total = it.get("line_total", 0)
                    if it_id not in item_counter:
                        item_counter[it_id] = {"id": it_id, "name": it_name, "quantity": 0, "revenue": 0}
                    item_counter[it_id]["quantity"] += it_qty
                    item_counter[it_id]["revenue"] += it_total
            except Exception:
                pass

        top_products = sorted(item_counter.values(), key=lambda x: x["quantity"], reverse=True)[:5]

        low_stock_rows = connection.execute(
            "SELECT id, name, price, stock FROM products WHERE stock <= 5 ORDER BY stock ASC LIMIT 10"
        ).fetchall()
        low_stock = [
            {"id": p_id, "name": name, "price": price, "stock": stock}
            for p_id, name, price, stock in low_stock_rows
        ]

        coupon_rows = connection.execute(
            "SELECT code, discount_type, discount_value, used_count, active FROM coupons ORDER BY used_count DESC"
        ).fetchall()
        coupons_list = [
            {"code": c, "type": t, "value": v, "used_count": u, "active": bool(a)}
            for c, t, v, u, a in coupon_rows
        ]

        return jsonify({
            "metrics": {
                "total_orders": total_orders,
                "valid_orders": valid_orders_count,
                "total_revenue": total_revenue,
                "total_discounts_granted": total_discounts,
                "average_order_value": avg_order_value,
            },
            "status_breakdown": status_breakdown,
            "top_products": top_products,
            "low_stock_products": low_stock,
            "coupons": coupons_list,
        })
    finally:
        connection.close()


@app.get("/api/admin/orders/export")
def admin_export_orders_endpoint():
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    status_filter = request.args.get("status")
    export_format = request.args.get("format", "steadfast").lower()

    connection = get_db_connection()
    try:
        if status_filter and status_filter != "all":
            rows = connection.execute(
                """
                SELECT reference, customer_name, customer_phone, delivery_notes,
                       items_json, total, status, created_at, courier_name, tracking_code
                FROM orders
                WHERE status = ?
                ORDER BY created_at DESC
                """,
                (status_filter,),
            ).fetchall()
        else:
            rows = connection.execute(
                """
                SELECT reference, customer_name, customer_phone, delivery_notes,
                       items_json, total, status, created_at, courier_name, tracking_code
                FROM orders
                WHERE status != 'cancelled'
                ORDER BY created_at DESC
                """
            ).fetchall()
    finally:
        connection.close()

    output = io.StringIO()
    writer = csv.writer(output)

    if export_format == "steadfast":
        writer.writerow(["Invoice", "Recipient Name", "Recipient Phone", "Recipient Address", "COD Amount", "Note"])
        for ref, name, phone, address, items_json, total, status, created_at, courier, tracking in rows:
            try:
                items_summary = ", ".join(f"{it.get('name')} x{it.get('quantity')}" for it in json.loads(items_json or "[]"))
            except Exception:
                items_summary = ""
            writer.writerow([ref, name, phone, address, total, items_summary])
    else:
        writer.writerow(["Reference", "Customer Name", "Customer Phone", "Delivery Notes", "Items", "Total (BDT)", "Status", "Created At", "Courier", "Tracking Code"])
        for ref, name, phone, address, items_json, total, status, created_at, courier, tracking in rows:
            try:
                items_summary = ", ".join(f"{it.get('name')} x{it.get('quantity')}" for it in json.loads(items_json or "[]"))
            except Exception:
                items_summary = ""
            writer.writerow([ref, name, phone, address, items_summary, total, status, created_at, courier, tracking])

    csv_data = output.getvalue()
    filename = f"arams_orders_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.csv"
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


@app.post("/api/coupons/validate")
def validate_coupon_endpoint():
    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    code = payload.get("code")
    subtotal = payload.get("subtotal")
    try:
        subtotal_int = int(subtotal)
    except (TypeError, ValueError):
        return jsonify({"valid": False, "error": "Subtotal must be a valid number."}), 400

    try:
        result = validate_coupon(code, subtotal_int)
        return jsonify(result)
    except ValueError as error:
        return jsonify({"valid": False, "error": str(error)}), 400


@app.get("/api/admin/coupons")
def list_coupons_endpoint():
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    connection = get_db_connection()
    try:
        rows = connection.execute(
            """
            SELECT code, discount_type, discount_value, min_spend, max_uses, used_count, expires_at, active, created_at
            FROM coupons
            ORDER BY created_at DESC
            """
        ).fetchall()
        coupons = [
            {
                "code": r[0],
                "discount_type": r[1],
                "discount_value": r[2],
                "min_spend": r[3],
                "max_uses": r[4],
                "used_count": r[5],
                "expires_at": r[6],
                "active": bool(r[7]),
                "created_at": r[8],
            }
            for r in rows
        ]
        return jsonify({"coupons": coupons})
    finally:
        connection.close()


@app.post("/api/admin/coupons")
def create_coupon_endpoint():
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    payload = request.get_json(silent=True) or request.form.to_dict() or {}
    code = (payload.get("code") or "").strip().upper()
    discount_type = (payload.get("discount_type") or "percent").strip().lower()
    try:
        discount_value = int(payload.get("discount_value", 0))
        min_spend = int(payload.get("min_spend", 0))
        max_uses = int(payload.get("max_uses", 0))
    except (TypeError, ValueError):
        return jsonify({"error": "Discount value, min spend, and max uses must be integers."}), 400

    if not code:
        return jsonify({"error": "Coupon code is required."}), 400
    if discount_type not in {"percent", "fixed"}:
        return jsonify({"error": "Discount type must be 'percent' or 'fixed'."}), 400
    if discount_value <= 0:
        return jsonify({"error": "Discount value must be greater than zero."}), 400
    if discount_type == "percent" and discount_value > 100:
        return jsonify({"error": "Percentage discount cannot exceed 100%."}), 400

    expires_at = (payload.get("expires_at") or "").strip()
    active = 1 if payload.get("active", True) in {True, "true", "1", 1} else 0
    now_iso = datetime.now(timezone.utc).isoformat()

    connection = get_db_connection()
    try:
        connection.execute(
            """
            INSERT INTO coupons (code, discount_type, discount_value, min_spend, max_uses, used_count, expires_at, active, created_at)
            VALUES (?, ?, ?, ?, ?, 0, ?, ?, ?)
            ON CONFLICT(code) DO UPDATE SET
                discount_type = excluded.discount_type,
                discount_value = excluded.discount_value,
                min_spend = excluded.min_spend,
                max_uses = excluded.max_uses,
                expires_at = excluded.expires_at,
                active = excluded.active
            """,
            (code, discount_type, discount_value, min_spend, max_uses, expires_at, active, now_iso),
        )
        connection.commit()
        return jsonify({"success": True, "code": code, "message": f"Coupon {code} saved."}), 201
    finally:
        connection.close()


@app.delete("/api/admin/coupons/<code>")
def delete_coupon_endpoint(code):
    auth_error = require_admin_auth()
    if auth_error is not None:
        return auth_error

    clean_code = code.strip().upper()
    connection = get_db_connection()
    try:
        cursor = connection.execute("DELETE FROM coupons WHERE code = ?", (clean_code,))
        connection.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Coupon not found."}), 404
        return jsonify({"success": True, "deleted": True, "code": clean_code})
    finally:
        connection.close()


@app.get("/api/catalog")
def get_unified_catalog_endpoint():
    category = (request.args.get("category") or "").strip().lower()
    search = (request.args.get("search") or "").strip().lower()
    sort = (request.args.get("sort") or "featured").strip().lower()

    catalog = []
    for pid, (name, price) in PRODUCTS.items():
        catalog.append({
            "id": pid,
            "name": name,
            "price": price,
            "category": "Accessories",
            "source": "static",
            "in_stock": True,
        })

    custom_products = list_custom_products(limit=500)
    for cp in custom_products:
        catalog.append({
            "id": cp["id"],
            "name": cp["name"],
            "price": cp["price"],
            "description": cp.get("description", ""),
            "color": cp.get("color", ""),
            "image": cp.get("image", ""),
            "category": "Custom",
            "stock": cp.get("stock", 0),
            "source": "database",
            "in_stock": cp.get("stock", 0) > 0,
        })

    if search:
        catalog = [item for item in catalog if search in item["name"].lower() or search in item.get("description", "").lower()]
    if category and category != "all":
        catalog = [item for item in catalog if category in item.get("category", "").lower() or category in item["name"].lower()]

    if sort == "low-high":
        catalog.sort(key=lambda x: x["price"])
    elif sort == "high-low":
        catalog.sort(key=lambda x: x["price"], reverse=True)

    return jsonify({"count": len(catalog), "products": catalog})


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


@app.get("/admin/orders")
@app.get("/admin")
@app.get("/admin/dashboard")
def admin_dashboard_page():
    if not session.get("admin_logged_in"):
        return send_from_directory(BASE_DIR, "admin_login.html")
    return send_from_directory(BASE_DIR, "admin_dashboard.html")

def admin_orders_page():
    if not session.get("admin_logged_in"):
        return send_from_directory(BASE_DIR, "admin_login.html")
    return send_from_directory(BASE_DIR, "admin_orders.html")

@app.get("/admin/products")
def admin_products_page():
    if not session.get("admin_logged_in"):
        return send_from_directory(BASE_DIR, "admin_login.html")
    return send_from_directory(BASE_DIR, "admin_products.html")

@app.get("/admin/coupons")
def admin_coupons_page():
    if not session.get("admin_logged_in"):
        return send_from_directory(BASE_DIR, "admin_login.html")
    return send_from_directory(BASE_DIR, "admin_coupons.html")

@app.get("/admin/settings")
def admin_settings_page():
    if not session.get("admin_logged_in"):
        return send_from_directory(BASE_DIR, "admin_login.html")
    return send_from_directory(BASE_DIR, "admin_settings.html")


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
    if username == ADMIN_USERNAME and verify_admin_password(password):
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
    payload = request.get_json(silent=True) or {}
    coupon_code = payload.get("coupon_code") or (payload.get("customer") or {}).get("coupon_code") or ""
    try:
        customer, items, total = build_order(payload, coupon_code=coupon_code)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    subtotal = sum(item["line_total"] for item in items)
    discount = max(0, subtotal - total)
    clean_coupon = coupon_code.strip().upper() if (discount > 0 and isinstance(coupon_code, str)) else ""

    reference = f"AR-{secrets.token_hex(4).upper()}"
    created_at = datetime.now(timezone.utc).isoformat()
    reserve_stock_for_order(items)
    if clean_coupon:
        record_coupon_usage(clean_coupon)

    connection = get_db_connection()
    try:
        connection.execute(
            """
            INSERT INTO orders (
                reference, customer_name, customer_phone, customer_email,
                delivery_notes, items_json, total, status, created_at,
                discount, coupon_code
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                discount,
                clean_coupon,
            ),
        )
        connection.commit()
    finally:
        connection.close()

    return jsonify({
        "reference": reference,
        "total": total,
        "subtotal": subtotal,
        "discount": discount,
        "coupon_code": clean_coupon,
        "whatsapp_url": make_whatsapp_url(reference, customer, items, total, discount=discount, coupon_code=clean_coupon),
    }), 201


initialize_database()


if __name__ == "__main__":
    app.run(
        host=os.environ.get("HOST", "127.0.0.1"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False,
    )
