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
const priceElement = document.querySelector("#product-price");
const colorElement = document.querySelector("#product-color");
const descriptionElement = document.querySelector("#product-description");
const detailsElement = document.querySelector("#product-details-text");
const form = document.querySelector("#product-order-form");
const toast = document.querySelector("#product-toast");

nameElement.textContent = productName;
breadcrumbElement.textContent = productName;
document.title = `${productName} | ARAMS`;
imageElement.src = productImage;
imageElement.alt = `${productName} in ${productColor}`;
priceElement.textContent = currency(productPrice);
colorElement.textContent = productColor;
descriptionElement.textContent = productDescription;
detailsElement.textContent = `${productDescription}. Color or finish: ${productColor}.`;

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
