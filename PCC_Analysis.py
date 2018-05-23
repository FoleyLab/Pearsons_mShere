'''
 PCC_Analysis.py - software for the statistical analysis of gene co-expression 
  
    Copyright (C) 2018  Reem Eldabagh, Andrew Lucila, James Arnone, and Jonathan J. Foley IV
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    Electronic Contact:  foleyj10@wpunj.edu
    Mail Contact:   Prof. Jonathan Foley
                    Department of Chemistry, William Paterson University
                    300 Pompton Road
		    Wayne NJ 07470
'''
import sys
import math
import numpy as np
from xlrd import open_workbook
import xlwt
from random import randint
import matplotlib.pyplot as plt

def get_array_from_row(row):
	new_array = []

	for col in Expression_Profile_Columns:
		try:
			new_array.append(worksheet.cell(row, col).value)
		except:
			print ("[" + str(row) + "," + str(col) + "] [row, col] is invalid.")
			return None
	return new_array


def PCC(x, y):
#make phi(X)
        #print("going to compute PCC between vectors x and y")
        #print("x is ")
        #print(x)
        #print("y is ")
        #print(y)
	n = len(x)
	pDifX = []
	PpowX = []
	PdivX = []
	for i in range(0, n, 1):
		difX = x[0] - x[i]
		pDifX.append(difX)
		powPX = math.pow(pDifX[i], 2)
		PpowX.append(powPX)
		XdivN = PpowX[i] / (n- 1)
#I KNOW WHY!!!!! The "n" Dr.Foley is working only...
#...includes all numbers but the offset or x[0]
		PdivX.append(XdivN)
		PsumX = math.fsum(PdivX)
		PhiX = math.sqrt(PsumX)
#make phi(Y)
	m = len(y)
	pDifY = []
	PpowY = []
	PdivY = []
	for j in range(0, m, 1):
		difY = y[0] - y[j]
		pDifY.append(difY)
		powPY = math.pow(pDifY[j], 2)
		PpowY.append(powPY)
		YdivM = PpowY[j] / (m- 1)
		PdivY.append(YdivM)
		PsumY = math.fsum(PdivY)
		PhiY = math.sqrt(PsumY)
#PCC X-component 
	nXy = len(x)
	IdifX = [] 
	CompXY = []
	nY = len(y)
	IdifY = [] 
	ProdXY = []
	for ixy in range (0, nXy, 1):
		difix = x[0] - x[ixy]
		IdifX.append(difix)
		Xcomp = IdifX[ixy] / PhiX
#PCC Y-component 
		difiy = y[0] - y[ixy]
		IdifY.append(difiy)
		Ycomp = IdifY[ixy] / PhiY
#PCC multiply x,y
		XYProd = Xcomp * Ycomp
		ProdXY.append(XYProd)
	SumXY = math.fsum(ProdXY)
	PCCXY = SumXY / (n- 1)
	#pcc.append(PCCXY)
        return PCCXY

	#print (PhiX)
	#print (PhiY)
	#print (PCCXY)
def output(filename, sheet1, list1):
	book = xlwt.Workbook()
	sh = book.add_sheet(sheet1)
	n = 0
	col_one = 'PCC Value'
	col_two = 'Gene 1'
	col_three = 'Gene 2'
	sh.write(0,0, col_one,)
	sh.write(0,1, col_two)
	sh.write(0,2, col_three)
	for m, e1 in enumerate(pcc, n+1):
		sh.write(m, 0, e1)
	for m, e2 in enumerate(geneone, n+1):
		sh.write(m, 1, e2)
	for m, e3 in enumerate(genetwo, n+1):
		sh.write(m, 2, e3)
	book.save(filename)


## Begin Main Function Here
if len(sys.argv) < 2:
        print ("You must pass a data file like so: python geo.pyworks1 <data file>")
        sys.exit()
workbook = open_workbook(sys.argv[1])
wsindex_question = input('Which sheet would you like to use?  (0 -> first sheet, 1 -> second sheet, etc) ')
wsindex = int(wsindex_question)
worksheet = workbook.sheet_by_index(wsindex)
first_array = []
second_array = []
pcc = []
geneone= []
genetwo = []
repeat = []
print("repeat")
print(repeat)
gene_name_question = input('What column are the gene names under: ')
gene_name_col = int(gene_name_question)
expression_col_question = input('How many time-points are there?: ')
expression_col = int(expression_col_question)
data_col_start_question = input('What is the column number where the data starts?  (A -> 0, B -> 1, etc) ')
data_col_start = int(data_col_start_question)
expression_col_a = range(data_col_start, expression_col)
expression_col_b = list(expression_col_a)
Expression_Profile_Columns = expression_col_b
bin_size_q = input('What is the preferred bin size?: ')
bin_size_a = (float(bin_size_q))
Total_Iteration_Question = input('How many iterations would you like to run?: ')
Total_Iteration_a = int(Total_Iteration_Question)
total_genes_q = input('How many genes in total are in the spreadsheet?: ')
total_genes_a = int(total_genes_q)
adj_genepair_q = input('How many adjacent gene pairs are in this gene family?: ')
adj_genepair_a = int(adj_genepair_q)
debug_output_printing_q = input('Do you want to print EVERY PCC VALUE to an excel file? (Hint:  type 0 if you are doing greater than 65,000 comparison, type 1 for yes) ')
debug_output_printing = int(debug_output_printing_q)

# Second array value can not be zero for some reason. So instruct user that profile must start on second row
First_Row_In_Sheet = 1
Total_Iterations = Total_Iteration_a


skipped=0

selection_array = np.zeros(total_genes_a)

for count in range(0, Total_Iterations):

       #genes = np.zeros(adj_genepair_a,dtype=np.int)
        genes = np.random.choice(range(1,total_genes_a), adj_genepair_a, replace=False)
        #sel_array = [None] * total_genes_q
        #sa = len(sel_array)
        #print(sa)

        for i in range(len(genes)):
            selection_array[genes[i]] += 1
 

        ## Gene 1
        #random_row = randint(First_Row_In_Sheet, worksheet.nrows-1)
        #first_array = get_array_from_row(random_row)

        #twogene = np.zeros(adj_genepair_a,dtype=np.int )
        #print("Gene 1")
        #print(first_array)
        #print("Gene 2 initialized")
        #print(genes)
      
        ## Just fill gene2 with random row numbers
        #for gcount in range(0,adj_genepair_a-1):
        #	random_row = randint(First_Row_In_Sheet, worksheet.nrows-1)
	#	genes[gcount] = random_row

        #print(genes)
        ## Now go through gene2 and compute #pcc everytime you have an entry 
        ## that refers to a gene that is not the same as gene1
        

        numpairs = adj_genepair_a*(adj_genepair_a-1)/2
        temp = np.zeros(numpairs)
        paircount = 0
        for gcount1 in range(0, adj_genepair_a-1):
                w = genes[gcount1]

                gen = len(genes) 
                for gcount2 in range(gcount1+1, gen):
                    #print("w")
                    #print(w)
                    #print("t")
                    t = genes[gcount2]
                    #print(t) 
                    first_array = get_array_from_row(w)
                    second_array = get_array_from_row(t)

                    if w == t:                
                        skipped += 1

                    else:
                       #print(first_array)
                       #print(second_array)
                        temp[paircount] = PCC(first_array, second_array)
                       #print(temp)
                       #print(paircount)
                        paircount +=1
                        

                   # pcc.append(np.mean(temp))
        h = np.mean(temp)
        pcc.append(h)
        #print(np.mean(temp))
        #print(pcc)

		#if (random_row != genes[gcount]):
    #first_array = get_array_from_row(w)		        
    #second_array = get_array_from_row(t)
			#gene1 = worksheet.cell_value(rowx=random_row, colx=(gene_name_col-1))
			#genes.append(gene1)
			#gene2 = worksheet.cell_value(rowx=twogene[gcount], colx=(gene_name_col-1))
			#genes.append(gene2)
			#PCC(first_array, second_array)	
                        
		#else:
		#	skipped += 1



print ("Skipped Iterations: " + str(skipped))
print ('Workbook Made')
#histogram = plt.hist(pcc, bins= 100)
#plt.show()

if (debug_output_printing==1):
    output('PCC_Results.xls', 'pcc_value', pcc)


#### Reem may modify and test for-loops, array handling, conditionals, etc below this line!


print("Printing PCC Array\n")
#print(pcc)
rg = len(pcc)
print(" Printing range\n")
print(rg)

print(bin_size_a)
w = 2/bin_size_a
e = w+1 
p=np.linspace(-1, 1, e, endpoint=True)
N=e
y = np.zeros(N)
prg = len(p)

for x in range(rg):
    if pcc[x] < p[0] :
        print(x)
        print(pcc[x])
        y[0]=y[0] + 1
    for z in range(1, prg) :
        if (pcc[x]>=p[z-1] and pcc[x]<p[z]) :
            y[z]=y[z]+1

print(p, y)





import xlsxwriter

workbook = xlsxwriter.Workbook('histogram.sample.xlsx')
worksheet1 = workbook.add_worksheet('PCC_Histogram')

row1 = 0
col1 = 0
#for item, cost in (data):
#    worksheet.write(row, col,   item)
#    worksheet.write(row, col + 1, cost)
#    row += 1

for item in (y):
    worksheet1.write(row1, col1 +1, item)
    row1 += 1

row1 = 0
for item in (p):
    worksheet1.write(row1, col1, item)
    row1 += 1

worksheet1.write(row1, 0, 'Total Iterations')
worksheet1.write(row1, 1, '=SUM(B1:B401)')

# An example of creating Excel Line charts with Python and XlsxWriter.
#
# Copyright 2013-2017, John McNamara, jmcnamara@cpan.org

# Create a new chart object. In this case an embedded chart.
chart1 = workbook.add_chart({'type': 'column'})

# Configure the first series.

#array = range(1, total_genes_a+1)
#str0 = "A"
#str1_start = "A$" + str(array[1])
#str1_end = ":A$" + str(array[total_genes_a-1])
#fullstring1 = str1_start + str1_end
#print(str1_start)
#print(str1_end)
#print(fullstring1)

#str2 = "B"
#str2_start = "B$" + str(array[1])
#str2_end = ":B$" + str(array[total_genes_a-1])
#fullstring2 = str2_start + str2_end
#print(str2_start)
#print(str2_end)
#print(fullstring2)

chart1.add_series({
    'categories': '=PCC_Histogram!$A$1:$A$401',
    'values': '=PCC_Histogram!$B$1:$B$401',
})

# Add a chart title and some axis labels.
chart1.set_title ({'name': 'Histogram'})
chart1.set_x_axis({'name': 'PCC'})
chart1.set_y_axis({'name': 'Number of Gene Pairs'})

# Set an Excel chart style. Colors with white outline and shadow.
chart1.set_style(11)

# Insert the chart into the worksheet (with an offset).
worksheet1.insert_chart('D2', chart1, {'x_offset': 25, 'y_offset': 10})

chart2 = workbook.add_chart({'type': 'column', 'subtype': 'clustered'})

#2nd histogram below

worksheet2 = workbook.add_worksheet('Randomness_Check')

row2 = 0
col2 = 0

for thing in (selection_array):
    worksheet2.write(row2, col2 +1, thing)
    row2 += 1

row2 = 0
for thing in (genes):
    worksheet2.write(row2, col2, thing)
    row2 += 1

#worksheet2.write(row2, 0, 'Total Choices')
#worksheet2.write(row2, 1, '=SUM(B1:B83')

chart2 = workbook.add_chart({'type': 'column'})

chart2.add_series({
    'categories' : '=Randomness_Check!$A$1:$A$73',
    'values' : '=Randomness_Check!$B$1:$B$73',
})

chart2.set_title ({'name': 'Randomness Check'})
chart2.set_x_axis({'name': 'Gene Number'})
chart2.set_y_axis({'name': 'Frequency'})

#chart2.set.style(10)

worksheet2.insert_chart('D2', chart2, {'x_offset': 25, 'y_offset': 10})

chart3 = workbook.add_chart({'type': 'column', 'subtype': 'clustered'})

workbook.close()

#print(histogram)



#x = [ 0.000000, -0.128000, -0.097000, -0.020000, -0.272000, -0.198000, -0.333000]
#y = [ 0.775000, 0.849000, 0.518000, 0.116000, -0.076000, -0.090000, 0.102000]
#PCC(x, y)


