def count_vowels(word):
    count = 0
    
    for ch in word.lower():
        if ch in "aeiou":
            count += 1
    return count

def get_total_vowels(words):
    total = 0 
    
    for word in words:
        total += count_vowels(word)
    return total

def display_vowel_count(words):
    for word in words:
        print(f"{word} = {count_vowels(word)}")
    print(f"\nTotal vowels : {get_total_vowels(words)}")
    
    
def main():
    word_count = int(input("How many words: "))
    
    words = []
    
    for i in range (1, word_count + 1):
        word_input = input(f"Word {i}: ")
        
        if word_input == "":
            print("Empty")
        else:
            words.append(word_input)
            
    display_vowel_count(words)

main()