import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ProjectRevision as prog
import unittest
datas = pd.read_excel('dataNew.xls') #read the file
ProjectRevision = datas['Calories']
data = datas['Period'].str.split(' ',n=1, expand=True) #split the column
datas = datas.assign(Year=data[1])  #Assign year to top left column
datas.index = datas["Year"] #assign index to dataframe
print(datas) #print the dataframe
q1 = datas[(datas["Year"] >= str(1900)) & (datas["Year"] <= str(1910))]
ps = q1['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Period');
plt.ylabel('Calories');
plt.xticks(index, ps.index);
plt.title('(1900-1910)');
plt.bar(ps.index,ps.values);
plt.show();
print("Year: 1900-1910")
print("Mean:")
print(round(datas[1:11]["Calories"].mean(), 2))
print("Total:")
print(round(datas["Calories"].head(11).sum(), 2))#end of first bar chat
q2 = datas[(datas["Year"] >= str(1911)) & (datas["Year"] <= str(1921))]
ps = q2['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Period');
plt.ylabel('Calories');
plt.xticks(index, ps.index);
plt.title('(1911-1920)');
plt.bar(ps.index, ps.values);
plt.show();
print("Year: 1911-1920")
print("Mean:")
print(round(datas[11:21]["Calories"].mean(), 2))
print("Total:")
print(round(datas[11:21]["Calories"].sum(), 2))
q3 = datas[(datas["Year"] >= str(1921)) & (datas["Year"] <= str(1931))]
ps = q3['Calories'].sort_values()
index = np.arange(len(ps.index))
plt.xlabel('Period');
plt.ylabel('Calories');
plt.xticks(index, ps.index);
plt.title('(1921-1930)');
plt.bar(ps.index, ps.values);
plt.show();
print("Year: 1921-1930")
print("Mean:")
print(round(datas[21:31]["Calories"].mean(), 2))
print("Total:")
print(round(datas[21:31]["Calories"].sum(), 2))


class EvaluateMarks(unittest.TestCase):
    def test_total(self):
        result = prog.EvaluateMarks.total(ProjectRevision)
        self.assertEqual(result, '9358.6')

    def test_mean(self):
        result = prog.EvaluateMarks.mean(sum(ProjectRevision), len(ProjectRevision))
        self.assertEqual(result, '301.89032258064515')

if __name__ == '__main__':
    unittest.main()