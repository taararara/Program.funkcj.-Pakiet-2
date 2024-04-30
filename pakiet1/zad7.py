slowa =('Ananas', 'Banan', 'Czerwiec', 'lipiec', 'uho')
filter_s = filter(lambda word: len(word) > 5, slowa)
f = list(filter_s)
print(f)
