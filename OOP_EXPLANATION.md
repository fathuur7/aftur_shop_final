# Penjelasan Implementasi OOP di Aftur Shop

Dokumen ini menjelaskan mengapa bagian-bagian tertentu dalam kode disebut sebagai penerapan konsep Object-Oriented Programming (OOP).

## 1. Class (Kelas)
**Konsep**: Blueprint atau cetakan untuk membuat objek.
**Implementasi**: `class Product` (di `classes/Product.php`) dan `class ProductRepository` (di `classes/ProductRepository.php`).
**Penjelasan**:
Kode diawali dengan keyword `class`. Ini mendefinisikan struktur data (properti seperti `$nama`, `$harga`) dan perilaku (method seperti `getId()`, `getAll()`) yang akan dimiliki oleh objek yang dibuat dari kelas ini. Ini belum berupa data nyata, baru sebatas definisi.

## 2. Object (Objek)
**Konsep**: Bentuk nyata (instansi) dari sebuah Class.
**Implementasi**: `$product = new Product(...)` (di `classes/ProductRepository.php` baris 23).
**Penjelasan**:
Ketika keyword `new` digunakan, PHP mencetak satu unit "barang jadi" berdasarkan cetakan `class Product`. Variabel `$product` di sini memegang data nyata (misalnya: "Sepatu", "Rp 50000") yang diambil dari database. Jika ada 10 baris di database, akan ada 10 *object* `$product` yang berbeda di memori.

## 3. Encapsulation (Enkapsulasi)
**Konsep**: Membungkus data dan membatasi akses langsung dari luar untuk keamanan/integritas.
**Implementasi**: `private $db;` (di `classes/ProductRepository.php` baris 7).
**Penjelasan**:
Properti `$db` diberi visibilitas `private`. Artinya, kode di luar class `ProductRepository` (misalnya di `index.php`) tidak bisa langsung menulis `$repo->db = null;`. Ini melindungi koneksi database agar tidak rusak atau diubah sembarangan oleh bagian kode lain. Akses ke `$db` hanya bisa dilakukan oleh method di dalam class itu sendiri.

## 4. Inheritance (Pewarisan)
**Konsep**: Sebuah class (Anak) mengambil alih properti dan method dari class lain (Induk).
**Implementasi**: `class Product extends ProductPrototype` (di `classes/Product.php` baris 4).
**Penjelasan**:
Dengan kata kunci `extends`, class `Product` otomatis memiliki semua properti yang didefinisikan di `ProductPrototype` (`$nama`, `$harga`, `$kategori`, `$gambar`). Kita tidak perlu menulis ulang properti tersebut di `Product`. Ini mengurangi duplikasi kode.

## 5. Polymorphism (Polimorfisme)
**Konsep**: Satu nama method yang sama memiliki perilaku yang berbeda (bisa lewat Overloading atau Overriding).
**Implementasi**: Method `__clone()` di `classes/Product.php` (baris 26).
**Penjelasan**:
Di class induk (`ProductPrototype`), `__clone()` didefinisikan sebagai `abstract` (hanya kerangka). Di class anak (`Product`), kita menulis ulang (override) method tersebut dengan logika spesifik: `$this->nama .= " (Copy)";`.
Meskipun namanya sama-sama `__clone`, implementasinya bisa berbeda-beda tergantung class anaknya. Inilah polimorfisme (banyak bentuk).

## 6. Abstraction (Abstraksi)
**Konsep**: Menyembunyikan detail implementasi yang kompleks dan hanya menampilkan kerangka luarnya saja.
**Implementasi**: `abstract class ProductPrototype` (di `classes/ProductPrototype.php` baris 2).
**Penjelasan**:
Class ini diberi label `abstract`. Artinya, class ini **tidak boleh** dibuat objeknya secara langsung (`new ProductPrototype` akan error). Ia hanya berfungsi sebagai konsep abstrak "Produk Dasar" yang harus diperjelas lagi oleh class turunannya. Ini memaksa programmer lain untuk mengikuti struktur yang sudah ditetapkan tanpa perlu tahu detail internalnya di awal.
