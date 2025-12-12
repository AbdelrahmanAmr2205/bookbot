def count_words(text):
    words= text.split()
    return len(words)

def get_char_stats(text):
    text= text.lower()
    char_stats= {}
    for c in text:
        if c not in char_stats:
            char_stats[c] = 1
        else:
            char_stats[c] += 1
    return char_stats

def sort_on(dictionary):
    return dictionary["count"]

def get_sorted_char_stats(char_stats):
    sorted_char_stats= []
    for char, count in char_stats.items():
        sorted_char_stats.append({"char": char, "count": count})
    sorted_char_stats.sort(reverse=True, key=sort_on)
    return sorted_char_stats