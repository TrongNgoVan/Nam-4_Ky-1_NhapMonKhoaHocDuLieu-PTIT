import pandas as pd

path = 'B:\Documents\DataScience Research(09 2024)\BTL_KHDL\Chuanhoa\PreprocessingData.csv'

data = pd.read_csv(path)

df = pd.DataFrame(data)

df.to_excel('B:\Documents\DataScience Research(09 2024)\BTL_KHDL\Chuanhoa\PreprocessingData.xlsx')
print('Done')