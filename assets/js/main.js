/**
 * ===========================
 * PRODUCT SEARCH FUNCTIONALITY
 * ===========================
 */

/**
 * Search products by name or category
 * Filters product cards based on search input
 */
function searchProducts() {
    const searchInput = document.getElementById('searchInput');
    const searchTerm = searchInput.value.toLowerCase();
    const productCards = document.querySelectorAll('.product-card');
    
    productCards.forEach(card => {
        const productTitle = card.querySelector('.product-title').textContent.toLowerCase();
        const productCategory = card.querySelector('.product-category').textContent.toLowerCase();
        
        // Show card if title or category matches search term
        const isMatch = productTitle.includes(searchTerm) || productCategory.includes(searchTerm);
        card.style.display = isMatch ? '' : 'none';
    });
}

/**
 * ===========================
 * EVENT LISTENERS
 * ===========================
 */

// Initialize search functionality when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    
    if (searchInput) {
        // Trigger search on every keystroke for instant results
        searchInput.addEventListener('keyup', function(event) {
            searchProducts();
        });
    }
});
