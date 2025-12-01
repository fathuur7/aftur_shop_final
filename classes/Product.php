<?php
require_once "ProductPrototype.php";

// [Class] Blueprint/kerangka untuk membuat objek Product
// [Inheritance] Pewarisan sifat. Product (Anak) mewarisi properti & method dari ProductPrototype (Induk)
class Product extends ProductPrototype
{
    public $id;

    public function __construct($nama, $harga, $kategori, $gambar)
    {
        $this->nama = $nama;
        $this->harga = $harga;
        $this->kategori = $kategori;
        $this->gambar = $gambar;
    }

    public function setId($id)
    {
        $this->id = $id;
    }

    public function getId()
    {
        return $this->id;
    }

    // [Polymorphism] Kemampuan method memiliki bentuk berbeda.
    // Ini adalah Overriding: mendefinisikan ulang method __clone dari parent class
    public function __clone()
    {
        $this->nama .= " (Copy)";
        // gambar tetap sama
    }
}