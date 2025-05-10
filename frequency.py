from collections import Counter
import re

# The text extracted from the image
text = """
																												
"""

# Use regular expressions to split text by whitespace
words = re.findall(r'\S+', text)

# Calculate word frequency
word_freq = Counter(words)

# Extract the specific word frequencies
#specific_words = ["計畫", "輔導", "分包", "節能", "製造業", "能源", "管理"]
#specific_word_freq = {word: word_freq[word] for word in specific_words}

print(word_freq)
#print(specific_word_freq)
