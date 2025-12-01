<?php
// (Abstraction) Penyederhanaan objek, tidak bisa buat product langsung, hanya bisa diturunkan.
abstract class ProductPrototype
{
    public $nama;
    public $harga;
    public $kategori;
    public $gambar;

    abstract public function __clone();
}