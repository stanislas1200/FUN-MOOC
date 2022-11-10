def file_histogram(filename):
    """Returns a histogram of the words in filename."""
    histogram = {}
    with open(filename, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            if char in histogram:
                histogram[char] += 1
            else:
                histogram[char] = 1
    return histogram

def words_by_length(filename):
    """Returns a histogram of the words in filename by length."""  """What a peace of shit"""
    histogram = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.replace("\n", '').replace("'", ' ').replace(",", ' ').replace(".", ' ').replace("!", ' ').replace("?", ' ').replace(":", ' ').replace(";", ' ').replace("-", ' ').replace("(", ' ').replace(")", ' ').replace('"', ' ')
            for word in line.split(' '):
                word = word.strip().lower()
                if len(word) in histogram and word not in histogram[len(word)]:
                    histogram[len(word)].append(word)
                elif len(word) not in histogram:
                    histogram[len(word)] = [word]
    del histogram[0]
    for key in histogram:
        histogram[key].sort()
    return dict(sorted(histogram.items()))