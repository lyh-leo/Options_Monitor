from WindPy import w
import pandas as pd
import numpy as np

w.start()

DATE = '2002'
k = 3600

data_300 = w.wsq("000300.SH", "rt_last")
lp_300 = data_300.Data[0][0]
lp_300_round = round(lp_300, -2)

dict = {}
for i_k in np.arange(lp_300_round-200, lp_300_round+250, 50):
    i_k = int(i_k)
    dict["IO"+DATE+'-'+str(i_k)] = []
    data_option = w.wsq("IO"+DATE+"-C-" + str(i_k)+".CFE,IO"+DATE+"-P-"+str(i_k)+".CFE", "rt_last,rt_imp_volatility")
    lp_option = data_option.Data[0]
    iv_option = data_option.Data[1]

    sp_option = lp_option[0] - lp_option[1]
    sk_spread = lp_300 - i_k
    basis_point = sp_option - sk_spread

    print(i_k)
    print(basis_point)
    dict["IO"+DATE+'-'+str(i_k)].append((i_k))
    dict["IO"+DATE+'-'+str(i_k)].append(basis_point)
    dict["IO"+DATE+'-'+str(i_k)].append(iv_option[0])
    dict["IO"+DATE+'-'+str(i_k)].append(iv_option[1])

index_list = ["行权价","合成基差","认购隐含波动率","认沽隐含波动率"]
df = pd.DataFrame(dict, index = index_list)

