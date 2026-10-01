const products = [
  { id: "sola-frames", name: "Sola Frames", price: 1850, color: "Tortoise", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80", description: "Sculpted acetate, soft tint" },
  { id: "atlas-aviators", name: "Atlas Aviators", price: 2100, color: "Gold / smoke", image: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80", description: "Classic shape, easy fit" },
  { id: "noir-square-sunglasses", name: "Noir Square Sunglasses", price: 1950, color: "Black", image: "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80", description: "Bold black frames with a soft tint" },
  { id: "coast-round-sunglasses", name: "Coast Round Sunglasses", price: 1750, color: "Brown", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80", description: "Rounded lenses for bright days" },
  { id: "summit-sport-shades", name: "Summit Sport Shades", price: 2250, color: "Smoke", image: "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=900&q=80", description: "Lightweight wraparound everyday pair" },
  { id: "sunset-metal-shades", name: "Sunset Metal Shades", price: 2400, color: "Gold / brown", image: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=900&q=80", description: "Fine metal frame with warm lenses" },
  { id: "gulshan-cat-eye", name: "Gulshan Cat-Eye Shades", price: 2150, color: "Black / smoke", image: "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80", description: "A lifted shape with soft smoke lenses" },
  { id: "riverline-aviators", name: "Riverline Aviators", price: 2350, color: "Gunmetal", image: "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=900&q=80", description: "Light metal frame for bright commutes" },
  { id: "padma-polarized-shades", name: "Padma Polarized Shades", price: 2600, color: "Matte black", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80", description: "Comfortable polarized lenses for long days" },
  { id: "banani-soft-square", name: "Banani Soft Square Shades", price: 2050, color: "Tortoise", image: "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80", description: "Soft square frame with a warm tint" },
  { id: "field-watch", name: "Field Watch", price: 3450, color: "Black", image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80", description: "Clean dial, everyday strap" },
  { id: "luna-watch", name: "Luna Watch", price: 3200, color: "Silver", image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80", description: "Slim profile with a bright face" },
  { id: "mens-trousers", name: "Daily Trousers", price: 2650, color: "Stone", image: "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=900&q=80", description: "Tapered fit for everyday wear" },
  { id: "relaxed-cargo-trousers", name: "Relaxed Cargo Trousers", price: 3150, color: "Olive", image: "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=900&q=80", description: "Roomy pockets, easy cotton fit" },
  { id: "weekend-chinos", name: "Weekend Chinos", price: 2850, color: "Navy", image: "https://images.unsplash.com/photo-1506629905607-d9d3b9a4f9d4?auto=format&fit=crop&w=900&q=80", description: "Soft twill with a clean taper" },
  { id: "linen-wide-leg-trousers", name: "Linen Wide-Leg Trousers", price: 2950, color: "Ivory", image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=900&q=80", description: "Breathable linen with an easy drape" },
  { id: "city-pleat-trousers", name: "City Pleat Trousers", price: 3250, color: "Charcoal", image: "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?auto=format&fit=crop&w=900&q=80", description: "A neat pleat with a relaxed leg" },
  { id: "everyday-taper-trousers", name: "Everyday Taper Trousers", price: 2750, color: "Black", image: "https://images.unsplash.com/photo-1506629905607-d9d3b9a4f9d4?auto=format&fit=crop&w=900&q=80", description: "Soft stretch fabric for busy days" },
  { id: "utility-denim-trousers", name: "Utility Denim Trousers", price: 3050, color: "Indigo", image: "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=900&q=80", description: "Sturdy denim with a straight fit" },
  { id: "linen-straight-trousers", name: "Linen Straight Trousers", price: 2850, color: "Sand", image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=900&q=80", description: "Lightweight straight cut for warm days" },
  { id: "workday-twill-trousers", name: "Workday Twill Trousers", price: 2950, color: "Charcoal", image: "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=900&q=80", description: "Clean twill with a comfortable taper" },
  { id: "gulshan-wide-leg-trousers", name: "Gulshan Wide-Leg Trousers", price: 3100, color: "Black", image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=900&q=80", description: "Fluid wide leg with a clean waistband" },
  { id: "uttara-cord-trousers", name: "Uttara Cord Trousers", price: 3200, color: "Rust", image: "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=900&q=80", description: "Soft corduroy with a straight fit" },
  { id: "metro-steel-watch", name: "Metro Steel Watch", price: 2850, color: "Steel", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=80", description: "Polished steel for daily wear" },
  { id: "heritage-leather-watch", name: "Heritage Leather Watch", price: 2950, color: "Brown", image: "https://images.unsplash.com/photo-1508057198894-247b23fe5ade?auto=format&fit=crop&w=900&q=80", description: "Warm leather, clean numbers" },
  { id: "noor-mini-watch", name: "Noor Mini Watch", price: 2750, color: "Gold", image: "https://images.unsplash.com/photo-1539874754764-5a96559165b0?auto=format&fit=crop&w=900&q=80", description: "Small face with a bright finish" },
  { id: "apex-chronograph", name: "Apex Chronograph", price: 4250, color: "Black / steel", image: "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&w=900&q=80", description: "Sport details, ready for weekends" },
  { id: "rally-sport-watch", name: "Rally Sport Watch", price: 2450, color: "Blue", image: "https://images.unsplash.com/photo-1495857000853-fe46c8aefc30?auto=format&fit=crop&w=900&q=80", description: "A bright dial with an easy strap" },
  { id: "sundarban-field-watch", name: "Sundarban Field Watch", price: 3050, color: "Green", image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80", description: "Quiet colors for every day" },
  { id: "dhaka-dial-watch", name: "Dhaka Dial Watch", price: 3650, color: "Silver / black", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=80", description: "Classic numerals with a polished case" },
  { id: "meghna-mesh-watch", name: "Meghna Mesh Watch", price: 3350, color: "Rose gold", image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80", description: "Slim mesh strap with a warm face" },
  { id: "uttara-classic-watch", name: "Uttara Classic Watch", price: 3500, color: "Cream / tan", image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80", description: "Bright dial with a refined leather strap" },
  { id: "motijheel-steel-watch", name: "Motijheel Steel Watch", price: 3900, color: "Steel blue", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=80", description: "Strong steel bracelet for daily use" },
  { id: "casio-a159wa", name: "Casio A-159WA Digital Watch", price: 990, color: "Silver", image: "https://nagram.com.bd/cdn/shop/files/a14c72d7-60e2-478e-bdb5-4f2ccf62b651.jpg?v=1785762354&width=900", description: "Vintage digital face with an adjustable steel band" },
  { id: "everyday-shirt", name: "Everyday Shirt", price: 2250, color: "White", image: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=80", description: "Relaxed cotton, made to layer" },
  { id: "city-layer", name: "City Layer", price: 3850, color: "Olive", image: "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=900&q=80", description: "Lightweight utility overshirt" },
  { id: "mens-shorts", name: "Everyday Shorts", price: 1850, color: "Olive", image: "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?auto=format&fit=crop&w=900&q=80", description: "Relaxed cotton with easy movement" },
  { id: "weekend-tote", name: "Weekend Tote", price: 2950, color: "Tan", image: "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=900&q=80", description: "Room for all the essentials" },
  { id: "soft-form", name: "Soft Form Top", price: 2400, color: "Blue", image: "https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=900&q=80", description: "An easy shape for everyday" }
];

const gorurPants = [
  ["Baggy Fit Cargo Pants in Off-White", 1500, "Off-White", "https://gorurghash.com/wp-content/uploads/2026/08/hf_20260827_073132_b17d6815-31ec-4d0c-a63b-2f11b0ad6c9d-copy-300x300.jpg"],
  ["Baggy Fit Cargo Pants in Dark Jungle Green", 1300, "Dark Jungle Green", "https://gorurghash.com/wp-content/uploads/2026/03/DSC9313-copy-2-300x300.jpg"],
  ["Baggy Fit Cargo Pants in Deep Blue", 1300, "Deep Blue", "https://gorurghash.com/wp-content/uploads/2023/09/hf_20260730_063715_05bfe933-01a2-4484-979e-4a019368dfb4-copy-300x300.jpg"],
  ["Baggy Fit Cargo Pants in Black", 1300, "Black", "https://gorurghash.com/wp-content/uploads/2023/09/hf_20260730_064057_bb4efeb5-abc4-4207-a0ef-3cd2c98be216-copy-300x300.jpg"],
  ["Men's Straight Fit Carpenter Pants in Black", 1300, "Black", "https://gorurghash.com/wp-content/uploads/2025/10/DSC5531-copy-300x300.jpg"],
  ["Men's Straight Fit Carpenter Pants in Brown", 1300, "Brown", "https://gorurghash.com/wp-content/uploads/2025/10/DSC5552-copy-300x300.jpg"],
  ["Men's Baggy Cord Pants in Green", 1400, "Green", "https://gorurghash.com/wp-content/uploads/2025/11/DSC6437-copy-2-300x300.jpg"],
  ["Men's Baggy Cord Pants in Off-White", 1400, "Off-White", "https://gorurghash.com/wp-content/uploads/2025/07/DSC4495-copy-300x300.jpg"],
  ["Men's Baggy Cord Pants in Brown", 1400, "Brown", "https://gorurghash.com/wp-content/uploads/2025/07/DSC4471-copy-300x300.jpg"],
  ["Men's Baggy Cord Pants in Black", 1400, "Black", "https://gorurghash.com/wp-content/uploads/2025/07/DSC4519-copy-300x300.jpg"],
  ["Unisex Baggy Jeans in Light Blue", 1850, "Light Blue", "https://gorurghash.com/wp-content/uploads/2026/02/DSC8068-copy-2-web-300x300.jpg"],
  ["Unisex Bootcut Jeans in Blue", 1850, "Blue", "https://gorurghash.com/wp-content/uploads/2026/02/DSC8101-copy-2-web-300x300.jpg"],
  ["Unisex Bootcut Jeans in Black", 1850, "Black", "https://gorurghash.com/wp-content/uploads/2026/02/DSC8124-copy-2-web-300x300.jpg"],
  ["Unisex Baggy Jeans in Navy", 1850, "Navy", "https://gorurghash.com/wp-content/uploads/2026/02/DSC8149-copy-2-web-300x300.jpg"],
  ["Men's White Pleated Relaxed Gurkha Pants", 1800, "White", "https://gorurghash.com/wp-content/uploads/2026/03/DSC0111-copy-2-300x300.jpg"],
  ["Men's Light Grey Classic Pleated Gurkha Pants with New Belt", 1800, "Light Grey", "https://gorurghash.com/wp-content/uploads/2025/08/DSC0149-copy2-300x300.jpg"],
  ["Men's Dark Brown Classic Pleated Gurkha Pants with New Belt", 1800, "Dark Brown", "https://gorurghash.com/wp-content/uploads/2025/08/DSC0218-copy2-300x300.jpg"],
  ["Men's Cream Classic Pleated Gurkha Pants with New Belt", 1800, "Cream", "https://gorurghash.com/wp-content/uploads/2025/08/DSC0183-copy-2-300x300.jpg"],
  ["Men's White Formal Pleated Pants", 1700, "White", "https://gorurghash.com/wp-content/uploads/2025/03/DSC0480-copy-300x300.jpg"],
  ["Men's Black Formal Pleated Pants", 1700, "Black", "https://gorurghash.com/wp-content/uploads/2025/03/DSC0433-copy-300x300.jpg"],
  ["Men's Black Classic Pleated Gurkha Pants with New Belt", 1800, "Black", "https://gorurghash.com/wp-content/uploads/2025/08/DSC0075-copy2-300x300.jpg"],
  ["Men's White Straight Fit Pleated Formal Gurkha Pants", 1800, "White", "https://gorurghash.com/wp-content/uploads/2024/06/PPWM4-3-300x300.jpg"],
  ["Men's Pinstripe High Waisted Relaxed Pants in Navy Blue", 1800, "Navy Blue", "https://gorurghash.com/wp-content/uploads/2026/05/DSC0373-copy2-1-300x300.jpg"],
  ["Men's Pinstripe High Waisted Relaxed Pants in Grey", 1800, "Grey", "https://gorurghash.com/wp-content/uploads/2026/05/DSC0346-copy2-1-300x300.jpg"],
  ["Men's Barrel Pants in Black", 1500, "Black", "https://gorurghash.com/wp-content/uploads/2026/05/DSC0414-copy2-1-300x300.jpg"],
  ["Men's Classic Relaxed Fit Pants in White", 1700, "White", "https://gorurghash.com/wp-content/uploads/2025/03/DSC0558-copy-300x300.jpg"],
  ["Men's Classic Relaxed Fit Pants in Black", 1700, "Black", "https://gorurghash.com/wp-content/uploads/2025/03/DSC0521-copy-300x300.jpg"],
  ["Pleated Summer Shorts in Cream", 800, "Cream", "https://gorurghash.com/wp-content/uploads/2025/07/DSC4393-copy-300x300.jpg"],
  ["Pleated Summer Shorts in Black", 800, "Black", "https://gorurghash.com/wp-content/uploads/2025/07/DSC4448-copy-300x300.jpg"]
].map(([name, price, color, image], index) => ({
  id: `gorur-pants-${String(index + 1).padStart(3, "0")}`,
  name,
  price,
  color,
  image,
  description: "Bangladesh men's pants collection"
}));
products.push(...gorurPants);
const bestSellingPerfumes = [
  ["Armaf Club De Nuit Intense EDP Man", 7200, "Full bottle", "https://buyperfumeinbangladesh.com/wp-content/uploads/2020/11/Armaf-Club-de-Nuit-Intense-EDP-for-Men-200ml.jpg"],
  ["Armaf Club de Nuit Intense EDT for Men", 4300, "Full bottle", "https://buyperfumeinbangladesh.com/wp-content/uploads/2017/07/Armaf-Club-de-Nuit-Intense-EDT-for-Men-105m.jpg"],
  ["Versace Eros Pour Homme EDT", 10700, "Full bottle", "https://buyperfumeinbangladesh.com/wp-content/uploads/2017/01/Versace-Eros-EDT-for-Men-100ml-Bottle.jpg"],
  ["Davidoff Cool Water EDT For Men", 4500, "Full bottle", "https://buyperfumeinbangladesh.com/wp-content/uploads/2016/11/Davidoff-Cool-Water-EDT-for-Men-125ml.jpg"]
].map(([name, price, color, image], index) => ({
  id: `perfume-${String(index + 1).padStart(3, "0")}`,
  name,
  price,
  color,
  image,
  description: "Best selling fragrance from Bangladesh perfume edit"
}));
products.push(...bestSellingPerfumes);

const marketSunglassesImages = [
  "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=900&q=80"
];
const marketSunglassesNames = [
  ["Trendsetter Black Sunglasses", 897, "Men"], ["White Metal Frame Sunglasses", 997, "Unisex"],
  ["Unisex Plastic Summer Sunglasses", 977, "Unisex"], ["RIDERACE Sports Cycling Goggles", 407, "Men"],
  ["Popular Women's Punk Oval Y2K Sunglasses", 349, "Women"], ["UV400 Windproof Cycling Goggles", 474, "Unisex"],
  ["Y2K UV400 Sports Sunglasses", 402, "Unisex"], ["Black to White UV400 Sunglasses", 339, "Men"],
  ["White Frame Sunglasses for Men", 996, "Men"], ["Transparent Frame Sunglasses for Men", 996, "Men"],
  ["Wayfarer Sunglasses for Men", 996, "Men"], ["SCVCN Outdoor MTB UV400 Glasses", 662, "Unisex"],
  ["Polarized Round UV400 Sunglasses", 922, "Unisex"], ["Vintage Cat Eye Sunglasses for Women", 277, "Women"],
  ["ONEVAN 2023 Square Sunglasses", 995, "Men"], ["DKS04694 Flexible Polycarbonate Sunglasses", 254, "Men"],
  ["Unisex Metal UV Protection Sunglasses", 376, "Unisex"], ["Roza Retro Sunglasses for Men", 219, "Men"],
  ["Rectangular Black MC Stan Sunglasses", 998, "Unisex"], ["OMEKOL Photochromic Cycling Glasses", 415, "Unisex"]
];
products.push(...marketSunglassesNames.map(([name, price], index) => ({
  id: `market-sunglasses-${String(index + 1).padStart(3, "0")}`,
  name,
  price,
  color: "As shown",
  image: marketSunglassesImages[index % marketSunglassesImages.length],
  description: "Bangladesh marketplace reference listing"
})));

const pronounWatchCatalog = [
  ["Fastrack Urban Crest FT-UC-242", 999, "https://pronoun.pro/wp-content/uploads/2026/09/White-PN-1420-scaled.webp"],
  ["Fastrack Meridian FT-MD-241", 1120, "https://pronoun.pro/wp-content/uploads/2026/09/Navy-Blue-PN-1416-scaled.webp"],
  ["Universe Point Royal Noir UP-RN427", 999, "https://pronoun.pro/wp-content/uploads/2026/06/White.webp"],
  ["Fastrack Groove 3321SM01 Men's Watch", 800, "https://pronoun.pro/wp-content/uploads/2026/05/White-Dial_-scaled.webp"],
  ["Fastrack PRN-SQ17 Modern Edge", 999, "https://pronoun.pro/wp-content/uploads/2026/04/Black-PN-1351.webp"],
  ["Mark M6278 Ultra Thin Watch", 1299, "https://pronoun.pro/wp-content/uploads/2026/03/Toton-Balck-PN-12570-scaled.webp"],
  ["OMEGA ZQ98 Triple Calendar Watch", 1599, "https://pronoun.pro/wp-content/uploads/2026/02/Silver-white-PN-12560-scaled.webp"],
  ["Fastrack 9947 Mens Watch", 750, "https://pronoun.pro/wp-content/uploads/2025/10/Silver.jpg"],
  ["Universe Point 2232B IBSO 7MM Ultra-Thin Rectangle Dial Classic Quartz Wristwatch", 1020, "https://pronoun.pro/wp-content/uploads/2025/09/White-PN-103-scaled.webp"],
  ["Hublot Gang Sang Spider Dial Watch", 1050, "https://pronoun.pro/wp-content/uploads/2025/12/Silver-Black-scaled.webp"],
  ["Forest F-740", 1399, "https://pronoun.pro/wp-content/uploads/2025/05/Picsart_25-06-19_23-29-14-052-min-scaled.webp"],
  ["Titan Chain Man's Watch", 899, "https://pronoun.pro/wp-content/uploads/2025/11/Silver.webp"],
  ["TOMI T077A Elegant Narrative", 899, "https://pronoun.pro/wp-content/uploads/2026/08/Image-1.webp"],
  ["Fastrack ES-214 Men's Watch", 850, "https://pronoun.pro/wp-content/uploads/2026/05/Brown-1-scaled.jpg"],
  ["Hublot Obsidian Prime", 999, "https://pronoun.pro/wp-content/uploads/2026/05/Silver-Black_-1.webp"],
  ["Forest F-1035 Urban Drift Men's Watch", 1150, "https://pronoun.pro/wp-content/uploads/2026/05/Black-1.webp"]
];
products.push(...pronounWatchCatalog.map(([name, price, image], index) => ({
  id: `pronoun-watch-${String(index + 1).padStart(3, "0")}`,
  name,
  price,
  color: "As shown",
  image,
  description: "Bangladesh watch market listing"
})));

const premiumBagNames = ["Dhaka Carryall", "Jamuna Leather Satchel", "Bengal Work Tote", "Gulshan Shoulder Bag"];
const premiumBagColors = ["Tan", "Black", "Cognac", "Olive", "Stone", "Burgundy", "Navy", "Camel"];
const premiumBagImages = [
  "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=900&q=80"
];
products.push(...Array.from({ length: premiumBagNames.length }, (_, index) => ({
  id: `premium-bag-${String(index + 1).padStart(3, "0")}`,
  name: `${premiumBagNames[index % premiumBagNames.length]} ${String(index + 1).padStart(3, "0")}`,
  price: 3850 + ((index * 375) % 12151),
  color: premiumBagColors[index % premiumBagColors.length],
  image: premiumBagImages[index % premiumBagImages.length],
  description: "Premium finish for work, travel, and weekends"
})));

const formatMoney = new Intl.NumberFormat("en-BD");
const money = (amount) => `৳${formatMoney.format(amount)}`;
const cart = new Map();
const grid = document.querySelector("#buy-product-grid");
const summaryList = document.querySelector("#summary-list");
const summaryTotal = document.querySelector("#summary-total");
const toast = document.querySelector("#toast");
let toastTimer;

function renderProducts() {
  grid.innerHTML = products.map((product) => `
    <article class="product-card buy-card">
      <div class="product-image-wrap">
        <img class="product-image" src="${product.image}" alt="${product.name}" loading="lazy">
        <div class="product-actions">
          <button class="quick-add" type="button" data-add="${product.id}">Add to order</button>
          <button class="buy-now" type="button" data-buy="${product.id}">Buy now <span aria-hidden="true">→</span></button>
        </div>
      </div>
      <div class="product-meta">
        <h3 class="product-name">${product.name}</h3>
        <p class="product-price">${money(product.price)}</p>
      </div>
      <p class="product-description">${product.description} · ${product.color}</p>
    </article>
  `).join("");
}

function orderEntries() {
  return [...cart.entries()].map(([id, quantity]) => {
    const product = products.find((item) => item.id === id);
    return { product, quantity };
  });
}

function renderSummary() {
  const entries = orderEntries();
  const total = entries.reduce((sum, { product, quantity }) => sum + product.price * quantity, 0);

  summaryTotal.textContent = money(total);
  summaryList.innerHTML = entries.length
    ? entries.map(({ product, quantity }) => `
        <div class="summary-item">
          <div>
            <strong>${product.name}</strong>
            <span>Qty: ${quantity}</span>
          </div>
          <span>${money(product.price * quantity)}</span>
        </div>
      `).join("")
    : '<div class="summary-empty">Your order is empty. Add a few pieces to continue.</div>';
}

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("is-visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 2500);
}

function addToOrder(productId) {
  const product = products.find((item) => item.id === productId);
  if (!product) return;

  cart.set(product.id, (cart.get(product.id) || 0) + 1);
  renderSummary();
  showToast(`${product.name} added to order`);
}

function updateFromBagButtons(event) {
  const button = event.target.closest("[data-add], [data-buy]");
  if (!button) return;
  addToOrder(button.dataset.add || button.dataset.buy);
  if (button.hasAttribute("data-buy")) {
    document.querySelector("#checkout").scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

grid.addEventListener("click", updateFromBagButtons);

document.querySelector("#buy-form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const entries = orderEntries();
  if (!entries.length) {
    showToast("Add at least one product before ordering.");
    return;
  }

  const form = event.currentTarget;
  const formData = new FormData(form);
  const submitButton = form.querySelector('button[type="submit"]');
  const originalText = submitButton.textContent;

  submitButton.disabled = true;
  submitButton.textContent = "Sending...";

  try {
    const response = await fetch("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        customer: Object.fromEntries(formData.entries()),
        items: entries.map(({ product, quantity }) => ({ id: product.id, quantity }))
      })
    });

    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Could not place your order.");

    window.location.href = result.whatsapp_url;
  } catch (error) {
    showToast(error.message || "Could not place your order.");
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = originalText;
  }
});

renderProducts();
renderSummary();
