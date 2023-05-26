def fcfs(tasks):
    n = len(tasks)  # Jumlah tugas
    waiting_time = [0] * n  # Inisialisasi waktu tunggu
    turnaround_time = [0] * n  # Inisialisasi waktu putar
    total_waiting_time = 0
    total_turnaround_time = 0

    # Menghitung waktu tunggu dan waktu putar untuk setiap tugas
    for i in range(1, n):
        waiting_time[i] = tasks[i - 1][1] + waiting_time[i - 1]
        turnaround_time[i] = tasks[i][1] + waiting_time[i]

    # Menghitung total waktu tunggu dan waktu putar
    for i in range(n):
        total_waiting_time += waiting_time[i]
        total_turnaround_time += turnaround_time[i]

    # Menghitung rata-rata waktu tunggu dan waktu putar
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Menampilkan hasil
    print("Hasil FCFS Scheduling:")
    print("Tugas\tWaktu Eksekusi\tWaktu Tunggu\tWaktu Putar")
    for i in range(n):
        print(f"{tasks[i][0]}\t\t{tasks[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"Total Waktu Tunggu: {total_waiting_time}")
    print(f"Total Waktu Putar: {total_turnaround_time}")
    print(f"Rata-rata Waktu Tunggu: {average_waiting_time}")
    print(f"Rata-rata Waktu Putar: {average_turnaround_time}")


# Main program
n = int(input("Masukkan jumlah tugas: "))
tasks = []
for i in range(n):
    task_name = input(f"Masukkan nama tugas {i + 1}: ")
    task_time = int(input(f"Masukkan waktu eksekusi tugas {i + 1}: "))
    tasks.append((task_name, task_time))

fcfs(tasks)