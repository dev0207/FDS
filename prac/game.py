 def remove_duplicates(lst):
    # Helper function to remove duplicates from a list
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

def both_cricket_and_badminton(group_a, group_b):
    result = []
    for student in group_a:
        if student in group_b:
            result.append(student)
    return remove_duplicates(result)

def either_cricket_or_badminton_not_both(group_a, group_b):
    result = []
    for student in group_a:
        if student not in group_b:
            result.append(student)
    for student in group_b:
        if student not in group_a:
            result.append(student)
    return remove_duplicates(result)

def neither_cricket_nor_badminton(all_students, group_a, group_b):
    result = []
    for student in all_students:
        if student not in group_a and student not in group_b:
            result.append(student)
    return len(result)

def cricket_and_football_not_badminton(group_a, group_c, group_b):
    result = []
    for student in group_a:
        if student in group_c and student not in group_b:
            result.append(student)
    return len(remove_duplicates(result))

def no_game(all_students, group_a, group_b, group_c):
    result = []
    for student in all_students:
        if student not in group_a and student not in group_b and student not in group_c:
            result.append(student)
    return len(result)

def at_least_one_game(group_a, group_b, group_c):
    result = group_a + group_b + group_c
    return remove_duplicates(result)

def all_three_games(group_a, group_b, group_c):
    result = []
    for student in group_a:
        if student in group_b and student in group_c:
            result.append(student)
    return remove_duplicates(result)

# Main function to demonstrate the functionality
def main():
    # Taking input from the user
    print("Enter the names of students who play cricket ")
    group_a = input().split(",")
    group_a = [name.strip() for name in group_a]

    print("\nEnter the names of students who play badminton ")
    group_b = input().split(",")
    group_b = [name.strip() for name in group_b]

    print("\nEnter the names of students who play football:")
    group_c = input().split(",")
    group_c = [name.strip() for name in group_c]

    print("\nEnter the names of all students in the class ")
    all_students = input().split(",")
    all_students = [name.strip() for name in all_students]

    # a) Students who play both cricket and badminton
    print("\nStudents who play both cricket and badminton:")
    print(both_cricket_and_badminton(group_a, group_b))

    # b) Students who play either cricket or badminton but not both
    print("\nStudents who play either cricket or badminton but not both:")
    print(either_cricket_or_badminton_not_both(group_a, group_b))

    # c) Number of students who play neither cricket nor badminton
    print("\nNumber of students who play neither cricket nor badminton:")
    print(neither_cricket_nor_badminton(all_students, group_a, group_b))

    # d) Number of students who play cricket and football but not badminton
    print("\nNumber of students who play cricket and football but not badminton:")
    print(cricket_and_football_not_badminton(group_a, group_c, group_b))

    # e) Number of students who do not play any game
    print("\nNumber of students who do not play any game:")
    print(no_game(all_students, group_a, group_b, group_c))

    # f) Students who play at least one game
    print("\nStudents who play at least one game:")
    print(at_least_one_game(group_a, group_b, group_c))

    # g) Students who play all three games
    print("\nStudents who play all three games:")
    print(all_three_games(group_a, group_b, group_c))

# Call the main function to execute
main()
    
 
    

   
# remove_duplicates(lst) - O(n^2)
# both_cricket_and_badminton(group_a, group_b) - O(n×m)
# either_cricket_or_badminton_not_both(group_a, group_b) - O(n×m+(n+m)^2)
# neither_cricket_nor_badminton(all_students, group_a, group_b) - O(k×(n+m))
# cricket_and_football_not_badminton(group_a, group_c, group_b) - O(n×m)
# no_game(all_students, group_a, group_b, group_c) - O(k×(n+m+p))
# at_least_one_game(group_a, group_b, group_c) - O((n+m+p)^2)
# all_three_games(group_a, group_b, group_c) - O(n×(m+p))


# Where n,m, and p are the sizes of group_a, group_b, and group_c, respectively, and k is the size of all_students
