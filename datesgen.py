def gen_dates(year_from, year_to):
    if year_from < 2000:
        zeros = tuple(f'{x:02}' for x in range(0, year_to - 1999))
        ninths = tuple(x for x in range(year_from - 1900, 100))
        years = ninths + zeros
    else:
        years = tuple(f'{x:02}' for x in range(year_from - 2000, year_to - 1999))
    for year in tuple(range(year_from, year_to+1)) + years:
        for month in range(1, 13):
            for day in range(1, 32):
                if month in (4, 6, 9, 11) and day == 31:
                    continue
                if month == 2:
                    if day > 29:
                        continue
                    if int(year) % 4 != 0 and day == 29:
                        continue
                yield f'{day:02}{month:02}{year}\n'


file = open("dates.txt", "w")
file.writelines(gen_dates(1980, 2019))
file.close()
