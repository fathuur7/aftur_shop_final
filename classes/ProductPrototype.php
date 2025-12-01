<?php
// [Abstraction] Penyederhanaan objek. Class ini abstract, jadi tidak bisa di-instansiasi langsung (new ProductPrototype), hanya bisa diturunkan.
abstract class ProductPrototype
{
    public $nama;
    public $harga;
    public $kategori;
    public $gambar;

    abstract public function __clone();
}