# -*- coding:utf-8 -*-
import pandas as pd

# We want to fill the Nan value by zero
df_temp = pd.read_csv(r'I:\FiveCitiePMData\ShanghaiPM20100101_20151231.csv',sep=',', encoding='utf-8', engine='python', iterator=True, chunksize=1000)
SH = pd.concat(df_temp, ignore_index=True)
SH.fillna(value=0, inplace=True)
SH.to_csv(r'I:\FiveCitiePMData\ShanghaiPM.csv', index=False)

df_temp = pd.read_csv(r'I:\FiveCitiePMData\BeijingPM20100101_20151231.csv',sep=',', encoding='utf-8', engine='python', iterator=True, chunksize=1000)
BJ = pd.concat(df_temp, ignore_index=True)
BJ.fillna(value=0, inplace=True)
BJ.to_csv(r'I:\FiveCitiePMData\BeijingPM.csv', index=False)

df_temp = pd.read_csv(r'I:\FiveCitiePMData\GuangzhouPM20100101_20151231.csv',sep=',', encoding='utf-8', engine='python', iterator=True, chunksize=1000)
GZ = pd.concat(df_temp, ignore_index=True)
GZ.fillna(value=0, inplace=True)
GZ.to_csv(r'I:\FiveCitiePMData\GuangzhouPM.csv', index=False)

df_temp = pd.read_csv(r'I:\FiveCitiePMData\ShenyangPM20100101_20151231.csv',sep=',', encoding='utf-8', engine='python', iterator=True, chunksize=1000)
SY = pd.concat(df_temp, ignore_index=True)
SY.fillna(value=0, inplace=True)
SY.to_csv(r'I:\FiveCitiePMData\ShenyangPM.csv', index=False)

df_temp = pd.read_csv(r'I:\FiveCitiePMData\ChengduPM20100101_20151231.csv',sep=',', encoding='utf-8', engine='python', iterator=True, chunksize=1000)
CD = pd.concat(df_temp, ignore_index=True)
CD.fillna(value=0, inplace=True)
CD.to_csv(r'I:\FiveCitiePMData\ChengduPM.csv', index=False)