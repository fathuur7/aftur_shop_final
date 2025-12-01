<?php
/**
 * ===========================
 * AFTUR SHOP - EDIT PRODUCT CONTROLLER
 * ===========================
 * Controller untuk mengedit produk
 */

require_once "../koneksi.php";
require_once "../classes/Product.php";
require_once "../classes/ProductRepository.php";

$productRepository = new ProductRepository($koneksi);

// 1. Get Product ID
// Ambil ID produk dari URL (misal: edit.php?id=1)
$id = $_GET['id'] ?? null;
if (!$id) {
    echo "<script>alert('ID Produk tidak valid'); window.location='../index.php';</script>";
    exit;
}

// 2. Fetch Product Data (LOGIC)
// Ambil data produk berdasarkan ID untuk ditampilkan di form
$product = $productRepository->getById($id);

if (!$product) {
    echo "<script>alert('Data produk tidak ditemukan.'); window.location='../index.php';</script>";
    exit;
}

// 3. Handle Form Submission (LOGIC)
// Proses update data jika tombol submit ditekan
if (isset($_POST['submit'])) {
    $nama = $_POST['nama'];
    $harga = $_POST['harga'];
    $kategori = $_POST['kategori'];
    $gambar = $product->gambar; // Default gunakan gambar lama

    // 4. Handle File Upload
    // Jika ada gambar baru yang diupload
    if (!empty($_FILES['gambar']['name'])) {
        // Hapus gambar lama jika ada
        if ($gambar && file_exists("../uploads/$gambar")) {
            unlink("../uploads/$gambar");
        }

        // Upload gambar baru
        $gambar = time() . "_" . $_FILES['gambar']['name'];
        move_uploaded_file($_FILES['gambar']['tmp_name'], "../uploads/" . $gambar);
    }

    // 5. Update Product Object
    // Update property object dengan data baru
    $product->nama = $nama;
    $product->harga = $harga;
    $product->kategori = $kategori;
    $product->gambar = $gambar;

    // 6. Save to Database
    // Simpan perubahan ke database
    if ($productRepository->update($product)) {
        echo "<script>alert('Produk berhasil diupdate!'); window.location='../index.php';</script>";
    } else {
        echo "<script>alert('Gagal mengupdate produk');</script>";
    }
}

// 7. Load View (PRESENTATION)
// Tampilkan form edit dengan data yang sudah diambil
require_once "../views/edit_product.php";
?>