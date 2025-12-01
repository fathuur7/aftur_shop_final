<?php
/**
 * ===========================
 * AFTUR SHOP - CATEGORIES CONTROLLER
 * ===========================
 */

// Mock Data for Categories
$categories = [
    (object)[
        'id' => 1,
        'nama' => 'Electronics',
        'icon' => 'fa-laptop',
        'count' => 120
    ],
    (object)[
        'id' => 2,
        'nama' => 'Fashion',
        'icon' => 'fa-tshirt',
        'count' => 85
    ],
    (object)[
        'id' => 3,
        'nama' => 'Home & Living',
        'icon' => 'fa-couch',
        'count' => 64
    ],
    (object)[
        'id' => 4,
        'nama' => 'Beauty',
        'icon' => 'fa-spa',
        'count' => 42
    ],
    (object)[
        'id' => 5,
        'nama' => 'Sports',
        'icon' => 'fa-running',
        'count' => 38
    ],
    (object)[
        'id' => 6,
        'nama' => 'Books',
        'icon' => 'fa-book',
        'count' => 95
    ]
];

$pageTitle = "Categories";
$pageDescription = "Browse products by category.";

require_once "./views/categories.php";
?>
