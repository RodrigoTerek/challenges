
def run():
    list = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        # [21, 22, 23, 24, 25],
    ]
    
    result = []
    i, j= 0, -1
    increasing, ijFlag = True, True
    xlen, ylen = len(list) - 1, len(list[0])

    try:
        while len(result) < (len(list) * len(list[0])):
            if ijFlag:
                for _ in range(0, ylen, 1):
                    if increasing:
                        j += 1
                    else:
                        j -= 1
                    result.append(list[i][j])

                ijFlag = not ijFlag

            else:
                for _ in range(0, xlen, 1):
                    if increasing:
                        i += 1
                    else:
                        i -= 1
                    result.append(list[i][j])

                xlen -= 1
                ylen -= 1
                increasing = not increasing
                ijFlag = not ijFlag
        
        print('\n', result)
 
    except BaseException as err:
        print(err)
        print("ERROR: i,j", i, j)   
        print("ERROR: x, y lens", xlen, ylen)
