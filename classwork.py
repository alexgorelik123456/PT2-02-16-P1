import re
string = "2014-9-01T12:48:3.2182"

def parse(string):
    split_T_string = re.split(r'T', string)

    time_stamp_prev = split_T_string[1:2]
    date_stamp_prev = split_T_string[:1]

    time_string = ''.join(time_stamp_prev)
    date_string = ''.join(date_stamp_prev)

    time_stamp_t = re.split(r'[:.]', time_string)
    date_stamp_d = re.split(r'-', date_string)

    time_stamp = {'hour': time_stamp_t[:1], 'minute': time_stamp_t[1:2], 'second': time_stamp_t[2:3]}
    date_stamp = {'year': date_stamp_d[:1], 'month': date_stamp_d[1:2], 'day': date_stamp_d[2:3]}
    return time_stamp, date_stamp

ts,ds = parse(string)
print(ts)
print(ds)
