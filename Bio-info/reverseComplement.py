import Getting_fre as gf

# Get list with each letter of file as an element
initial = gf.str_to_list(gf.get_text("./dataset_3_2.txt"))
#initial = gf.str_to_list("AAAACCCGGT")

complement = initial
# Reverse complement
complement.reverse()

# Loop on every element to replace it by its complement
for letter_id in range(len(complement)):

    if complement[letter_id] == "A":
        complement[letter_id] = "T"
    
    elif complement[letter_id] == "T":
        complement[letter_id] = "A"
    
    elif complement[letter_id] == "G":
        complement[letter_id] = "C"
    
    elif complement[letter_id] == "C":
        complement[letter_id] = "G"

# Make it a string
complement = "".join(complement)
print(complement)