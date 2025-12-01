<?php

require_once "Product.php";

class ProductRepository
{
    // (Encapsulation) Pembungkusan data. Properti $db di-set private agar tidak bisa diakses/diubah sembarangan dari luar class.
    private $db;

    // Constructor menerima koneksi database
    public function __construct($db)
    {
        $this->db = $db;
    }

    // Mengambil semua data produk dari database
    // Mengembalikan array of Product objects
    public function getAll()
    {
        $products = [];
        $query = mysqli_query($this->db, "SELECT * FROM produk ORDER BY id DESC");
        
        while ($row = mysqli_fetch_assoc($query)) {
            // [Object] Instansi nyata dari Class Product.
            // Data dari database diubah menjadi bentuk Objek.
            $product = new Product(
                $row['nama'],
                $row['harga'],
                $row['kategori'],
                $row['gambar']
            );
            $product->setId($row['id']);
            $products[] = $product;
        }
        return $products;
    }

    // Menghitung total jumlah produk
    public function countProducts()
    {
        $query = mysqli_query($this->db, "SELECT COUNT(*) as total FROM produk");
        $data = mysqli_fetch_assoc($query);
        return $data['total'];
    }

    // Menghitung total kategori unik
    public function countCategories()
    {
        $query = mysqli_query($this->db, "SELECT DISTINCT kategori FROM produk");
        return mysqli_num_rows($query);
    }

    // Mengambil satu produk berdasarkan ID
    public function getById($id)
    {
        $id = (int)$id;
        $query = mysqli_query($this->db, "SELECT * FROM produk WHERE id=$id");
        $row = mysqli_fetch_assoc($query);

        if ($row) {
            $product = new Product(
                $row['nama'],
                $row['harga'],
                $row['kategori'],
                $row['gambar']
            );
            $product->setId($row['id']);
            return $product;
        }

        return null;
    }

    // Menyimpan produk baru ke database
    public function create(Product $product)
    {
        $nama = mysqli_real_escape_string($this->db, $product->nama);
        $harga = (int)$product->harga;
        $kategori = mysqli_real_escape_string($this->db, $product->kategori);
        $gambar = mysqli_real_escape_string($this->db, $product->gambar);

        return mysqli_query($this->db, "INSERT INTO produk (nama, harga, kategori, gambar)
                             VALUES ('$nama', '$harga', '$kategori', '$gambar')");
    }

    // Mengupdate data produk yang sudah ada
    public function update(Product $product)
    {
        $id = (int)$product->id;
        $nama = mysqli_real_escape_string($this->db, $product->nama);
        $harga = (int)$product->harga;
        $kategori = mysqli_real_escape_string($this->db, $product->kategori);
        $gambar = mysqli_real_escape_string($this->db, $product->gambar);

        return mysqli_query($this->db, "UPDATE produk
                             SET nama='$nama', harga='$harga', kategori='$kategori', gambar='$gambar'
                             WHERE id=$id");
    }

    // Menghapus produk berdasarkan ID
    public function delete($id)
    {
        $id = (int)$id;
        
        // Get image to delete file
        $product = $this->getById($id);
        if ($product && $product->gambar && file_exists("../uploads/" . $product->gambar)) {
            unlink("../uploads/" . $product->gambar);
        } else if ($product && $product->gambar && file_exists("uploads/" . $product->gambar)) {
            // Handle path difference if called from root vs app dir
             unlink("uploads/" . $product->gambar);
        }

        return mysqli_query($this->db, "DELETE FROM produk WHERE id=$id");
    }
}
