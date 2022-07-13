replace_example = "kritika is a beautiful and she is out standing "

insdez= replace_example.find("is", 1)
print(replace_example.find("is", insdez+1))
half_sentence= replace_example[replace_example.find("is", insdez+1):].replace("is","was",1)
full_sentence= replace_example[:replace_example.find("is", insdez+1)] + half_sentence
print(full_sentence)
