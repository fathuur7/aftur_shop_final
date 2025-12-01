<?php 
/**
 * ===========================
 * AFTUR SHOP - MAIN CONTROLLER
 * ===========================
 * Controller untuk halaman utama
 */

// 1. Load Database Connection
// File ini berisi kredensial database dan membuat koneksi ($koneksi)
require_once "koneksi.php"; 

// 2. Load ProductRepository Class
// Class ini menangani semua operasi database untuk produk (CRUD)
require_once "classes/ProductRepository.php";

// 3. Initialize Repository
// Kita membuat instance dari ProductRepository dengan koneksi database yang sudah ada
$productRepository = new ProductRepository($koneksi); 

// 4. Fetch Data (LOGIC / MODEL)
// Di sini kita mengambil data yang dibutuhkan dari database.
// Controller bertugas menyiapkan data sebelum ditampilkan ke user.
$totalProducts = $productRepository->countProducts();      // Hitung total produk
$totalCategories = $productRepository->countCategories();  // Hitung total kategori
$products = $productRepository->getAll();                  // Ambil semua data produk

// 5. Load View (PRESENTATION / VIEW)
// Setelah data siap, kita panggil file View untuk menampilkannya.
// Variable $products, $totalProducts, dll akan otomatis bisa diakses di dalam file view.
require_once "views/home.php";
?>