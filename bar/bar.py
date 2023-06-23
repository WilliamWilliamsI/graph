import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
# sns.set(style="whitegrid")

# plt.rcParams['font.sans-serif'] = ['KaiTi']
# plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("./combination.csv")
color = []
flag = False
methods = df["method"].values.tolist()
for i in range(0, len(methods)):
    if methods[i] == "Buy-Hold":
        flag = True
        color.append("gray")    # darkgrey
    elif i+1 < len(methods) and methods[i+1] == "Buy-Hold":
        color.append("silver")
    elif not flag:
        # #9CB4D6
        color.append("steelblue")    # grey
    elif flag:
        color.append("silver")
fig = plt.figure(figsize=(20, 10))
fig.set_figheight(12)
fig.set_figwidth(24)
plt.bar(range(0, len(df["profit-mean"])), df["profit-mean"], align="center", color=color, alpha=1)
plt.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.12)
plt.axhline(0.0864937289074244, c='red', lw=2, label="买入持有年化收益率均值")
plt.xticks(range(0, len(df["profit-mean"])), df["method"], rotation=90, fontsize=12)
# plt.xlim([-1, 80])
plt.ylim([0, 0.30])
plt.ylabel("年  化  收  益  率  均  值", fontsize=40, labelpad=20, fontproperties="STKAITI")
plt.grid(axis='y')
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf', size=30)
plt.legend(prop=myfont)
# plt.show()
plt.savefig("./pic.png", dpi=400)
