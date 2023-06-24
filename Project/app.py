import dash
import pandas as pd
from dash import dcc
from dash import html
from datetime import date
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Question 1
url = 'https://raw.githubusercontent.com/Follyboy/Aviation_Accident_Analysis/main/Project/cleaned_dataframe.csv'
df = pd.read_csv(url)

cat_col = ['Country', 'Month', 'Day', 'Injury_Severity', 'Engine_Type', 'Weather_Condition', 'Amateur_Built',
           'Investigation_Type', 'Aircraft_damage', 'Number_of_Engines']
value_cat_col = []
for a in cat_col:
    feat = {
        'label': a,
        'value': a
    }
    value_cat_col.append(feat)

cat_col_1 = ['Month', 'Day', 'Injury_Severity', 'Engine_Type', 'Weather_Condition', 'Amateur_Built',
             'Investigation_Type', 'Aircraft_damage', 'Number_of_Engines']
value_cat_col_1 = []
for a in cat_col_1:
    feat = {
        'label': a,
        'value': a
    }
    value_cat_col_1.append(feat)

country_col = df['Country'].unique()
value_country_col = []
for i in country_col:
    feat = {
        'label': i,
        'value': i
    }
    value_country_col.append(feat)

month_col = ['January', 'February', 'March', 'April', 'May',
             'June', 'July', 'August', 'September', 'October',
             'November', 'December']
value_month_col = []
for i in month_col:
    feat = {
        'label': i,
        'value': i
    }
    value_month_col.append(feat)

day_col = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
           'Saturday', 'Sunday']
value_day_col = []
for i in day_col:
    feat = {
        'label': i,
        'value': i
    }
    value_day_col.append(feat)

sev_col = df['Injury_Severity'].unique()
value_sev_col = []
for i in sev_col:
    feat = {
        'label': i,
        'value': i
    }
    value_sev_col.append(feat)

ety_col = df['Engine_Type'].unique()
value_ety_col = []
for i in ety_col:
    feat = {
        'label': i,
        'value': i
    }
    value_ety_col.append(feat)

weather_col = df['Weather_Condition'].unique()
value_weather_col = []
for i in weather_col:
    feat = {
        'label': i,
        'value': i
    }
    value_weather_col.append(feat)

am_col = df['Amateur_Built'].unique()
value_am_col = []
for i in am_col:
    feat = {
        'label': i,
        'value': i
    }
    value_am_col.append(feat)

it_col = df['Investigation_Type'].unique()
value_it_col = []
for i in it_col:
    feat = {
        'label': i,
        'value': i
    }
    value_it_col.append(feat)

ad_col = df['Aircraft_damage'].unique()
value_ad_col = []
for i in ad_col:
    feat = {
        'label': i,
        'value': i
    }
    value_ad_col.append(feat)

numo_col = df['Number_of_Engines'].unique()
value_numo_col = []
for i in numo_col:
    feat = {
        'label': i,
        'value': i
    }
    value_numo_col.append(feat)

block = {'display': 'block'}
none = {'display': 'none'}

dis_col_ = ['Total_Fatal_Injuries', 'Total_Serious_Injuries', 'Total_Minor_Injuries', 'Total_Uninjured']
dis_col = []
for i in dis_col_:
    feat = {
        'label': i,
        'value': i
    }
    dis_col.append(feat)

dis_col_2 = ['Private Aircraft', 'Chartered Aircraft', 'Commercial Aircraft']
dis_col_2_ = []
for i in dis_col_2:
    feat = {
        'label': i,
        'value': i
    }
    dis_col_2_.append(feat)

p_col_ = ['Total_Fatal_Injuries', 'Total_Serious_Injuries', 'Total_Minor_Injuries', 'Total_Uninjured', 'Year',
          'Number_of_passengers']
p_col = []
for i in p_col_:
    feat = {
        'label': i,
        'value': i
    }
    p_col.append(feat)

input_style_title = {
    'font-family': 'Times New Roman',
    'font-weight': 'bold',
    'text-align': 'center'
}

input_style = {
    'font-family': 'Times New Roman',
    'font-weight': 'bold',
    'text-align': 'center',
}

heading_style = {
    'padding-top': '6%',
    'font-family': 'Arial',
    'font-weight': 'bold',
    'text-align': 'left',
    'font-size': '28px',
    'line-height': '34px',
}

graph_heading_style = {
    'padding-top': '6%',
    'font-family': 'Arial',
    'font-weight': 'bold',
    'text-align': 'center',
    'font-size': '28px',
    'line-height': '34px',
}

sub_heading_style = {
    'font-family': 'Arial',
    'font-style': 'normal',
    'font-weight': 400,
    'font-size': '15px',
    'line-height': '18px',
}

continent_style = {
    'font-family': 'Arial',
    'font-weight': 'bold',
    'text-align': 'left',
    'font-size': '20px',
}

cat_style = {
    'font-family': 'Arial',
    'font-weight': 'bold',
    'text-align': 'left',
    'font-size': '20px',
}

# Question 6
q6_style = {'width': '50%', 'display': 'inline-block',
            'vertical-align': 'middle'}

external_stylesheets = [dbc.themes.SLATE]
my_app = dash.Dash('Final Project', external_stylesheets=external_stylesheets)
server = my_app.server


def draw_figure():
    df__ = df.copy()
    mask = df__[cat_col[0]].isin(['Mexico', 'Puerto Rico'])
    filter_df = df__[mask]
    group_bar = filter_df.groupby(['Country', 'Year']).size().reset_index(name='Count')
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.bar(group_bar, x='Year', y='Count', color='Country', barmode='stack',
                                  title='Accidents by Country').update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        margin={"r": 0, "t": 60, "l": 0, "b": 0},
                        height=300
                    ),
                    config={
                        'displayModeBar': False
                    },
                )
            ])
        ),
    ])


def draw_line():
    df__ = df.copy()
    mask = df__[cat_col[0]].isin(['Mexico', 'Puerto Rico', 'Bahamas'])
    filter_df = df__[mask]
    group_bar = filter_df.groupby(['Country', 'Year']).size().reset_index(name='Count')
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.line(group_bar, x='Year', y='Count', color='Country',
                                   title='Accidents by Country').update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        margin={"r": 0, "t": 60, "l": 0, "b": 0},
                        height=300
                    ),
                    config={
                        'displayModeBar': False
                    },
                )
            ])
        ),
    ])


def draw_geo():
    df__ = df.copy()
    df__ = df__.drop_duplicates(subset=['Country'])
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.scatter_geo(df__, locations='Country', locationmode='country names',
                                          projection='natural earth').update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        margin={"r": 0, "t": 0, "l": 0, "b": 0},
                        height=400,
                    ),
                    config={
                        'displayModeBar': False
                    },
                )
            ])
        ),
    ])


def draw_pie():
    df__ = df.copy()

    counts = df__['Day'].value_counts().reset_index()
    counts.columns = ['Day', 'Count']

    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    figure=px.pie(counts, values='Count', names='Day', title=f'Accidents by Day').update_layout(
                        template='plotly_dark',
                        plot_bgcolor='rgba(0, 0, 0, 0)',
                        paper_bgcolor='rgba(0, 0, 0, 0)',
                        margin={"r": 0, "t": 60, "l": 0, "b": 0},
                        height=300,
                    ),
                    config={
                        'displayModeBar': False
                    },
                )
            ])
        ),
    ])


main_content = html.Div(
    children=[
        html.Div(
            className='header',
            children=[
                html.P('Aviation Accident Analysis Dashboard', className='header-title', style=heading_style),
                html.P('Commercial and Private Flight Dataset (Jan 1974 - Dec 2022)', className='header-sub-title',
                       style=sub_heading_style),
                dbc.Card(
                    dbc.CardBody([
                        dbc.Row([
                            html.P('Graphs', className='continent-title',
                                   style=continent_style),
                            dbc.Col([
                                draw_figure()
                            ], width=6),
                            dbc.Col([
                                draw_pie()
                            ], width=6),
                        ], align='center'),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                draw_line()
                            ], width=12),
                        ], align='center'),
                        html.Br(),
                        dbc.Row([
                            dbc.Col([
                                html.P('Accidents by Continent', className='continent-title',
                                       style=continent_style),
                                draw_geo()
                            ], width=12)
                        ], align='center'),
                    ]), color='dark'
                )
            ],
        ),
    ],
    className="main-content",
    style={'width': '100%'})

button_style = {
    'width': '100%',
    'margin': '3%',
    'background-color': 'lightgray',
    'border': 'none',
    'cursor': 'pointer'
}

sidebar = html.Div(
    children=[
        html.Img(src='assets/image_header_2.png',
                 style={
                     'width': '70%',
                     'top': '50%',
                     'left': '50%',
                     'border-radius': '5%',
                 }),
        html.Hr(),
        html.Div([
            dbc.Nav(
                [
                    dbc.NavLink(
                        [html.Img(src='assets/dashboard.png', style={'width': '10%', 'margin-right': '5%'}),
                         "Dashboard"],
                        href="/", active="exact"),
                    html.Br(),
                    html.P([html.Img(src='assets/chart.png', style={'width': '8%', 'margin-right': '5%'}),
                            'Charts & Plots']),
                    dbc.NavLink([html.Img(src='assets/line.png', style={'width': '8%', 'margin-right': '5%'}), "Line"],
                                href="/line", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink([html.Img(src='assets/bar.png', style={'width': '8%', 'margin-right': '5%'}), "Bar"],
                                href="/bar", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink([html.Img(src='assets/pie.png', style={'width': '8%', 'margin-right': '5%'}), "Pie"],
                                href="/pie", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink(
                        [html.Img(src='assets/dis.png', style={'width': '8%', 'margin-right': '5%'}), "Displot"],
                        href="/displot", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink([html.Img(src='assets/kde.png', style={'width': '8%', 'margin-right': '5%'}), "KDE"],
                                href="/kde", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink(
                        [html.Img(src='assets/scatter.png', style={'width': '8%', 'margin-right': '5%'}), "Scatter"],
                        href="/scatter", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink([html.Img(src='assets/box.png', style={'width': '8%', 'margin-right': '5%'}), "Box"],
                                href="/box", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink(
                        [html.Img(src='assets/hist.png', style={'width': '8%', 'margin-right': '5%'}), "Histogram"],
                        href="/histogram", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink([html.Img(src='assets/pair.png', style={'width': '8%', 'margin-right': '5%'}), "Pair"],
                                href="/pair", active="exact", style={'text-align': 'left'}),
                    dbc.NavLink(
                        [html.Img(src='assets/heat.png', style={'width': '8%', 'margin-right': '5%'}), "Heat Map"],
                        href="/heat-map", active="exact", style={'text-align': 'left'}),
                    html.Br(),
                    html.Br(),
                    dbc.NavLink(
                        [html.Img(src='assets/about.png', style={'width': '8%', 'margin-right': '5%'}), "About Model"],
                        href="/about", active="exact"),
                    html.Br(),
                    html.Br(),
                    html.P('Developer'),
                    html.Img(src='assets/fola.png',
                             style={'margin-left': '25%', 'width': '45%', 'border-radius': '50%'}),
                    html.P('Folaranmi Adeyeri', style={'font-weight': 'bold'}),
                    html.A(html.P('folar.adeyeri@gmail.com'), href='mailto:folar.adeyeri@gmail.com'),
                    dbc.Row([
                        dbc.Col([
                            html.A(
                                html.Img(src='assets/git.png',
                                         style={'margin-left': '70%', 'width': '23%'}),
                                href='https://github.com/Follyboy',
                                target='_blank'
                            ),
                        ], width=6),
                        dbc.Col([
                            html.A(
                                html.Img(src='assets/linkedin.png',
                                         style={'margin-right': '80%', 'width': '20%'}),
                                href='https://www.linkedin.com/in/folaranmi-adeyeri-88800b124/',
                                target='_blank'
                            ),
                        ], width=6)
                    ], align='center'),
                ],
                vertical=True,
                pills=True,
                style={'width': '300px'}
            ),

        ],
            className="sidebar",
            style={
                'text-align': 'center',
                'align-items': 'center'
            }
        ),
    ],
    className="sidebar-content",
    style={'width': '20%', 'justify-content': 'center', 'align-items': 'center'}
)

content = html.Div(id="page-content", style={'width': '80%'})

my_app.layout = html.Div(
    children=[
        dcc.Location(id="url"),
        sidebar,
        content,
    ],
    style={'display': 'flex', 'width': '100%'}
)

line_layout = html.Div(
    children=[
        html.P('Line Plot', className='header-title-line', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick a Category"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                        html.Li("Pick from the option displayed for that category"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col', options=value_cat_col, value='Country', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_1',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                html.Br(),
                html.Div(id='a_1', children=[
                    html.P('Aviation Accident Analysis by Country over the years', style=graph_heading_style),
                    html.P('Pick the Country or Ocean', style=cat_style),
                    dcc.Dropdown(id='dropdown_country', options=value_country_col, value=['United States'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_2', children=[
                    html.P('Aviation Accident Analysis by Month over the years', style=graph_heading_style),
                    html.P('Pick the Month', style=cat_style),
                    dcc.Dropdown(id='dropdown_month', options=value_month_col, value=['January'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_3', children=[
                    html.P('Aviation Accident Analysis by Day over the years', style=graph_heading_style),
                    html.P('Pick the Day', style=cat_style),
                    dcc.Dropdown(id='dropdown_day', options=value_day_col, value=['Monday'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_4', children=[
                    html.P('Aviation Accident Analysis by Injury Severity over the years', style=graph_heading_style),
                    html.P('Pick the Injury Severity', style=cat_style),
                    dcc.Dropdown(id='dropdown_sev', options=value_sev_col, value=['Fatal'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_5', children=[
                    html.P('Aviation Accident Analysis by Engine Type over the years', style=graph_heading_style),
                    html.P('Pick the Engine Type', style=cat_style),
                    dcc.Dropdown(id='dropdown_ety', options=value_ety_col, value=['Reciprocating'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_6', children=[
                    html.P('Aviation Accident Analysis by Weather Condition over the years', style=graph_heading_style),
                    html.P('Pick the Weather Condition', style=cat_style),
                    dcc.Dropdown(id='dropdown_weather', options=value_weather_col, value=['IMC'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_7', children=[
                    html.P('Aviation Accident Analysis by Amateur Built Aircraft over the years',
                           style=graph_heading_style),
                    html.P('Pick the Amateur Built', style=cat_style),
                    dcc.Dropdown(id='dropdown_am', options=value_am_col, value=['Yes'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_8', children=[
                    html.P('Aviation Accident Analysis by Investigation Type over the years',
                           style=graph_heading_style),
                    html.P('Pick the Investigation Type', style=cat_style),
                    dcc.Dropdown(id='dropdown_it', options=value_it_col, value=['Accident'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_9', children=[
                    html.P('Aviation Accident Analysis by Aircraft damage over the years', style=graph_heading_style),
                    html.P('Pick the Aircraft damage', style=cat_style),
                    dcc.Dropdown(id='dropdown_ad', options=value_ad_col, value=['Destroyed'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='a_10', children=[
                    html.P('Aviation Accident Analysis by Number of Engines in Aircraft over the years',
                           style=graph_heading_style),
                    html.P('Pick the Number of Engines', style=cat_style),
                    dcc.Dropdown(id='dropdown_numo', options=value_numo_col, value=['2'], multi=True),
                ], style={'display': 'none'}),
                dcc.Graph(id='my-graph'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='line-content',
)

bar_layout = html.Div(
    children=[
        html.P('Bar Chart', className='header-title-bar', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick a Category"),
                        html.Li("Pick the type of plot"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                        html.Li("Pick from the option display for that category"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_bar', options=value_cat_col, value='Country', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick Plot:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.RadioItems(
                            id='radio_bar',
                            options=[
                                {'label': 'Time Series Stack Plot', 'value': 'Time Series Stack Plot'},
                                {'label': 'Time Series Group Plot', 'value': 'Time Series Group Plot'},
                            ],
                            value='Time Series Stack Plot',
                            labelStyle={'display': 'inline', 'margin': '10px'}
                        ),
                    ], width=10),
                ]),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_2',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                html.Div(id='b_1', children=[
                    html.P('Aviation Accident Analysis by Country over the years', style=graph_heading_style),
                    html.P('Pick the Country or Ocean', style=cat_style),
                    dcc.Dropdown(id='dropdown_country_bar', options=value_country_col, value=['United States'],
                                 multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_2', children=[
                    html.P('Aviation Accident Analysis by Month over the years', style=graph_heading_style),
                    html.P('Pick the Month', style=cat_style),
                    dcc.Dropdown(id='dropdown_month_bar', options=value_month_col, value=['January'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_3', children=[
                    html.P('Aviation Accident Analysis by Day over the years', style=graph_heading_style),
                    html.P('Pick the Day', style=cat_style),
                    dcc.Dropdown(id='dropdown_day_bar', options=value_day_col, value=['Monday'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_4', children=[
                    html.P('Aviation Accident Analysis by Injury Severity over the years', style=graph_heading_style),
                    html.P('Pick the Injury Severity', style=cat_style),
                    dcc.Dropdown(id='dropdown_sev_bar', options=value_sev_col, value=['Fatal'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_5', children=[
                    html.P('Aviation Accident Analysis by Engine Type over the years', style=graph_heading_style),
                    html.P('Pick the Engine Type', style=cat_style),
                    dcc.Dropdown(id='dropdown_ety_bar', options=value_ety_col, value=['Reciprocating'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_6', children=[
                    html.P('Aviation Accident Analysis by Weather Condition over the years', style=graph_heading_style),
                    html.P('Pick the Weather Condition', style=cat_style),
                    dcc.Dropdown(id='dropdown_weather_bar', options=value_weather_col, value=['IMC'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_7', children=[
                    html.P('Aviation Accident Analysis by Amateur Built Aircraft over the years',
                           style=graph_heading_style),
                    html.P('Pick the Amateur Built', style=cat_style),
                    dcc.Dropdown(id='dropdown_am_bar', options=value_am_col, value=['Yes'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_8', children=[
                    html.P('Aviation Accident Analysis by Investigation Type over the years',
                           style=graph_heading_style),
                    html.P('Pick the Investigation Type', style=cat_style),
                    dcc.Dropdown(id='dropdown_it_bar', options=value_it_col, value=['Accident'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_9', children=[
                    html.P('Aviation Accident Analysis by Aircraft damage over the years', style=graph_heading_style),
                    html.P('Pick the Aircraft damage', style=cat_style),
                    dcc.Dropdown(id='dropdown_ad_bar', options=value_ad_col, value=['Destroyed'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='b_10', children=[
                    html.P('Aviation Accident Analysis by Number of Engines in Aircraft over the years',
                           style=graph_heading_style),
                    html.P('Pick the Number of Engines', style=cat_style),
                    dcc.Dropdown(id='dropdown_numo_bar', options=value_numo_col, value=['2'], multi=True),
                ], style={'display': 'none'}),
                dcc.Graph(id='my-graph2'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='bar-content',
)

pie_layout = html.Div(
    children=[
        html.P('Pie Chart', className='header-title-pie', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick a Category"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_pie', options=value_cat_col_1, value='Month', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_3',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph3'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='pie-content',
)

dis_layout = html.Div(
    children=[
        html.P('Displot', className='header-title-dis', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick an Incident you want to analyze"),
                        html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                        html.Li("Pick a Category"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Incident:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_dis', options=dis_col, value='Total_Fatal_Injuries', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dcc.Checklist(
                    id='dis_check',
                    options=dis_col_2_,
                    value=dis_col_2,
                    inline=True,
                    labelStyle={'margin-right': '10px'}
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_dis_2', options=value_cat_col_1, value='Amateur_Built',
                                     multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_4',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph4'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='dis-content',
)

kde_layout = html.Div(
    children=[
        html.P('KDE', className='header-title-kde', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick an Incident you want to analyze"),
                        html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                        html.Li("Pick Hue (This will analyze other data points in your plot)"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Incident:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_kde', options=dis_col, value='Total_Fatal_Injuries', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dcc.Checklist(
                    id='kde_check',
                    options=dis_col_2_,
                    value=dis_col_2,
                    inline=True,
                    labelStyle={'margin-right': '10px'}
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Hue:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_kde_2', options=cat_col_1, value='Total_Fatal_Injuries',
                                     multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_5',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph5'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='kde-content',
)

scatter_layout = html.Div(
    children=[
        html.P('Scatter Plot', className='header-title-scatter', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick an Incident you want to analyze"),
                        html.Li("Pick an second Incident you want to analyze against the first"),
                        html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                        html.Li("Pick Hue (This will analyze other data points in your plot)"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Incident:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_sc', options=dis_col, value='Total_Fatal_Injuries', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dcc.Checklist(
                    id='sc_check',
                    options=dis_col_2_,
                    value=dis_col_2,
                    inline=True,
                    labelStyle={'margin-right': '10px'}
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Second Incident:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_sc_2', options=dis_col, value='Total_Fatal_Injuries', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Hue:', style=continent_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_sc_3', options=cat_col_1, multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_6',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph6'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='scatter-content',
)

box_layout = html.Div(
    children=[
        html.P('Box Plot', className='header-title-box', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick a Category"),
                        html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                        html.Li("Pick an Incident you want to analyze"),
                        html.Li("Pick Hue (This will analyze other data points in your plot)"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_bo', options=cat_col_1, value='Day', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dcc.Checklist(
                    id='bo_check',
                    options=dis_col_2_,
                    value=dis_col_2,
                    inline=True,
                    labelStyle={'margin-right': '10px'}
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Incident:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_bo_2', options=dis_col, value='Total_Fatal_Injuries', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Hue:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_bo_3', options=cat_col, multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_7',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph7'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='box-content',
)

hist_layout = html.Div(
    children=[
        html.P('Histogram', className='header-title-hist', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick a Category"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                        html.Li("Pick from the option display for that category"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_h', options=value_cat_col, value='Country', multi=False,
                                     style={'width': '20vw'}),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_8',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                html.Div(id='h_1', children=[
                    html.P('Aviation Accident Analysis by Country over the years', style=graph_heading_style),
                    html.P('Pick the Country or Ocean', style=cat_style),
                    dcc.Dropdown(id='dropdown_country_h', options=value_country_col, value=['United States'],
                                 multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_2', children=[
                    html.P('Aviation Accident Analysis by Month over the years', style=graph_heading_style),
                    html.P('Pick the Month', style=cat_style),
                    dcc.Dropdown(id='dropdown_month_h', options=value_month_col, value=['January'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_3', children=[
                    html.P('Aviation Accident Analysis by Day over the years', style=graph_heading_style),
                    html.P('Pick the Day', style=cat_style),
                    dcc.Dropdown(id='dropdown_day_h', options=value_day_col, value=['Monday'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_4', children=[
                    html.P('Aviation Accident Analysis by Injury Severity over the years', style=graph_heading_style),
                    html.P('Pick the Injury Severity', style=cat_style),
                    dcc.Dropdown(id='dropdown_sev_h', options=value_sev_col, value=['Fatal'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_5', children=[
                    html.P('Aviation Accident Analysis by Engine Type over the years', style=graph_heading_style),
                    html.P('Pick the Engine Type', style=cat_style),
                    dcc.Dropdown(id='dropdown_ety_h', options=value_ety_col, value=['Reciprocating'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_6', children=[
                    html.P('Aviation Accident Analysis by Weather Condition over the years', style=graph_heading_style),
                    html.P('Pick the Weather Condition', style=cat_style),
                    dcc.Dropdown(id='dropdown_weather_h', options=value_weather_col, value=['IMC'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_7', children=[
                    html.P('Aviation Accident Analysis by Amateur Built Aircraft over the years',
                           style=graph_heading_style),
                    html.P('Pick the Amateur Built', style=cat_style),
                    dcc.Dropdown(id='dropdown_am_h', options=value_am_col, value=['Yes'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_8', children=[
                    html.P('Aviation Accident Analysis by Investigation Type over the years',
                           style=graph_heading_style),
                    html.P('Pick the Investigation Type', style=cat_style),
                    dcc.Dropdown(id='dropdown_it_h', options=value_it_col, value=['Accident'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_9', children=[
                    html.P('Aviation Accident Analysis by Aircraft damage over the years', style=graph_heading_style),
                    html.P('Pick the Aircraft damage', style=cat_style),
                    dcc.Dropdown(id='dropdown_ad_h', options=value_ad_col, value=['Destroyed'], multi=True),
                ], style={'display': 'none'}),
                html.Div(id='h_10', children=[
                    html.P('Aviation Accident Analysis by Number of Engines in Aircraft over the years',
                           style=graph_heading_style),
                    html.P('Pick the Number of Engines', style=cat_style),
                    dcc.Dropdown(id='dropdown_numo_h', options=value_numo_col, value=['2'], multi=True),
                ], style={'display': 'none'}),
                dcc.Graph(id='my-graph8'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='hist-content',
)

pair_layout = html.Div(
    children=[
        html.P('Pair Plot', className='header-title-pair', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick a Category"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                        html.Li("Set width you want for your graph (Default is already set to 1190)"),
                        html.Li("Set height you want for your graph (Default is already set to 800)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Category:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_p', options=p_col, value='Total_Fatal_Injuries', multi=True),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_9',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dbc.Row([
                    dbc.Col([
                        html.P('Width:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Input(
                            id='width',
                            type='number',
                            value=1190,
                            min=500,
                            step=1
                        ),
                    ], width=10),
                ], align='center'),
                dbc.Row([
                    dbc.Col([
                        html.P('Height:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Input(
                            id='height',
                            type='number',
                            value=800,
                            min=500,
                            step=1
                        ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph9'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='pair-content',
)

heat_layout = html.Div(
    children=[
        html.P('Heat Map', className='header-title-heat', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                html.P('Steps:', style=continent_style),
                html.Ul(
                    [
                        html.Li("Pick an Incident"),
                        html.Li("Select a Date (This is imperative in order to get the result)"),
                        html.Li(
                            "Result might not show due to the time chosen (dataset does not exist for that particular time)"),
                    ]
                ),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Pick the Incident:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.Dropdown(id='dropdown_col_he', options=p_col,
                                     value=['Total_Fatal_Injuries', 'Total_Serious_Injuries'],
                                     multi=True),
                    ], width=10),
                ], align='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.P('Select Date:', style=cat_style),
                    ], width=2),
                    dbc.Col([
                        dcc.DatePickerRange(id='date_10',
                                            min_date_allowed=date(1974, 1, 1),
                                            max_date_allowed=date(2023, 1, 1)
                                            ),
                    ], width=10),
                ], align='center'),
                dcc.Graph(id='my-graph10'),
            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='heat-content',
)

about_layout = html.Div(
    children=[
        html.P('About the Model', className='header-title-about', style=heading_style),
        html.Hr(),
        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.Img(src='assets/image1.png',
                                 style={'width': '100%', 'border-radius': '10%', 'margin-right': '5%'}),
                    ], width=5),
                    dbc.Col([
                        html.P('Aviation accidents pose significant risks to human life and the aviation industry. '
                               'Understanding their causes and contributing factors is crucial for enhancing safety and '
                               'preventing future incidents. This abstract provides an overview of aviation accident analysis, '
                               'its importance, methods employed, and desired outcomes.',
                               style={'margin-top': '4%',
                                      'text-align': 'justify'}),
                        html.P(
                            'Aviation accident analysis involves systematic investigation to determine causes and contributing factors.'
                            ' It employs methodologies such as accident scene investigation, data analysis, human factors'
                            ' analysis, and simulation modeling. These approaches analyze technical malfunctions, human errors, '
                            'environmental conditions, and organizational factors.',
                            style={'text-align': 'justify'}),
                    ], width=7),
                ], align='center'),
                dbc.Row([
                    dbc.Col([
                        html.P(
                            'The primary goal of aviation accident analysis is to identify root causes and develop effective safety recommendations.'
                            ' It enhances safety standards, improves operational procedures, and implements necessary changes. Insights '
                            'gained help understand complex interactions between humans, technological systems, and organizations.'
                            ' Valuable lessons learned lead to improved training programs, enhanced aircraft design, and regulatory enhancements.',
                            style={'text-align': 'justify'}),
                        html.P(
                            'Accident analysis also contributes to safety research and the development of new technologies. '
                            'It refines predictive models, establishes proactive safety measures, and improves safety regulations,'
                            ' standards, and practices.',
                            style={'text-align': 'justify'}),
                    ], width=7),
                    dbc.Col([
                        html.Img(src='assets/image2.png',
                                 style={'width': '100%', 'border-radius': '10%', 'margin-right': '5%'}),
                    ], width=5),
                ], align='center'),
                dbc.Row([
                    dbc.Col([
                        html.Img(src='assets/image3.png',
                                 style={'width': '100%', 'border-radius': '3%', 'margin-right': '5%'}),
                    ], width=5),
                    dbc.Col([
                        html.P(
                            'In conclusion, aviation accident analysis plays a critical role in enhancing safety. '
                            'By investigating accidents, identifying root causes, and implementing safety recommendations,'
                            ' it prevents future incidents and improves overall safety in the aviation industry. Continued investment '
                            'in accident analysis research and collaboration between stakeholders is essential for ongoing improvement.',
                            style={'text-align': 'justify'})
                    ], width=7),
                ], align='center'),

            ]),
        ),
    ],
    style={'margin-top': '2.5%'},
    className='about-content',
)


@my_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return main_content
    elif pathname == "/line":
        return line_layout
    elif pathname == "/bar":
        return bar_layout
    elif pathname == "/pie":
        return pie_layout
    elif pathname == "/displot":
        return dis_layout
    elif pathname == "/kde":
        return kde_layout
    elif pathname == "/scatter":
        return scatter_layout
    elif pathname == "/box":
        return box_layout
    elif pathname == "/histogram":
        return hist_layout
    elif pathname == "/pair":
        return pair_layout
    elif pathname == "/heat-map":
        return heat_layout
    elif pathname == "/about":
        return about_layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@my_app.callback(
    [
        Output(component_id='a_1', component_property='style'),
        Output(component_id='a_2', component_property='style'),
        Output(component_id='a_3', component_property='style'),
        Output(component_id='a_4', component_property='style'),
        Output(component_id='a_5', component_property='style'),
        Output(component_id='a_6', component_property='style'),
        Output(component_id='a_7', component_property='style'),
        Output(component_id='a_8', component_property='style'),
        Output(component_id='a_9', component_property='style'),
        Output(component_id='a_10', component_property='style'),
        Output(component_id='my-graph', component_property='figure'),
    ],
    [
        Input(component_id='dropdown_col', component_property='value'),
        Input(component_id='dropdown_country', component_property='value'),
        Input(component_id='dropdown_month', component_property='value'),
        Input(component_id='dropdown_day', component_property='value'),
        Input(component_id='dropdown_sev', component_property='value'),
        Input(component_id='dropdown_ety', component_property='value'),
        Input(component_id='dropdown_weather', component_property='value'),
        Input(component_id='dropdown_am', component_property='value'),
        Input(component_id='dropdown_it', component_property='value'),
        Input(component_id='dropdown_ad', component_property='value'),
        Input(component_id='dropdown_numo', component_property='value'),
        Input(component_id='date_1', component_property='start_date'),
        Input(component_id='date_1', component_property='end_date')
    ]
)
def update_line(col, country, month, day, sev, ety, weather, am, it, ad, numo, d1, d2):
    df_ = df.copy()
    df_ = df_[(df_['Event_Date'] >= d1) & (df_['Event_Date'] <= d2)]
    mask = []
    if col == cat_col[0]:
        mask = df_[col].isin(country)
    elif col == cat_col[1]:
        mask = df_[col].isin(month)
    elif col == cat_col[2]:
        mask = df_[col].isin(day)
    elif col == cat_col[3]:
        mask = df_[col].isin(sev)
    elif col == cat_col[4]:
        mask = df_[col].isin(ety)
    elif col == cat_col[5]:
        mask = df_[col].isin(weather)
    elif col == cat_col[6]:
        mask = df_[col].isin(am)
    elif col == cat_col[7]:
        mask = df_[col].isin(it)
    elif col == cat_col[8]:
        mask = df_[col].isin(ad)
    elif col == cat_col[9]:
        mask = df_[col].isin(numo)

    filtered_df = df_[mask]
    grouped = filtered_df.groupby([col, 'Year']).size().reset_index(name='Count')

    # create a line plot using Plotly
    fig = px.line(grouped, x='Year', y='Count', color=col,
                  title=f'Aviation Accidents by {col} over the Years').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    if col == cat_col[0]:
        return block, none, none, none, none, none, none, none, none, none, fig
    elif col == cat_col[1]:
        return none, block, none, none, none, none, none, none, none, none, fig
    elif col == cat_col[2]:
        return none, none, block, none, none, none, none, none, none, none, fig
    elif col == cat_col[3]:
        return none, none, none, block, none, none, none, none, none, none, fig
    elif col == cat_col[4]:
        return none, none, none, none, block, none, none, none, none, none, fig
    elif col == cat_col[5]:
        return none, none, none, none, none, block, none, none, none, none, fig
    elif col == cat_col[6]:
        return none, none, none, none, none, none, block, none, none, none, fig
    elif col == cat_col[7]:
        return none, none, none, none, none, none, none, block, none, none, fig
    elif col == cat_col[8]:
        return none, none, none, none, none, none, none, none, block, none, fig
    elif col == cat_col[9]:
        return none, none, none, none, none, none, none, none, none, block, fig


@my_app.callback(
    [
        Output(component_id='b_1', component_property='style'),
        Output(component_id='b_2', component_property='style'),
        Output(component_id='b_3', component_property='style'),
        Output(component_id='b_4', component_property='style'),
        Output(component_id='b_5', component_property='style'),
        Output(component_id='b_6', component_property='style'),
        Output(component_id='b_7', component_property='style'),
        Output(component_id='b_8', component_property='style'),
        Output(component_id='b_9', component_property='style'),
        Output(component_id='b_10', component_property='style'),
        Output(component_id='my-graph2', component_property='figure'),
    ],
    [
        Input(component_id='dropdown_col_bar', component_property='value'),
        Input(component_id='radio_bar', component_property='value'),
        Input(component_id='dropdown_country_bar', component_property='value'),
        Input(component_id='dropdown_month_bar', component_property='value'),
        Input(component_id='dropdown_day_bar', component_property='value'),
        Input(component_id='dropdown_sev_bar', component_property='value'),
        Input(component_id='dropdown_ety_bar', component_property='value'),
        Input(component_id='dropdown_weather_bar', component_property='value'),
        Input(component_id='dropdown_am_bar', component_property='value'),
        Input(component_id='dropdown_it_bar', component_property='value'),
        Input(component_id='dropdown_ad_bar', component_property='value'),
        Input(component_id='dropdown_numo_bar', component_property='value'),
        Input(component_id='date_2', component_property='start_date'),
        Input(component_id='date_2', component_property='end_date')
    ]
)
def update_bar(col, plot, country, month, day, sev, ety, weather, am, it, ad, numo, d1, d2):
    df_2 = df.copy()
    df_2 = df_2[(df_2['Event_Date'] >= d1) & (df_2['Event_Date'] <= d2)]
    mask = []
    if col == cat_col[0]:
        mask = df_2[col].isin(country)
    elif col == cat_col[1]:
        mask = df_2[col].isin(month)
    elif col == cat_col[2]:
        mask = df_2[col].isin(day)
    elif col == cat_col[3]:
        mask = df_2[col].isin(sev)
    elif col == cat_col[4]:
        mask = df_2[col].isin(ety)
    elif col == cat_col[5]:
        mask = df_2[col].isin(weather)
    elif col == cat_col[6]:
        mask = df_2[col].isin(am)
    elif col == cat_col[7]:
        mask = df_2[col].isin(it)
    elif col == cat_col[8]:
        mask = df_2[col].isin(ad)
    elif col == cat_col[9]:
        mask = df_2[col].isin(numo)

    filtered_df = df_2[mask]
    grouped = filtered_df.groupby([col, 'Year']).size().reset_index(name='Count')
    if plot == 'Time Series Stack Plot':
        fig = px.bar(grouped, x='Year', y='Count', color=col, barmode='stack',
                     title=f'Aviation Accidents by {col} over the Years').update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )
    else:
        fig = px.bar(grouped, x='Year', y='Count', color=col, barmode='group',
                     title=f'Aviation Accidents by {col} over the Years').update_layout(
            template='plotly_dark',
            plot_bgcolor='rgba(0, 0, 0, 0)',
            paper_bgcolor='rgba(0, 0, 0, 0)',
        )

    if col == cat_col[0]:
        return block, none, none, none, none, none, none, none, none, none, fig
    elif col == cat_col[1]:
        return none, block, none, none, none, none, none, none, none, none, fig
    elif col == cat_col[2]:
        return none, none, block, none, none, none, none, none, none, none, fig
    elif col == cat_col[3]:
        return none, none, none, block, none, none, none, none, none, none, fig
    elif col == cat_col[4]:
        return none, none, none, none, block, none, none, none, none, none, fig
    elif col == cat_col[5]:
        return none, none, none, none, none, block, none, none, none, none, fig
    elif col == cat_col[6]:
        return none, none, none, none, none, none, block, none, none, none, fig
    elif col == cat_col[7]:
        return none, none, none, none, none, none, none, block, none, none, fig
    elif col == cat_col[8]:
        return none, none, none, none, none, none, none, none, block, none, fig
    elif col == cat_col[9]:
        return none, none, none, none, none, none, none, none, none, block, fig


@my_app.callback(
    [
        Output(component_id='my-graph3', component_property='figure'),
    ],
    [
        Input(component_id='dropdown_col_pie', component_property='value'),
        Input(component_id='date_3', component_property='start_date'),
        Input(component_id='date_3', component_property='end_date')
    ]
)
def update_pie(col, d1, d2):
    df_3 = df.copy()
    df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    counts = df_3[col].value_counts().reset_index()
    counts.columns = [col, 'Count']

    fig = px.pie(counts, values='Count', names=col, title=f'Pie Chart of the Distribution of {col}').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return [fig]


@my_app.callback(
    Output(component_id='my-graph4', component_property='figure'),
    [
        Input(component_id='dropdown_col_dis', component_property='value'),
        Input(component_id='dis_check', component_property='value'),
        Input(component_id='dropdown_col_dis_2', component_property='value'),
        Input(component_id='date_4', component_property='start_date'),
        Input(component_id='date_4', component_property='end_date')
    ]
)
def update_dis(col, check, col2, d1, d2):
    df_3 = df.copy()
    if 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Number_of_passengers'] < 20) & (df_3['Number_of_passengers'] >= 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[(df_3['Number_of_passengers'] >= 20) & (df_3['Number_of_passengers'] < 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    fig = px.histogram(df_3, x=col, color=col2, nbins=10, title=f'Displot of {col} with {col2}').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig


@my_app.callback(
    Output(component_id='my-graph5', component_property='figure'),
    [
        Input(component_id='dropdown_col_kde', component_property='value'),
        Input(component_id='kde_check', component_property='value'),
        Input(component_id='dropdown_col_kde_2', component_property='value'),
        Input(component_id='date_5', component_property='start_date'),
        Input(component_id='date_5', component_property='end_date')
    ]
)
def update_kde(col, check, col2, d1, d2):
    df_3 = df.copy()
    if 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Number_of_passengers'] < 20) & (df_3['Number_of_passengers'] >= 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[(df_3['Number_of_passengers'] >= 20) & (df_3['Number_of_passengers'] < 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    fig = px.density_contour(df_3, x=col, color=col2, title=f'KDE of {col} with {col2}').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig


@my_app.callback(
    Output(component_id='my-graph6', component_property='figure'),
    [
        Input(component_id='dropdown_col_sc', component_property='value'),
        Input(component_id='sc_check', component_property='value'),
        Input(component_id='dropdown_col_sc_2', component_property='value'),
        Input(component_id='dropdown_col_sc_3', component_property='value'),
        Input(component_id='date_6', component_property='start_date'),
        Input(component_id='date_6', component_property='end_date')
    ]
)
def update_sc(col, check, col2, hue, d1, d2):
    df_3 = df.copy()
    if 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Number_of_passengers'] < 20) & (df_3['Number_of_passengers'] >= 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[(df_3['Number_of_passengers'] >= 20) & (df_3['Number_of_passengers'] < 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    fig = px.scatter(df_3, x=col, y=col2, color=hue, trendline='ols',
                     title=f'Scattered plot of {col} vs {col2} with {hue}').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig


@my_app.callback(
    Output(component_id='my-graph7', component_property='figure'),
    [
        Input(component_id='dropdown_col_bo', component_property='value'),
        Input(component_id='bo_check', component_property='value'),
        Input(component_id='dropdown_col_bo_2', component_property='value'),
        Input(component_id='dropdown_col_bo_3', component_property='value'),
        Input(component_id='date_7', component_property='start_date'),
        Input(component_id='date_7', component_property='end_date')
    ]
)
def update_box(col, check, col2, hue, d1, d2):
    df_3 = df.copy()
    if 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[(df_3['Number_of_passengers'] < 20) & (df_3['Number_of_passengers'] >= 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[(df_3['Number_of_passengers'] >= 20) & (df_3['Number_of_passengers'] < 200)]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' not in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' in check:
        df_3 = df_3[df_3['Number_of_passengers'] >= 200]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]
    elif 'Private Aircraft' in check and 'Chartered Aircraft' not in check and 'Commercial Aircraft' not in check:
        df_3 = df_3[df_3['Number_of_passengers'] < 20]
        df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    fig = px.box(df_3, x=col, y=col2, color=hue).update_layout(
        title=f'Box Plot of {col} vs {col2} with {hue}',
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig


@my_app.callback(
    [
        Output(component_id='h_1', component_property='style'),
        Output(component_id='h_2', component_property='style'),
        Output(component_id='h_3', component_property='style'),
        Output(component_id='h_4', component_property='style'),
        Output(component_id='h_5', component_property='style'),
        Output(component_id='h_6', component_property='style'),
        Output(component_id='h_7', component_property='style'),
        Output(component_id='h_8', component_property='style'),
        Output(component_id='h_9', component_property='style'),
        Output(component_id='h_10', component_property='style'),
        Output(component_id='my-graph8', component_property='figure'),
    ],
    [
        Input(component_id='dropdown_col_h', component_property='value'),
        Input(component_id='dropdown_country_h', component_property='value'),
        Input(component_id='dropdown_month_h', component_property='value'),
        Input(component_id='dropdown_day_h', component_property='value'),
        Input(component_id='dropdown_sev_h', component_property='value'),
        Input(component_id='dropdown_ety_h', component_property='value'),
        Input(component_id='dropdown_weather_h', component_property='value'),
        Input(component_id='dropdown_am_h', component_property='value'),
        Input(component_id='dropdown_it_h', component_property='value'),
        Input(component_id='dropdown_ad_h', component_property='value'),
        Input(component_id='dropdown_numo_h', component_property='value'),
        Input(component_id='date_8', component_property='start_date'),
        Input(component_id='date_8', component_property='end_date')
    ]
)
def update_hist(col, country, month, day, sev, ety, weather, am, it, ad, numo, d1, d2):
    df_ = df.copy()
    df_ = df_[(df_['Event_Date'] >= d1) & (df_['Event_Date'] <= d2)]
    mask = []
    if col == cat_col[0]:
        mask = df_[col].isin(country)
    elif col == cat_col[1]:
        mask = df_[col].isin(month)
    elif col == cat_col[2]:
        mask = df_[col].isin(day)
    elif col == cat_col[3]:
        mask = df_[col].isin(sev)
    elif col == cat_col[4]:
        mask = df_[col].isin(ety)
    elif col == cat_col[5]:
        mask = df_[col].isin(weather)
    elif col == cat_col[6]:
        mask = df_[col].isin(am)
    elif col == cat_col[7]:
        mask = df_[col].isin(it)
    elif col == cat_col[8]:
        mask = df_[col].isin(ad)
    elif col == cat_col[9]:
        mask = df_[col].isin(numo)

    filtered_df = df_[mask]
    grouped = filtered_df.groupby([col, 'Year']).size().reset_index(name='Count')

    # create a line plot using Plotly
    fig = px.histogram(grouped, x='Year', y='Count', color=col, marginal='violin',
                       title=f'Aviation Accidents by {col} over the Years').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    if col == cat_col[0]:
        return block, none, none, none, none, none, none, none, none, none, fig
    elif col == cat_col[1]:
        return none, block, none, none, none, none, none, none, none, none, fig
    elif col == cat_col[2]:
        return none, none, block, none, none, none, none, none, none, none, fig
    elif col == cat_col[3]:
        return none, none, none, block, none, none, none, none, none, none, fig
    elif col == cat_col[4]:
        return none, none, none, none, block, none, none, none, none, none, fig
    elif col == cat_col[5]:
        return none, none, none, none, none, block, none, none, none, none, fig
    elif col == cat_col[6]:
        return none, none, none, none, none, none, block, none, none, none, fig
    elif col == cat_col[7]:
        return none, none, none, none, none, none, none, block, none, none, fig
    elif col == cat_col[8]:
        return none, none, none, none, none, none, none, none, block, none, fig
    elif col == cat_col[9]:
        return none, none, none, none, none, none, none, none, none, block, fig


@my_app.callback(
    Output(component_id='my-graph9', component_property='figure'),
    [
        Input(component_id='dropdown_col_p', component_property='value'),
        Input(component_id='width', component_property='value'),
        Input(component_id='height', component_property='value'),
        Input(component_id='date_9', component_property='start_date'),
        Input(component_id='date_9', component_property='end_date')
    ]
)
def update_pair(col, width, height, d1, d2):
    df_3 = df.copy()
    df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    fig = px.scatter_matrix(df_3[col], title=f'Pair Plot between {col}').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        width=width,  # set the width of the plot
        height=height,  # set the height of the plot
    )
    fig.update_traces(diagonal_visible=False)

    return fig


@my_app.callback(
    Output(component_id='my-graph10', component_property='figure'),
    [
        Input(component_id='dropdown_col_he', component_property='value'),
        Input(component_id='date_10', component_property='start_date'),
        Input(component_id='date_10', component_property='end_date')
    ]
)
def update_heat(col, d1, d2):
    df_3 = df.copy()
    df_3 = df_3[(df_3['Event_Date'] >= d1) & (df_3['Event_Date'] <= d2)]

    corr = df_3[col].corr()

    fig = px.density_heatmap(corr, title=f'Density Heat Map between {col}').update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )

    return fig


if __name__ == '__main__':
    my_app.run_server(debug=True, host='0.0.0.0', port=8010)
