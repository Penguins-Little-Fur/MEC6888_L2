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
def drawPlot():
    import matplotlib.pyplot as plt
    sum_data = []
    for x in range(24):
        for y in range(59):
            sum_data.append(getIntIrradiance(x, y, hour_value, min_value))
    plt.plot(sum_data)
    plt.show()


# unit MJ/m2
def getSumArea(hour_value):
    ## roughly! not accurancy, in hour
    area_sum = 0
    for i in range(22):
        area_sum += (hour_value[i + 1] + hour_value[i]) / 2 * 3600
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


if __name__ == '__main__':
    hour_value = []
    # 0 - 23
    for h in range(24):
        I_tot = sc.cal_core(hour=h, min=0)
        if I_tot < 0:
            I_tot = 0
        hour_value.append(I_tot)

    hour_value = roughDelAbnormalValue(hour_value)

    ##############################################
    # mannual input, surface area, in unit m2
    ##############################################
    surface_area = 24
    # total solar irradiation unit:kW
    # in special time
    spec_time = 14

    ##############################################

    Q_solar = hour_value[spec_time] * surface_area / 1000

    # Insolution H unit MJ/m2
    # from integral graph
    # total area
    H = getSumArea(hour_value=hour_value)

    # total solar energy incident unit MJ
    E_solar = H * surface_area

    print(hour_value[spec_time])
    print("total solar irradiation(at {} hour):\t{:.2f}kW,\n"
          "Insolution:\t\t\t\t\t\t{:.1f}MJ/m2,\n"
          "total solar energy incident:\t{:.1f}MJ,\n"
          .format(spec_time, Q_solar, H, E_solar))

###
# author: Bernsieg Chan
# date: 9/8/2021
# version: 3.0
