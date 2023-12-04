def bull_and_cow(scode,gcode):
    try:
        bulls = 0
        cows = 0
        lst_scode = list(scode)
        lst_gcode = list(gcode)

        if len(lst_scode) != len(lst_gcode):
            return f"length of secret code : {len(lst_scode)}"
        
        for i in lst_scode:
            for j in lst_gcode:
                if lst_scode.index(i) == lst_gcode.index(j):
                    if i == j:
                        bulls += 1
                    elif i != j:
                        cows += 1

        return [bulls , cows]
    except Exception as e:
        print(e)


print(bull_and_cow("1234","123"))