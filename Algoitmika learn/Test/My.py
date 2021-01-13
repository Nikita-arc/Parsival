from time import *

start_time = time()
phrase = input("напишите отзыв о нас: ")
end_time = time()

total_time = end_time - start_time
symbols = len(phrase)
print("Скорость печати:", symbols/total_time*60)