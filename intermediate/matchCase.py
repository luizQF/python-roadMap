# Match-case statement (switch): an alternative to using many elif statement 
# execute some code if a value matches a 'case'

def day_week(day):
    match day:
        case 1: 
            return "sunday"
        case 2:
            return "monday"
        case 3: 
            return "tuesday"
        case "saturn" | "sun": # or
            return "super"
        case _:
            return "not a valid day"