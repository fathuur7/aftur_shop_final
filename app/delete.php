<?php
/**
 * ===========================
 * AFTUR SHOP - DELETE PRODUCT
 * ===========================
 * Script untuk menghapus produk
 */

require_once "../koneksi.php";
require_once "../classes/Product.php";
require_once "../classes/ProductRepository.php";

$productRepository = new ProductRepository($koneksi);

$id = $_GET['id'] ?? null;

if ($id) {
    if ($productRepository->delete($id)) {
        echo "<script>alert('Produk dihapus'); window.location='../index.php';</script>";
    } else {
        echo "<script>alert('Gagal menghapus produk'); window.location='../index.php';</script>";
    }
} else {
    header("Location: ../index.php");
}