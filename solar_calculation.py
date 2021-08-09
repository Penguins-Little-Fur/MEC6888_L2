import solar_core as sc

# unit W/m2
# hour_value = [0, 0, 0, 0, 0, 0,
#               41.9, 392, 663, 861, 983, 1023,
#               979, 853, 651, 375, 26.1, 0,
#               0, 0, 0, 0, 0, 0]
# min_value = [6, 45, 17, 15]
min_value = []


### 获取实时总太阳辐射量
def getIntIrradiance(hour, min, hour_value, min_value):
    if hour == min_value[0]:
        if min <= min_value[1]:
            return 0
        else:
            return (min - min_value[1]) / (60 - min_value[1]) * hour_value[min_value[0]]

    if hour == min_value[2]:
        if min <= min_value[3]:
            return (min_value[3] - min) / min_value[3] * hour_value[min_value[2]]
        else:
            return 0

    return (60 - min) / 60 * (hour_value[hour - 1] - hour_value[hour]) + hour_value[hour]


# 作图
def drawPlot(sum_data):
    import matplotlib.pyplot as plt
    plt.plot(sum_data)
    plt.show()

# 获得一天所有数值（精确到分钟）
def getAllData(month,day,LSTM,longtitude,latitude,
             tilt,south_angle,elevation,A,B,C,rho):
    res_data = []
    for x in range(24):
        for y in range(60):
            I_tot = sc.cal_core(
                month=month,
                day=day,
                hour=x,
                min=y,
                LSTM=LSTM,
                latitude=latitude,  # 纬度 NS
                longtitude=longtitude, # 经度 WE
                tilt=tilt,
                south_angle=south_angle,
                elevation=elevation,
                A=A,
                B=B,
                C=C,
                rho=rho
            )
            if I_tot > 100000:
                I_tot = 100000
            res_data.append(I_tot)
    return res_data


# unit MJ/m2
def getSumArea(hour_value):
    ## roughly! not accurancy, in hour
    area_sum = 0
    for i in range(22):
        area_sum += (hour_value[i + 1] + hour_value[i]) / 2 * 3600
    return area_sum / 1e6

# unit MJ/m2
def getSumArea_2(hour_value):
    ## roughly! not accurancy, in minute
    area_sum = sum(hour_value) * 60
    return area_sum / 1e6


def roughDelAbnormalValue(hour_value):
    ## abnormal value delete
    ## the time-boundary can be calculate more accurate into minutes
    for i in range(24):
        if hour_value[i] == 0:
            continue
        hour_value[i] = 0
        break

    for i in range(23, 0, -1):
        if hour_value[i] == 0:
            continue
        hour_value[i] = 0
        break

    return hour_value

def correctValue(res_value,epi=0.1):
    ## abnormal value delete
    ## the time-boundary can be calculate more accurate into minutes
    p = 24 * 30
    for i in range(p,0,-1):
        if res_value[i] < epi:
            res_value[:i] = i * [0]
            break
    for i in range(p, len(res_value),1):
        if res_value[i] < epi:
            res_value[i:len(res_value)] = (len(res_value) - i) * [0]
            break
    return res_value


def cal_core(month,day,LSTM,longtitude,latitude,
             tilt,south_angle,elevation,A,B,C,rho,
             surface_area,spec_hour,spec_min=0):
    res_value = getAllData(
                month=month,
                day=day,
                LSTM=LSTM,
                latitude=latitude,  # 纬度 NS
                longtitude=longtitude, # 经度 WE
                tilt=tilt,
                south_angle=south_angle,
                elevation=elevation,
                A=A,
                B=B,
                C=C,
                rho=rho
            )
    res_value = correctValue(res_value)

    # hour_value = roughDelAbnormalValue(hour_value)

    ##############################################
    # mannual input, surface area, in unit m2
    ##############################################
    surface_area = surface_area
    # total solar irradiation unit:kW
    # in special time
    spec_time = spec_hour * 60

    ##############################################

    Q_solar = res_value[spec_time] * surface_area / 1000

    # Insolution H unit MJ/m2
    # from integral graph
    # total area
    H = getSumArea_2(hour_value=res_value)

    # total solar energy incident unit MJ
    E_solar = H * surface_area

    # print(hour_value)
    print("total solar irradiation(at {} hour):\t{:.2f}kW,\n"
          "Insolution:\t\t\t\t\t\t\t\t{:.1f}MJ/m2,\n"
          "total solar energy incident:\t\t\t{:.1f}MJ"
          .format(spec_hour, Q_solar, H, E_solar))

    print("----------------------------------------")
    return res_value


if __name__ == '__main__':
    # cal_core()
    pass

###
# author: Bernsieg Chan
# date: 9/8/2021
# version: 4.0
# time zone refer page: http://www.timeofdate.com/city/United%20States