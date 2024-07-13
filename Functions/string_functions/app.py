def process_text(sentence, replacements):
    
    #split the sentence into words
    words=sentence.split()
    print(f"Split words: {words}")
    
    #reverse the words
    words.reverse()
    print(f"Reversed words: {words}")
    
    #join the words into the sentence
    reversed_sentence = " ".join(words)
    print(f"Reversed sentence: {reversed_sentence}")
    
    #replace specified words using a dictionary
    for old_word, new_word in replacements.items():
        reversed_sentence = reversed_sentence.replace(old_word, new_word)
        
    print(f"Replaced words sentence: {reversed_sentence}")
    
    #strip the leading and trailing whitespaces
    final_sentence=reversed_sentence.strip()   
    print(f"final striped sentence: {final_sentence}")
    
    return final_sentence

sentence=input("Enter the sentence: ")
replacement_num = int(input("How many words do you want to replace: "))

replacements={}

for _ in range(replacement_num):
    old_word = input("Enter the word to be replaced: ")
    new_word = input("Enter the new word: ")
    replacements[old_word]=new_word
    
final_sentence=process_text(sentence,replacements)
print(f"Final processed sentence: {final_sentence}")