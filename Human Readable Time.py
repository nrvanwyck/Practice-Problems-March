# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

def make_readable(seconds):

    seconds = seconds % 360000

    time_dict = {}
    time_dict['hours'] = seconds // 3600
    time_dict['minutes'] = (seconds % 3600) // 60
    time_dict['seconds'] = (seconds % 3600) % 60
    
    for unit in time_dict:
        if time_dict[unit] >= 10:
            time_dict[unit] = str(time_dict[unit])
        else:
            time_dict[unit] = f'0{time_dict[unit]}'

    return f"{time_dict['hours']}:{time_dict['minutes']}:{time_dict['seconds']}"