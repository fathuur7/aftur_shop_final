<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tokokita - Premium Marketplace</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        primary: '#10B981', // Emerald 500
                        secondary: '#34D399', // Emerald 400
                        dark: '#1F2937',
                        light: '#F3F4F6'
                    }
                }
            }
        }
    </script>
    <style>
        /* Custom scrollbar for webkit */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94a3b8;
        }
    </style>
</head>
<body class="bg-gray-50 font-sans text-gray-800 antialiased">

    <!-- Navbar -->
    <?php include 'views/partials/navbar.php'; ?>

    <!-- Hero Section -->
    <div class="relative bg-dark overflow-hidden">
        <div class="absolute inset-0">
            <img src="https://images.unsplash.com/photo-1441986300917-64674bd600d8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1950&q=80" alt="Hero Background" class="w-full h-full object-cover opacity-40">
        </div>
        <div class="relative max-w-7xl mx-auto py-24 px-4 sm:px-6 lg:px-8 flex flex-col items-center text-center">
            <h1 class="text-4xl md:text-6xl font-extrabold text-white tracking-tight mb-4">
                End of Season Sale
            </h1>
            <p class="mt-4 text-xl text-gray-200 max-w-2xl mx-auto">
                Save up to 50% on selected items. Don't miss out on these limited-time offers!
            </p>
            <div class="mt-8">
                <a href="#products" class="inline-block bg-primary border border-transparent rounded-md py-3 px-8 text-base font-medium text-white hover:bg-emerald-600 md:text-lg shadow-lg hover:shadow-xl transition transform hover:-translate-y-1">
                    Shop Now
                </a>
            </div>
        </div>
    </div>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12" id="products">
        
        <!-- Section Header -->
        <div class="flex justify-between items-end mb-8">
            <div>
                <h2 class="text-2xl font-bold text-gray-900">Featured Products</h2>
                <p class="text-gray-500 mt-1">Handpicked selection just for you</p>
            </div>
            <div class="hidden sm:flex gap-2">
                <button class="w-8 h-8 rounded-full border border-gray-300 flex items-center justify-center text-gray-500 hover:border-primary hover:text-primary transition"><i class="fas fa-chevron-left"></i></button>
                <button class="w-8 h-8 rounded-full border border-gray-300 flex items-center justify-center text-gray-500 hover:border-primary hover:text-primary transition"><i class="fas fa-chevron-right"></i></button>
            </div>
        </div>

        <!-- Stats (Optional, keeping it subtle) -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-12 hidden">
            <div class="bg-white p-4 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
                <div class="w-12 h-12 bg-blue-50 text-blue-500 rounded-lg flex items-center justify-center text-xl"><i class="fas fa-box"></i></div>
                <div>
                    <div class="text-2xl font-bold text-gray-900"><?= $totalProducts ?></div>
                    <div class="text-xs text-gray-500 uppercase tracking-wide">Products</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl shadow-sm border border-gray-100 flex items-center gap-4">
                <div class="w-12 h-12 bg-purple-50 text-purple-500 rounded-lg flex items-center justify-center text-xl"><i class="fas fa-tags"></i></div>
                <div>
                    <div class="text-2xl font-bold text-gray-900"><?= $totalCategories ?></div>
                    <div class="text-xs text-gray-500 uppercase tracking-wide">Categories</div>
                </div>
            </div>
        </div>

        <!-- Product Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <?php foreach ($products as $product) : ?>
            <div class="product-card group bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 overflow-hidden flex flex-col h-full">
                <!-- Image Container -->
                <div class="relative aspect-[4/3] overflow-hidden bg-gray-100">
                    <?php if (!empty($product->gambar)) : ?>
                        <img src="uploads/<?= htmlspecialchars($product->gambar) ?>" alt="<?= htmlspecialchars($product->nama) ?>" class="w-full h-full object-cover object-center group-hover:scale-110 transition-transform duration-500">
                    <?php else : ?>
                        <div class="w-full h-full flex items-center justify-center text-gray-300">
                            <i class="fas fa-image text-4xl"></i>
                        </div>
                    <?php endif; ?>
                    
                    <!-- Overlay Actions -->
                    <div class="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-3">
                        <a href="app/edit.php?id=<?= $product->id ?>" class="w-10 h-10 bg-white text-gray-800 rounded-full flex items-center justify-center hover:bg-primary hover:text-white transition transform hover:scale-110 shadow-lg" title="Edit">
                            <i class="fas fa-edit"></i>
                        </a>
                        <a href="app/duplicate.php?id=<?= $product->id ?>" class="w-10 h-10 bg-white text-gray-800 rounded-full flex items-center justify-center hover:bg-blue-500 hover:text-white transition transform hover:scale-110 shadow-lg" title="Duplicate">
                            <i class="fas fa-copy"></i>
                        </a>
                        <a href="app/delete.php?id=<?= $product->id ?>" onclick="return confirm('Are you sure?')" class="w-10 h-10 bg-white text-gray-800 rounded-full flex items-center justify-center hover:bg-red-500 hover:text-white transition transform hover:scale-110 shadow-lg" title="Delete">
                            <i class="fas fa-trash"></i>
                        </a>
                    </div>

                    <!-- Badge -->
                    <div class="absolute top-3 left-3">
                        <span class="bg-white/90 backdrop-blur-sm text-xs font-bold px-2 py-1 rounded-md shadow-sm uppercase tracking-wider">New</span>
                    </div>
                </div>

                <!-- Content -->
                <div class="p-5 flex flex-col flex-grow">
                    <div class="text-xs text-gray-500 mb-1 uppercase tracking-wide font-semibold">
                        <?= htmlspecialchars($product->kategori) ?>
                    </div>
                    <h3 class="product-name text-lg font-bold text-gray-900 mb-2 line-clamp-2 group-hover:text-primary transition-colors">
                        <?= htmlspecialchars($product->nama) ?>
                    </h3>
                    <div class="mt-auto flex items-center justify-between">
                        <span class="text-xl font-bold text-gray-900">
                            Rp <?= number_format($product->harga, 0, ',', '.') ?>
                        </span>
                        <button class="w-8 h-8 rounded-full bg-gray-100 text-gray-600 flex items-center justify-center hover:bg-primary hover:text-white transition">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>
                </div>
            </div>
            <?php endforeach; ?>
        </div>

        <!-- Empty State -->
        <?php if (empty($products)) : ?>
        <div class="text-center py-24">
            <div class="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-6 text-gray-400">
                <i class="fas fa-box-open text-4xl"></i>
            </div>
            <h3 class="text-xl font-bold text-gray-900 mb-2">No Products Found</h3>
            <p class="text-gray-500 mb-8">Get started by adding your first product to the store.</p>
            <a href="app/add.php" class="inline-flex items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-emerald-600 shadow-lg transition">
                <i class="fas fa-plus mr-2"></i> Add Product
            </a>
        </div>
        <?php endif; ?>

    </main>

    <!-- Footer -->
    <?php include 'views/partials/footer.php'; ?>

    <script>
    // Live Search Product Filter
    document.getElementById('searchInput').addEventListener('input', function() {
        const keyword = this.value.toLowerCase().trim();
        const cards = document.querySelectorAll('.product-card');

        cards.forEach(card => {
            const name = card.querySelector('.product-name').textContent.toLowerCase();
            const category = card.querySelector('.text-xs.text-gray-500').textContent.toLowerCase();

            // Bisa search berdasarkan nama atau kategori
            const match = name.includes(keyword) || category.includes(keyword);

            card.style.display = match ? 'block' : 'none';
        });
    });
    </script>
</body>
</html>
