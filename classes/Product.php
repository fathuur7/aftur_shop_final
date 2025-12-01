<?php
require_once "ProductPrototype.php";

// (Inheritance) Pewarisan sifat mewarisi properti & method dari ProductPrototype (Induk)
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

    // encapsulation (bungkus data id)
    public function setId($id)
    {
        $this->id = $id;
    }

    public function getId()
    {
        return $this->id;
    }

    // (Polymorphism)Overriding: mendefinisikan ulang method __clone dari parent class
    public function __clone()
    {
        $this->nama .= " (Copy)";
        // gambar tetap sama
    }
}