<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $pageTitle ?> - Tokokita</title>
    
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
</head>
<body class="bg-gray-50 font-sans text-gray-800 antialiased flex flex-col min-h-screen">

    <!-- Navbar -->
    <?php include 'views/partials/navbar.php'; ?>

    <!-- Page Header -->
    <div class="bg-white shadow-sm py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-3xl font-extrabold text-gray-900 sm:text-4xl">
                <?= $pageTitle ?>
            </h1>
            <p class="mt-4 text-lg text-gray-500">
                <?= $pageDescription ?>
            </p>
        </div>
    </div>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 flex-grow w-full">
        
        <!-- Product Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
            <?php foreach ($products as $product) : ?>
            <div class="group bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 overflow-hidden flex flex-col h-full">
                <!-- Image Container -->
                <div class="relative aspect-[4/3] overflow-hidden bg-gray-100">
                    <div class="w-full h-full flex items-center justify-center text-gray-300 bg-gray-200">
                        <img src="<?= htmlspecialchars($product->gambar) ?>" alt="<?= htmlspecialchars($product->nama) ?>" class="w-full h-full object-cover">
                    </div>
                    
                    <!-- Badge -->
                    <div class="absolute top-3 left-3">
                        <span class="bg-primary/90 backdrop-blur-sm text-white text-xs font-bold px-2 py-1 rounded-md shadow-sm uppercase tracking-wider">New Arrival</span>
                    </div>
                </div>

                <!-- Content -->
                <div class="p-5 flex flex-col flex-grow">
                    <div class="text-xs text-gray-500 mb-1 uppercase tracking-wide font-semibold">
                        <?= htmlspecialchars($product->kategori) ?>
                    </div>
                    <h3 class="text-lg font-bold text-gray-900 mb-2 line-clamp-2 group-hover:text-primary transition-colors">
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

    </main>

    <!-- Footer -->
    <?php include 'views/partials/footer.php'; ?>

</body>
</html>
