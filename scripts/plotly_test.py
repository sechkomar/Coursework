import plotly.plotly as py
import plotly.graph_objs as go
from numpy.random import randint
import plotly
plotly.tools.set_credentials_file(username='schkbsh', api_key='cV6Zcf9yeHIyvMa5sKDt')

trace = go.Heatmap(z=[[randint(20) for i in range(100)] for j in range(100)])
data = [trace]
py.iplot(data, filename='basic-heatmap')
