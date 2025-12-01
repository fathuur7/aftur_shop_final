<?php
/**
 * ===========================
 * AFTUR SHOP - SALE CONTROLLER
 * ===========================
 */

// Mock Data for Sale Items
$products = [
    (object)[
        'id' => 301,
        'nama' => 'Summer Dress',
        'harga' => 250000,
        'harga_asli' => 500000,
        'kategori' => 'Fashion',
        'gambar' => 'https://placehold.co/600x400?text=Summer+Dress'
    ],
    (object)[
        'id' => 302,
        'nama' => 'Bluetooth Speaker',
        'harga' => 450000,
        'harga_asli' => 750000,
        'kategori' => 'Electronics',
        'gambar' => 'https://placehold.co/600x400?text=Bluetooth+Speaker'
    ],
    (object)[
        'id' => 303,
        'nama' => 'Ceramic Vase Set',
        'harga' => 150000,
        'harga_asli' => 300000,
        'kategori' => 'Home & Living',
        'gambar' => 'https://placehold.co/600x400?text=Ceramic+Vase'
    ],
    (object)[
        'id' => 304,
        'nama' => 'Gaming Mouse',
        'harga' => 350000,
        'harga_asli' => 600000,
        'kategori' => 'Electronics',
        'gambar' => 'https://placehold.co/600x400?text=Gaming+Mouse'
    ]
];

$pageTitle = "Flash Sale";
$pageDescription = "Limited time offers with up to 50% off!";

require_once "./views/sale.php";
?>
