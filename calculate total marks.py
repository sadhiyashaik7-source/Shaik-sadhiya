def calculate_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'E'
def main():
    print("Enter marks for 3 subjects(out of100):")
    subject1 = int(input("Subject1:"))
    subject2 = int(input("Subject2:"))
    subject3 = int(input("Subject3:"))

    total_marks = subject1 + subject2 + subject3
    percentage = total_marks/3
    grade = calculate_grade(percentage)

    print(f"\n Total Marks: {total_marks:.2f}")
    print(f"percentage: {percentage:.2f}")
    print(f"Grade: {grade}")

if __name__ == '__main__':
    main()