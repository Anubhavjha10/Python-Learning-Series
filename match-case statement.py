# match case statement (switch) = An alternative to using many 'elif' statement
#                                 Execute some code if a value matches a 'case'
#                                 Benefits: Cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "Mon"
        case 2:
            return "Tue"
        case 3:
             return "Wed"
        case 4:
            return "Thu"
        case 5:
            return "Fri"
        case 6:
            return "Sat"
        case 7:
            return "Sun"
        case _:
            return "Not a valid day"

    print(day_of_week(2))