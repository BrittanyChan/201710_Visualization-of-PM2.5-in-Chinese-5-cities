# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

#Extract PM_data from each city, and plot it...
SH = pd.read_csv(r'C:\Users\chenxi\Desktop\FiveCitiePMData\data\ShanghaiPM.csv',sep=',', index_col=0)
group_Jingan = SH['PM_Jingan'].groupby(SH['year']).mean()
group_PM_US_Post = SH['PM_US Post'].groupby(SH['year']).mean()
group_Xuhui = SH['PM_Xuhui'].groupby(SH['year']).mean()
mix = pd.DataFrame({'PM_Jingan':group_Jingan,'PM_US_Post':group_PM_US_Post,'PM_Xuhui':group_Xuhui})
#print (mix)
plt.style.use('ggplot')
mix.plot(kind='bar',stacked=True,alpha=0.3)
plt.xlabel('Year')
plt.ylabel('PM2.5 concentration (ug/m^3)')
plt.title('PM_Shanghai')
plt.show()

