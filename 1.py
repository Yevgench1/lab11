import csv
from collections import Counter

with open("paper.txt", "r", encoding="utf-8") as file:
    text = file.read().lower()

user_word = input("Введіть слово: ").lower()

letter_counts = Counter(letter for letter in text if letter in user_word)

with open("frequency.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Літера", "Частота"])
    for letter, freq in letter_counts.items():
        writer.writerow([letter, freq])

print("Частоти літер успішно записано у файл frequency.csv")
