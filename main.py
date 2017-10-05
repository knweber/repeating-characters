import sys

def char_counts(input):
    vals = []
    words_arr = input.strip().split(" ")
    for word in words_arr:
        count = dict()
        chars = list(word)
        for c in chars:
            count[c] = count.get(c,0) + 1
        vals.append(most_repeats_in_word(count))
    print(vals)

def most_repeats_in_word(dict):
    maximum = max(dict, key=dict.get)
    return(maximum)
    # maximum

def compare_occurrences(input):
    print("yo")
    # return(letter_counts)
    # count = 0
    # for word in letter_counts:
        # v=list(letter_counts.values())
        # k=list(letter_counts.keys())
        # return k[v.index(max(v))]
        # most = max(word, key=word.get)
        # if word[most] > count:
        #     count = word[most]

# def run(file_input):
#     char_dict = char_counts(file_input)
#     repeat_dict = most_repeats_in_word(char_dict)
#     compare_occurrences(repeat_dict)

def cli():
    filename = sys.argv[1]
    file = open(filename,"r")
    filetext = file.read()
    char_counts(filetext)
    file.close()
