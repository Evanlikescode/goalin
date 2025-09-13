
# GOALIN ⚽
Goalin adalah web aplikasi yang berfungsi sebagai tempat penjualan perlengkapan sepak bola. Latar belakang pemilihan nama didasari dengan kata "goal" yang selalu diteriakkan oleh para supporter ketika tim andalannya mencetak poin. Maka dari itu, sebagai pengembang dari toko ini, saya ingin menghadirkan energi positif kepada teman-teman pecinta bola bahwa kita selalu memiliki harapan dan hal itu dapat dimulai dengan mempersiapkan berbagai perlengkapan penting sebelum melakukan sesuatu, termasuk bermain bola.




# Dokumentasi Pengembangan
## DOKUMENTASI TUGAS 2
- Setup proyek dengan menginisiasi environment folder sebagai tempat menyimpan package dari proyek
- Inisiasi git pada proyek aplikasi dan melakukan remote terhadap repository yang sudah dibuat di github dengan branch master
- Membuat .gitignore file untuk mencegah sensitive files / folder, seperti .env dan folder env ikut ter-upload ke dalam repo
- Aktivasi env folder dan melakukan instalasi beberapa package (django, python-dotenv, gunicorn, dkk) yang terdapat di requirements.txt
- Melakukan running "django-admin startproject <nama_project> ." sebagai pembuatan project django dan panel admin yang akan digunakan kelak
- Inisiasi .env dan .env.prod files untuk konfigurasi environment variables, seperti database dan status production
- Modifikasi settings.py untuk melakukan pembacaan .env dan .env.prod files pada aplikasi
- Modifikasi allowed_hosts pada settings.py dengan menambahkan host lokal sehingga aplikasi dapat dijalankan pada browser secara lokal
- Modifikasi pengaturan penggunaan database ketika production berstatus True dan False. Ketika True akan menggunakan database postgresql kampus dan False akan menggunakan sqlite yang sudah terdefinisikan pada proyek
- Menjalankan command 'python3 manage.py startapp main' untuk inisiasi directory aplikasi main
- Modifikasi INSTALLED_APPS di settings.py untuk menambahkan 'main' sebagai directory yang akan ikut serta dalam pengembangan proyek
- Modifikasi urlpatterns pada urls.py di folder goalin_app dengan menambahkan parent url dari directory main (konteks di sini digunakan sebagai tampilan utama dari aplikasi web sehingga path(''))
- Membuat folder templates pada folder main dan menginisiasi file layout.html dan landing_page.html. Di sini, layout.html berfungsi sebagai pondasi layouting setiap html file yang akan dibuat pada proyek ini. Lalu, pendukung layouting, CDN bootstrap 5.3 diikutsertakan. Kemudian, landing_page adalah html file yang berfungsi sebagai tampilan utama web aplikasi dengan melakukan extend terhadap file layout.html.
- Modifikasi views.py di folder main dengan menambahkan function yang akan melakukan rendering terhadap landing_page.html dan mengirimkan context data yang akan ditampilkan pada landing_page.html
- Modifikasi urls.py di folder main dengan menambahkan path untuk function landing_page sehingga fungsi tersebut terdaftar dalam routing aplikasi main 
- Melakukan pembuatan tabel Product pada models.py di folder main dengan kolom-kolom utamanya adalah "name, price, description, thumbnail, category, is_featured" dan tambahan kolom "stock" sebagai data stok dari produk, "created_at" sebagai log datetime pembuatan produk, serta "updated_at" sebagai log datetime suatu produk mengalami perubahan. Lalu, menambahkan function "__str__" yang merepresentasikan string dari setiap objek dari Product
- Menjalankan perintah "python3 manage.py makemigrations" untuk membuat berkas migrasi yang nantinya akan dieksekusi
- Menjalankan perintah "python3 manage.py migrate" untuk memerintah django melakukan query terhadap config yang sudah disimpan dalam berkas migrasi dan mengaplikasikannya ke database
- Setelah itu, hal selanjutnya adalah konfigurasi proyek pada pws dengan melakukan penambahan project pada web pws, pengisian environment variables, dan penambahan remote repository pada git proyek. Kemudian, semua kode yang sudah dibuat di-push ke repository PWS sehingga nantinya proyek dapat diakses melalui jaringan internet (bukan localhost lagi). Lalu, juga menambahkan url pws di allowed host pada settings.py agar aplikasi dapat dijalankan.

## DOKUMENTASI TUGAS 3
- Mengubah layout.html tidak lagi terletak di main directory, tetapi dipindahkan ke project directory dengan membuat folder templates pada directory tersebut
- Modifikasi variabel TEMPLATES pada settings.py dengan menambahkan BASE_DIR / 'templates' di key 'DIRS' sehingga folder templates pada project directory dapat terbaca dan file layout.html dapat dijadikan base layout ketika ada file html pada setiap aplikasi meng-extend
- Modifikasi layout.html dengan melakukan include navbar.html sehingga di setiap page akan tertera navbar dan mengubah body color menjadi aliceblue
- Modifikasi main/templages/landing_page.html untuk menambahkan card yang akan ditampilkan ketika ada product featured. Lalu, juga menambahkan button yang href ke "main:create_product" untuk redirect ke halaman pembuatan product
- Menambahkan csrf trusted origin pada settings.py untuk link pws sehingga nantinya web app yang berjalan secara online di pws dapat melakukan request csrf token
- Membuat file forms.py pada main directory untuk membuat meta data form berdasarkan informasi / field yang ada di models
- Modifikasi main/views.py dengan menambahkan fungsi create_product (sebagai fungsi yang mengatasi permasalahan pembuatan produk) dan show_product (sebagai fungsi yang mengatasi penampilan produk keseluruhan dan by id)
- Modifikasi create_product.html (html untuk create_product), show_product.html (html untuk show_product dengan get all product), more_product (html untuk show_product dengan get product by id). Lalu, untuk more_product ditambahkan button yang href ke "main:show_product" untuk redirect ke halaman show product
- Modifikasi main/urls.py untuk menambahkan url pada create_product, show_product (all), dan show_product (by id)
- Modifikasi main/views.py kembali untuk menambahkan fungsi penampilan produk dalam json dan xml format; show_product_json -> show produk keseluruhan dan by id dengan json format, show_product_xml -> show produk keseluruhan dan by id dengan xml format
- Modifikasi main/urls.py kembali untuk menambahkan path terhadap json dan xml format untuk penampilan data produk.
- Implementasi penampilan produk secara keseluruhan dan by id, saya lakukan dalam satu fungsi dengan menambahkan default None pada parameter id dan ketika ada id yang ditulis akan mengembalikan data sesuai id dari produk secara khusus
# Penjelasan Bagan
Berikut link untuk bagan yang telah saya buat:
https://ristek.link/bagan_ehw

Penjelasan:
- User akan mengirimkan request http ke web aplikasi. Lalu, web aplikasi akan menerima request melalui urls.py parent directory
- Endpoint awal yang ditemukan akan diteruskan menuju urls.py dari app directory, sedangkan yang tidak ditemukan akan diteruskan dengan pesan 404 Not Found
- Endpoint awal yang ditemukan sebelumnya ketika diteruskan menuju urls.py dari app directory akan dicek endpoint childnya. Jika terdaftar, akan diteruskan ke fungsi yang menaunginya di views.py. Namun, web akan mengirimkan 404 Not Found kembali ketika endpoint child tidak ditemukan
- Endpoint child yang sebelumnya sudah terdaftar, ketika dikirim ke views.py, akan mengecek kebutuhan akses atau tidak ke models.py di app directory. Jika membutuhkan, maka request dikirimkan ke models.py dan views.py menerima hasil transaksi basis data tersebut. Namun, ketika tidak membutuhkan, proses langsung menjalani rendering html.
- Rendering html akan terjadi ketika filepath html yang berada pada fungsi di views.py itu exist (ada) di folder app/templates. Jika tidak, akan diteruskan dengan pesan 500 server error.
# Peran settings.py 
Settings.py merupakan file krusial yang mengatur berbagai konfigurasi dari proyek Django untuk dapat dijalankan sebagaimana mestinya. Pengaturan itu, meliputi

- Konfigurasi basis data: di file ini akan disimpan berbagai informasi untuk koneksi ke engine database. Lalu, di sini juga mengatur bagaimana penggunaan basis data di proyek Django (apakah seterusnya menggunakan database yang sama atau bisa ada 2 / lebih database berbeda)
- Pengaturan INSTALLED_APPS: setiap kali ada perintah, seperti 'python3 manage.py startapp <nama_aplikasi>', nama aplikasi harus didaftarkan di file ini sehingga proyek Django akan mengenalinya dan mengeksekusi. Hal tersebut berlaku untuk setiap aplikasi yang dibuat programmer ataupun bawaan Django-nya.
- Konfigurasi middleware: banyak hal di belakang layar sudah di-handle oleh Django. Contohnya adalah middleware untuk mengetahui apakah user sudah login atau belum. Maka, settings.py berfungsi sebagai tempat penyimpanan berbagai middleware yang sebelumnya telah ada di Django ataupun yang akan kita buat sendiri.
- Pengaturan lokasi templates dan static files: berbagai file html dan css sudah terkonfigurasi nama folder penyimpanannya dan informasi mengenai bagaimana Django mengetahuinya disimpan juga di settings.py
- Konfigurasi sistem keamanan: Django memiliki kecanggihan dalam menjaga proyeknya secara internal ataupun eksternal. Oleh sebab itu, framework ini mewajibkan setiap penggunanya untuk mendaftarkan host yang dapat mengakses proyek dan kerangka juga melibatkan kita mengatur berbagai sistem keamanan lainnya, seperti apakah setiap saat DEBUG dan PRODUCTION aplikasi terus berjalan atau tidak.
- Pengaturan Zona Waktu: Django juga telah menyediakan konfigurasi untuk penggunaan zona waktu pada proyek kita di settings.py sehingga kita dapat menyesuaikannya sesuai yang kita inginkan.


# Cara kerja migrasi database di Django

- Langkah pertama: membuat struktur tabel yang diinginkan di models.py
- Langkah kedua: jalankan perintah "python3 manage.py makemigrations"
- Langkah ketiga: jalankan perintah "python3 manage.py migrate"

Langkah-langkah di atas terlihat begitu mudah dan cukup simpel untuk dilakukan. Namun, di belakang layar, Django melakukan beberapa langkah untuk memastikan proses ini berjalan lancar.

Maka, proses itu adalah

- Ketika perintah "python3 manage.py makemigrations" berjalan, django akan membaca dan melakukan perbandingan antara models.py dengan file migration sebelumnya (jika sudah ada) serta membentuk file baru yang berisi instruksi-instruksi python untuk melakukan pembuatan atau pengubahan tabel. File ini terletak pada folder migrations yang ada di app directory.
- Kemudian, ketika perintah "python3 manage.py migrate" dieksekusi, django akan membaca migration file yang ada di folder migrations itu dan mengubah setiap instruksi dari python ke query database yang dipakai pengembang aplikasi. Contohnya, jika menggunakan mysql, maka instruksi python yang ada di file migration akan diubah ke query mysql. Setelah itu, query dijalankan di engine database dan tabel yang didefinisikan sebelumnya di models.py terbentuk di basis data.
# Kenapa Django?
Django adalah kerangka / framework web berbasis bahasa pemrograman Python yang menggunakan arstiektur MVT (model - view - template). Kerangka ini dikenal dengan pendekatan batteries included yang artinya ia sudah dilengkapi dengan berbagai fitur bawaan fundamental, seperti ORM, sistem template, dan lainnya. Maka, tidak salah jika dikatakan bahwa Django dapat menjadi opsi untuk mengembangkan sebuah aplikasi web dengan cepat dan efisien secara waktu. 

Alasan framework ini digunakan sebagai permulaan pembelajaran pengembangan perangkat lunak adalah karena,
- mahasiswa fasilkom angkatan 2024 memulai pembelajaran bahasa pemrograman dengan bahasa python sehingga hal tersebut secara gamblang dapat memperlihatkan kegunaan mempelajari bahasa tersebut pada real-case (situasi. sebenarnya)
- django adalah framework besar dan hal itu dapat dijadikan acuan untuk mempelajari framework lainnya, seperti laravel, springboot, nestjs, dan lain-lain karena sebagian besar framework serupa memiliki arsitektur MVC/MVT
- django tidak hanya mengajarkan sisi frontend atau backend saja, tetapi dapat mengajarkan keduanya dalam satu waktu (fullstack web development). Hal tersebut akhirnya memberikan gambaran kepada mahasiswa mengenai pengembangan web secara garis besar seperti apa dan cara membuat web aplikasi itu bagaimana prosesnya.
# Fungsi Data Delivery
Menurut saya, web development bukan hanya tentang satu pondasi yang didirikan untuk dirinya sendiri. Banyak kasus dari pengembangan web juga menopang berbagai aplikasi. Sebagai contoh, sistem backend, frontend, dan mobile-app memiliki servisnya masing-masing. Lalu, semisal semua data berasal dari backend yang sama. Maka, frontend dan mobile-app yang tidak dapat mengakses data secara langsung ke suatu database yang dibawahi oleh backend membutuhkan suatu format untuk diaksesnya atau yang sering dikenal dengan API (Application Programming Interface). Dari hal tersebut, fungsi data delivery adalah
 - memungkinkan setiap sistem berkomunikasi secara mudah dan cepat
 - data terintegrasi pada setiap servis 
 - data yang diberikan dan didapat sesuai versi yang sama.
Data delivery ini biasanya disajikan dengan format JSON atau XML.

# JSON vs XML
Sebelumnya, kita sudah membahas fungsi dari data delivery. Sekarang, kita akan membandingkan format data delivery yang lebih baik dan alasan JSON lebih populer dibandingkan XML.

Javascript Object Notation atau yang dikenal dengan JSON adalah format yang digunakan untuk penyimpanan dan pengiriman data berbasis key dan value.
Format ini lebih mudah dibaca manusia karena tingkat kompleksitasnya yang tidak terlalu tinggi.

Extensible Markup Language atau XML adalah format yang berfungsi sama, seperti JSON, tetapi berbasis struktur tree. Format ini mungkin lebih sulit atau butuh ketelitian lebih untuk membacanya karena adanya struktur hirarki pada setiap data dan semua tag xml terdapat pembuka dan penutupnya. Namun, format ini dapat menyimpan data yang lebih kompleks secara strukturnya (tidak terbatas pada penyimpanan, seperti array, string atau integer biasa).

Keduanya memiliki kelebihan dan kekurangannya tersendiri, tetapi bagi saya sendiri JSON lebih baik ketika digunakan dalam konteks API. Alasannya karena untuk melakukan proses fetching lebih mudah, proses pembacaan setiap data pun lebih nyaman di mata, dan strukturnya cenderung familiar dengan python dictionary.

JSON sendiri lebih populer dari XML karena kelebihan-kelebihan yang sudah saya sampaikan sebelumnya. Kemudian, JSON memiliki ukuran file yang lebih kecil, parsing data lebih cepat, dan jauh lebih aman daripada XML yang cukup rentan terhadap XXE injection. Selanjutnya, JSON digunakan secara intens pada pengembangan API dan XML pada dokumen konfigurasi.

# Fungsi is_valid
Pada proses penyimpanan data dari form menuju database, django menggunakan fungsi is_valid() untuk proses validasi. Method ini akan melakukan pengecekan terkait kebenaran data yang akan diinputkan ke dalam setiap fields database yang akan diisi. Hal yang dicek adalah tipe data, panjang karakter, required field, dan validasi lainnya yang diwajibkan pada struktur kolom. Jika data yang diinput sudah sesuai dengan struktur kolom database, maka fungsi akan mengembalikan nilai True dan False ketika masih terdapat kesalahan.

# Kegunaan CSRF
Token CSRF sangat krusial dalam pengimplementasiannya. Tanpa token ini, suatu web akan sering menjumpai kerentanan sekuritas terhadap request akan suatu form. Misalnya, terdapat seorang user yang meninggalkan session di suatu web bank dan ia tidak sengaja mengakses web aneh yang dibuat seorang hacker untuk mengakses web bank milik targetnya itu. Tanpa adanya csrf token, hacker dengan mudah melakukan request terhadap suatu form karena form tidak memvalidasi apapun selain penerimaan request dan session. Alhasil, hacker berhasil melakukan hal yang ia inginkan dengan menggunakan kredensial user tersebut.

Django sendiri sudah mewajibkan setiap pengembang untuk mengikutsertakan csrf token pada proses form input. Hal ini digunakan untuk sistem web melakukan validasi terhadap host yang mengakses form. Django dengan ini juga telah mewajibkan para pengembang untuk mendaftarkan setiap url / host yang dapat meminta request token sehingga di luar host yang terdaftar, suatu form tidak dapat dieksekusi (meskipun sudah mendapatkan session/cookies).

Cara kerja csrf token di django sendiri adalah
 - Token di-generate dan disisipkan pada form request
 - Form yang dikirimkan oleh user, token csrfnya akan divalidasi oleh middleware Django
 - Jika tokennya sesuai dan hostnya sudah terdaftar di konfigurasi project directory, form akan dieksekusi berhasil.

Maka dari itu, form di Django yang tidak menerapkan atau melibatkan csrf token, secara otomatis akan mendapatkan pesan error dengan himbauan wajib menerapkan csrf token.
# Feedback untuk asisten dosen
## Tutorial 1
Sejauh ini, tutorial sangat membantu saya dalam mempelajari framework Django karena penjelasannya sangat detail dan mudah dipahami. Saran saya ke depan adalah tetap dipertahankan dalam pemberian tutorial, seperti kemarin dan tidak lupa untuk selalu memberikan kesempatan kepada para mahasiswa ketika ingin memperdalam suatu hal berkaitan dengan django ataupun web development. Terima kasih sudah selalu hadir dan fast-response, tim Asdos PBP! 🚀

## Tutorial 2
Tutorial kemarin sudah sangat baik. Dokumentasi pembelajaran yang diberikan mudah dipahami. Saya semakin salut dengan semua yang sudah disiapkan oleh tim Asdos PBP. Maka dari itu, saya mengucapkan terima kasih yang sebesar-besarnya.

# Screenshot POSTMAN
## Fetch All Products (JSON)
- https://drive.google.com/file/d/1-KwJpqqiOVE2gzpKciVWkI6fDUp112rV/view?usp=sharing
## Fetch All Products (XML)
- https://drive.google.com/file/d/14PX8pvljL6fw9CNqz0evmgfD5B_wlbVh/view?usp=drive_link
## Fetch Products By ID (JSON)
- https://drive.google.com/file/d/1XkrYqsFp5lAuMWoPjA9pnMauBvZTnuOB/view?usp=drive_link
## Fetch Products By ID (XML)
- https://drive.google.com/file/d/1u3-R4_-55jxxoU8pN8cGD4REFcpRY9No/view?usp=drive_link

# References
- https://aws.amazon.com/compare/the-difference-between-json-xml/
- https://docs.djangoproject.com/en/5.2/ref/csrf/
- https://www.geeksforgeeks.org/html/difference-between-json-and-xml/
- https://owasp.org/www-community/attacks/csrf#overview
