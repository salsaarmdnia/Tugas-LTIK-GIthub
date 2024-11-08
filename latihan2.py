#Nama: Salsabila Rahma Ramadhania
#NIM: 2409878
#Kelas: RPL 1B

#Buat Deret Fibonacci dengan menggunakan fungsi sebanyak N dari user input

def fibonacci(n):
    n1, n2 = 0, 1
    hasil = []
    for i in range(n):
       hasil.append(n1)
       total = n1 + n2
       n1 = n2
       n2 = total
    return hasil
    
n = int(input("Masukkan jumlah deret fibonacci: "))
print(fibonacci(n))