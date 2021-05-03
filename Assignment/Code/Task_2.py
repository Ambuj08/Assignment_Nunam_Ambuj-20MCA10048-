import pandas as pd
#Read CSV file for Each dataset
detailCSV = pd.read_csv(r'../../Results/Task_1/detail.csv',
                        parse_dates=['Absolute Time'],
                        index_col=['Absolute Time'])

detailVolCSV = pd.read_csv(r'../../Results/Task_1/detailVol.csv',
                        parse_dates=['Realtime'],
                        index_col=['Realtime'])

detailTempCSV = pd.read_csv(r'../../Results/Task_1/detailTemp.csv',
                        parse_dates=['Realtime'],
                        index_col=['Realtime'])
#taking the max  sample of each perticular minute
detailDownCSV = detailCSV.resample('1Min').max()
detailVolDownCSV = detailVolCSV.resample('1Min').max()
detailTempDownCSV = detailTempCSV.resample('1Min').max()
#convert into CSV
detailDownCSV.to_csv(r'../../Results/Task_2/detailDownsampled.csv')
detailVolDownCSV.to_csv(r'../../Results/Task_2/detailVolDownsampled.csv')
detailTempDownCSV.to_csv(r'../../Results/Task_2/detailTempDownsampled.csv')
