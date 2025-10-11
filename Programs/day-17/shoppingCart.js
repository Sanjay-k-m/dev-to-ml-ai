// Sample products
  const products = [
    { id: 1, name: "Wireless Headphones", price: 59.99, image: "https://m.media-amazon.com/images/I/61GrtFhbGSL.jpg" },
    { id: 2, name: "Smart Watch", price: 99.99, image: "https://m.media-amazon.com/images/I/61ZjlBOp+rL.jpg" },
    { id: 3, name: "Bluetooth Speaker", price: 39.99, image: "https://m.media-amazon.com/images/I/71QBCTOhiiL.jpg" },
    { id: 4, name: "VR Headset", price: 199.99, image: "https://img.freepik.com/free-vector/realistic-virtual-headset-augmented-reality_52683-52869.jpg?w=360" }
  ];

  const productsContainer = document.getElementById('products');
  const cartContainer = document.getElementById('cart');
  const cartTotalEl = document.getElementById('cart-total');

  // Cart data: array of objects {id, name, price, quantity}
  let cart = [];

  // Render products on page
  function renderProducts() {
    products.forEach(product => {
      const productEl = document.createElement('div');
      productEl.className = 'product';
      productEl.innerHTML = `
        <img src="${product.image}" alt="${product.name}">
        <h3>${product.name}</h3>
        <p>Price: $${product.price.toFixed(2)}</p>
        <button data-id="${product.id}">Add to Cart</button>
      `;
      productsContainer.appendChild(productEl);
    });
  }

  // Render cart
  function renderCart() {
    cartContainer.innerHTML = ''; // clear previous

    if(cart.length === 0) {
      cartContainer.innerHTML = '<p>Your cart is empty.</p>';
      cartTotalEl.textContent = 'Total: $0.00';
      return;
    }

    // Cart header row
    const header = document.createElement('div');
    header.className = 'cart-header';
    header.innerHTML = `
      <div style="flex: 2;">Product</div>
      <div>Qty</div>
      <div>Price</div>
      <div></div>
    `;
    cartContainer.appendChild(header);

    let total = 0;

    cart.forEach(item => {
      total += item.price * item.quantity;

      const itemEl = document.createElement('div');
      itemEl.className = 'cart-item';
      itemEl.innerHTML = `
        <div style="flex: 2;">${item.name}</div>
        <div>${item.quantity}</div>
        <div>$${(item.price * item.quantity).toFixed(2)}</div>
        <button class="remove-btn" data-id="${item.id}">Remove</button>
      `;
      cartContainer.appendChild(itemEl);
    });

    cartTotalEl.textContent = `Total: $${total.toFixed(2)}`;
  }

  // Add to cart handler
  function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if(!product) return;

    const cartItem = cart.find(item => item.id === productId);
    if(cartItem) {
      cartItem.quantity++;
    } else {
      cart.push({ ...product, quantity: 1 });
    }

    renderCart();
  }

  // Remove from cart handler
  function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    renderCart();
  }

  // Event listeners
  productsContainer.addEventListener('click', (e) => {
    if(e.target.tagName === 'BUTTON') {
      const id = parseInt(e.target.getAttribute('data-id'));
      addToCart(id);
    }
  });

  cartContainer.addEventListener('click', (e) => {
    if(e.target.classList.contains('remove-btn')) {
      const id = parseInt(e.target.getAttribute('data-id'));
      removeFromCart(id);
    }
  });

  // Initial render
  renderProducts();
  renderCart();