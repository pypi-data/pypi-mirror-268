import numpy as np
import pandas as pd

def day_case(x, y):
    day = []
    day_maxt = []
    day_maxy = []
    day_mint = []
    day_miny = []
    day_meany = []
    sum, maxY, maxInd, minY, minInd, cnt, strD = 0, 0, 0, 100000, 0, 0, str(x[i]).split()[0]

    for i in range(len(x)):
        if(str(x[i]).split()[0] == strD):
            cnt += 1
            sum += y[i]
            if(maxY < y[i]):
                maxY = y[i]
                maxInd = i
            if(minY > y[i]):
                minY = y[i]
                minInd = i
        else:
            day.append(strD)
            day_maxt.append(str(x[maxInd]).split()[1])
            day_maxy.append(maxY)
            day_mint.append(str(x[minInd]).split()[1])
            day_miny.append(minY)
            day_meany.append(sum/cnt)

            sum, maxY, maxInd, minY, minInd, cnt, strD = 0, 0, 0, 100000, 0, 0, str(x[i]).split()[0]
            i -= 1

    df = pd.DataFrame({"day": day, "day_maxT": day_maxt, "day_maxY": day_maxy, "day_minT": day_mint, "day_minY": day_miny, "day_meanY": day_meany})
    return df