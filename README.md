# Praktikum Algoritma Pencarian (Search Algorithms)

## 📌 Deskripsi
Repository ini berisi implementasi berbagai algoritma pencarian dalam **Python**, khususnya:
- **Uninformed Search**: Depth First Search (DFS), Breadth First Search (BFS), dan Uniform Cost Search (UCS).

Dimana setiap algoritma tersebut digunakan untuk mencari jalur dalam graf berbobot maupun tidak berbobot sesuai dengan karakteristiknya masing-masing.


## 📖 Penjelasan Algoritma

### 1️⃣ Depth First Search (DFS)
DFS adalah algoritma pencarian yang menjelajahi graf dengan strategi **menyelam** ke dalam cabang sejauh mungkin sebelum kembali ke simpul sebelumnya. Algoritma ini menggunakan **struktur data stack** (baik secara eksplisit dengan tumpukan atau secara implisit dengan rekursi).

### 2️⃣ Breadth First Search (BFS)
BFS bekerja dengan cara menjelajahi simpul-simpul graf **berdasarkan kedalaman**. Artinya, simpul yang lebih dekat ke titik awal akan dikunjungi lebih dulu dibandingkan simpul yang lebih dalam. Algoritma ini menggunakan **struktur data queue**.

### 3️⃣ Uniform Cost Search (UCS)
UCS merupakan varian dari BFS yang memperhitungkan **biaya** antar simpul. Algoritma ini menggunakan **priority queue** untuk memastikan simpul dengan biaya terendah selalu diproses terlebih dahulu, sehingga cocok untuk menemukan **jalur terpendek** dalam graf berbobot.

## 📂 File dalam Repository
- `dfs.py` → Implementasi Depth First Search
- `bfs.py` → Implementasi Breadth First Search
- `ucs.py` → Implementasi Uniform Cost Search

## 🚀 Cara Menjalankan Kode di Google Colab
1. **Clone repository ini ke Google Colab atau komputer lokal**
2. **Jalankan kode dalam Google Colab, dengan Langkah berikut**:
   - Upload file Python ke Google Colab.
   - Tambahkan sel kode berikut untuk menjalankan algoritma:
 
     !python dfs.py  # Untuk menjalankan DFS
     !python bfs.py  # Untuk menjalankan BFS
     !python ucs.py  # Untuk menjalankan UCS
     
3. **Pastikan semua dependensi telah terinstal**:
   
4. **Jalankan dan analisis hasilnya!**
