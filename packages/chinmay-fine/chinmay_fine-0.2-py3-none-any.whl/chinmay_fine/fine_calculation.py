from datetime import date

def calculate_fine(issuedate):
    days = (date.today() - issuedate).days
    fine = max(0, (days - 15) * 10)
    return fine
