import pandas as pd
import plotly.express as px

#以下路径替换为自己的
data = pd.read_excel("D:/data/旭日图数据.xlsx")
data.head()
fig = px.sunburst(data, path=['地区', '省/自治区', '城市'], 
                  values='数量', color='数量')
fig.show()
