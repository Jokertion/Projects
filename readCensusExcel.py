#！ python3
#readCensusExcel.py - Tabulates population and number of census tracts for 
# each county.
#从Excel中读取数据，计算每个县中普查区总数目，计算每个县总人口
#技能包：openpyxl模块，pprint模块（将数据结构写入一个.py文本文件中）

#STEP1.读取表格数据
import openpyxl, pprint
print('Opening workbook...')
wb =openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

#TODO: Fill in countyData with each county's population and tracts.
print ('Reading rows...')
for row in range(2, sheet.max_row + 1):
	#Each row in the spreadsheet has data for one census tract.
	State = sheet['B' + str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value
#TODO: Open a new text file and write the contents of countyData to it.

	
#STEP2.填充数据结构
	#Make sure the key for this state exists.
	countyData.setdefault(State, {})
	#Make sure the key for this county in this state exists.
	countyData[State].setdefault(county, {'tracts':0, 'pop':0})
	
	#Each row represents one census tract, so increment by one.
	countyData[State][county]['tracts'] += 1
	#Increase the county pop by the pop in this ccensus tract.
	countyData[State][county]['pop'] += int(pop)
#TODO: Open a new text file and write the contents of countyData to it.


#STEP3.将结果写入文件
#TODO: Open a new text file and write the contents of countyData to do it.
print('Writing results...')
resultFile = open('census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print ('Done.')






	
