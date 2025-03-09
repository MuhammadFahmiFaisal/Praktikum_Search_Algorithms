# -*- coding: utf-8 -*-
"""bfs.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BmlLOm_UDwqzYWI6UHwScbzF_cvwrmfG
"""

import collections

def bfs_path(graph, start, goal):
    queue = collections.deque([[start]])  # Antrian menyimpan jalur, bukan hanya simpul
    visited = set()

    while queue:
        path = queue.popleft()  # Ambil jalur terdepan dari antrian
        node = path[-1]  # Ambil simpul terakhir dalam jalur

        if node == goal:
            print("Jalur ditemukan:", " -> ".join(map(str, path)))
            return  # Keluar setelah menemukan jalur

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                new_path = list(path)  # Salin jalur sebelumnya
                new_path.append(neighbor)  # Tambahkan tetangga ke jalur
                queue.append(new_path)  # Masukkan jalur baru ke antrian

    print(f"Tidak ada jalur dari {start} ke {goal}")

# Kode Pengguna
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

    start_node = 0
    target_node = 3
    print(f"Mencari jalur dari {start_node} ke {target_node} menggunakan BFS:")
    bfs_path(graph, start_node, target_node)