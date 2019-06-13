import pandas
dir(pandas)

import plotly
dir(plotly)

studentlist = [["Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
print(studentlist)

studentlistdf = pandas.DataFrame(studentlist,columns = ["Name","Age","Gender"],index = ["Person 1","Person 2","Person 3","Person 4"])
print(studentlistdf)

from plotly.offline import plot
import plotly.graph_objs as go

agename = plotly.graph_objs.Bar(x=studentlistdf["Name"],y=studentlistdf["Age"])

plot([agename])
 
import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel ("GISdata.xlsx", sheet_name = "womenOccupation")

womenoccupation = go.Bar(x=df["occupation"], y=df["women"],

marker = {"color": df["women"], "colorscale" : "Jet" }

)

plot([womenoccupation])



titles = go.Layout (
        
                     title = "Percentage of Women Employed by Occupation",
                        
                      xaxis=go.layout.XAxis(
                              title=go.layout.xaxis.Title(
                              text="Year",     
                                        
                                                
                                )
                                                                
                                )
                                   
                                ),
                                
                     yaxis=go.layout.YAxis(
                             title=go.layout.yaxis.Title(
                             text="Percentage", 
                               )
        
                               )
                                
                                
fig = go.Figure(data=[womenoccupation], layout=titles)

plot(fig)



