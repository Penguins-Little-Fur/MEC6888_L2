import solar_calculation as s_cal
import solar_core as s_c

# Denver Colorado
res_Denver = s_c.cal_core(
    name="Denver",
    month =12,
    day=19,
    hour=10,
    min=0,
    LSTM=15*7,
    latitude=39+44/60,  # 纬度 NS
    longtitude=104+59/60,     # 经度 WE
    p_s=True
)


# Atlanta Geprgoa
res_Atlanta = s_c.cal_core(
    name="Atlanta",
    month =3,
    day=2,
    hour=14,
    min=30,
    LSTM=15*5,
    latitude=33+45/60,  # 纬度 NS
    longtitude=84+23/60,     # 经度 WE
    p_s=True
)


# Albany NewYork
res_Albany = s_c.cal_core(
    name="Albany",
    month =8,
    day=20,
    hour=11,
    min=0,
    LSTM=15*4,
    latitude=42+39/60,  # 纬度 NS
    longtitude=73+45/60,     # 经度 WE
    p_s=True
)

###

# Columbus Ohio
res_Columbus1 = s_c.cal_core(
    name="Columbus",
    month=1,
    day=21,
    hour=15,
    min=0,
    LSTM=15 * 5,
    latitude=39 + 58 / 60,  # 纬度 NS
    longtitude=83 + 0 / 60,  # 经度 WE
    tilt=60,
    south_angle=0,
    elevation=0.275,
    A=1230,
    B=0.142,
    C=0.058,
    rho=0.3,
    p=True
)
res_Columbus2 = s_cal.cal_core(
    month=1,
    day=21,
    LSTM=15 * 5,
    latitude=39 + 58 / 60,  # 纬度 NS
    longtitude=83 + 0 / 60,  # 经度 WE
    tilt=60,
    south_angle=0,
    elevation=0.275,
    A=1230,
    B=0.142,
    C=0.058,
    rho=0.3,
    surface_area=24,
    spec_hour=13
)


# Springfield Ilinois
res_Springfield1 = s_c.cal_core(
    name="Springfield",
    month=11,
    day=21,
    hour=10,
    min=30,
    LSTM=15 * 5,
    latitude=37 + 11 / 60,  # 纬度 NS
    longtitude=93 + 17 / 60,  # 经度 WE
    tilt=70,
    south_angle=0,
    elevation=0.396,
    A=1221,
    B=0.149,
    C=0.063,
    rho=0.15,
    p=True
)
res_Springfield2 = s_cal.cal_core(
    month=11,
    day=21,
    LSTM=15 * 5,
    latitude=37 + 11 / 60,  # 纬度 NS
    longtitude=93 + 17 / 60,  # 经度 WE
    tilt=70,
    south_angle=0,
    elevation=0.396,
    A=1221,
    B=0.149,
    C=0.063,
    rho=0.15,
    surface_area=18,
    spec_hour=11
)


# Austin Texas
res_Austin1 = s_c.cal_core(
    name="Austin",
    month=7,
    day=12,
    hour=11,
    min=30,
    LSTM=15 * 5,
    latitude=30 + 15 / 60,  # 纬度 NS
    longtitude=97 + 45 / 60,  # 经度 WE
    tilt=0,
    south_angle=0,
    elevation=0.149,
    A=1085.9,
    B=0.2064,
    C=0.1354,
    rho=0.3,
    p=True
)
res_Austin2 = s_cal.cal_core(
    month=7,
    day=12,
    LSTM=15 * 5,
    latitude=30 + 15 / 60,  # 纬度 NS
    longtitude=97 + 45 / 60,  # 经度 WE
    tilt=0,
    south_angle=0,
    elevation=0.149,
    A=1085.9,
    B=0.2064,
    C=0.1354,
    rho=0.3,
    surface_area=60,
    spec_hour=12
)

# example in book, Boston
res_Boston1 = s_c.cal_core(
    name="Boston",
    hour=14,
    min=0,
    month=2,
    day=21,
    LSTM=15 * 5,
    latitude=42.36,  # 纬度 NS
    longtitude=71.06,  # 经度 WE
    tilt=60,
    south_angle=0,
    elevation=0.043,
    A=1215,
    B=0.144,
    C=0.060,
    rho=0.2,
    p=True
)
res_Boston2 = s_cal.cal_core(
    month=2,
    day=21,
    LSTM=15 * 5,
    latitude=42.36,  # 纬度 NS
    longtitude=71.06,  # 经度 WE
    tilt=60,
    south_angle=0,
    elevation=0.043,
    A=1215,
    B=0.144,
    C=0.060,
    rho=0.2,
    surface_area=24,
    spec_hour=14
)
# s_cal.drawPlot(res_Boston2)


###
# author: Bernsieg Chan
# date: 9/8/2021
# version: 4.0
# time zone refer page: http://www.timeofdate.com/city/United%20States