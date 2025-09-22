
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

## DOKUMENTASI TUGAS 4
- Modifikasi main/views.py dengan menambahkan fungsi registrasi, login, dan logout.
- Fungsi registrasi menggunakan UserCreationForm untuk form pembuatan usernya; Fungsi login menggunakan AuthenticationForm untuk loginnya; Login dan logout akan menggunakan HttpResponseRedirect sebagai redirect page modulenya. Lalu, ada juga penambahan implementasi cookie yang menyimpan waktu last login dan akan dihapus ketika logout
- Modifikasi main/models.py dengan menambahkan column user pada tabel Product sebagai foreign key yang akan menghubungkan antara tabel User dan Product
- Modifikasi fungsi create_product dengan menambahkan saving user ke model Product
- Modifikasi show_product dengan menambahkan adanya request query parameter terhadap filter product. "all" untuk semua barang tanpa melakukan pembedaan terhadap owner barang. "my" --> untuk semua barang milik owner yang login saat itu
- Menambahkan decorator @login_required terhadap page landing_page, create_product, show_product, show_product_json, show_product_xml, dan logout_user sehingga halaman ini memerlukan kredensial login terlebih dahulu sebelum diakses/diekseskusi
- Modifikasi main/templates/show_product.html dengan menambahkan adanya button untuk show product all dan my products 
- Modifikasi main/templates/show_product.html, main/templates/more_product.html dan main/templates/landing_page.html untuk menambahkan informasi user terhadap kepemilikan product penjualan
- Modifikasi juga di halaman landing_page.html dengan menambahkan informasi last login
- Modifikasi templates/navbar.html untuk menambahkan href logout pada elemen navbar.
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

# Django AuthenticationForm (Kelebihan dan Kekurangan)
Django AuthenticationForm adalah class bawaan django yang berfungsi untuk melakukan validasi login dengan menerima argumen, seperti request, username, dan password. Form ini digunakan untuk memeriksa apakah username dan password yang di-input user terdapat / sebelumnya tersimpan di sistem autentikasi Django atau tidak.

## Kelebihan
- __Ready to use__. Sistem ini sangat mudah untuk diimplementasikan dengan hanya melakukan import class AuthenticationForm pada aplikasi yang ingin kita gunakan
- __Aman__. Django dengan module ini sudah menerapkan hashing pada form password sehingga tidak perlu khawatir dengan hal penyimpanan password pada basis data
- __Fleksibel__. Authentication form secara gamblang sudah menyiapkan html view sendiri untuk penerapan form ini. Oleh sebab itu, developer yang ingin membuat aplikasi dengan cepat bisa menerapkannya secara cepat.

## Kekurangan
- __View Sederhana__. Meskipun, html view sudah disediakan, tetapi tampilannya sangat sederhana / tidak ada keindahan yang dibantu oleh css
- __Hanya Menerima Username/Password__. Login yang dilakukan hanya dengan field username dan password. Selain kedua itu, tidak bisa diterapkan.
- __Error message terbatas__. Pesan error yang disiapkan hanya pesan default yang biasa digunakan pada web sederhana.

# Perbedaan Autentikasi dan Otorisasi
## Autentikasi
Autentikasi adalah suatu proses yang melakukan verifikasi identitas pengguna ketika masuk ke dalam suatu sistem yang terbatas (restricted). Hal nyata implementasi ini adalah pada proses login berlangsung.

__Salah satu cara menerapkan Autentikasi di Django adalah dengan__ 
- Pengecekan identitas, seperti username dan password yang di-input user dengan fungsi authenticate dan keterlibatan model User di dalamnya.
- Jika authenticate berhasil, maka dengan fungsi login, user akan disimpan informasi pribadinya pada session yang dibuat melalui Django.

## Otorisasi
Otorisasi adalah proses yang melakukan verifikasi terhadap hak akses yang dimiliki oleh user. Hal ini sering ditemukan ketika seseorang hanya dapat mengakses halaman tertentu dengan beberapa kondisi.

__Salah satu cara menerapkan Otorisasi di Django adalah dengan__ 
- Semisal suatu halaman hanya dapat diakses oleh admin / staff, Maka kita dapat menambahkan decorator @staff_member_required(raise_exception=True) pada halaman yang ingin kita restriksi.
- Hal ini diawali dengan import decorator itu dari django.contrib.auth.decorators 
- Raise exception = true ini nantinya akan mengembalikan status http 403 yang mana artinya forbidden access

# Kelebihan dan Kekurangan Session dan Cookies dalam Menyimpan State di Aplikasi Web
## Session
__Kelebihan__
- Lebih aman karena menyimpan data di server / tidak di browser. Pada browser yang disimpan hanya session ID saja.
- Dapat menyimpan data besar atau tidak terbatas hanya beberapa kilobytes.
- Data pada session bisa dipindahkan ke cache, seperti redis atau memcache
__Kekurangan__
- Akses cenderung lebih lambat karena memakan waktu dalam hal akses melalui server
- Tidak bisa diakses oleh client-side secara langsung atau butuh API sendiri dalam hal aksesnya
- Membebankan server karena semakin banyak session yang disimpan, maka memori server pun semakin kecil

## Cookies
__Kelebihan__
- Tidak membebankan server karena disimpan pada browser
- Bisa diakses secara langsung oleh client-side tanpa harus ada perantara, seperti API
- Masa expired cookies dapat diatur sehingga tidak langsung hilang ketika browser ditutup
__Kekurangan__
- Rentan terhadap XSS injection, jika tidak diamankan dengan biak
- Kapasitas terbatas atau hanya 4 KB per cookies
- Mudah dimanipulasi oleh pengguna karena tersimpan pada client-side 

# Penggunaan Cookies Aman Secara Default?
Tanpa ada konfigurasi dengan benar, cookies tergolong sangat rentan dalam hal keamanan karena data yang disimpan dalam browser sehingga manipulasi melalui client-side tidak dapat dipungkiri sering terjadi. Risiko utama yang terjadi adalah XSS injection dengan masalah lain yang mengikutinya, seperti CSRF attack dan session hijacking.

XSS injection terjadi ketika attacker melakukan penyisipan kode javascript yang mengambil isi cookies dari targetnya. Jika ada session ID ataupun csrf token yang disimpan pada cookies, hal ini dapat menambah masalah karena attacker pun bisa melakukan manipulasi terhadap suatu sistem yang rentan dengan session ID atau csrf token tersebut.

Django mengatasi permasalahan XSS ini dengan,
- Melakukan auto escaping di template engine sehingga jika ada script pada html hanya akan tertampil sebagai teks
- Menggunakan is_valid() sehingga attacker gagal melakukan injection xss melalui form yang biasanya sering mereka lakukan karena input data ke suatu form harus sesuai dengan apa yang diharapkan pada fieldnya
- Penambahan CSP middleware sehingga setiap ada script js yang berasal dari sumber tidak dikenal otomatis diblokir / tidak dieksekusi
- Menambahkan status True pada session_cookie_secure dan csrf_cookie_secure sehingga setiap cookie session id dan token csrf yang disimpan melalui cookie hanya dapat dikirim melalui HTTPS protokol
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
