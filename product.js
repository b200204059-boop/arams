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
  const rawImages = params.get("images") || params.get("image");
  if (!rawImages) return null;
  try {
    const parsed = JSON.parse(rawImages);
    if (Array.isArray(parsed) && parsed.length) return parsed.filter(Boolean);
  } catch (error) {
    if (rawImages.includes("||")) return rawImages.split("||").map(s => s.trim()).filter(Boolean);
    if (rawImages.includes(",")) return rawImages.split(",").map(s => s.trim()).filter(Boolean);
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

const checkoutDialog = document.querySelector("#checkout-dialog");
const successDialog = document.querySelector("#success-dialog");
const checkoutForm = document.querySelector("#checkout-form");
const closeCheckoutBtn = document.querySelector("#close-checkout");
const closeSuccessBtn = document.querySelector("#close-success");
const successContinueBtn = document.querySelector("#success-continue");
const checkoutTotal = document.querySelector("#checkout-total");
const successReference = document.querySelector("#success-reference");
const applyCouponBtn = document.querySelector("#apply-coupon");
const couponInput = document.querySelector("#checkout-coupon");
const couponMessage = document.querySelector("#coupon-message");

let pendingQuantity = 1;

form.addEventListener("submit", (event) => {
  event.preventDefault();
  pendingQuantity = Number(new FormData(form).get("quantity"));
  
  if (checkoutDialog) {
    const total = pendingQuantity * productPrice;
    checkoutTotal.textContent = currency(total);
    checkoutDialog.showModal();
  }
});

if (closeCheckoutBtn) closeCheckoutBtn.addEventListener("click", () => checkoutDialog.close());
if (closeSuccessBtn) closeSuccessBtn.addEventListener("click", () => successDialog.close());
if (successContinueBtn) {
  successContinueBtn.addEventListener("click", () => {
    successDialog.close();
    window.location.href = '/';
  });
}

if (checkoutForm) {
  checkoutForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const submitBtn = checkoutForm.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.textContent = "Processing...";
    
    const formData = new FormData(checkoutForm);
    const customerData = Object.fromEntries(formData.entries());
    const couponCode = customerData.coupon_code || "";
    
    try {
      const response = await fetch("/api/orders", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          customer: { 
            name: customerData.name, 
            phone: customerData.phone, 
            email: customerData.email, 
            notes: customerData.notes 
          },
          items: [{ id: productId, quantity: pendingQuantity }],
          coupon_code: couponCode
        })
      });
      const result = await response.json();
      if (!response.ok) throw new Error(result.error || "Could not place the order.");
      
      checkoutDialog.close();
      if (successReference) successReference.textContent = result.reference || "CONFIRMED";
      if (successDialog) successDialog.showModal();
      checkoutForm.reset();
    } catch (error) {
      toast.textContent = error.message;
      toast.classList.add("is-visible");
      setTimeout(() => toast.classList.remove("is-visible"), 3000);
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    }
  });
}

if (applyCouponBtn) {
  applyCouponBtn.addEventListener("click", async () => {
    const code = couponInput.value.trim();
    if (!code) return;
    
    try {
      const res = await fetch("/api/coupons/validate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          coupon_code: code,
          items: [{ id: productId, quantity: pendingQuantity }]
        })
      });
      const data = await res.json();
      if (res.ok && data.valid) {
        couponMessage.textContent = `Coupon applied! Discount: ${currency(data.discount_amount)}`;
        couponMessage.style.color = "green";
        const newTotal = (pendingQuantity * productPrice) - data.discount_amount;
        checkoutTotal.textContent = currency(newTotal > 0 ? newTotal : 0);
      } else {
        couponMessage.textContent = data.error || "Invalid coupon";
        couponMessage.style.color = "red";
        checkoutTotal.textContent = currency(pendingQuantity * productPrice);
      }
    } catch (e) {
      couponMessage.textContent = "Error validating coupon";
      couponMessage.style.color = "red";
    }
  });
}
const sizeContainer = document.querySelector("#size-container");
const sizeSelect = document.querySelector("#product-size");

const isClothing = productId && (productId.startsWith("katua-") || productId.startsWith("gorur-pants-") || productId.startsWith("gorur-polo-") || productId === "mens-trousers" || productId === "everyday-shirt" || productId === "mens-shorts" || productId.includes("trousers") || productId.includes("pants"));
let selectedSize = "";

if (isClothing && sizeContainer && sizeSelect) {
  sizeContainer.style.display = "grid";
  const sizes = ["S", "M", "L", "XL", "XXL"];
  if (productId.includes("pants") || productId.includes("trousers")) {
    sizes.splice(0, sizes.length, "28", "30", "32", "34", "36", "38");
  }
  
  sizes.forEach(size => {
    const option = document.createElement("option");
    option.value = size;
    option.textContent = size;
    sizeSelect.appendChild(option);
  });
}

// Sticky Mobile Buy Bar
const stickyBar = document.querySelector("#mobile-sticky-buy");
const stickyName = document.querySelector("#sticky-name");
const stickyPrice = document.querySelector("#sticky-price");
const stickyBtn = document.querySelector("#sticky-buy-btn");
const mainBuyBtn = document.querySelector(".product-buy-button");

if (stickyBar && mainBuyBtn) {
  stickyName.textContent = productName;
  stickyPrice.textContent = currency(productPrice);
  
  const observer = new IntersectionObserver((entries) => {
    const mainBtnEntry = entries[0];
    if (!mainBtnEntry.isIntersecting && mainBtnEntry.boundingClientRect.top < 0) {
      stickyBar.classList.add("is-visible");
    } else {
      stickyBar.classList.remove("is-visible");
    }
  }, { threshold: 0 });
  
  observer.observe(mainBuyBtn);
  
  stickyBtn.addEventListener("click", () => {
    // Scroll up to the form or open checkout directly
    if (isClothing && sizeSelect.value === "") {
      document.querySelector(".product-detail-copy").scrollIntoView({ behavior: "smooth" });
      toast.textContent = "Please select a size first.";
      toast.classList.add("is-visible");
      setTimeout(() => toast.classList.remove("is-visible"), 3000);
    } else {
      form.dispatchEvent(new Event("submit", { cancelable: true, bubbles: true }));
    }
  });
}
