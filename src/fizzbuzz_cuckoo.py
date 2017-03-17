def fizz_buzz_cuckoo_clock(time):
    time = map(int, time.split(':'))
    if time[1] == 0:
        if time[0] > 12:
            return ('Cuckoo ' * (time[0] - 12)).strip()
        else:
            return ('Cuckoo ' * time[0]).strip()
    if time[1] == 30:
        return 'Cuckoo'
    if time[1] % 3 == 0 and time[1] % 5 == 0:
        return 'Fizz Buzz'
    if time[1] % 3 == 0:
        return 'Fizz'
    if time[1] % 5 == 0:
        return 'Buzz'
    else:
        return 'tick'
