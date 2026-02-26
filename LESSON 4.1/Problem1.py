def number_quiz():
    while True:
        try:
            number_of_quiz = int(input("Enter number of quiz: "))
            if number_of_quiz >= 1:
                return number_of_quiz
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
        
def score_quiz(index):
    while True:
        try:
            score = int(input(f"Enter score {index} (0-10): "))
            if score >= 1 and score <= 10:
                return score
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
        except TypeError:
            print("Invalid Input")
        
           
def main():
    number_of_quiz = number_quiz()
    
    total = 0
    perfect_score = 0
    failing_score = 0
    
    for i in range (1, number_of_quiz + 1):
        score = score_quiz(i)
        
        total += score # for total score
        
        if score == 10: #for perfectscore
            perfect_score += 1
            
        if score <= 4: #for fail score
            failing_score += 1
            
    print("")
    print(f"Total Points: {total}")
    print(f"Perfect Points: {perfect_score}")
    print(f"Failing Points: {failing_score}")
    
main()