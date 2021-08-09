import numpy as np
import datetime

def cal_core(hour,min,p=False):
    ###################################################
    ### mannual edit
    ###################################################

    month = 2
    day = 21
    LST = datetime.datetime(2000, 1, 1, hour, min, 0)
    # 时区 注意正负
    LSTM = 15 * (5)
    longitude = 71.06
    latitude = 42.36
    # tilt angle 倾斜角 单位：度
    beta_2 = 60
    # 朝向正南方 为0（与正南方向夹角） 单位：度
    alpha_2 = 0
    # 海拔 单位km
    elevation = 0.043
    # 辐射系数 A,B,C
    # A unit W/m2
    A = 1215
    B = 0.144
    C = 0.060
    # reflectivity
    # 植物 草 0.2 水泥 0.3 雪 0.8 碎石 0.15
    rho = 0.2

    ###################################################

    days_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # 累加前几个月的总天数
    total_days = sum(days_of_month[: month - 1])
    # 累加当月天数
    total_days += day

    # declination angle, unit:degree
    delta = 23.45 * np.sin((total_days + 284) / 365 * 2 * np.pi)

    # 计算 D 值, 单位：度
    D = (total_days - 81) / 365 * 360

    # equation of time
    D_ = np.deg2rad(D)
    ET = 9.87 * np.sin(2 * D_) - 7.53 * np.cos(D_) - 1.5 * np.sin(D_)

    # 真太阳时
    ### 注意正负
    AST = LST.hour * 60 + LST.minute + 4 * (LSTM - longitude) + ET

    if p:
        print("N:{},"
              "declination angle:\t\t{:.2f}°,\n"
              "D(有时候叫做B):\t\t\t\t{:.2f}°,\n"
              "equation of time:\t\t\t{:.2f}min,\n"
              "apparent solar time:\t\t{:.1f}min,\n"
              .format(total_days, delta, D, ET, AST))

    # hour angle unit:degree
    H = (AST - 720) / 4
    latitude_ = np.deg2rad(latitude)
    delta_ = np.deg2rad(delta)
    H_ = np.deg2rad(H)
    # solar altitude angle
    # sin(beta_1)
    sin_beta_1 = np.cos(latitude_) * np.cos(delta_) * np.cos(H_) \
                 + np.sin(latitude_) * np.sin(delta_)
    # unit: degree
    beta_1 = np.rad2deg(np.arcsin(sin_beta_1))

    # solar azimuth angle
    # cos(alpha_1)
    cos_alpha_1 = (np.sin(np.deg2rad(beta_1)) * np.sin(latitude_) - np.sin(delta_)) \
                  / (np.cos(np.deg2rad(beta_1)) * np.cos(latitude_))
    # unit: degree
    alpha_1 = np.rad2deg(np.arccos(cos_alpha_1))

    # change to rad
    beta_1_ = np.deg2rad(beta_1)
    beta_2_ = np.deg2rad(beta_2)
    delta_alpha = np.deg2rad(alpha_1 - alpha_2)

    # collector angle
    cos_theta = np.sin(beta_1_) * np.cos(beta_2_) \
                + np.cos(beta_1_) * np.sin(beta_2_) * np.cos(delta_alpha)

    if p:
        print("hour angle:\t\t{:.2f}°,\n"
              "sin_beta_1:\t\t{:.4f},\n"
              "beta_1:\t\t\t{:.2f}°,\n"
              "cos_alpha_1:\t{:.4f},\n"
              "alpha_1:\t\t{:.2f}°,\n"
              "collection angle:{:.4f}\n"
              .format(H, sin_beta_1, beta_1, cos_alpha_1, alpha_1, cos_theta))

    # pressure_ratio
    pressure_ratio = np.exp(-0.1184 * elevation)
    # normal irradiance unit: W/m2
    I_DN = A * np.exp(-pressure_ratio * B / sin_beta_1)
    # direct irradiance unit W/m2
    I_D = I_DN * cos_theta

    # Scattered irradiance unit W/m2
    I_S = C * I_DN * ((1 + np.cos(np.deg2rad(beta_2))) / 2)

    # reflected irradiance unit W/m2
    I_R = I_DN * rho * (C + sin_beta_1) * ((1 + np.cos(np.deg2rad(beta_2))) / 2)

    # total irradiance
    I_tot = I_D + I_S + I_R

    if p:
        print("pressure_ratio:\t{:.4f},\n"
              "I_DN:\t\t\t{:.1f}W/m2,\n"
              "I_D:\t\t\t{:.1f}W/m2,\n"
              "I_S:\t\t\t{:.2f}W/m2,\n"
              "I_R:\t\t\t{:.2f}W/m2,\n"
              "I_tot:\t\t\t{:.1f}W/m2,\n"
              .format(pressure_ratio, I_DN, I_D, I_S, I_R, I_tot))

    return I_tot

if __name__ == '__main__':
    result = cal_core(14,0)
    print(result)

###
# author: Bernsieg Chan
# date: 9/8/2021
# version: 3.0