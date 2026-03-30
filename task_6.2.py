import string
total_seconds = int(input('how much seconds: '))
seconds_in_day = 24 * 60 * 60
seconds_in_hour = 60 * 60
seconds_in_minute = 60
days, remainder = divmod(total_seconds, seconds_in_day)
hours, remainder = divmod(remainder, seconds_in_hour)
minutes, remainder = divmod(remainder, seconds_in_minute)
if days % 10 == 1 and days % 100 != 11:
    day_word = 'day'
    hour_word = 'hour'
    minute_word = 'minute'
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = 'day'
else :
    day_word = 'days'
time_string = f'{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(remainder) .zfill(2)}'
print(f'{days} {day_word} {time_string}')
