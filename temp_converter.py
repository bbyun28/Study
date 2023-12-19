def convert_temp_c_to_f(c_temp):
    f_temp = (float(c_temp) * 9 / 5 + 32)
    return f_temp

def convert_temp_f_to_c(f_temp):
    c_temp = (float(f_temp) - 32) * 5 / 9
    return c_temp
