import json
import os
import re
import secrets
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

from flask import Flask, abort, jsonify, request, send_from_directory


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
    "weekend-chinos": ("Weekend Chinos", 2850),
    "linen-wide-leg-trousers": ("Linen Wide-Leg Trousers", 2950),
    "city-pleat-trousers": ("City Pleat Trousers", 3250),
    "everyday-taper-trousers": ("Everyday Taper Trousers", 2750),
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
    ("Universe Point 2232B IBSO 7MM Ultra-Thin Rectangle Dial Classic Quartz Wristwatch", 1020),
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
    ("Armaf Club De Nuit Intense EDP Man", 7200),
    ("Armaf Club de Nuit Intense EDT for Men", 4300),
    ("Versace Eros Pour Homme EDT", 10700),
    ("Davidoff Cool Water EDT For Men", 4500),
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
    match = re.fullmatch(r"perfume-(\d{3})", product_id)
    if not match:
        return None
    index = int(match.group(1)) - 1
    if index < 0 or index >= len(PERFUME_PRODUCTS):
        return None
    return PERFUME_PRODUCTS[index]

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024
app.config["DATABASE"] = os.environ.get(
    "ARAMS_DATABASE", str(Path(app.instance_path) / "orders.sqlite3")
)
WHATSAPP_NUMBER = re.sub(r"\D", "", os.environ.get("ARAMS_WHATSAPP", "8801815653564"))


def initialize_database():
    database_path = Path(app.config["DATABASE"])
    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    try:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                reference TEXT PRIMARY KEY,
                customer_name TEXT NOT NULL,
                customer_phone TEXT NOT NULL,
                customer_email TEXT NOT NULL DEFAULT '',
                delivery_notes TEXT NOT NULL,
                items_json TEXT NOT NULL,
                total INTEGER NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.commit()
    finally:
        connection.close()


def clean_field(value, field, maximum, required=True):
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


@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.get("/buy")
def buy_page():
    return send_from_directory(BASE_DIR, "buy.html")


@app.get("/watch/casio-a159wa")
def casio_product_page():
    return send_from_directory(BASE_DIR, "casio.html")


@app.get("/<path:filename>")
def frontend_asset(filename):
    if filename not in {"app.js", "buy.js", "styles.css", "buy.html", "casio.html"}:
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