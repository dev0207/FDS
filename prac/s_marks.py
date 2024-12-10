def average_score(marks):
    total = 0
    count = 0
    for mark in marks:
        if mark is not None:  # Exclude absent students
            total += mark
            count += 1
    if count == 0:
        return 0
    return total / count

def highest_and_lowest_scores(marks):
    highest = None
    lowest = None
    for mark in marks:
        if mark is not None:
            if highest is None or mark > highest:
                highest = mark
            if lowest is None or mark < lowest:
                lowest = mark
    return highest, lowest

def count_absent_students(marks):
    count = 0
    for mark in marks:
        if mark is None:
            count += 1
    return count

def mark_with_highest_frequency(marks):
    frequency = {}
    for mark in marks:
        if mark is not None:
            if mark not in frequency:
                frequency[mark] = 1
            else:
                frequency[mark] += 1
    # Find the mark with highest frequency
    max_freq = 0
    most_frequent_mark = None
    for mark, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_mark = mark
    return most_frequent_mark

def pass_fail_percentage(marks, passing_score=50):
    passed = 0
    failed = 0
    total = 0
    for mark in marks:
        if mark is not None:
            total += 1
            if mark >= passing_score:
                passed += 1
            else:
                failed += 1
    if total == 0:
        return 0, 0  # Avoid division by zero if no student has marks
    return (passed / total) * 100, (failed / total) * 100

def top_three_highest_scores(marks):
    valid_marks = [mark for mark in marks if mark is not None]
    valid_marks.sort(reverse=True)
    return valid_marks[:3]  # Top 3 highest scores

# Main function to input marks and call other functions
def main():
    # List of marks for 10 students (None represents absent student)
    marks = []
    print("Enter the marks of 10 students (enter None for absent students):")
    for i in range(10):
        while True:
            try:
                mark = input(f"Enter marks for student {i+1}: ")
                if mark.lower() == 'none':  # Representing absent students
                    marks.append(None)
                else:
                    mark = int(mark)
                    marks.append(mark)
                break
            except ValueError:
                print("Invalid input, please enter a valid number or 'None' for absent students.")
    
    print("\nMarks of students:", marks)

    # a) Average score of the class
    avg = average_score(marks)
    print(f"Average score of the class: {avg:.2f}")

    # b) Highest and lowest score
    highest, lowest = highest_and_lowest_scores(marks)
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")

    # c) Count of students who were absent
    absent_count = count_absent_students(marks)
    print(f"Number of absent students: {absent_count}")

    # d) Mark with the highest frequency
    most_frequent_mark = mark_with_highest_frequency(marks)
    print(f"Mark with highest frequency: {most_frequent_mark}")

    # e) Percentages of passed and failed students
    passed_percentage, failed_percentage = pass_fail_percentage(marks)
    print(f"Percentage of passed students: {passed_percentage:.2f}%")
    print(f"Percentage of failed students: {failed_percentage:.2f}%")

    # f) Top three highest scores
    top_scores = top_three_highest_scores(marks)
    print(f"Top three highest scores: {top_scores}")

if __name__ == "__main__":
    main()
    
    
    

# Thus, the overall time complexity of the entire program is O(nlogn)
