<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product - Tokokita</title>
    
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
<body class="bg-gray-50 font-sans text-gray-800 antialiased">
    
    <?php $path_prefix = '../'; include '../views/partials/navbar.php'; ?>

    <div class="min-h-screen flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md">
            <div class="flex justify-center">
                <div class="w-12 h-12 bg-primary rounded-xl flex items-center justify-center text-white text-2xl">
                    <i class="fas fa-shopping-bag"></i>
                </div>
            </div>
            <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
                Add New Product
            </h2>
            <p class="mt-2 text-center text-sm text-gray-600">
                Or
                <a href="../index.php" class="font-medium text-primary hover:text-emerald-500">
                    return to dashboard
                </a>
            </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10 border border-gray-100">
                <form method="POST" enctype="multipart/form-data" class="space-y-6">
                    
                    <!-- Nama Produk -->
                    <div>
                        <label for="nama_produk" class="block text-sm font-medium text-gray-700">
                            Product Name
                        </label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <i class="fas fa-box text-gray-400"></i>
                            </div>
                            <input type="text" name="nama" id="nama_produk" required class="focus:ring-primary focus:border-primary block w-full pl-10 sm:text-sm border-gray-300 rounded-md py-2 border" placeholder="e.g. Wireless Headphones">
                        </div>
                    </div>

                    <!-- Harga Produk -->
                    <div>
                        <label for="harga_produk" class="block text-sm font-medium text-gray-700">
                            Price
                        </label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <span class="text-gray-500 sm:text-sm">Rp</span>
                            </div>
                            <input type="number" name="harga" id="harga_produk" min="0" required class="focus:ring-primary focus:border-primary block w-full pl-12 sm:text-sm border-gray-300 rounded-md py-2 border" placeholder="0">
                        </div>
                    </div>

                    <!-- Kategori -->
                    <div>
                        <label for="kategori_produk" class="block text-sm font-medium text-gray-700">
                            Category
                        </label>
                        <div class="mt-1 relative rounded-md shadow-sm">
                            <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                                <i class="fas fa-tag text-gray-400"></i>
                            </div>
                            <input type="text" name="kategori" id="kategori_produk" required class="focus:ring-primary focus:border-primary block w-full pl-10 sm:text-sm border-gray-300 rounded-md py-2 border" placeholder="e.g. Electronics">
                        </div>
                    </div>

                    <!-- Gambar Produk -->
                    <div>
                        <label class="block text-sm font-medium text-gray-700">
                            Product Image
                        </label>
                        <div class="mt-1 flex justify-center px-6 pt-5 pb-6 border-2 border-gray-300 border-dashed rounded-md hover:border-primary transition-colors cursor-pointer" onclick="document.getElementById('gambar_produk').click()">
                            <div class="space-y-1 text-center">
                                <i class="fas fa-cloud-upload-alt text-4xl text-gray-400 mb-3"></i>
                                <div class="flex text-sm text-gray-600 justify-center">
                                    <label for="gambar_produk" class="relative cursor-pointer bg-white rounded-md font-medium text-primary hover:text-emerald-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-primary">
                                        <span>Upload a file</span>
                                        <input id="gambar_produk" name="gambar" type="file" class="sr-only" accept="image/*" onchange="previewImage(this)">
                                    </label>
                                    <p class="pl-1">or drag and drop</p>
                                </div>
                                <p class="text-xs text-gray-500">
                                    PNG, JPG, GIF up to 10MB
                                </p>
                            </div>
                        </div>
                        <!-- Preview -->
                        <div id="imagePreview" class="mt-4 hidden">
                            <p class="text-sm text-gray-500 mb-2">Preview:</p>
                            <img id="preview" class="h-32 w-auto rounded-lg shadow-sm border border-gray-200 object-cover">
                        </div>
                    </div>

                    <div class="flex items-center gap-4 pt-4">
                        <button type="submit" name="submit" class="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-primary hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary transition">
                            Save Product
                        </button>
                        <a href="../index.php" class="w-full flex justify-center py-2 px-4 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary transition">
                            Cancel
                        </a>
                    </div>

                </form>
            </div>
        </div>
    </div>
    
    <?php include '../views/partials/footer.php'; ?>

    <script>
        function previewImage(input) {
            const preview = document.getElementById('preview');
            const previewContainer = document.getElementById('imagePreview');
            
            if (input.files && input.files[0]) {
                const reader = new FileReader();
                
                reader.onload = function(e) {
                    preview.src = e.target.result;
                    previewContainer.classList.remove('hidden');
                };
                
                reader.readAsDataURL(input.files[0]);
            } else {
                previewContainer.classList.add('hidden');
            }
        }
    </script>

</body>
</html>
