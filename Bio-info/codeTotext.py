import Getting_fre as g
import text as t

# Get text
text = t.get_text('./dataSets/enigme/Rawtext.txt')

# Get a copy of the text
text_copy = text

# Get repartition of symbols and sort it.
text_as_list = g.str_to_list(text)
symbolsByOrder = g.sort_dict_to_list(g.get_freq_element(text_as_list))

# Define list of letters based on frequency of apparition.
english_letter = ["e", "t", "a", "o", "i", "n", "s", "r", "h", "l", "d", "c", "u", "m", "f", "p", "g", "w", "y", "b", "v", "k", "x", "j", "q", "z"]



# Loop on all letters from English
for letter_id in range(len(symbolsByOrder)):
    # Replace symbol by correspsonding letter
    text_copy = text_copy.replace(symbolsByOrder[letter_id], english_letter[letter_id])


# Write decoded text into file
decoded = open('./decoded.txt', 'w')
decoded.write(text_copy)
decoded.close()
