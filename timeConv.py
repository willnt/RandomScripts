def startSecond(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    years = days / 365
def startMinute(minutes):
    seconds = minutes * 60
    hours = minutes / 60
    days = hours / 24
    weeks = days / 7
    years = days / 365
def startHours(hours):
    minutes = hours * 60
    seconds = minutes * 60
    days = hours / 24
    weeks = days / 7
    years = days / 365
def startDays(days):
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    weeks = days / 7
    year = days / 365
def startWeek(week):
    days = week * 7
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    year =  days / 365
def startYear(years):
    weeks = years * 52
    days = weeks * 7
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
