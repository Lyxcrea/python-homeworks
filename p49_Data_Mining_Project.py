# Program Name: p49_Data_Mining_Project.py
# Name: Charlize Serrano
# Version: Python 3.7.0
# Date Started - Date Finished: 11/11/18 - 11/11/18
# Description: Write a python program to calculate the average for each month of
# every year. You will calculate the averages for every month, store them in a
# list, and then show the list to the user.

def get_data_list(FILE_NAME):
    myFile = open(FILE_NAME, 'r')
    listOfLines = myFile.read().splitlines()
    data_list = []
    for line in listOfLines:
        listItems = line.split(',')
        data_list.append(listItems)        
    return data_list

def get_monthly_averages(data_list):
    # start variables
    monthly_average_list = []
    monthly_average_list.append(['Month', 'Year', 'Average'])
    total = 0
    cnt = 0
    fulldate = data_list[1][0]
    fd = fulldate.split('-')
    year = fd[0]
    month = fd[1]

    for i in range(1, len(data_list), 1):
        fulldate = data_list[i][0]
        fd = fulldate.split('-')
        if fd[1] != month:
            avg = total / cnt
            avgstr = '%06.2f' % avg
            monthly_average_list.append([month, year, avgstr])
            # reset the value of year and month
            year = fd[0]
            month = fd[1]
            # reset total and cnt to zero
            total = 0
            cnt = 0
            
        adjclose = float(data_list[i][6])
        total += adjclose
        cnt += 1

    avg = total / cnt
    avgstr = '%06.2f' % avg
    monthly_average_list.append([month, year, avgstr])
    return monthly_average_list 


def print_info(monthly_average_list):
    for i in range(0, len(monthly_average_list), 1):
        print("monthly_average_list[" + str(i) + "] = "
              + str(monthly_average_list[i]))
    
    

data_list = get_data_list('table-1.csv')
monthly_average_list = get_monthly_averages(data_list)
print_info(monthly_average_list)


'''
>>> 
=== RESTART: C:\Users\Charlize\Documents\Python\p49_Data_Mining_Project.py ===
monthly_average_list[0] = ['Month', 'Year', 'Average']
monthly_average_list[1] = ['09', '2008', '437.70']
monthly_average_list[2] = ['08', '2008', '485.91']
monthly_average_list[3] = ['07', '2008', '510.03']
monthly_average_list[4] = ['06', '2008', '556.32']
monthly_average_list[5] = ['05', '2008', '575.92']
monthly_average_list[6] = ['04', '2008', '497.58']
monthly_average_list[7] = ['03', '2008', '440.33']
monthly_average_list[8] = ['02', '2008', '503.80']
monthly_average_list[9] = ['01', '2008', '611.81']
monthly_average_list[10] = ['12', '2007', '695.40']
monthly_average_list[11] = ['11', '2007', '676.37']
monthly_average_list[12] = ['10', '2007', '635.39']
monthly_average_list[13] = ['09', '2007', '540.43']
monthly_average_list[14] = ['08', '2007', '509.83']
monthly_average_list[15] = ['07', '2007', '532.48']
monthly_average_list[16] = ['06', '2007', '515.02']
monthly_average_list[17] = ['05', '2007', '473.01']
monthly_average_list[18] = ['04', '2007', '472.50']
monthly_average_list[19] = ['03', '2007', '452.91']
monthly_average_list[20] = ['02', '2007', '467.22']
monthly_average_list[21] = ['01', '2007', '490.58']
monthly_average_list[22] = ['12', '2006', '473.50']
monthly_average_list[23] = ['11', '2006', '485.63']
monthly_average_list[24] = ['10', '2006', '440.53']
monthly_average_list[25] = ['09', '2006', '397.06']
monthly_average_list[26] = ['08', '2006', '377.09']
monthly_average_list[27] = ['07', '2006', '403.53']
monthly_average_list[28] = ['06', '2006', '393.59']
monthly_average_list[29] = ['05', '2006', '383.80']
monthly_average_list[30] = ['04', '2006', '413.78']
monthly_average_list[31] = ['03', '2006', '358.87']
monthly_average_list[32] = ['02', '2006', '370.00']
monthly_average_list[33] = ['01', '2006', '445.71']
monthly_average_list[34] = ['12', '2005', '418.95']
monthly_average_list[35] = ['11', '2005', '399.14']
monthly_average_list[36] = ['10', '2005', '322.47']
monthly_average_list[37] = ['09', '2005', '304.24']
monthly_average_list[38] = ['08', '2005', '286.92']
monthly_average_list[39] = ['07', '2005', '298.21']
monthly_average_list[40] = ['06', '2005', '287.55']
monthly_average_list[41] = ['05', '2005', '239.71']
monthly_average_list[42] = ['04', '2005', '199.21']
monthly_average_list[43] = ['03', '2005', '181.16']
monthly_average_list[44] = ['02', '2005', '195.01']
monthly_average_list[45] = ['01', '2005', '192.85']
monthly_average_list[46] = ['12', '2004', '181.77']
monthly_average_list[47] = ['11', '2004', '177.50']
monthly_average_list[48] = ['10', '2004', '153.23']
monthly_average_list[49] = ['09', '2004', '113.23']
monthly_average_list[50] = ['08', '2004', '105.26']
>>>
'''
