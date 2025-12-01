<?php
/**
 * ===========================
 * AFTUR SHOP - NEW ARRIVALS CONTROLLER
 * ===========================
 */

// Mock Data for New Arrivals
$products = [
    (object)[
        'id' => 101,
        'nama' => 'Smart Watch Series 7',
        'harga' => 4500000,
        'kategori' => 'Electronics',
        'gambar' => 'assets/images/products/watch.png'
    ],
    (object)[
        'id' => 102,
        'nama' => 'Leather Backpack',
        'harga' => 850000,
        'kategori' => 'Fashion',
        'gambar' => 'assets/images/products/backpack.png'
    ],
    (object)[
        'id' => 103,
        'nama' => 'Wireless Earbuds Pro',
        'harga' => 1200000,
        'kategori' => 'Electronics',
        'gambar' => 'assets/images/products/earbuds.png'
    ],
    (object)[
        'id' => 104,
        'nama' => 'Minimalist Desk Lamp',
        'harga' => 350000,
        'kategori' => 'Home & Living',
        'gambar' => 'assets/images/products/lamp.png'
    ]
];

$pageTitle = "New Arrivals";
$pageDescription = "Check out the latest additions to our store.";


require_once "./views/new_arrivals.php";
?>
