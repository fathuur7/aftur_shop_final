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
        <div class="max-w-3xl mx-auto bg-white rounded-2xl shadow-sm border border-gray-100 p-8 prose prose-emerald">
            
            <h3>Shipping Policy</h3>
            <p>
                We strive to deliver your orders as quickly as possible. Standard shipping usually takes 3-5 business days.
                Expedited shipping options are available at checkout.
            </p>

            <h3>Returns Policy</h3>
            <p>
                If you are not completely satisfied with your purchase, you may return it within 30 days of receipt.
                Items must be unused and in their original packaging.
            </p>

            <h3>How to Return</h3>
            <ol>
                <li>Log in to your account.</li>
                <li>Go to "My Orders" and select the order you wish to return.</li>
                <li>Follow the instructions to print a return label.</li>
                <li>Drop off the package at the nearest shipping center.</li>
            </ol>

        </div>
    </main>

    <!-- Footer -->
    <?php include 'views/partials/footer.php'; ?>

</body>
</html>
