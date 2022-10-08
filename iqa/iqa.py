from math import exp, log

def calc_q_od(od):
    return round(100 * exp(-(((od-100) ** 2)/2*(0.025 ** 2))))

def calc_q_ph(ph):
    return round(93 * exp(-(((ph-7.5) ** 2)/2*(0.652 ** 2))))

def calc_q_dbo(dbo):
    return round(-30.1 * log(dbo)+103.45)

def calc_q_ta(ta):
    return round(92 * exp(-(((ta-0) ** 2)/2*(0.25 ** 2))))

def calc_q_t(t):
    return round(-26.45 * log(t)+136.37)

w_od = 0.17
w_ph = 0.12
w_dbo = 0.10
w_ta = 0.10
w_t = 0.08

od = 80
q_od = calc_q_od(od)
print('od:', q_od)

ph = 8.54
q_ph = calc_q_ph(ph)
print('ph:', q_ph)

dbo = 9.3
q_dbo = calc_q_dbo(dbo)
print('dbo:', q_dbo)

ta = 0
q_ta = calc_q_ta(ta)
print('ta:', q_ta)

t = 6
q_t = calc_q_t(t)
print('t:', q_t)

#formula with all parameters
#(qiOD^wOD)* (qiCT^wCT)*(qipH^wpH)*(qiDBO5.20^wDBO5.20)* (qiTA^wTA)* (qiNT^wNT)* (qiFT^wFT)*(qiT^wT)*(qiRT^wRT)

print()
w = round(w_dbo + w_od + w_ph + w_t + w_ta, 2)
print('metrics total weigth', w)
w_rest = round(1 - w_dbo - w_od - w_ph - w_t - w_ta, 2)
print('metrics rest weigth', w_rest)
r_w = w_rest / 5 # 5 metrics
print('metrics divided weigth', r_w)

print('\noriginal weights')
print(f'{w_od = }')
print(f'{w_ph = }')
print(f'{w_dbo = }')
print(f'{w_ta = }')
print(f'{w_t = }')

# w_od = w_od + (w * w_od)
# w_ph = w_ph + (w * w_ph)
# w_dbo = w_dbo + (w * w_dbo)
# w_ta = w_ta + (w * w_ta)
# w_t = w_t + (w * w_t)

w_od = w_od + r_w
w_ph = w_ph + r_w
w_dbo = w_dbo + r_w
w_ta = w_ta + r_w
w_t = w_t + r_w

print('\nnew weights')
print(f'{w_od = }')
print(f'{w_ph = }')
print(f'{w_dbo = }')
print(f'{w_ta = }')
print(f'{w_t = }')

new_w =  w_dbo + w_od + w_ph + w_t + w_ta
print('metrics redistributed total weigth', new_w)

# new_w = w_od + w_ph + w_dbo + w_ta + w_t
# print('w_od + w_ph + w_dbo + w_ta + w_t =', w_od + w_ph + w_dbo + w_ta + w_t)

iqa = (q_od ** w_od) * (q_ph ** w_ph) * (q_dbo ** w_dbo) * (q_ta ** w_ta) * (q_t ** w_t)
print('\niqa =', iqa)

iqa_ratio = 52 / iqa
print('iqa_ratio =', iqa_ratio)
print('final result =',iqa * iqa_ratio)
