#MATH UTILITIES

#Calculates the square of a number / Sayının karesini hesaplar
get_square = lambda x: x * x

# Calculates the cube of a number / Sayının küpünü hesaplar
get_cube = lambda x: x**3

# Adds two numbers / İki sayıyı toplar
add_numbers = lambda x, y: x + y

# Calculates average of given numbers / Verilen sayıların ortalamasını hesaplar
# Used *args for flexible input / Esnek giriş için *args kullanıldı
get_average = lambda *args: sum(args) / len(args) if args else 0


# List of tuples: (Name, Age) / Tuple listesi: (İsim, Yaş)
students_tuple = [("ahmet", 40), ("mehmet", 30), ("oyleboyle", 55)]

# List of dictionaries: Student details / Sözlük listesi: Öğrenci detayları
students_dict = [
    {"first_name": "berat", "last_name": "Yildiz", "age": 30},
    {"first_name": "asguc", "last_name": "ayyildiz", "age": 20}
]


# --- SORTING OPERATIONS (SIRALAMA İŞLEMLERİ) ---

# Sorting tuple list by the second element (age) 
# Tuple listesini ikinci elemana (yaş) göre sıralama
students_tuple.sort(key=lambda x: x[1])

# Sorting dictionary list by 'age' key 
# Sözlük listesini 'age' anahtarına göre sıralama
students_dict.sort(key=lambda x: x["age"])


# --- OUTPUTS (ÇIKTILAR) ---

print(f"Sum: {add_numbers(5, 6)}")
print(f"Average: {get_average(2, 4, 6, 8, 10, 20)}")
print(f"Sorted Tuples: {students_tuple}")
print(f"Sorted Dictionaries: {students_dict}")
