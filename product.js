const params = new URLSearchParams(window.location.search);
const productId = params.get("id");
const productName = params.get("name") || "ARAMS product";
const productPrice = Number(params.get("price")) || 0;
const productColor = params.get("color") || "Available now";
const productDescription = params.get("description") || "Product details from ARAMS.";
const productImage = params.get("image") || "";
const numberFormat = new Intl.NumberFormat("en-BD");
const currency = (amount) => `\u09F3${numberFormat.format(amount)}`;
const nameElement = document.querySelector("#product-name");
const breadcrumbElement = document.querySelector("#product-breadcrumb-name");
const imageElement = document.querySelector("#product-image");
const thumbnailRow = document.querySelector("#product-thumbnail-row");
const priceElement = document.querySelector("#product-price");
const colorElement = document.querySelector("#product-color");
const descriptionElement = document.querySelector("#product-description");
const detailsElement = document.querySelector("#product-details-text");
const form = document.querySelector("#product-order-form");
const toast = document.querySelector("#product-toast");

const productGalleryMap = {
  "pronoun-watch-008": [
    "https://pronoun.pro/wp-content/uploads/2025/10/Silver.jpg",
    "https://pronoun.pro/wp-content/uploads/2025/10/Silver.webp",
    "https://pronoun.pro/wp-content/uploads/2025/10/Toton.webp"
  ],
  "perfume-001": [
    "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=900&q=80"
  ],
  "perfume-002": [
    "https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?auto=format&fit=crop&w=900&q=80"
  ],
  "perfume-003": [
    "https://images.unsplash.com/photo-1594035910387-fea47794261f?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1541643600914-78b084683601?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?auto=format&fit=crop&w=900&q=80"
  ],
  "market-sunglasses-001": [
    "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1577803947579-9f6d1d3c6d1b?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1573497491208-6b1acb260507?auto=format&fit=crop&w=900&q=80"
  ]
};

const parseGalleryFromUrl = () => {
  const rawImages = params.get("images");
  if (!rawImages) return null;
  try {
    const parsed = JSON.parse(rawImages);
    if (Array.isArray(parsed) && parsed.length) return parsed.filter(Boolean);
  } catch (error) {
    if (rawImages.includes("||")) return rawImages.split("||").filter(Boolean);
    if (rawImages.includes(",")) return rawImages.split(",").filter(Boolean);
  }
  return null;
};

const normalizedProductName = (productName || "").toLowerCase();
const isFastrack9947 =
  productId === "pronoun-watch-008" ||
  normalizedProductName.includes("fastrack 9947") ||
  normalizedProductName.includes("fastrack 9947 mens watch");
const isPerfume = Boolean(productId && productId.startsWith("perfume-"));

const galleryImages = parseGalleryFromUrl() || productGalleryMap[productId] || [productImage].filter(Boolean);
const mainDescription = isFastrack9947
  ? "A clean silver statement watch with a refined dial, polished finish, and everyday versatility for workdays, weekends, and special plans."
  : isPerfume
    ? `${productName} pairs premium fragrance notes with a polished, confident profile designed for daily wear and long-lasting presence.`
    : productDescription;
const extrasText = isFastrack9947
  ? "Fastrack 9947 Mens Watch features a premium metal case, a sleek silver finish, and a classic profile designed for all-day wear. Choose from available Black, Silver, or Toton finishes for a look that balances everyday style and confidence. Built for comfortable daily wear with a polished design that transitions easily from casual to polished occasions."
  : isPerfume
    ? `${productName} is crafted for a long-lasting impression with a balanced note profile, premium bottle presentation, and a fragrance experience that works from day to night. ${productDescription}.`
    : `${productDescription}. Color or finish: ${productColor}.`;

nameElement.textContent = productName;
breadcrumbElement.textContent = productName;
document.title = `${productName} | ARAMS`;
imageElement.src = galleryImages[0] || productImage;
imageElement.alt = `${productName} in ${productColor}`;
priceElement.textContent = currency(productPrice);
colorElement.textContent = productColor;
descriptionElement.textContent = mainDescription;
detailsElement.textContent = extrasText;

if (thumbnailRow) {
  const images = galleryImages.length ? galleryImages : [productImage].filter(Boolean);
  thumbnailRow.innerHTML = images.map((image, index) => `
    <button type="button" class="product-thumb ${index === 0 ? "is-selected" : ""}" data-index="${index}" aria-label="View product image ${index + 1}">
      <img src="${image}" alt="${productName} view ${index + 1}">
    </button>
  `).join("");

  thumbnailRow.querySelectorAll(".product-thumb").forEach((thumb) => {
    thumb.addEventListener("click", () => {
      const index = Number(thumb.dataset.index);
      imageElement.src = images[index];
      thumbnailRow.querySelectorAll(".product-thumb").forEach((button) => button.classList.toggle("is-selected", Number(button.dataset.index) === index));
    });
  });
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const button = form.querySelector("button");
  const quantity = Number(new FormData(form).get("quantity"));
  const originalText = button.textContent;
  button.disabled = true;
  button.textContent = "Preparing order...";
  try {
    const response = await fetch("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        customer: { name: "Product page customer", phone: "Pending confirmation", email: "", notes: "Please confirm delivery details on WhatsApp." },
        items: [{ id: productId, quantity }]
      })
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Could not prepare the order.");
    window.location.href = result.whatsapp_url;
  } catch (error) {
    toast.textContent = error.message;
    toast.classList.add("is-visible");
    setTimeout(() => toast.classList.remove("is-visible"), 3000);
  } finally {
    button.disabled = false;
    button.textContent = originalText;
  }
});
