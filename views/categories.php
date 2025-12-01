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
        
        <!-- Category Grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
            <?php foreach ($categories as $category) : ?>
            <a href="#" class="group bg-white rounded-2xl shadow-sm hover:shadow-xl transition-all duration-300 border border-gray-100 p-8 flex items-center gap-6 hover:-translate-y-1">
                <div class="w-16 h-16 bg-emerald-50 text-primary rounded-xl flex items-center justify-center text-3xl group-hover:bg-primary group-hover:text-white transition-colors duration-300">
                    <i class="fas <?= htmlspecialchars($category->icon) ?>"></i>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-gray-900 group-hover:text-primary transition-colors">
                        <?= htmlspecialchars($category->nama) ?>
                    </h3>
                    <p class="text-gray-500 mt-1">
                        <?= $category->count ?> Products
                    </p>
                </div>
                <div class="ml-auto text-gray-300 group-hover:text-primary transition-colors">
                    <i class="fas fa-chevron-right"></i>
                </div>
            </a>
            <?php endforeach; ?>
        </div>

    </main>

    <!-- Footer -->
    <?php include 'views/partials/footer.php'; ?>

</body>
</html>
