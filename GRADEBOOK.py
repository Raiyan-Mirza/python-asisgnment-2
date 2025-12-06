GradeBook Analyzer
Title  : GradeBook Analyzer
Author : Chandra Prakash Mishra
Date   : 05/12/2025
Roll No : 2501010311
"""

import csv
import statistics   #optional
def print_welcome():
    print("=" * 40)
    print("      GRADEBOOK ANALYZER (CLI)")
    print("=" * 40)
    print("1. Enter student data manually")
    print("2. Load student data from CSV file")
    print("3. Exit")
    print("-" * 40)

# -- Task 3: statistical functions --
def manual_entry():
    """
    Ask user for number of students, then read name and marks.
    Return a dictionary: {name: marks}
    """
    marks = {}
    n = int(input("How many students? "))

    for i in range(n):
        name = input(f"Enter name for student {i+1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score

    return marks
def calculate_average(marks_dict):
    scores = list(marks_dict.values())
    if not scores:
    if not marks_dict:
        return 0
    return sum(scores) / len(scores)
    total = sum(marks_dict.values())
    return total / len(marks_dict)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0
    scores = sorted(marks_dict.values())
    n = len(scores)
    if n == 0:
        return 0
    mid = n // 2
    if n % 2 == 1:
    if n % 2 == 1:          # for odd no
        return scores[mid]
    else:
    else:                   # for even no
        return (scores[mid - 1] + scores[mid]) / 2

def find_max_score(marks_dict):
    if not marks_dict:
        return None, None
    name = max(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]
    max_name = max(marks_dict, key=marks_dict.get)
    return max_name, marks_dict[max_name]

def find_min_score(marks_dict):
    if not marks_dict:
        return None, None
    name = min(marks_dict, key=marks_dict.get)
    return name, marks_dict[name]

# -- Task 4: grade assignment --

def assign_grade(score):
    min_name = min(marks_dict, key=marks_dict.get)
    return min_name, marks_dict[min_name]
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
@@ -52,129 +66,137 @@ def assign_grade(score):
        return "D"
    else:
        return "F"

def build_grades_dict(marks_dict):
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        grades[name] = assign_grade(score)
        grades[name] = get_grade(score)
    return grades

def grade_distribution(grades_dict):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades_dict.values():
        if g in dist:
            dist[g] += 1
    for grade in grades_dict.values():
        if grade in dist:
            dist[grade] += 1
    return dist

# -- Task 2: input methods --

def manual_entry():
    marks = {}
    print("Enter student data (blank name to stop).")
    while True:
        name = input("Student name (or press Enter to finish): ").strip()
        if name == "":
            break
        score_str = input(f"Marks for {name}: ")
        try:
            score = float(score_str)
        except ValueError:
            print("Invalid marks, try again.")
            continue
        marks[name] = score
    return marks

def load_from_csv(filename):
    marks = {}
    with open(filename, newline="") as f:
        reader = csv.reader(f)
        # if file has header, uncomment the next line:
        # next(reader, None)
        for row in reader:
            if len(row) < 2:
                continue
            name = row[0].strip()
            try:
                score = float(row[1])
            except ValueError:
                continue
            marks[name] = score
    return marks

# -- Task 5: pass / fail using list comprehension --

def get_pass_fail_lists(marks_dict):
def print_grade_summary(dist):
    print("\nGrade Distribution:")
    for grade, count in dist.items():
        print(f"{grade}: {count} student(s)")
def pass_fail_lists(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]
    return passed_students, failed_students

# -- Task 6: table printing --

    print("\nPass/Fail Summary:")
    print(f"Passed ({len(passed_students)}): {', '.join(passed_students) if passed_students else 'None'}")
    print(f"Failed ({len(failed_students)}): {', '.join(failed_students) if failed_students else 'None'}")
def print_results_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("---------------------------------")
    print("-" * 32)
    for name, score in marks_dict.items():
        grade = grades_dict.get(name, "-")
        # adjust formatting if names are long
        print(f"{name:10}\t{score:.1f}\t{grade}")
        print(f"{name:10}\t{score:5.1f}\t{grade}")
def run_analysis(marks):
    if not marks:
        print("No data to analyze.")
        return

    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)

    grades = assign_grades(marks)
    dist = grade_distribution(grades)

    print_results_table(marks, grades)
    print("\nSummary Statistics:")
    print(f"Average score: {avg:.2f}")
    print(f"Median score : {median:.2f}")
    print(f"Highest score: {max_score} ({max_name})")
    print(f"Lowest score : {min_score} ({min_name})")

    print_grade_summary(dist)
    pass_fail_lists(marks)

    # CSV export (bonus)
    choice = input("\nDo you want to export the results to a CSV file? (y/n): ").lower()
    if choice == "y":
        export_to_csv(marks, grades)

# -- Task 1 & 6: CLI loop --

def main():
    print("===== GradeBook Analyzer =====")
    while True:
        print("\n1. Manual entry")
        print("2. Load from CSV")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "3":
            print("Goodbye!")
            break
        print_welcome()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            marks = manual_entry()
            run_analysis(marks)

        elif choice == "2":
            filename = input("Enter CSV filename (with path if needed): ")
            marks = load_from_csv(filename)
        else:
            print("Invalid option, try again.")
            continue

        if not marks:
            print("No student data found.")
            continue

        # -- Task 3: statistics --
        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_name, max_score = find_max_score(marks)
        min_name, min_score = find_min_score(marks)

        print("\n--- Statistical Summary ---")
        print(f"Average score: {avg:.2f}")
        print(f"Median score : {med:.2f}")
        print(f"Highest score: {max_score} ({max_name})")
        print(f"Lowest score : {min_score} ({min_name})")

        # -- Task 4: grades & distribution --
        grades = build_grades_dict(marks)
        dist = grade_distribution(grades)

        print("\n--- Grade Distribution ---")
        for g, count in dist.items():
            print(f"{g}: {count} student(s)")

        # -- Task 5: pass / fail --
        passed, failed = get_pass_fail_lists(marks)
        print("\n--- Pass / Fail ---")
        print(f"Passed ({len(passed)}): {', '.join(passed)}")
        print(f"Failed ({len(failed)}): {', '.join(failed)}")

        # -- Task 6: table  --
        print_results_table(marks, grades)

        # repeat or not is already handled by outer while loop
            marks = load_from_csv()
            run_analysis(marks)

        elif choice == "3":
            print("Exiting GradeBook Analyzer. Goodbye!")
        input("\nPress Enter to return to the main menu...")


import csv

def load_from_csv():
    """
    Load student data from a CSV file.
    Return a dictionary: {name: marks}
    """
    marks = {}
    filename = input("Enter CSV filename to load (e.g. grades.csv): ").strip()
    
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    score = float(row[1].strip())
                    marks[name] = score
        print(f"Data loaded successfully from '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print("Something went wrong while reading the file:", e)
    
    return marks


def export_to_csv(marks_dict, grades_dict):
    """
    Export the final results table (Name, Marks, Grade) to a CSV file.
    """
    if not marks_dict:
        print("No data available to export.")
        return

    filename = input("\nEnter filename to save (e.g. results.csv): ").strip()
    if filename == "":
        filename = "gradebook_output.csv"

    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            # header row
            writer.writerow(["Name", "Marks", "Grade"])
            # data rows
            for name, score in marks_dict.items():
                grade = grades_dict.get(name, "-")
                writer.writerow([name, score, grade])

        print(f"Results exported successfully to '{filename}'.")
    except Exception as e:
        print("Something went wrong while saving the file:", e)


if __name__ == "__main__":
    main()
