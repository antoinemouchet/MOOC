import TextMod as t
import StringMod as s
import patternBioMod as pb
import PatternMod as p

# Get list with each letter of file as an element
initial = s.str_to_list(t.get_text("./dataSets/dataset_3_2.txt"))
#initial = gf.str_to_list("AAAACCCGGT")

print(pb.getReverseComplement(initial))


print(pb.numberToPattern(5437, 8))

print(p.findPatterns(t.get_text("./VibrioCholerae_ori.txt"), 9))

print(s.sort_dict_to_list(s.get_freq_element(s.str_to_list(t.get_text('./VibrioCholerae_ori.txt')))))