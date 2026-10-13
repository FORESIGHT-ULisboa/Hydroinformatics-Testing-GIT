"""Student B. Word counting and frequencies.

Standard library only. See docs/TASKS.md, issue 2.
"""


def word_counts(text:str, top:int=None)->list[str]:
    """Return a list of (word, count) sorted by count descending, then word ascending.

    Words are lowercased and stripped of surrounding punctuation.
    `top` limits the result to the n most frequent words; None returns all.
    """
    text = "".join([char for char in text if char not in """.,;:!?"'()"""])
    list_of_words:list[str] = text.lower().split(" ")
    list_of_count:list[str] = [(word,len([1 for candidate_word in list_of_words if candidate_word == word ])) for word in list_of_words]
    value_count_extraction = lambda tup: list(tup)[1]

    if top == None:
        return list_of_count
    else:
        return list(set([tup for tup in sorted(list_of_count,key=value_count_extraction) if value_count_extraction(tup) == top]))
