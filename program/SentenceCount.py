
from collections import Counter

charArray = ['.','!','?']

# def count_Sentence(string):
#     s_count = 0   
#     for st in string:   
#         for c in charArray:
#             if c in st:
#                 s_count+=1     
#     print(s_count)
#     return s_count
# count_Sentence("hello.how are you?")

def count_Sentence(string):
    dot=string.count(".")
    questionmark=string.count("?")
    comma=string.count("!")
    count=dot+questionmark+comma
    return(count)
print(count_Sentence("Hello. How are You? Iam fine!"))