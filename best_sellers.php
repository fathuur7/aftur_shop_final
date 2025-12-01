<?php
/**
 * ===========================
 * AFTUR SHOP - BEST SELLERS CONTROLLER
 * ===========================
 */

// Mock Data for Best Sellers
$products = [
    (object)[
        'id' => 201,
        'nama' => 'Ergonomic Office Chair',
        'harga' => 2500000,
        'kategori' => 'Furniture',
        'gambar' => 'assets/images/products/chair.png'
    ],
    (object)[
        'id' => 202,
        'nama' => 'Mechanical Keyboard',
        'harga' => 1500000,
        'kategori' => 'Electronics',
        'gambar' => 'assets/images/products/keyboard.png'
    ],
    (object)[
        'id' => 203,
        'nama' => 'Stainless Steel Water Bottle',
        'harga' => 250000,
        'kategori' => 'Lifestyle',
        'gambar' => 'assets/images/products/bottle.png'
    ],
    (object)[
        'id' => 204,
        'nama' => 'Running Shoes',
        'harga' => 950000,
        'kategori' => 'Fashion',
        'gambar' => 'https://placehold.co/600x400?text=Running+Shoes'
    ]
];

$pageTitle = "Best Sellers";
$pageDescription = "Our most popular products loved by customers.";

require_once "./views/best_sellers.php";
?>
