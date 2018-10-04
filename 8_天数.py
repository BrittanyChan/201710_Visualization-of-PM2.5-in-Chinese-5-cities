# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#SH
SH = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\ShanghaiPM.csv',sep=',', index_col=0)
group_Jingan = SH['PM_Jingan'].groupby([SH['year'],SH['month'],SH['day']]).mean()
group_PM_US_Post_SH = SH['PM_US Post'].groupby([SH['year'],SH['month'],SH['day']]).mean()
group_Xuhui = SH['PM_Xuhui'].groupby([SH['year'],SH['month'],SH['day']]).mean()
mix = pd.DataFrame({'group_Jingan':group_Jingan,'group_PM_US_Post_SH':group_PM_US_Post_SH,'group_Xuhui':group_Xuhui})
mix = mix[(mix.group_Jingan>=75.0)&(mix.group_PM_US_Post_SH>=75.0)]
mix = mix[(mix.group_Xuhui)>=75.0]
print (len(mix))

#print (len(mix)/(365*3))

#plt.style.use('ggplot')
#mix.plot()
#plt.show()
