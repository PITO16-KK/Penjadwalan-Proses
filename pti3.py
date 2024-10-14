class Process: 
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time

def round_robin(processes, quantum):
    time = 0 
    queue = processes[:]  # Salin daftar proses

    while queue:
        process = queue.pop(0)  # Mengambil proses pertama dari antrian
        if process.burst_time > quantum:
            print(f"Proses {process.pid} berjalan selama {quantum} satuan waktu")
            process.burst_time -= quantum
            time += quantum
            queue.append(process)  # Tambahkan kembali ke antrian
        else:
            print(f"Proses {process.pid} selesai setelah {time + process.burst_time} satuan waktu")
            time += process.burst_time  # Tambahkan sisa waktu burst ke total

# Contoh proses
p1 = Process('P1', 10)
p2 = Process('P2', 5)
p3 = Process('P3', 8)

# Menjadwalkan penjadwalan Round Robin dengan quantum 4
round_robin([p1, p2, p3], 4) 
