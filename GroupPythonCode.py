import plotly.graph_objs as go

df = pd.read_excel ("GISdata.xlsx", sheet_name = "womenCEOs")

print(df)

womenceo = go.Bar(x = df["Year"], y=df["CEOs"],

#Color for Graph
marker = {"color": df["CEOs"], "colorscale" : "Jet" }

)

#plot([womenceo])



titles = go.Layout (
        
                    title = "Percentage of Women Employed by Occupation",
                        
                    #Defining Title for X-Axis
                    xaxis=go.layout.XAxis(
                              title=go.layout.xaxis.Title(
                              text="Year" )
                                                
                     ),
                              
                    #Defining Title for Y-Axis            
                    yaxis=go.layout.YAxis(
                             title=go.layout.yaxis.Title(
                             text="Percentage" 
                               )
                             )
                     )
                    
                                
fig = go.Figure(data=[womenceo], layout=titles)

plot(fig)