import pandas as pd

path = r'B:\Documents\Kỳ 1 - Năm 4\ChatRealtimeApp_JavaSocket_Ver1\udp_exam_scores.csv'

data = pd.read_csv(path)

df = pd.DataFrame(data)

df.to_excel(r'B:\Documents\Kỳ 1 - Năm 4\ChatRealtimeApp_JavaSocket_Ver1\udp_exam_scores.xlsx')
print('Done')
