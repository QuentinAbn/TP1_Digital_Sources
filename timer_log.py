import time
from collections import Counter
import matplotlib.pyplot as plt

# Define the decorator
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    return wrapper

# Count words using a dictionary
@time_decorator
def count_words_dict(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower()
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Count words using the Counter function
@time_decorator
def count_words_counter(text):
    words = text.split()
    word_count = Counter(words)
    return word_count

# Import text file
with open("t8_shakespeare.txt", "r") as file:
    shakespeare_text = file.read()

# Run 100 times
execution_times_dict = []
execution_times_counter = []

for _ in range(100):
    execution_time_dict = count_words_dict(shakespeare_text)
    execution_times_dict.append(execution_time_dict)
    execution_time_counter = count_words_counter(shakespeare_text)
    execution_times_counter.append(execution_time_counter)

# Line plot
plt.plot(execution_times_dict, label='Dictionary Function', alpha=0.5)
plt.plot(execution_times_counter, label='Counter Function', alpha=0.5)
plt.legend()
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.show()