const products = [
  {
    id: 1,
    name: "Wireless headphone",
    price: 59.99,
    image:
      "https://media.istockphoto.com/id/1412240771/photo/headphones-on-white-background.jpg?s=612x612&w=0&k=20&c=DwpnlOcMzclX8zJDKOMSqcXdc1E7gyGYgfX5Xr753aQ=",
  },
  {
    id: 2,
    name: "Smart Watch",
    price: 59.99,
    image:
      "https://media.istockphoto.com/id/1412240771/photo/headphones-on-white-background.jpg?s=612x612&w=0&k=20&c=DwpnlOcMzclX8zJDKOMSqcXdc1E7gyGYgfX5Xr753aQ=",
  },
  {
    id: 3,
    name: "Bluetooth speaker",
    price: 59.99,
    image:
      "https://media.istockphoto.com/id/1412240771/photo/headphones-on-white-background.jpg?s=612x612&w=0&k=20&c=DwpnlOcMzclX8zJDKOMSqcXdc1E7gyGYgfX5Xr753aQ=",
  },
  {
    id: 4,
    name: "VR headset",
    price: 59.99,
    image:
      "https://media.istockphoto.com/id/1412240771/photo/headphones-on-white-background.jpg?s=612x612&w=0&k=20&c=DwpnlOcMzclX8zJDKOMSqcXdc1E7gyGYgfX5Xr753aQ=",
  },
];

const productContainer = document.getElementById("products");
const cartContainer = document.getElementById("cart");
const cartTotalEl = document.getElementById("cart-total");

let cart = [];
function renderProducts() {
  const productEl = document.createElement("div");
  productEl.className = "product";
  productEl.innerHTML = `<img src="${product.image}" alt = "${product.name}">
  <h3>${product.name}</h3>
  <p>price : ${product.price.toFixed(2)} </p>
  <button data-id="${product.id}">Add to Cart </button>
  `;
  productContainer.appendChild(productEl);
}

function renderCart() {
  cartContainer.innerHTML = "";
  if (cart.length === 0) {
    cartContainer.innerHTML = "<p> Your cart is empty </p>";
    cartTotalEl.textContent = "Total : $0.00";
    return;
  }
}

const header = document.createElement("div");
header.className = "cart-header";
header.innerHTML = `<div style="flex 2">product</div>
<div>Qty</div>
<div> price</div>
<div></div>
cartContainer.appendChild(header)`;

let total = 0;
cart.forEach((item) => {
  total += item.price * item.quantity;
  const itemEl = document.createElement("div");
  itemEl.className = "cart-item";
  itemEl.innerHTML = `<div style ='flex 2'>${item.name}</div>
    <div>${item.quantity}</div>
    <div>${(item.price * item.quantity).toFixed(2)}</div>
    <button class="remove-btn" data-id="${item.id}">Remove</button>`;
  cartContainer.appendChild(itemEl);
});
