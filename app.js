const products = [
  { id: "sola-frames", name: "Sola Frames", groups: ["Sunglasses", "Women"], description: "Sculpted acetate, soft tint", price: 1850, tag: "Popular", color: "Tortoise", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80" },
  { id: "atlas-aviators", name: "Atlas Aviators", groups: ["Sunglasses", "Men"], description: "A classic shape, easy fit", price: 2100, tag: "New", color: "Gold / smoke", image: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80" },
  { id: "noir-square-sunglasses", name: "Noir Square Sunglasses", groups: ["Sunglasses", "Women"], description: "Bold black frames with a soft tint", price: 1950, tag: "New", color: "Black", image: "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80" },
  { id: "coast-round-sunglasses", name: "Coast Round Sunglasses", groups: ["Sunglasses", "Women"], description: "Rounded lenses for bright days", price: 1750, tag: "Easy pick", color: "Brown", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80" },
  { id: "summit-sport-shades", name: "Summit Sport Shades", groups: ["Sunglasses", "Men"], description: "Lightweight wraparound everyday pair", price: 2250, tag: "Popular", color: "Smoke", image: "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=900&q=80" },
  { id: "sunset-metal-shades", name: "Sunset Metal Shades", groups: ["Sunglasses", "Men"], description: "Fine metal frame with warm lenses", price: 2400, tag: "Market pick", color: "Gold / brown", image: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=900&q=80" },
  { id: "gulshan-cat-eye", name: "Gulshan Cat-Eye Shades", groups: ["Sunglasses", "Women"], description: "A lifted shape with soft smoke lenses", price: 2150, tag: "New", color: "Black / smoke", image: "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80" },
  { id: "riverline-aviators", name: "Riverline Aviators", groups: ["Sunglasses", "Men"], description: "Light metal frame for bright commutes", price: 2350, tag: "Popular", color: "Gunmetal", image: "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=900&q=80" },
  { id: "padma-polarized-shades", name: "Padma Polarized Shades", groups: ["Sunglasses", "Men"], description: "Comfortable polarized lenses for long days", price: 2600, tag: "New", color: "Matte black", image: "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80" },
  { id: "banani-soft-square", name: "Banani Soft Square Shades", groups: ["Sunglasses", "Women"], description: "Soft square frame with a warm tint", price: 2050, tag: "Easy pick", color: "Tortoise", image: "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80" },
  { id: "field-watch", name: "Field Watch", groups: ["Watches", "Men"], description: "Clean dial, everyday strap", price: 3450, tag: "Bestseller", color: "Black", image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80" },
  { id: "luna-watch", name: "Luna Watch", groups: ["Watches", "Women"], description: "A slim profile with a bright face", price: 3200, tag: "Just in", color: "Silver", image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80" },
  { id: "metro-steel-watch", name: "Metro Steel Watch", groups: ["Watches", "Men"], description: "Polished steel for daily wear", price: 2850, tag: "Market pick", color: "Steel", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=80" },
  { id: "heritage-leather-watch", name: "Heritage Leather Watch", groups: ["Watches", "Men"], description: "Warm leather, clean numbers", price: 2950, tag: "Everyday", color: "Brown", image: "https://images.unsplash.com/photo-1508057198894-247b23fe5ade?auto=format&fit=crop&w=900&q=80" },
  { id: "noor-mini-watch", name: "Noor Mini Watch", groups: ["Watches", "Women"], description: "Small face with a bright finish", price: 2750, tag: "New", color: "Gold", image: "https://images.unsplash.com/photo-1539874754764-5a96559165b0?auto=format&fit=crop&w=900&q=80" },
  { id: "apex-chronograph", name: "Apex Chronograph", groups: ["Watches", "Men"], description: "Sport details, ready for weekends", price: 4250, tag: "Popular", color: "Black / steel", image: "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?auto=format&fit=crop&w=900&q=80" },
  { id: "rally-sport-watch", name: "Rally Sport Watch", groups: ["Watches", "Men"], description: "A bright dial with an easy strap", price: 2450, tag: "Value pick", color: "Blue", image: "https://images.unsplash.com/photo-1495857000853-fe46c8aefc30?auto=format&fit=crop&w=900&q=80" },
  { id: "sundarban-field-watch", name: "Sundarban Field Watch", groups: ["Watches", "Women"], description: "Quiet colors for every day", price: 3050, tag: "Just in", color: "Green", image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80" },
  { id: "dhaka-dial-watch", name: "Dhaka Dial Watch", groups: ["Watches", "Men"], description: "Classic numerals with a polished case", price: 3650, tag: "New", color: "Silver / black", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=80" },
  { id: "meghna-mesh-watch", name: "Meghna Mesh Watch", groups: ["Watches", "Women"], description: "Slim mesh strap with a warm face", price: 3350, tag: "Market pick", color: "Rose gold", image: "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=900&q=80" },
  { id: "uttara-classic-watch", name: "Uttara Classic Watch", groups: ["Watches", "Women"], description: "Bright dial with a refined leather strap", price: 3500, tag: "New", color: "Cream / tan", image: "https://images.unsplash.com/photo-1524592094714-0f0654e20314?auto=format&fit=crop&w=900&q=80" },
  { id: "motijheel-steel-watch", name: "Motijheel Steel Watch", groups: ["Watches", "Men"], description: "Strong steel bracelet for daily use", price: 3900, tag: "Bestseller", color: "Steel blue", image: "https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=900&q=80" },
  { id: "casio-a159wa", name: "Casio A-159WA Digital Watch", groups: ["Watches", "Men"], description: "Vintage digital face with an adjustable steel band", price: 990, tag: "Limited offer", color: "Silver", image: "https://nagram.com.bd/cdn/shop/files/a14c72d7-60e2-478e-bdb5-4f2ccf62b651.jpg?v=1785762354&width=900" },
  { id: "everyday-shirt", name: "Everyday Shirt", groups: ["Men"], description: "Relaxed cotton, made to layer", price: 2250, tag: "Easy pick", color: "White", image: "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=80" },
  { id: "city-layer", name: "City Layer", groups: ["Men"], description: "Lightweight utility overshirt", price: 3850, tag: "New", color: "Olive", image: "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=900&q=80" },
  { id: "mens-shorts", name: "Everyday Shorts", groups: ["Men"], description: "Relaxed cotton with easy movement", price: 1850, tag: "New", color: "Olive", image: "https://images.unsplash.com/photo-1591195853828-11db59a44f6b?auto=format&fit=crop&w=900&q=80" },
  { id: "mens-trousers", name: "Daily Trousers", groups: ["Men", "Trousers"], description: "Tapered fit for everyday wear", price: 2650, tag: "Everyday", color: "Stone", image: "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=900&q=80" },
  { id: "relaxed-cargo-trousers", name: "Relaxed Cargo Trousers", groups: ["Men", "Trousers"], description: "Roomy pockets, easy cotton fit", price: 3150, tag: "New", color: "Olive", image: "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=900&q=80" },
  { id: "linen-wide-leg-trousers", name: "Linen Wide-Leg Trousers", groups: ["Women", "Trousers"], description: "Breathable linen with an easy drape", price: 2950, tag: "New", color: "Ivory", image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=900&q=80" },
  { id: "city-pleat-trousers", name: "City Pleat Trousers", groups: ["Women", "Trousers"], description: "A neat pleat with a relaxed leg", price: 3250, tag: "Popular", color: "Charcoal", image: "https://images.unsplash.com/photo-1551488831-00ddcb6c6bd3?auto=format&fit=crop&w=900&q=80" },
  { id: "utility-denim-trousers", name: "Utility Denim Trousers", groups: ["Men", "Trousers"], description: "Sturdy denim with a straight fit", price: 3050, tag: "Everyday", color: "Indigo", image: "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=900&q=80" },
  { id: "linen-straight-trousers", name: "Linen Straight Trousers", groups: ["Women", "Trousers"], description: "Lightweight straight cut for warm days", price: 2850, tag: "New", color: "Sand", image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=900&q=80" },
  { id: "workday-twill-trousers", name: "Workday Twill Trousers", groups: ["Men", "Trousers"], description: "Clean twill with a comfortable taper", price: 2950, tag: "Everyday", color: "Charcoal", image: "https://images.unsplash.com/photo-1473966968600-fa801b869a1a?auto=format&fit=crop&w=900&q=80" },
  { id: "gulshan-wide-leg-trousers", name: "Gulshan Wide-Leg Trousers", groups: ["Women", "Trousers"], description: "Fluid wide leg with a clean waistband", price: 3100, tag: "New", color: "Black", image: "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=900&q=80" },
  { id: "uttara-cord-trousers", name: "Uttara Cord Trousers", groups: ["Men", "Trousers"], description: "Soft corduroy with a straight fit", price: 3200, tag: "Market pick", color: "Rust", image: "https://images.unsplash.com/photo-1542272604-787c3835535d?auto=format&fit=crop&w=900&q=80" },
  { id: "weekend-tote", name: "Weekend Tote", groups: ["Women"], description: "Room for all the essentials", price: 2950, tag: "Popular", color: "Tan", image: "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=900&q=80" },
  { id: "soft-form", name: "Soft Form Top", groups: ["Women"], description: "An easy shape for everyday", price: 2400, tag: "Just in", color: "Blue", image: "https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=900&q=80" }
];

const marketSunglassesImages = [
  "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1577803645773-f96470509666?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1508296695146-257a814070b4?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=900&q=80"
];
const gorurGhashPolos = [
  ["Diamond Knit Polo in Navy Blue", 1500, "https://gorurghash.com/wp-content/uploads/2026/06/DSC0928-copy2.jpg"],
  ["Zigzag Knit Polo in Green", 1500, "https://gorurghash.com/wp-content/uploads/2026/06/DSC0970-copy2.jpg"],
  ["Zigzag Knit Polo in Deep Brown", 1500, "https://gorurghash.com/wp-content/uploads/2026/06/DSC0956-copy2.jpg"],
  ["Diamond Knit Polo in Maroon", 1500, "https://gorurghash.com/wp-content/uploads/2026/05/DSC0901-copy2.jpg"],
  ["Unisex Horizontal Striped Knit Polo in Forest Green", 1750, "https://gorurghash.com/wp-content/uploads/2026/03/DSC9987-copy-2.jpg"],
  ["Unisex Horizontal Striped Knit Polo in Maroon", 1750, "https://gorurghash.com/wp-content/uploads/2026/03/DSC0021-copy-2.jpg"],
  ["Unisex Half-Sleeve Knitted Polo in Green, Navy and Cream", 1750, "https://gorurghash.com/wp-content/uploads/2026/03/DSC0096-copy-2.jpg"],
  ["Unisex Half-Sleeve Knitted Polo in Navy, Maroon and Cream", 1750, "https://gorurghash.com/wp-content/uploads/2026/03/DSC0049-copy-2.jpg"],
  ["Diamond Knit Polo in Bottle Green", 1500, "https://gorurghash.com/wp-content/uploads/2025/08/hf_20260730_060218_af0f5609-2ba8-4a9c-98e0-a5ac9ce4d784-copy.jpg"],
  ["Zip-Up Loop Patterned Knit Polo in Olive", 1500, "https://gorurghash.com/wp-content/uploads/2025/07/hf_20260730_060700_179a46c3-a96c-4498-8948-b387d5afca63-copy.jpg"],
  ["Braided Cable Knit Polo in Cornflower Blue", 1500, "https://gorurghash.com/wp-content/uploads/2025/05/hf_20260730_061012_2773bda8-5386-4552-a6d1-98a3ec4e6ae2-copy-1.jpg"],
  ["Braided Cable Knit Polo in Brown", 1500, "https://gorurghash.com/wp-content/uploads/2025/03/hf_20260730_061403_e7ce840d-273e-46d9-8aac-38c2435c4187-copy.jpg"],
  ["Diamond Knit Polo in Light Pink", 1500, "https://gorurghash.com/wp-content/uploads/2025/02/hf_20260730_061621_0d34fbb9-af24-4a60-8926-33bfd03aaf38-copy.jpg"]
].map(([name, price, image], index) => ({
  id: `gorur-polo-${String(index + 1).padStart(3, "0")}`,
  name,
  groups: ["Polos", "Men", "Unisex"],
  description: "Original Bangladesh polo listing",
  price,
  tag: "Polo edit",
  color: "As shown",
  image
}));
products.push(...gorurGhashPolos);
const katuaCatalog = [
  ["Henley Katua Wooden | Lavender Blush", 1125, "https://goodybro.com/cdn/shop/files/HK_Wooden_Lavender_Blush.png?v=1790756118&width=900", "Sale"],
  ["Henley Katua Wooden | Dark Olive", 1250, "https://goodybro.com/cdn/shop/files/HK_Wooden_Dark_Olive.png?v=1790756194&width=900", "Katua edit"],
  ["V-Neck Katua | Graphite Grey", 1350, "https://goodybro.com/cdn/shop/files/V-Neck_Katua_Graphite_Grey.png?v=1790756229&width=900", "Katua edit"],
  ["V-Neck Katua | Black", 1350, "https://goodybro.com/cdn/shop/files/Front_9d24e375-de4b-4484-b68d-3678ad85574d.png?v=1778160652&width=900", "Katua edit"],
  ["V-Neck Katua | Mocha", 1350, "https://goodybro.com/cdn/shop/files/DSC06190_1_-2.jpg?v=1779562448&width=900", "Katua edit"],
  ["V-Neck Katua | Grey", 1350, "https://goodybro.com/cdn/shop/files/DSC06237.jpg?v=1779562757&width=900", "Katua edit"],
  ["Henley Katua Wooden | Black", 1250, "https://goodybro.com/cdn/shop/files/Front_a406b145-65de-4542-84da-6230095d2f2d.jpg?v=1784012818&width=900", "Katua edit"],
  ["Henley Katua Wooden | Graphite Grey", 1250, "https://goodybro.com/cdn/shop/files/Front_21d34483-e589-4eef-a10b-380b6e8ad3a5.jpg?v=1784011708&width=900", "Katua edit"],
  ["Henley Katua Wooden | Mocha", 1250, "https://goodybro.com/cdn/shop/files/Style_ed2bcb14-1233-41e3-9237-14f8cb5d6c3a.jpg?v=1784012082&width=900", "Katua edit"],
  ["V-Neck Katua | Dark Navy", 1350, "https://goodybro.com/cdn/shop/files/Front_145f2685-ae92-46f3-a65d-9dc2cd8a3d96.jpg?v=1784011178&width=900", "Katua edit"],
  ["V-Neck Katua | Sage", 1350, "https://goodybro.com/cdn/shop/files/Front_08e8c3fb-caca-42c3-a7c0-c1d2cb24e369.png?v=1784010911&width=900", "Katua edit"],
  ["Henley Katua Wooden | Lime Green", 1125, "https://goodybro.com/cdn/shop/files/DSC05932.jpg?v=1778163982&width=900", "Sale"],
  ["Hooded Katua | Beige", 945, "https://goodybro.com/cdn/shop/files/Front_4.png?v=1772260239&width=900", "Sale"],
  ["Hooded Katua | Black", 945, "https://goodybro.com/cdn/shop/files/Front_5.png?v=1772258290&width=900", "Sale"],
  ["Henley Katua | Pastel Pink", 1125, "https://goodybro.com/cdn/shop/files/DSC04520.jpg?v=1784031752&width=900", "Sale"],
  ["Henley Katua Wooden | Brown", 1250, "https://goodybro.com/cdn/shop/files/Front_1.png?v=1771920463&width=900", "Katua edit"],
  ["Henley Katua | Sage", 1125, "https://goodybro.com/cdn/shop/files/Front.png?v=1771919445&width=900", "Sale"],
  ["Henley Katua | Grey", 1125, "https://goodybro.com/cdn/shop/files/Front_3.png?v=1771917138&width=900", "Sale"],
  ["Henley Katua | Oasis Sandstone", 1250, "https://goodybro.com/cdn/shop/files/6_Front.png?v=1769513728&width=900", "Katua edit"],
  ["Henley Katua | Mushroom Brown", 1062, "https://goodybro.com/cdn/shop/files/4_Front.png?v=1769509506&width=900", "Sale"],
  ["Henley Katua | Printed Desert Sands", 1250, "https://goodybro.com/cdn/shop/files/3_Front.png?v=1769508222&width=900", "Katua edit"],
  ["Henley Katua | Plum Wine", 1250, "https://goodybro.com/cdn/shop/files/1_Front.png?v=1769502110&width=900", "Katua edit"],
  ["Henley Katua | Mocha", 1250, "https://goodybro.com/cdn/shop/files/7_Front.png?v=1769515426&width=900", "Katua edit"]
].map(([name, price, image, tag], index) => ({
  id: `katua-${String(index + 1).padStart(3, "0")}`,
  name,
  groups: ["Katua", "Men"],
  description: "Everyday Katua with a comfortable fit",
  price,
  tag,
  color: name.split("|")[1].trim(),
  image
}));
products.push(...katuaCatalog);
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
  groups: ["Pants", "Men"],
  description: "Bangladesh men's pants collection",
  price,
  tag: "Pants edit",
  color,
  image
}));
products.push(...gorurPants);
const bestSellingPerfumes = [
  ["perfume-001", "Arabiyat Oud al Layl Midnight Edition EDP 100ml", 1850, "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=900&q=80", "Bold Unisex Fragrance. Top Notes: Saffron, Rose. Middle Notes: Amber, Woody Notes. Base Notes: Oud, Musk. Perfect for evening wear."],
  ["perfume-002", "Tad Angel Attractive EDP Men 100ml", 1650, "https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?auto=format&fit=crop&w=900&q=80", "A masculine, bold Arabian perfume. Features rich spicy top notes fading into a fresh aquatic heart with a deep woody base."],
  ["perfume-003", "Vampire Blood Perfume Oil (Euro Valley)", 850, "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=900&q=80", "Intense Attar/Perfume Oil. A rich, dark, and sweet fragrance with deep red rose, sandalwood, and musk. Alcohol-free."],
  ["perfume-004", "Brandy Perfumes Sunset EDP 100ml", 1450, "https://images.unsplash.com/photo-1617897903246-719242758050?auto=format&fit=crop&w=900&q=80", "A beautiful evening scent reflecting the golden hour. Top Notes: Citrus, Peach. Middle: White Flowers. Base: Vanilla, Amber."],
  ["perfume-005", "Jean Lowe Azure by Maison Alhambra EDP 100ml", 3500, "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?auto=format&fit=crop&w=900&q=80", "A luxurious men's fragrance. Top Notes: Bergamot, Grapefruit. Middle: Ginger, Mint. Base: Vetiver, Cedarwood, Amber."],
  ["perfume-006", "Swiss Arabian Shaghaf Oud Ahmar 75ml", 4200, "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=900&q=80", "A warm, sweet and woody masterpiece. Features notes of sweet melon, amber, vanilla, and premium oud."],
  ["perfume-007", "Rasasi Hawas Ice EDP for Men 100ml", 3100, "https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?auto=format&fit=crop&w=900&q=80", "A cool, fresh scent with a crisp citrus finish. Top Notes: Bergamot, Lemon. Middle: Melon, Violet. Base: Musk, Cedar."],
  ["perfume-008", "Maison Francis Kurkdjian Baccarat Rouge 540 EDP", 32500, "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=900&q=80", "Iconic Unisex Niche Perfume. A luminous, sophisticated amber floral and woody breeze. Top Notes: Saffron, Jasmine. Middle: Amberwood. Base: Fir Resin, Cedar."],
  ["perfume-009", "Parfums de Marly Layton EDP for Men 125ml", 24500, "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?auto=format&fit=crop&w=900&q=80", "Distinguished Masculine Luxury. A refined blend of fresh fruit and warm spices. Top Notes: Apple, Bergamot, Lavender. Middle: Jasmine, Violet. Base: Vanilla, Pepper, Guaiac Wood."],
  ["perfume-010", "Xerjoff Erba Pura EDP Unisex 100ml", 21000, "https://images.unsplash.com/photo-1523293182086-7651a899d37f?auto=format&fit=crop&w=900&q=80", "Vibrant Fruity-Musky Masterpiece. An indulgent elixir of fruits and amber. Top Notes: Sicilian Orange, Calabrian Bergamot. Middle: Fruity Notes. Base: White Musk, Madagascar Vanilla."],
  ["perfume-011", "Amouage Interlude Man EDP 100ml", 28000, "https://images.unsplash.com/photo-1617897903246-719242758050?auto=format&fit=crop&w=900&q=80", "The Blue Beast. A powerful, spicy-woody and balsamic experience. Top Notes: Bergamot, Oregano. Middle: Amber, Frankincense. Base: Leather, Agarwood (Oud), Sandalwood."]
].map(([id, name, price, image, description], index) => ({
  id,
  name,
  groups: ["Perfumes", index % 2 === 0 ? "Men" : "Women"],
  description,
  price,
  tag: index < 4 ? "Best seller" : "New arrival",
  color: "Full bottle",
  image
}));
products.push(...bestSellingPerfumes);
const marketSunglasses = [
  ["Trendsetter Black Sunglasses", 897, "Men"],
  ["White Metal Frame Sunglasses", 997, "Unisex"],
  ["Unisex Plastic Summer Sunglasses", 977, "Unisex"],
  ["RIDERACE Sports Cycling Goggles", 407, "Men"],
  ["Popular Women's Punk Oval Y2K Sunglasses", 349, "Women"],
  ["UV400 Windproof Cycling Goggles", 474, "Unisex"],
  ["Y2K UV400 Sports Sunglasses", 402, "Unisex"],
  ["Black to White UV400 Sunglasses", 339, "Men"],
  ["White Frame Sunglasses for Men", 996, "Men"],
  ["Transparent Frame Sunglasses for Men", 996, "Men"],
  ["Wayfarer Sunglasses for Men", 996, "Men"],
  ["SCVCN Outdoor MTB UV400 Glasses", 662, "Unisex"],
  ["Polarized Round UV400 Sunglasses", 922, "Unisex"],
  ["Vintage Cat Eye Sunglasses for Women", 277, "Women"],
  ["ONEVAN 2023 Square Sunglasses", 995, "Men"],
  ["DKS04694 Flexible Polycarbonate Sunglasses", 254, "Men"],
  ["Unisex Metal UV Protection Sunglasses", 376, "Unisex"],
  ["Roza Retro Sunglasses for Men", 219, "Men"],
  ["Rectangular Black MC Stan Sunglasses", 998, "Unisex"],
  ["OMEKOL Photochromic Cycling Glasses", 415, "Unisex"]
].map(([name, price, audience], index) => ({
  id: `market-sunglasses-${String(index + 1).padStart(3, "0")}`,
  name,
  groups: ["Sunglasses", audience],
  description: "Bangladesh marketplace reference listing",
  price,
  tag: "Market listing",
  color: "As shown",
  image: marketSunglassesImages[index % marketSunglassesImages.length]
}));
products.push(...marketSunglasses);

const pronounWatchCatalog = [
  ["Fastrack Urban Crest FT-UC-242", 999, "https://pronoun.pro/wp-content/uploads/2026/09/White-PN-1420-scaled.webp"],
  ["Fastrack Meridian FT-MD-241", 1120, "https://pronoun.pro/wp-content/uploads/2026/09/Navy-Blue-PN-1416-scaled.webp"],
  ["Universe Point Royal Noir UP-RN427", 999, "https://pronoun.pro/wp-content/uploads/2026/06/White.webp"],
  ["Fastrack Groove 3321SM01 Men's Watch", 800, "https://pronoun.pro/wp-content/uploads/2026/05/White-Dial_-scaled.webp"],
  ["Fastrack PRN-SQ17 Modern Edge", 999, "https://pronoun.pro/wp-content/uploads/2026/04/Black-PN-1351.webp"],
  ["Mark M6278 Ultra Thin Watch", 1299, "https://pronoun.pro/wp-content/uploads/2026/03/Toton-Balck-PN-12570-scaled.webp"],
  ["OMEGA ZQ98 Triple Calendar Watch", 1599, "https://pronoun.pro/wp-content/uploads/2026/02/Silver-white-PN-12560-scaled.webp"],
  ["Fastrack 9947 Mens Watch", 750, "https://pronoun.pro/wp-content/uploads/2025/10/Silver.jpg"],
  ["Hublot Gang Sang Spider Dial Watch", 1050, "https://pronoun.pro/wp-content/uploads/2025/12/Silver-Black-scaled.webp"],
  ["Forest F-740", 1399, "https://pronoun.pro/wp-content/uploads/2025/05/Picsart_25-06-19_23-29-14-052-min-scaled.webp"],
  ["Titan Chain Man's Watch", 899, "https://pronoun.pro/wp-content/uploads/2025/11/Silver.webp"],
  ["TOMI T077A Elegant Narrative", 899, "https://pronoun.pro/wp-content/uploads/2026/08/Image-1.webp"],
  ["Fastrack ES-214 Men's Watch", 850, "https://pronoun.pro/wp-content/uploads/2026/05/Brown-1-scaled.jpg"],
  ["Hublot Obsidian Prime", 999, "https://pronoun.pro/wp-content/uploads/2026/05/Silver-Black_-1.webp"],
  ["Forest F-1035 Urban Drift Men's Watch", 1150, "https://pronoun.pro/wp-content/uploads/2026/05/Black-1.webp"]
].map(([name, price, image], index) => ({
  id: `pronoun-watch-${String(index + 1).padStart(3, "0")}`,
  name,
  groups: ["Watches", "Men"],
  description: "Bangladesh watch market listing",
  price,
  tag: "Market listing",
  color: "As shown",
  image
}));
products.push(...pronounWatchCatalog);

const premiumBagNames = ["Dhaka Carryall", "Jamuna Leather Satchel", "Bengal Work Tote", "Gulshan Shoulder Bag"];
const premiumBagColors = ["Tan", "Black", "Cognac", "Olive", "Stone", "Burgundy", "Navy", "Camel"];
const premiumBagImages = [
  "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?auto=format&fit=crop&w=900&q=80",
  "https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=900&q=80"
];
const premiumBags = Array.from({ length: premiumBagNames.length }, (_, index) => ({
  id: `premium-bag-${String(index + 1).padStart(3, "0")}`,
  name: `${premiumBagNames[index % premiumBagNames.length]} ${String(index + 1).padStart(3, "0")}`,
  groups: ["Bags", index % 2 ? "Women" : "Men"],
  description: "Premium finish for work, travel, and weekends",
  price: 3850 + ((index * 375) % 12151),
  tag: index % 4 === 0 ? "Premium" : "Market pick",
  color: premiumBagColors[index % premiumBagColors.length],
  image: premiumBagImages[index % premiumBagImages.length]
}));
products.push(...premiumBags);

function removeRepeatedProductImages(productList) {
  const seenImages = new Set();
  const uniqueProducts = productList.filter((product) => {
    if (!product.image || seenImages.has(product.image)) return false;
    seenImages.add(product.image);
    return true;
  });
  productList.splice(0, productList.length, ...uniqueProducts);
}

removeRepeatedProductImages(products);

const numberFormat = new Intl.NumberFormat("en-BD");
const currency = { format: (amount) => `৳${numberFormat.format(amount)}` };
const grid = document.querySelector("#product-grid");
const watchGrid = document.querySelector("#watch-grid");
const sunglassesGrid = document.querySelector("#sunglasses-grid");
const trousersGrid = document.querySelector("#trousers-grid");
const pantsGrid = document.querySelector("#pants-grid");
const perfumesGrid = document.querySelector("#perfumes-grid");
const polosGrid = document.querySelector("#polos-grid");
const katuaGrid = document.querySelector("#katua-grid");
const bagsGrid = document.querySelector("#bags-grid");
const cart = new Map();
let checkoutItems = null;
let activeCategory = "All";
let activeSort = "featured";
let searchTerm = "";
let toastTimer;

function visibleProducts() {
  let result = products.filter((product) => {
    const matchesCategory = activeCategory === "All" || product.groups.includes(activeCategory);
    const searchableText = `${product.name} ${product.description} ${product.groups.join(" ")} ${product.color}`.toLowerCase();
    const matchesSearch = searchTerm.split(/\s+/).filter(Boolean).every((term) => searchableText.includes(term));
    return matchesCategory && matchesSearch;
  });
  if (activeSort === "low-high") result = [...result].sort((a, b) => a.price - b.price);
  if (activeSort === "high-low") result = [...result].sort((a, b) => b.price - a.price);
  return result;
}

function productDetailsUrl(product) {
  const images = Array.isArray(product.gallery) && product.gallery.length ? product.gallery : [product.image];
  const query = new URLSearchParams({
    id: product.id,
    name: product.name,
    price: String(product.price),
    color: product.color,
    description: product.description,
    image: product.image,
    images: JSON.stringify(images),
  });
  return `/product/${encodeURIComponent(product.id)}?${query}`;
}

function renderProducts() {
  const items = visibleProducts();
  document.querySelector("#item-total").textContent = `${String(items.length).padStart(2, "0")} products`;
  if (!items.length) {
    grid.innerHTML = `
      <div class="search-empty-state">
        <p>${searchTerm ? "No products match your search." : "No products in this category."}</p>
        <button id="clear-search" type="button">Show all products</button>
      </div>`;
    grid.querySelector("#clear-search").addEventListener("click", () => {
      document.querySelector("#search-input").value = "";
      searchTerm = "";
      selectCategory("All");
    });
    return;
  }
  grid.innerHTML = items.map((product, index) => `
    <article class="product-card" style="animation-delay:${index * 55}ms">
      <div class="product-image-wrap">
        <img class="product-image" src="${product.image}" alt="${product.name} in ${product.color}" loading="lazy">
        <span class="product-tag">${product.tag}</span>
        <div class="product-actions">
          <button class="quick-add" type="button" data-add="${product.id}">Add to bag</button>
          <button class="buy-now" type="button" data-buy="${product.id}">Buy now <span aria-hidden="true">→</span></button>
        </div>
      </div>
      <div class="product-meta"><h3 class="product-name"><a href="${productDetailsUrl(product)}">${product.name}</a></h3><p class="product-price">${currency.format(product.price)}</p></div>
      <p class="product-description">${product.description} · ${product.groups[0]}</p>
      <a class="product-detail-link" href="${productDetailsUrl(product)}">View details <span aria-hidden="true">↗</span></a>
    </article>`).join("");
}

function renderCollection(collectionGrid, category) {
  collectionGrid.innerHTML = products.filter((product) => product.groups.includes(category)).map((product, index) => `
    <article class="product-card" style="animation-delay:${index * 55}ms">
      <div class="product-image-wrap">
        <img class="product-image" src="${product.image}" alt="${product.name} in ${product.color}" loading="lazy">
        <span class="product-tag">${product.tag}</span>
        <div class="product-actions">
          <button class="quick-add" type="button" data-add="${product.id}">Add to bag</button>
          <button class="buy-now" type="button" data-buy="${product.id}">Buy now <span aria-hidden="true">→</span></button>
        </div>
      </div>
      <div class="product-meta"><h3 class="product-name"><a href="${productDetailsUrl(product)}">${product.name}</a></h3><p class="product-price">${currency.format(product.price)}</p></div>
      <p class="product-description">${product.description} · ${product.groups[0]}</p>
      <a class="product-detail-link" href="${productDetailsUrl(product)}">View details <span aria-hidden="true">↗</span></a>
    </article>`).join("");
}

function cartEntries() {
  return [...cart.entries()].map(([id, quantity]) => ({ product: products.find((product) => product.id === id), quantity }));
}

function checkoutEntries() {
  return checkoutItems || cartEntries();
}

function renderCart() {
  const entries = cartEntries();
  const quantity = entries.reduce((sum, entry) => sum + entry.quantity, 0);
  const total = entries.reduce((sum, entry) => sum + entry.product.price * entry.quantity, 0);
  const orderEntries = checkoutEntries();
  const orderTotal = orderEntries.reduce((sum, entry) => sum + entry.product.price * entry.quantity, 0);
  document.querySelector("#bag-count").textContent = quantity;
  document.querySelector("#bag-empty").hidden = entries.length > 0;
  document.querySelector("#bag-bottom").hidden = entries.length === 0;
  document.querySelector("#bag-subtotal").textContent = currency.format(total);
  document.querySelector("#checkout-total").textContent = currency.format(orderTotal);
  document.querySelector("#checkout-items").innerHTML = orderEntries.map(({ product, quantity: count }) => `
    <div class="checkout-item"><span>${product.name} × ${count}</span><strong>${currency.format(product.price * count)}</strong></div>`).join("");
  document.querySelector("#bag-items").innerHTML = entries.map(({ product, quantity: count }) => `
    <article class="bag-line">
      <img src="${product.image}" alt="">
      <div class="bag-line-info"><strong>${product.name}</strong><span>${product.color} · ${currency.format(product.price)}</span>
        <div class="quantity-control"><button type="button" data-change="-1" data-id="${product.id}" aria-label="Remove one ${product.name}">−</button><output>${count}</output><button type="button" data-change="1" data-id="${product.id}" aria-label="Add one ${product.name}">+</button></div>
      </div>
      <div class="bag-line-price">${currency.format(product.price * count)}<br><button class="remove-item" type="button" data-remove="${product.id}">Remove</button></div>
    </article>`).join("");
}

function showToast(message) {
  const toast = document.querySelector("#toast");
  toast.textContent = message;
  toast.classList.add("is-visible");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 2300);
}

function openBag() {
  document.querySelector("#drawer-backdrop").hidden = false;
  requestAnimationFrame(() => {
    document.querySelector("#drawer-backdrop").classList.add("is-visible");
    document.querySelector("#bag-drawer").classList.add("is-open");
    document.querySelector("#bag-drawer").setAttribute("aria-hidden", "false");
  });
  document.body.style.overflow = "hidden";
  document.querySelector("#close-bag").focus();
}

function closeBag() {
  document.querySelector("#drawer-backdrop").classList.remove("is-visible");
  document.querySelector("#bag-drawer").classList.remove("is-open");
  document.querySelector("#bag-drawer").setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
  setTimeout(() => { document.querySelector("#drawer-backdrop").hidden = true; }, 260);
  document.querySelector("#open-bag").focus();
}

function selectCategory(category) {
  activeCategory = category;
  document.querySelectorAll(".category-tab").forEach((tab) => tab.classList.toggle("is-active", tab.dataset.category === category));
  renderProducts();
}

document.addEventListener("click", (event) => {
  const categoryLink = event.target.closest("[data-category]");
  if (categoryLink) selectCategory(categoryLink.dataset.category);
});

document.querySelector("#search-form").addEventListener("submit", (event) => {
  event.preventDefault();
  searchTerm = document.querySelector("#search-input").value.trim().toLowerCase();
  selectCategory("All");
  document.querySelector("#shop").scrollIntoView({ behavior: "smooth", block: "start" });
  grid.focus({ preventScroll: true });
});
document.querySelector("#search-input").addEventListener("input", (event) => {
  searchTerm = event.target.value.trim().toLowerCase();
  renderProducts();
});

document.querySelector("#sort-products").addEventListener("change", (event) => {
  activeSort = event.target.value;
  renderProducts();
});

function handleProductAction(event) {
  const button = event.target.closest("[data-add], [data-buy]");
  if (!button) return;
  const productId = button.dataset.add || button.dataset.buy;
  const product = products.find((item) => item.id === productId);
  if (button.hasAttribute("data-buy")) {
    checkoutItems = [{ product, quantity: 1 }];
    renderCart();
    document.querySelector("#checkout-dialog").showModal();
    return;
  }
  cart.set(product.id, (cart.get(product.id) || 0) + 1);
  renderCart();
  showToast(`${product.name} added to your bag`);
}

function handleProductCardNavigation(event) {
  if (event.target.closest("button, a, input, textarea, select, label")) return;

  const card = event.target.closest(".product-card");
  if (!card) return;

  const detailLink = card.querySelector(".product-name a, .product-detail-link");
  if (detailLink) {
    window.location.href = detailLink.href;
  }
}

grid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
watchGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
sunglassesGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
trousersGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
pantsGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
perfumesGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
polosGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});
bagsGrid.addEventListener("click", (event) => {
  if (event.target.closest("[data-add], [data-buy]")) {
    handleProductAction(event);
    return;
  }
  handleProductCardNavigation(event);
});

document.addEventListener("click", (event) => {
  const button = event.target.closest("[data-add], [data-buy]");
  if (button && !button.closest(".product-grid")) {
    handleProductAction(event);
  }
});

document.querySelector("#bag-items").addEventListener("click", (event) => {
  const changeButton = event.target.closest("[data-change]");
  const removeButton = event.target.closest("[data-remove]");
  if (removeButton) cart.delete(removeButton.dataset.remove);
  if (changeButton) {
    const id = changeButton.dataset.id;
    const next = (cart.get(id) || 0) + Number(changeButton.dataset.change);
    if (next > 0) cart.set(id, next);
    else cart.delete(id);
  }
  renderCart();
});

document.querySelector("#open-bag").addEventListener("click", openBag);
document.querySelector("#close-bag").addEventListener("click", closeBag);
document.querySelector("#continue-shopping").addEventListener("click", closeBag);
document.querySelector("#drawer-backdrop").addEventListener("click", closeBag);
document.querySelector("#checkout-button").addEventListener("click", () => {
  checkoutItems = null;
  renderCart();
  closeBag();
  document.querySelector("#checkout-dialog").showModal();
});
document.querySelector("#close-checkout").addEventListener("click", () => document.querySelector("#checkout-dialog").close());
document.querySelector("#checkout-dialog").addEventListener("close", () => {
  checkoutItems = null;
  appliedCoupon = null;
  const couponInput = document.querySelector("#checkout-coupon");
  if(couponInput) couponInput.value = "";
  const couponMsg = document.querySelector("#coupon-message");
  if(couponMsg) couponMsg.textContent = "";
  renderCart();
});
document.querySelector("#checkout-dialog").addEventListener("click", (event) => {
  if (event.target === event.currentTarget) event.currentTarget.close();
});
document.querySelector("#checkout-form").addEventListener("submit", async (event) => {
  event.preventDefault();
  const form = event.currentTarget;
  const formData = new FormData(form);
  const orderEntries = checkoutEntries();
  const isDirectCheckout = checkoutItems !== null;
  const submitButton = event.submitter || form.querySelector('button[type="submit"]');
  const originalButtonText = submitButton.textContent;
  submitButton.disabled = true;
  submitButton.textContent = "Processing order...";

  try {
    const payload = {
      customer: Object.fromEntries(formData.entries()),
      items: orderEntries.map(({ product, quantity }) => ({ id: product.id, quantity }))
    };
    if (appliedCoupon && appliedCoupon.code) {
      payload.customer.coupon_code = appliedCoupon.code;
    }

    const response = await fetch("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Could not place your order.");

    if (!isDirectCheckout) cart.clear();
    checkoutItems = null;
    appliedCoupon = null;
    const couponInput = document.querySelector("#checkout-coupon");
    if(couponInput) couponInput.value = "";
    const couponMsg = document.querySelector("#coupon-message");
    if(couponMsg) couponMsg.textContent = "";
    
    renderCart();
    form.reset();
    document.querySelector("#checkout-dialog").close();
    
    // Show the success dialog instead of redirecting
    document.querySelector("#success-reference").textContent = result.reference;
    document.querySelector("#success-dialog").showModal();
    showToast(`Order ${result.reference} confirmed successfully!`);
  } catch (error) {
    showToast(error.message || "Could not process your order. Please try again.");
  } finally {
    submitButton.disabled = false;
    submitButton.textContent = originalButtonText;
  }
});

let appliedCoupon = null;
document.querySelector("#apply-coupon")?.addEventListener("click", async () => {
  const code = document.querySelector("#checkout-coupon").value.trim();
  const messageEl = document.querySelector("#coupon-message");
  if (!code) {
    messageEl.textContent = "Please enter a code.";
    messageEl.style.color = "var(--danger-text)";
    return;
  }
  const orderEntries = checkoutEntries();
  const orderTotal = orderEntries.reduce((sum, entry) => sum + entry.product.price * entry.quantity, 0);

  try {
    const res = await fetch("/api/coupons/validate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code, subtotal: orderTotal })
    });
    const data = await res.json();
    if (!res.ok || !data.valid) {
      throw new Error(data.error || "Invalid coupon.");
    }
    appliedCoupon = data;
    messageEl.textContent = data.message;
    messageEl.style.color = "var(--success-text)";
    document.querySelector("#checkout-total").innerHTML = `<del style="color:var(--muted); font-size: 0.9em; margin-right:6px">৳${orderTotal.toLocaleString('en-BD')}</del> ৳${data.final_total.toLocaleString('en-BD')}`;
  } catch (err) {
    appliedCoupon = null;
    messageEl.textContent = err.message;
    messageEl.style.color = "var(--danger-text)";
    document.querySelector("#checkout-total").textContent = `৳${orderTotal.toLocaleString('en-BD')}`;
  }
});

// Event listeners for the success dialog
document.querySelector("#close-success")?.addEventListener("click", () => document.querySelector("#success-dialog").close());
document.querySelector("#success-continue")?.addEventListener("click", () => document.querySelector("#success-dialog").close());

document.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && document.querySelector("#bag-drawer").classList.contains("is-open")) closeBag();
});

renderProducts();
renderCollection(watchGrid, "Watches");
renderCollection(sunglassesGrid, "Sunglasses");
renderCollection(trousersGrid, "Trousers");
renderCollection(pantsGrid, "Pants");
renderCollection(perfumesGrid, "Perfumes");
renderCollection(polosGrid, "Polos");
renderCollection(katuaGrid, "Katua");
renderCollection(bagsGrid, "Bags");
renderCart();