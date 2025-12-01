<?php
// Default path prefix if not set
if (!isset($path_prefix)) {
    $path_prefix = '';
}
?>
<nav class="bg-white shadow-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16 items-center">
            <!-- Logo -->
            <a href="<?= $path_prefix ?>index.php" class="flex-shrink-0 flex items-center gap-2 cursor-pointer no-underline">
                <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center text-white">
                    <i class="fas fa-shopping-bag"></i>
                </div>
                <span class="font-bold text-xl tracking-tight text-dark">Tokokita</span>
            </a>

            <!-- Desktop Menu -->
            <div class="hidden md:flex space-x-8">
                <a href="<?= $path_prefix ?>new_arrivals.php" class="text-gray-900 font-medium hover:text-primary transition no-underline">New Arrivals</a>
                <a href="<?= $path_prefix ?>best_sellers.php" class="text-gray-500 font-medium hover:text-primary transition no-underline">Best Sellers</a>
                <a href="<?= $path_prefix ?>categories.php" class="text-gray-500 font-medium hover:text-primary transition no-underline">Categories</a>
                <a href="<?= $path_prefix ?>sale.php" class="text-red-500 font-medium hover:text-red-600 transition no-underline">Sale</a>
            </div>

            <!-- Search & Actions -->
            <div class="flex items-center gap-4">
                <!-- Search Form -->
                <input 
                    id="searchInput"
                    type="text" 
                    placeholder="Search products..." 
                    class="bg-gray-100 text-sm rounded-full pl-10 pr-4 py-2 focus:outline-none focus:ring-2 focus:ring-primary w-64 transition-all"
                >

                <a href="<?= $path_prefix ?>app/add.php" class="bg-primary hover:bg-emerald-600 text-white px-4 py-2 rounded-lg text-sm font-medium transition shadow-md hover:shadow-lg flex items-center gap-2 no-underline">
                    <i class="fas fa-plus"></i> <span class="hidden sm:inline">Add Product</span>
                </a>
                
                <div class="flex items-center gap-3 text-gray-500">
                    <button class="hover:text-primary transition"><i class="far fa-heart text-xl"></i></button>
                    <button class="hover:text-primary transition"><i class="fas fa-shopping-cart text-xl"></i></button>
                    <div class="w-8 h-8 bg-orange-200 rounded-full overflow-hidden border-2 border-white shadow-sm">
                        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" alt="User" class="w-full h-full object-cover">
                    </div>
                </div>
            </div>
        </div>
    </div>
</nav>
