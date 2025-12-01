<?php
/**
 * ===========================
 * AFTUR SHOP - DUPLICATE PRODUCT
 * ===========================
 * Script untuk menduplikasi produk
 */

require_once "../koneksi.php";
require_once "../classes/Product.php";
require_once "../classes/ProductRepository.php";

$productRepository = new ProductRepository($koneksi);

$id = $_GET['id'] ?? null;

if ($id) {
    // Get original product
    $originalProduct = $productRepository->getById($id);

    if ($originalProduct) {
        // Clone product (handled by __clone method in Product class)
        $clonedProduct = clone $originalProduct;

        // Save cloned product as new entry
        if ($productRepository->create($clonedProduct)) {
            echo "<script>alert('Produk berhasil di-duplicate'); window.location='../index.php';</script>";
        } else {
            echo "<script>alert('Gagal menduplikasi produk'); window.location='../index.php';</script>";
        }
    } else {
        echo "<script>alert('Produk tidak ditemukan'); window.location='../index.php';</script>";
    }
} else {
    header("Location: ../index.php");
}