# script.rpy

define narrator = Character(None)
define k = Character("Kamu", color="#ffd166")
define m = Character("Mira", color="#7bdff2")
define v = Character("Vesper", color="#ff5d8f")
define old = Character("Penyuluh Tua", color="#d9b3ff")

default hp = 100
default soul = 0
default resolve = 0
default mercy = 0
default despair = 0
default companion = False
default weapon = "Pisau Batu"
default class_name = "Pengembara"

label start:
    scene black
    with fade

    narrator "Kau terbangun di tengah ruang yang tak punya sudut."
    narrator "Di depanku, sebuah kobaran kecil menyala di tengah lautan abu."
    narrator "Suara yang tak pernah benar-benar ada berbisik dari dalam cermin."

    menu:
            "Ksatria Berkarat":
                $ class_name = "Ksatria Berkarat"
                $ hp = 120
                $ resolve += 2
                $ weapon = "Pedang Serpihan Api"

            "Penyihir Kegelapan":
                $ class_name = "Penyihir Kegelapan"
                $ hp = 90
                $ despair += 1
                $ weapon = "Tongkat Cermin"

            "Pengembara Tanpa Nama":
                $ class_name = "Pengembara Tanpa Nama"
                $ hp = 100
                $ mercy += 1
                $ weapon = "Pisau Batu"

    narrator "Kobaran itu menatapmu, bukan sebagai api, tapi sebagai ingatan."
    narrator "Maka, kau menapaki jalan yang menggantung di antara kematian dan keinginan."

    jump intro_gate

label intro_gate:
    scene dungeon
    with fade

    narrator "Di gerbang batu, berdiri seorang perempuan dengan wajah yang bukan wajah."
    m "Aku Mira. Atau mungkin aku hanya sisa kata-kata yang kau pilih untuk diingat."
    k "Aku tidak tahu namaku. Aku hanya tahu aku bangun di sini."
    m "Lalu pilihlah. Kau bisa mengikutiku, atau menyalakan api yang sedang menunggu."

    menu:
        "Ikuti Mira menuju lorong yang berbisik":
            $ mercy += 1
            $ companion = True
            narrator "Kau mengikuti langkah Mira. Setiap sebuah jalan menutup saat kau melewatinya."
            jump shrine

        "Menyalakan api di gerbang":
            $ resolve += 1
            $ soul += 1
            narrator "Api itu menjawab. Cahayanya memotong udara, dan mengungkapkan jejak-jejak makhluk yang menunggu di bawah."
            jump shrine

        "Membunuh bayangan di gerbang itu":
            $ despair += 2
            $ soul += 2
            narrator "Kau menusukkan pedang ke bayangan yang tak berjiwa. Darah yang tak ada menetes ke tanah."
            jump shrine

label shrine:
    scene shrine
    with fade

    old "Di ujung lorong ini, terdapat Cermin Tanpa Ada."
    old "Tak ada yang lahir dari cermin itu. Tak ada yang mati di dalamnya."
    old "Yang tinggal hanyalah pilihan."

    menu:
        "Menyentuh cermin":
            $ soul += 1
            narrator "Cermin itu memantulkanmu, tapi bukan wajahmu. Wajah itu adalah versi dirimu yang tak pernah memilih."
            jump trial

        "Menutup mata dan menghindari cermin":
            $ resolve += 1
            narrator "Kau mengabaikan godaan. Tapi bayanganmu tetap mengikuti dari belakang."
            jump trial

        "Membawa Mira mendekati cermin":
            $ mercy += 1
            $ companion = True
            m "Kalau begitu, kita lihat apa yang benar-benar menunggu di balik rasa takut."
            jump trial

label trial:
    scene boss
    with fade

    narrator "Dari dalam kegelapan, bangkitlah Vesper, Rajakuasa yang tak punya nama."
    v "Kau datang untuk menyelamatkan dunia ini? Atau hanya untuk menolak dunia yang telah menolakmu?"
    menu:
        "Serang Vesper dengan semua kekuatan":
            $ hp -= 25
            $ soul += 2
            if hp <= 0:
                jump ending_hollow
            narrator "Kau menyerang. Pedangmu membelah bayangan. Vesper tertawa saat luka itu menutup sendiri."
            jump judgment

        "Bertahan dan menunggu celah":
            $ resolve += 1
            $ hp += 10
            narrator "Kau tidak menyerang. Kau menunggu. Tiba-tiba Vesper melemah saat dirimu tak memberi ruang baginya."
            jump judgment

        "Menyapa Vesper seperti teman":
            $ mercy += 2
            $ companion = True
            narrator "Kau menurunkan senjata. 'Aku tidak ingin menjadi monster seperti yang kau harapkan.'"
            v "Lalu apa yang kau inginkan?"
            jump judgment

label judgment:
    scene altar
    with fade

    narrator "Di puncak menara berdiri altar api yang menyala tanpa abu."
    narrator "Sebuah pilihan hadir di depanmu, bukan sebagai hukum, tapi sebagai luka."

    menu:
        "Ambil api dan menjadi penjaga dunia":
            $ resolve += 2
            $ soul += 1
            narrator "Api menempel di telapak tanganmu. Dunia yang lumpuh mulai bergetar."
            jump final_choice

        "Biarkan api padam agar semua rasa sakit ikut hilang":
            $ despair += 2
            narrator "Kau menekan kobaran itu sampai redup. Dalam sekejap, segala suara berhenti."
            jump final_choice

        "Orang yang kau sayangi harus hidup, bukan api":
            $ mercy += 2
            $ companion = True
            m "Kalau begitu, kita akan menempuh jalan yang tak diketahui bersama."
            narrator "Mira memegang tanganmu saat dunia runtuh ke dalam bayangan."
            jump final_choice

label final_choice:
    scene void
    with fade

    narrator "Tiba saatnya. Di depanmu ada tiga jalan yang terbuka di tengah kekosongan."
    menu:
        "Jalan pertama: Menjadi Raja Batas, dengan kehendak yang tak bisa ditolak":
            $ resolve += 2
            $ despair += 1
            $ weapon = "Pedang Kegelapan"
            jump ending_decide

        "Jalan kedua: Menyisakan ruang untuk Mira dan dirimu sendiri":
            $ mercy += 2
            $ companion = True
            jump ending_decide

        "Jalan ketiga: Mengambil semua yang tersisa, tanpa takut menjadi hampa":
            $ despair += 3
            $ soul += 2
            jump ending_decide

label ending_decide:
    if companion and mercy >= 3 and despair < 3:
        jump ending_two_us

    if resolve >= 4 and mercy >= 2 and despair < 3:
        jump ending_warden

    if despair >= 4 or (soul >= 5 and resolve < 3):
        jump ending_hollow

    if weapon == "Pedang Kegelapan" and despair >= 2:
        jump ending_sovereign

    if mercy >= 3 and companion:
        jump ending_two_us

    if resolve >= 3 and soul >= 2:
        jump ending_bonfire

    jump ending_unknown

label ending_two_us:
    scene white
    with fade
    narrator "Kau dan Mira berjalan masuk ke ruang yang tidak punya ujung."
    narrator "Tidak ada dunia. Tidak ada api. Tidak ada masa depan."
    narrator "Hanya dua nama yang tetap berdiri dalam kekosongan, dan itu cukup."
    k "Kalau begitu, mari kita tetap ada, sampai tak ada lagi yang perlu dijawab."
    m "Kau dan aku adalah sisa yang memilih untuk tetap menyala."
    narrator "ENDING: Kau & Aku di Batas Ada"
    return

label ending_warden:
    scene bonfire
    with fade
    narrator "Kau mengambil api dan menempatkannya di tengah dunia yang baru."
    narrator "Tak ada lagi yang menghakimi, tak ada lagi yang melahap."
    narrator "Hanya kau, penjaga terakhir di antara bayangan dan cahaya."
    narrator "Kau menutup semua pintu, lalu memutuskan untuk menunggu sampai manusia kembali memilih."
    narrator "ENDING: Sang Penjaga Api Terakhir"
    return

label ending_hollow:
    scene black
    with fade
    narrator "Kau melepaskan semua yang pernah membuatmu manusia."
    narrator "Bukan karena kuat, tapi karena kau sudah terlalu lama menahan luka."
    narrator "Dunia menyebutmu raja. Dalam gelap, kau hanya tersisa sebagai suara yang menunggu."
    v "Kau bukan manusia lagi. Kau hanya ingatan yang menginginkan kehancuran."
    narrator "ENDING: Yang Tak Punya Nama"
    return

label ending_sovereign:
    scene throne
    with fade
    narrator "Pedangmu membentuk mahkota dari kegelapan."
    narrator "Semua bayangan berlutut. Semua cermin menatapmu dengan takut."
    narrator "Kau tidak lagi menjadi seseorang. Kau menjadi batas di antara ada dan tidak ada."
    narrator "Dunia menyebutmu penguasa. Hanya kau yang tahu itu hanyalah rasa sepi yang memakai nama."
    narrator "ENDING: Raja Kegelapan yang Tak Pernah Lahir"
    return

label ending_bonfire:
    scene dawn
    with fade
    narrator "Kau menyalakan api, bukan untuk menguasai dunia, tapi untuk mengingatkan semua yang terluka."
    narrator "Ruang berbisik. Bayangan melepaskan dirinya. Cermin retak menjadi cahaya."
    narrator "Bukan kemenangan. Bukan kekalahan."
    narrator "Hanya sebuah keputusan: hidup tetap berjalan, bahkan setelah semua yang mengerikan."
    narrator "ENDING: Api yang Tersisa"
    return

label ending_unknown:
    scene void
    with fade
    narrator "Kau tidak memilih apa pun."
    narrator "Dan karena itu, kau tetap berdiri di antara semua kemungkinan."
    narrator "Tak ada yang datang, tak ada yang pergi. Hanya ada ruang."
    narrator "Kau menjadi sesuatu yang tidak bisa disebut."
    narrator "ENDING: Tanpa Nama, Tanpa Akhir"
    return