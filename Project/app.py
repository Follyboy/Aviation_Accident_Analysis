import dash
import pandas as pd
from dash import dcc
from dash import html
from datetime import date
import plotly.express as px
from dash.dependencies import Input, Output

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
    'background-color': '#F2F2F2',
    'text-align': 'center',
}

# Question 6
q6_style = {'width': '50%', 'display': 'inline-block',
            'vertical-align': 'middle'}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
my_app = dash.Dash('HW4', external_stylesheets=external_stylesheets)
server = my_app.server

my_app.layout = html.Div([
    html.Div(
        className='header',
        children=[
            html.H1('Aviation Accident Analysis', className='header-title'),
            html.H6('Author: Folaranmi Adeyeri', className='header-title'),
        ],
        style=input_style
    ),
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='LINE', value='tab1', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Category"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                    html.Li("Pick from the option display for that category"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col', options=value_cat_col, value='Country', multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_1',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            html.Div(id='a_1', children=[
                html.H1('Aviation Accident Analysis by Country over the years', style=input_style_title),
                html.H3('Pick the Country or Ocean'),
                dcc.Dropdown(id='dropdown_country', options=value_country_col, value=['United States'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_2', children=[
                html.H1('Aviation Analysis by Month over the years', style=input_style_title),
                html.H3('Pick the Month'),
                dcc.Dropdown(id='dropdown_month', options=value_month_col, value=['January'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_3', children=[
                html.H1('Aviation Analysis by Day over the years', style=input_style_title),
                html.H3('Pick the Day'),
                dcc.Dropdown(id='dropdown_day', options=value_day_col, value=['Monday'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_4', children=[
                html.H1('Aviation Analysis by Injury Severity over the years', style=input_style_title),
                html.H3('Pick the Injury Severity'),
                dcc.Dropdown(id='dropdown_sev', options=value_sev_col, value=['Fatal'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_5', children=[
                html.H1('Aviation Analysis by Engine Type over the years', style=input_style_title),
                html.H3('Pick the Engine Type'),
                dcc.Dropdown(id='dropdown_ety', options=value_ety_col, value=['Reciprocating'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_6', children=[
                html.H1('Aviation Analysis by Weather Condition over the years', style=input_style_title),
                html.H3('Pick the Weather Condition'),
                dcc.Dropdown(id='dropdown_weather', options=value_weather_col, value=['IMC'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_7', children=[
                html.H1('Aviation Accident Analysis by Amateur Built Aircraft over the years', style=input_style_title),
                html.H3('Pick the Amateur Built'),
                dcc.Dropdown(id='dropdown_am', options=value_am_col, value=['Yes'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_8', children=[
                html.H1('Aviation Accident Analysis by Investigation Type over the years', style=input_style_title),
                html.H3('Pick the Investigation Type'),
                dcc.Dropdown(id='dropdown_it', options=value_it_col, value=['Accident'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_9', children=[
                html.H1('Aviation Accident Analysis by Aircraft damage over the years', style=input_style_title),
                html.H3('Pick the Aircraft damage'),
                dcc.Dropdown(id='dropdown_ad', options=value_ad_col, value=['Destroyed'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='a_10', children=[
                html.H1('Aviation Accident Analysis by Number of Engines in Aircraft over the years',
                        style=input_style_title),
                html.H3('Pick the Number of Engines'),
                dcc.Dropdown(id='dropdown_numo', options=value_numo_col, value=['2'], multi=True),
            ], style={'display': 'none'}),
            dcc.Graph(id='my-graph'),
        ]),
        dcc.Tab(label='BAR', value='tab2', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Category"),
                    html.Li("Pick the type of plot"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                    html.Li("Pick from the option display for that category"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col_bar', options=value_cat_col, value='Country', multi=False),
            html.H3('Pick Plot'),
            dcc.RadioItems(
                id='radio_bar',
                options=[
                    {'label': 'Time Series Stack Plot', 'value': 'Time Series Stack Plot'},
                    {'label': 'Time Series Group Plot', 'value': 'Time Series Group Plot'},
                ],
                value='Time Series Stack Plot',
                labelStyle={'display': 'inline', 'margin': '10px'}
            ),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_2',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            html.Div(id='b_1', children=[
                html.H1('Aviation Accident Analysis by Country over the years', style=input_style_title),
                html.H3('Pick the Country or Ocean'),
                dcc.Dropdown(id='dropdown_country_bar', options=value_country_col, value=['United States'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_2', children=[
                html.H1('Aviation Analysis by Month over the years', style=input_style_title),
                html.H3('Pick the Month'),
                dcc.Dropdown(id='dropdown_month_bar', options=value_month_col, value=['January'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_3', children=[
                html.H1('Aviation Analysis by Day over the years', style=input_style_title),
                html.H3('Pick the Day'),
                dcc.Dropdown(id='dropdown_day_bar', options=value_day_col, value=['Monday'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_4', children=[
                html.H1('Aviation Analysis by Injury Severity over the years', style=input_style_title),
                html.H3('Pick the Injury Severity'),
                dcc.Dropdown(id='dropdown_sev_bar', options=value_sev_col, value=['Fatal'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_5', children=[
                html.H1('Aviation Analysis by Engine Type over the years', style=input_style_title),
                html.H3('Pick the Engine Type'),
                dcc.Dropdown(id='dropdown_ety_bar', options=value_ety_col, value=['Reciprocating'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_6', children=[
                html.H1('Aviation Analysis by Weather Condition over the years', style=input_style_title),
                html.H3('Pick the Weather Condition'),
                dcc.Dropdown(id='dropdown_weather_bar', options=value_weather_col, value=['IMC'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_7', children=[
                html.H1('Aviation Accident Analysis by Amateur Built Aircraft over the years', style=input_style_title),
                html.H3('Pick the Amateur Built'),
                dcc.Dropdown(id='dropdown_am_bar', options=value_am_col, value=['Yes'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_8', children=[
                html.H1('Aviation Accident Analysis by Investigation Type over the years', style=input_style_title),
                html.H3('Pick the Investigation Type'),
                dcc.Dropdown(id='dropdown_it_bar', options=value_it_col, value=['Accident'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_9', children=[
                html.H1('Aviation Accident Analysis by Aircraft damage over the years', style=input_style_title),
                html.H3('Pick the Aircraft damage'),
                dcc.Dropdown(id='dropdown_ad_bar', options=value_ad_col, value=['Destroyed'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='b_10', children=[
                html.H1('Aviation Accident Analysis by Number of Engines in Aircraft over the years',
                        style=input_style_title),
                html.H3('Pick the Number of Engines'),
                dcc.Dropdown(id='dropdown_numo_bar', options=value_numo_col, value=['2'], multi=True),
            ], style={'display': 'none'}),
            dcc.Graph(id='my-graph2'),
            html.Br(),
        ]),
        dcc.Tab(label='PIE CHART', value='tab3', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Category"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col_pie', options=value_cat_col_1, value='Month', multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_3',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            dcc.Graph(id='my-graph3'),
        ]),
        dcc.Tab(label='DISPLOT', value='tab4', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick an Incident you want to analyze"),
                    html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                    html.Li("Pick a Category"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Incident'),
            dcc.Dropdown(id='dropdown_col_dis', options=dis_col, value='Total_Fatal_Injuries', multi=False),
            html.Br(),
            dcc.Checklist(
                id='dis_check',
                options=dis_col_2_,
                value=dis_col_2,
                inline=True,
                labelStyle={'margin-right': '10px'}
            ),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col_dis_2', options=value_cat_col_1, value='Amateur_Built', multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_4',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            dcc.Graph(id='my-graph4'),
        ]),
        dcc.Tab(label='KDE', value='tab5', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick an Incident you want to analyze"),
                    html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                    html.Li("Pick Hue (This will analyze other data points in your plot)"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Incident'),
            dcc.Dropdown(id='dropdown_col_kde', options=dis_col, value='Total_Fatal_Injuries', multi=False),
            html.Br(),
            dcc.Checklist(
                id='kde_check',
                options=dis_col_2_,
                value=dis_col_2,
                inline=True,
                labelStyle={'margin-right': '10px'}
            ),
            html.H3('Hue'),
            dcc.Dropdown(id='dropdown_col_kde_2', options=cat_col_1, value='Total_Fatal_Injuries', multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_5',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            dcc.Graph(id='my-graph5'),
        ]),
        dcc.Tab(label='SCATTER', value='tab6', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick an Incident you want to analyze"),
                    html.Li("Pick an second Incident you want to analyze against the first"),
                    html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                    html.Li("Pick Hue (This will analyze other data points in your plot)"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Incident'),
            dcc.Dropdown(id='dropdown_col_sc', options=dis_col, value='Total_Fatal_Injuries', multi=False),
            html.Br(),
            dcc.Checklist(
                id='sc_check',
                options=dis_col_2_,
                value=dis_col_2,
                inline=True,
                labelStyle={'margin-right': '10px'}
            ),
            html.H3('Pick the Second Incident'),
            dcc.Dropdown(id='dropdown_col_sc_2', options=dis_col, value='Total_Fatal_Injuries', multi=False),
            html.H3('Hue'),
            dcc.Dropdown(id='dropdown_col_sc_3', options=cat_col_1, multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_6',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            dcc.Graph(id='my-graph6'),
        ]),
        dcc.Tab(label='BOX', value='tab7', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Category"),
                    html.Li("Select multiple aircraft sizes you are wanting to analyze"),
                    html.Li("Pick an Incident you want to analyze"),
                    html.Li("Pick Hue (This will analyze other data points in your plot)"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col_bo', options=cat_col_1, value='Day', multi=False),
            html.Br(),
            dcc.Checklist(
                id='bo_check',
                options=dis_col_2_,
                value=dis_col_2,
                inline=True,
                labelStyle={'margin-right': '10px'}
            ),
            html.H3('Pick the Incident'),
            dcc.Dropdown(id='dropdown_col_bo_2', options=dis_col, value='Total_Fatal_Injuries', multi=False),
            html.H3('Hue'),
            dcc.Dropdown(id='dropdown_col_bo_3', options=cat_col, multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_7',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            dcc.Graph(id='my-graph7'),
        ]),
        dcc.Tab(label='HISTOGRAM', value='tab8', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Category"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                    html.Li("Pick from the option display for that category"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col_h', options=value_cat_col, value='Country', multi=False),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_8',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            html.Div(id='h_1', children=[
                html.H1('Aviation Accident Analysis by Country over the years', style=input_style_title),
                html.H3('Pick the Country or Ocean'),
                dcc.Dropdown(id='dropdown_country_h', options=value_country_col, value=['United States'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_2', children=[
                html.H1('Aviation Analysis by Month over the years', style=input_style_title),
                html.H3('Pick the Month'),
                dcc.Dropdown(id='dropdown_month_h', options=value_month_col, value=['January'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_3', children=[
                html.H1('Aviation Analysis by Day over the years', style=input_style_title),
                html.H3('Pick the Day'),
                dcc.Dropdown(id='dropdown_day_h', options=value_day_col, value=['Monday'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_4', children=[
                html.H1('Aviation Analysis by Injury Severity over the years', style=input_style_title),
                html.H3('Pick the Injury Severity'),
                dcc.Dropdown(id='dropdown_sev_h', options=value_sev_col, value=['Fatal'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_5', children=[
                html.H1('Aviation Analysis by Engine Type over the years', style=input_style_title),
                html.H3('Pick the Engine Type'),
                dcc.Dropdown(id='dropdown_ety_h', options=value_ety_col, value=['Reciprocating'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_6', children=[
                html.H1('Aviation Analysis by Weather Condition over the years', style=input_style_title),
                html.H3('Pick the Weather Condition'),
                dcc.Dropdown(id='dropdown_weather_h', options=value_weather_col, value=['IMC'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_7', children=[
                html.H1('Aviation Accident Analysis by Amateur Built Aircraft over the years', style=input_style_title),
                html.H3('Pick the Amateur Built'),
                dcc.Dropdown(id='dropdown_am_h', options=value_am_col, value=['Yes'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_8', children=[
                html.H1('Aviation Accident Analysis by Investigation Type over the years', style=input_style_title),
                html.H3('Pick the Investigation Type'),
                dcc.Dropdown(id='dropdown_it_h', options=value_it_col, value=['Accident'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_9', children=[
                html.H1('Aviation Accident Analysis by Aircraft damage over the years', style=input_style_title),
                html.H3('Pick the Aircraft damage'),
                dcc.Dropdown(id='dropdown_ad_h', options=value_ad_col, value=['Destroyed'], multi=True),
            ], style={'display': 'none'}),
            html.Div(id='h_10', children=[
                html.H1('Aviation Accident Analysis by Number of Engines in Aircraft over the years',
                        style=input_style_title),
                html.H3('Pick the Number of Engines'),
                dcc.Dropdown(id='dropdown_numo_h', options=value_numo_col, value=['2'], multi=True),
            ], style={'display': 'none'}),
            dcc.Graph(id='my-graph8'),
        ]),
        dcc.Tab(label='PAIR', value='tab9', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Category"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                    html.Li("Set width you want for your graph (Default is already set to 1500)"),
                    html.Li("Set height you want for your graph (Default is already set to 800)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Category'),
            dcc.Dropdown(id='dropdown_col_p', options=p_col, value='Total_Fatal_Injuries', multi=True),
            html.Br(),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_9',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            html.H3('Width:'),
            dcc.Input(
                id='width',
                type='number',
                value=1500,
                min=500,
                step=1
            ),
            html.H3('Height:'),
            dcc.Input(
                id='height',
                type='number',
                value=800,
                min=500,
                step=1
            ),
            dcc.Graph(id='my-graph9'),
        ]),
        dcc.Tab(label='HEAT MAP', value='tab10', children=[
            html.H3('Steps:'),
            html.Ul(
                [
                    html.Li("Pick a Incident"),
                    html.Li("Select a Date (This is imperative in order to get the result)"),
                ]
            ),
            html.Br(),
            html.H3('Pick the Incident'),
            dcc.Dropdown(id='dropdown_col_he', options=p_col, value=['Total_Fatal_Injuries', 'Total_Serious_Injuries'],
                         multi=True),
            html.Br(),
            html.H3('Select Date'),
            dcc.DatePickerRange(id='date_10',
                                min_date_allowed=date(1974, 1, 1),
                                max_date_allowed=date(2023, 1, 1)
                                ),
            dcc.Graph(id='my-graph10'),
        ]),
    ])
])


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
    fig = px.line(grouped, x='Year', y='Count', color=col, title=f'Aviation Accidents by {col} over the Years')

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
                     title=f'Aviation Accidents by {col} over the Years')
    else:
        fig = px.bar(grouped, x='Year', y='Count', color=col, barmode='group',
                     title=f'Aviation Accidents by {col} over the Years')

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

    fig = px.pie(counts, values='Count', names=col, title=f'Pie Chart of the Distribution of {col}')

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

    fig = px.histogram(df_3, x=col, color=col2, nbins=10, title=f'Displot of {col} with {col2}')

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

    fig = px.density_contour(df_3, x=col, color=col2, title=f'KDE of {col} with {col2}')

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

    fig = px.scatter(df_3, x=col, y=col2, color=hue, trendline='ols', title=f'Scattered plot of {col} vs {col2} with {hue}')

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

    fig = px.box(df_3, x=col, y=col2, color=hue)
    fig.update_layout(
        title=f'Box Plot of {col} vs {col2} with {hue}',
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
                       title=f'Aviation Accidents by {col} over the Years')

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

    fig = px.scatter_matrix(df_3[col], title=f'Pair Plot between {col}')
    fig.update_traces(diagonal_visible=False)
    fig.update_layout(
        width=width,  # set the width of the plot
        height=height,  # set the height of the plot
    )

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

    fig = px.density_heatmap(corr, title=f'Density Heat Map between {col}')

    return fig


if __name__ == '__main__':
    my_app.run_server(debug=True, host='0.0.0.0', port=8010)
