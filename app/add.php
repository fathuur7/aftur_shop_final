<?php 
/**
 * ===========================
 * AFTUR SHOP - ADD PRODUCT CONTROLLER
<?php 
/**
 * ===========================
 * AFTUR SHOP - ADD PRODUCT CONTROLLER
 * ===========================
 * Controller untuk menambahkan produk baru
 */

require_once "../koneksi.php";
require_once "../classes/Product.php";
require_once "../classes/ProductRepository.php";

$productRepository = new ProductRepository($koneksi);

// 1. Handle Form Submission (LOGIC)
// Cek apakah user telah mengklik tombol submit
if (isset($_POST['submit'])) {
    // Ambil data dari form
    $nama = $_POST['nama'];
    $harga = $_POST['harga'];
    $kategori = $_POST['kategori'];
    $gambar = null;

    // 2. Handle File Upload
    // Cek apakah ada file gambar yang diupload
    if (!empty($_FILES['gambar']['name'])) {
        $gambar = time() . "_" . $_FILES['gambar']['name']; // Beri nama unik dengan timestamp
        move_uploaded_file($_FILES['gambar']['tmp_name'], "../uploads/" . $gambar); // Pindahkan file ke folder uploads
    }

    // 3. Create Object
    // Buat object Product baru dengan data dari form
    $newProduct = new Product($nama, $harga, $kategori, $gambar);

    // 4. Save to Database
    // Gunakan Repository untuk menyimpan object ke database
    if ($productRepository->create($newProduct)) {
        echo "<script>alert('Produk Ditambahkan'); window.location='../index.php';</script>";
    } else {
        echo "<script>alert('Gagal menambahkan produk');</script>";
    }
}

// 5. Load View (PRESENTATION)
// Tampilkan form HTML kepada user
require_once "../views/add_product.php";
?>