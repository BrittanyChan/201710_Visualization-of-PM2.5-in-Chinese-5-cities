# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#SH
SH = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\ShanghaiPM.csv',sep=',', index_col=0)
group_Jingan = SH['PM_Jingan'].groupby(SH['year']).sum()
group_PM_US_Post_SH = SH['PM_US Post'].groupby(SH['year']).sum()
group_Xuhui = SH['PM_Xuhui'].groupby(SH['year']).sum()
mix_SH = group_Jingan + group_PM_US_Post_SH + group_Xuhui

#SY
SY = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\ShenyangPM.csv',sep=',', index_col=0)
group_Taiyuanjie = SY['PM_Taiyuanjie'].groupby(SY['year']).sum()
group_PM_US_Post_SY = SY['PM_US Post'].groupby(SY['year']).sum()
group_Xiaoheyan = SY['PM_Xiaoheyan'].groupby(SY['year']).sum()
mix_SY = group_Taiyuanjie + group_PM_US_Post_SY + group_Xiaoheyan

#GZ
GZ = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\GuangzhouPM.csv',sep=',', index_col=0)
group_City_Station = GZ['PM_City Station'].groupby(GZ['year']).sum()
group_PM_US_Post_GZ = GZ['PM_US Post'].groupby(GZ['year']).sum()
group_Middle = GZ['PM_5th Middle School'].groupby(GZ['year']).sum()
mix_GZ = group_City_Station + group_PM_US_Post_GZ + group_Middle

#CD
CD = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\ChengduPM.csv',sep=',', index_col=0)
group_Caotangsi = CD['PM_Caotangsi'].groupby(CD['year']).sum()
group_PM_US_Post_CD = CD['PM_US Post'].groupby(CD['year']).sum()
group_Shahepu = CD['PM_Shahepu'].groupby(CD['year']).sum()
mix_CD = group_Caotangsi + group_PM_US_Post_CD + group_Shahepu

#BJ
BJ = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\BeijingPM.csv',sep=',', index_col=0)
group_Dongsi = BJ['PM_Dongsi'].groupby(BJ['year']).sum()
group_PM_US_Post_BJ = BJ['PM_US Post'].groupby(BJ['year']).sum()
group_Dongsihuan = BJ['PM_Dongsihuan'].groupby(BJ['year']).sum()
group_Nongzhanguan = BJ['PM_Nongzhanguan'].groupby(BJ['year']).sum()
mix_BJ = group_Dongsi + group_PM_US_Post_BJ + group_Dongsihuan + group_Nongzhanguan

mix = pd.DataFrame({'mix_SH':mix_SH,'mix_GZ':mix_GZ,'mix_SY':mix_SY,'mix_BJ':mix_BJ,'mix_CD':mix_CD})
print (mix)
plt.style.use('ggplot')
mix.plot(kind='bar',stacked=False,alpha=0.3)
plt.xlabel('Year')
plt.ylabel('PM2.5 concentration (ug/m^3)')
plt.title('Five City Comparision')
plt.show()