import re


def count_words(sentence):
   # regex to search for special characters at end and start
   regx = r'\b\w+'
   filtered_words = re.findall(regx, sentence.lower())
   
   word_count = {}
   
   for word in filtered_words:
      word_count[word] = word_count.get(word, 0) + 1
   
   return word_count
   

if __name__ == "__main__":
   print(count_words("The Queen will address the House of Commons today"))

