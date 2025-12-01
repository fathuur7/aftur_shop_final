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
        <div class="max-w-3xl mx-auto space-y-6">
            
            <!-- FAQ Item -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
                <h3 class="text-lg font-bold text-gray-900 mb-2">How do I track my order?</h3>
                <p class="text-gray-600">You can track your order by logging into your account and visiting the "My Orders" section.</p>
            </div>

            <!-- FAQ Item -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
                <h3 class="text-lg font-bold text-gray-900 mb-2">What is your return policy?</h3>
                <p class="text-gray-600">We offer a 30-day return policy for all unused items in their original packaging.</p>
            </div>

            <!-- FAQ Item -->
            <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
                <h3 class="text-lg font-bold text-gray-900 mb-2">Do you ship internationally?</h3>
                <p class="text-gray-600">Yes, we ship to select countries worldwide. Shipping costs will be calculated at checkout.</p>
            </div>

        </div>
    </main>

    <!-- Footer -->
    <?php include 'views/partials/footer.php'; ?>

</body>
</html>
