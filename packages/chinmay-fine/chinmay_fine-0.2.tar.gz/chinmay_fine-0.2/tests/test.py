from datetime import date
from chinmay_fine.fine_calculation import calculate_fine

def main():
    # Example usage of the calculate_fine function
    # Replace the issuedate with the appropriate date
    issuedate = date(2024, 4, 1)  # Example: April 1, 2024
    fine = calculate_fine(issuedate)
    print("Fine calculated:", fine)

if __name__ == "__main__":
    main()





