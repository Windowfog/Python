import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

#sample data

data = {'Categories' : ['Category A', 'Category B', 'Category C'],
        'Values' : [25, 25, 18] }

#creating a pandas DataFrame from the data
df = pd.DataFrame(data)

#creating an interactive bar chart using Plotly Express
fig = px.bar(df,x='Categories', 
                y='Values',
                title='Interactive Bar Chart Example',
                labels= {'Categories': 'Categories', 'Values' : 'Values'})

#updating the layout (better presentation)
fig.update_layout(title='Interactive Bar Chart Example', xaxis_title='Categories', yaxis_title='Values' )

#show the plot
fig.show()