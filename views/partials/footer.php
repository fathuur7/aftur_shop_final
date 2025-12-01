<?php
// Default path prefix if not set
if (!isset($path_prefix)) {
    $path_prefix = '';
}
?>
<footer class="bg-white border-t border-gray-200 mt-12">
    <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div class="col-span-1 md:col-span-1">
                <div class="flex items-center gap-2 mb-4">
                    <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center text-white">
                        <i class="fas fa-shopping-bag"></i>
                    </div>
                    <span class="font-bold text-xl tracking-tight text-dark">Tokokita</span>
                </div>
                <p class="text-gray-500 text-sm">
                    Your one-stop shop for everything you need. Quality products, unbeatable prices.
                </p>
            </div>
            <div>
                <h4 class="font-bold text-gray-900 mb-4 uppercase text-sm tracking-wider">Shop</h4>
                <ul class="space-y-2 text-sm text-gray-500">
                    <li><a href="<?= $path_prefix ?>new_arrivals.php" class="hover:text-primary transition no-underline">New Arrivals</a></li>
                    <li><a href="<?= $path_prefix ?>best_sellers.php" class="hover:text-primary transition no-underline">Best Sellers</a></li>
                    <li><a href="<?= $path_prefix ?>sale.php" class="hover:text-primary transition no-underline">Sale</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-gray-900 mb-4 uppercase text-sm tracking-wider">Support</h4>
                <ul class="space-y-2 text-sm text-gray-500">
                    <li><a href="<?= $path_prefix ?>contact.php" class="hover:text-primary transition no-underline">Contact Us</a></li>
                    <li><a href="<?= $path_prefix ?>faq.php" class="hover:text-primary transition no-underline">FAQ</a></li>
                    <li><a href="<?= $path_prefix ?>shipping.php" class="hover:text-primary transition no-underline">Shipping & Returns</a></li>
                </ul>
            </div>
            <div>
                <h4 class="font-bold text-gray-900 mb-4 uppercase text-sm tracking-wider">Newsletter</h4>
                <p class="text-gray-500 text-sm mb-4">Subscribe for updates and promotions.</p>
                <div class="flex gap-2">
                    <input type="email" placeholder="Enter your email" class="bg-gray-100 text-sm rounded-lg px-4 py-2 w-full focus:outline-none focus:ring-2 focus:ring-primary">
                    <button class="bg-primary hover:bg-emerald-600 text-white px-4 py-2 rounded-lg text-sm font-medium transition">Subscribe</button>
                </div>
            </div>
        </div>
        <div class="border-t border-gray-200 mt-12 pt-8 text-center text-sm text-gray-400">
            &copy; 2024 Tokokita, Inc. All rights reserved.
        </div>
    </div>
</footer>
