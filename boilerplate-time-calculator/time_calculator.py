def add_time(start, duration, day=None):
    # init day dependencies
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # split variables from input
    start_time, meridiem = start.split(' ')
    start_h, start_m = start_time.split(':')
    duration_h, duration_m = duration.split(':')
    if day:
        day = day.capitalize()
        day_idx = days.index(day)

    # convert hours from 12 to 24 range
    if meridiem == 'PM':
        start_h = int(start_h) + 12

    # add minutes
    new_m = int(start_m) + int(duration_m)
    extra_h = new_m // 60
    new_m = new_m % 60

    # add hours
    new_h = int(start_h) + int(duration_h) + int(extra_h)
    extra_d = new_h // 24
    new_h = new_h % 24

    # calculate new meridiem
    temp_meridiem = new_h // 12
    new_meridiem = 'PM' if (temp_meridiem==1) else 'AM'
    new_h = (new_h - 1) % 12 + 1

    # generate initial output
    new_time = f"{new_h}:{new_m:02d} {new_meridiem}"

    # include day to output if provided
    if day:
        new_d = day_idx + extra_d
        new_d = new_d % 7
        new_time += f', {days[new_d]}'

    # include next day note if valid
    if extra_d > 0:
        if extra_d == 1:
            extra_day = ' (next day)'
        else:
            extra_day = f' ({extra_d} days later)' 
        new_time += extra_day
        
    return new_time