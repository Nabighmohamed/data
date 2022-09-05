import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)
# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

# ---------------------------------------------------------------
# Taken from https://opendata.cityofnewyork.us/

import pandas as pd




IPE = pd.read_excel('indice par ecosys.xlsx')

IPP = pd.read_excel('indice par prov.xlsx')

IP = pd.read_excel('Invest Prevision.xlsx')

db = pd.read_excel('dbb_andzoa.xlsx')

# ---------------------------------------------------------------

# _____________________________________________________________________---

app.layout = html.Div([
    dbc.Row(dbc.Col(html.H1("Reporting ANDZOA", style={'color': 'red', 'fontSize': 70, 'text-align': 'center'}),
                    width={'size': 12},
                    ),
            ),

    dbc.Row(dbc.Col(html.H2("Reportation Montant Global", style={'color': '#CC0000', 'fontSize': 34}),
                    width={'size': 6, 'offset': 1},
                    ),
            ),

    dbc.Row([dbc.Col(html.H3("Niveau Graphe", style={'color': '#990000', 'fontSize': 28}),
                    width={'size': 5, 'offset': 1},
                    ),
            dbc.Col(html.H3("Filters", style={'color': '#990000', 'fontSize': 28}),
                    width={'size': 5, 'offset': 6},
                    ),
            ]),
    dbc.Row([
        dbc.Col(dcc.RadioItems(
            id='rere',
            options=[
                {'label': 'two levels   ', 'value': 2},
                {'label': 'three levels', 'value': 3},
            ], value=2, style={"width": "50%"},inline=False), width={'size': 3, "offset": 1, 'order': 1}),

        dbc.Col(dcc.Dropdown(db.columns, id='parent', value='Région', placeholder="parent"),
                width={'size': 3, "offset": 2, 'order': 1}),
        dbc.Col(dcc.Dropdown(db.columns, id='son', value='Province', placeholder="son"),
                width={'size': 3, "offset": 6, 'order': 2}),
        dbc.Col(dcc.Dropdown(db.columns, id='option', value="Zone d'action", placeholder="option"),
                width={'size': 3, "offset": 6, 'order': 3}),
        dbc.Col(dcc.Dropdown(db.columns, id='measure', value='Montant Global', placeholder="value"),
                width={'size': 3, "offset": 6, 'order': 4})

            ]
        ),



    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='sunburst', figure={

                "layout": {
                    "title": "My Dash Graph",
                    "height": 700,  # px
                }}, ), width=12, )
        ]
    ),

    dbc.Row(dbc.Col(html.H2("Investissement Global Par Rapport Au Stratégie", style={'color': '#CC0000', 'fontSize': 34}),
                    width={'size': 6, 'offset': 1},
                    ),
            ),


    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='piechart'),
                    width=12, lg={'size': 12, "offset": 0, 'order': 'first'}
                    ),
        ]
    ),

    dbc.Row(
        [

            dbc.Col(dcc.Dropdown(id='zone', options=[{'label': i, 'value': i} for i in IPE["Zone d'action"].unique()],
                                 value='ZONES ZOA', placeholder="zone"),
                    width={'size': 3, "offset": 2, 'order': 3},

                    ),

        ],
    ),

    dbc.Row(
        [

            dbc.Col(dcc.Dropdown(IPE.columns, id='indice1', value='Nombre de lits pour 10000 habitants (Public)',
                                 placeholder="indice"),
                    width={'size': 3, "offset": 2, 'order': 3}),

        ],
    ),

    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='bar1'),
                    width=6
                    ),
            dbc.Col(dcc.Graph(id='bar2'),
                    width=6
                    ),
        ]
    ),

    dbc.Row(dbc.Col(html.H2("Indicateurs Socio-Economiques", style={'color': '#CC0000', 'fontSize': 34}),
                    width={'size': 6, 'offset': 1},
                    ),
            ),
    dbc.Row([dbc.Col(html.H3("Filter Indicateur", style={'color': '#990000', 'fontSize': 28}),
                     width={'size': 5, 'offset': 2},
                     ),
             ]),
    dbc.Row(
        [

            dbc.Col(dcc.Dropdown(IPP.columns, id='indice2', value="Nombre de lits pour 10000 habitants (Public)",
                                 placeholder="indice"),
                    width={'size': 3, "offset": 2, 'order': 3}),

        ],
    ),

    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='bar3'),
                    width=12
                    ),
        ]
    ),

    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='bar4'),
                    width=12
                    ),
        ]
    ),

    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='bar5'),
                    width=12
                    ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='bar6'),
                    width=12
                    ),
        ]
    ),

    dbc.Row([dbc.Col(html.H3("Filter Province", style={'color': '#990000', 'fontSize': 28}),
                     width={'size': 5, 'offset': 2},
                     ),
             ]),

    dbc.Row(
        [

            dbc.Col(dcc.Dropdown(id='zone1', options=[{'label': i, 'value': i} for i in IPP["Province"].unique()],
                                 value='Sidi ifni', placeholder="zone"),
                    width={'size': 3, "offset": 2, 'order': 3},

                    ),

        ],
    ),

    dbc.Row([dbc.Col(dcc.Graph(id='bar7'), width=6),
             dbc.Col(dcc.Graph(id='bar8'), width=6),]),

    dbc.Row([dbc.Col(dcc.Graph(id='bar9'), width=6),
             dbc.Col(dcc.Graph(id='bar10'), width=6), ]),

    dbc.Row([dbc.Col(dcc.Graph(id='bar11'), width=6),
             dbc.Col(dcc.Graph(id='bar12'), width=6),]),

    dbc.Row([dbc.Col(dcc.Graph(id='bar13'), width=6),
             dbc.Col(dcc.Graph(id='bar14'), width=6), ]),

])


# --------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='sunburst', component_property='figure'),
    [Input(component_id='parent', component_property='value'),
     Input(component_id='son', component_property='value'),
     Input(component_id='measure', component_property='value'),
     Input(component_id='option', component_property='value'),
     Input(component_id='rere', component_property='value'),
     ]
)
def build_graph(parent, son, measure,op,re):

    if re==2:

        dff = db
        fig = px.sunburst(dff, path=[parent, son], values=measure)
        return fig
    if re == 3:
        dff = db
        fig = px.sunburst(dff, path=[parent, son,op], values=measure)
        return fig


@app.callback(
    Output(component_id='piechart', component_property='figure'),
    [Input(component_id='parent', component_property='value')]
)
def build_pie(value):
    total = db['Montant Global'].sum()
    prive = db[db['type financement'] == 'Privé']['Montant Global'].sum()
    public = db[db['type financement'] != 'Privé']['Montant Global'].sum()

    x = ['investissement', 'total', 'prive', 'public']
    y = [92000000000, total, prive, public]

    import plotly.graph_objects as go
    import numpy as np

    txt = [np.floor(i / 1000000000) for i in y]

    fig = go.Figure([go.Bar(x=x, y=y, text=txt)])


    return fig


@app.callback(
    Output(component_id='bar1', component_property='figure'),
    [Input(component_id='zone', component_property='value'),
     Input(component_id='indice1', component_property='value')]
)
def build_pie(zone, ind):
    dff = IPE

    df = dff[dff["Zone d'action"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(
    Output(component_id='bar2', component_property='figure'),
    [Input(component_id='zone', component_property='value'),
     Input(component_id='indice1', component_property='value')]

)
def build_bar2(zone, ind):

    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    import numpy as np

    MGP = db[db['type financement'] != 'Privé']
    tg = MGP.groupby(by='Axe stratégique', axis=0, as_index=False).sum()
    pg = IP.groupby(by='Axe stratégique', axis=0, as_index=False).sum()

    x = ['investissement', 'prevision']
    Attractif = [tg['Montant Global'][0], pg['valeur Prévsions Stratégiques'][0]]
    Compétitif = [tg['Montant Global'][1], pg['valeur Prévsions Stratégiques'][1]]
    Préservé = [tg['Montant Global'][2], pg['valeur Prévsions Stratégiques'][2]]

    fig = make_subplots(rows=3, cols=1, shared_yaxes=True, subplot_titles=("Attractif", "Compétitif", "Préservé"))

    y = Attractif
    txt = [np.floor(i / 1000000000) for i in y]
    fig.add_trace(go.Bar(x=x, y=y, text=txt),
                  1, 1)
    y = Compétitif
    txt = [np.floor(i / 1000000000) for i in y]
    fig.add_trace(go.Bar(x=x, y=y, text=txt),
                  2, 1)
    y = Préservé
    txt = [np.floor(i / 1000000000) for i in y]
    fig.add_trace(go.Bar(x=x, y=y, text=txt),
                  3, 1)

    return fig


@app.callback(
    Output(component_id='bar3', component_property='figure'),
    [Input(component_id='zone', component_property='value'),
     Input(component_id='indice2', component_property='value')]

)
def build_bar3(zone, ind):

    df=IPP.copy()

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']
    dfc['annee'] = dfc['annee'] + 0.5

    frames = [dfn, dfc]

    ipp = pd.concat(frames)

    ip1 = ipp[(ipp['Province'] == 'Sidi ifni') | (ipp['Province'] == 'Guelmim ') | (ipp['Province'] == 'Assa zag') | (
                ipp['Province'] == 'Essaouira')]

    df = ip1



    b3 = px.bar(ip1, x="annee", y=ind, facet_col="Province", color="type annee")

    return b3


@app.callback(
    Output(component_id='bar4', component_property='figure'),
    [Input(component_id='zone', component_property='value'),
     Input(component_id='indice2', component_property='value')]

)
def build_bar4(zone, ind):
    df = IPP.copy()

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']
    dfc['annee'] = dfc['annee'] + 0.5

    frames = [dfn, dfc]

    ipp = pd.concat(frames)
    ip2 = ipp[(ipp['Province'] == 'Tiznit') | (ipp['Province'] == 'Tata') | (ipp['Province'] == 'Taroudant') | (
                ipp['Province'] == 'Inzegane Ait Melloul')]

    df = ip2



    b4 = px.bar(ip2, x="annee", y=ind, facet_col="Province", color="type annee")

    return b4


@app.callback(
    Output(component_id='bar5', component_property='figure'),
    [Input(component_id='zone', component_property='value'),
     Input(component_id='indice2', component_property='value')]

)
def build_bar5(zone, ind):
    df = IPP.copy()

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']
    dfc['annee'] = dfc['annee'] + 0.5

    frames = [dfn, dfc]

    ipp = pd.concat(frames)
    ip3 = ipp[(ipp['Province'] == 'Chtouka Ait Baha') | (ipp['Province'] == 'Agadir-Ida Ou Tanane') | (
                ipp['Province'] == 'Figuig ') | (ipp['Province'] == 'Zagora ')]

    df = ip3



    b5 = px.bar(ip3, x="annee", y=ind, facet_col="Province", color="type annee")

    return b5


@app.callback(
    Output(component_id='bar6', component_property='figure'),
    [Input(component_id='zone', component_property='value'),
     Input(component_id='indice2', component_property='value')]

)
def build_bar6(zone, ind):
    df = IPP.copy()

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']
    dfc['annee'] = dfc['annee'] + 0.5

    frames = [dfn, dfc]

    ipp = pd.concat(frames)

    ip4 = ipp[(ipp['Province'] == 'Tinghir ') | (ipp['Province'] == 'Ouarzazate') | (ipp['Province'] == 'Midelt ') | (
                ipp['Province'] == 'Errachidia ')]
    df = ip4


    b6 = px.bar(ip4, x="annee", y=ind, facet_col="Province", color="type annee")

    return b6


@app.callback(Output(component_id='bar7', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Nombre de lits pour 10000 habitants (Public)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar8', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Nombre de médecins pour 10000 habitants"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar9', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Taux d'accès à l'eau potable (%)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar10', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Taux d'électrification rurale (%)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar11', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Taux d'accessibilité aux routes en milieu rural (%)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar12', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Taux brut de scolarisation au cycle primaire (%)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar13', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Taux brut de scolarisation au cycle secondaire collégial (%)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


@app.callback(Output(component_id='bar14', component_property='figure'),
              [Input(component_id='zone1', component_property='value'),
               Input(component_id='indice2', component_property='value')])
def build_bar6(zone, indi):
    dff = IPP

    df = dff[dff["Province"] == zone]

    dfn = df[df['type annee'] == 'normal']
    dfc = df[df['type annee'] == 'cible']

    ind = "Taux brut de scolarisation au cycle secondaire qualifiant (%)"
    b1 = px.bar(dfn, x='annee', y=ind)
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[0]], dfc[ind][dfc[ind].index[0]]], name=' cible 2016'))
    b1.add_trace(
        go.Scatter(x=[2012, 2021], y=[dfc[ind][dfc[ind].index[1]], dfc[ind][dfc[ind].index[1]]], name=' cible 2020'))

    return b1


# ---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=False)
