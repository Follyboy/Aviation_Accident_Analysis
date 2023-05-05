import numpy as np
import pandas as pd

if __name__ == '__main__':
    # Load Original Data
    url = 'https://raw.githubusercontent.com/Follyboy/USA_Aviation_Accident_Analysis/main/Project/AviationData.csv'
    df = pd.read_csv(url, sep=",", encoding='cp1252', dtype='unicode')
    print(df.head())

    # Edit and Arrange names of columns
    df = df.rename(columns=lambda x: x.replace('.', '_'))
    arrange_col = ['Event_Date', 'Investigation_Type', 'Location', 'Country',
                   'Airport_Name', 'Injury_Severity', 'Aircraft_damage',
                   'Aircraft_Category', 'Make', 'Model', 'Amateur_Built', 'Number_of_Engines',
                   'Engine_Type', 'FAR_Description', 'Purpose_of_flight', 'Air_carrier',
                   'Total_Fatal_Injuries', 'Total_Serious_Injuries', 'Total_Minor_Injuries',
                   'Total_Uninjured', 'Weather_Condition', 'Broad_phase_of_flight', 'Report_Status']
    df = df[arrange_col]

    # Print number of observations in original dataset
    print(f'There are {len(df)} observations in the original dataset')
    print('=========================================================')
    print(df.isna().sum())
    print('=========================================================')

    # Remove or replace values that do not make sense in different columns
    country_values_to_drop = ['AY', 'BLOCK 651A', 'MISSING', 'UN']
    injury_values_to_drop = ['Unavailable']
    df = df[~df['Country'].isin(country_values_to_drop)]
    df = df[~df['Injury_Severity'].isin(injury_values_to_drop)]
    df = df.dropna(subset=['Aircraft_damage', 'Country', 'Engine_Type', 'Number_of_Engines', 'Injury_Severity', 'Total_Serious_Injuries', 'Total_Fatal_Injuries', 'Total_Minor_Injuries', 'Total_Uninjured', 'Weather_Condition'])
    df.loc[df['Injury_Severity'].str.startswith('Fatal'), 'Injury_Severity'] = 'Fatal'

    # Drop columns that are not needed in this analysis
    drop_columns = ['Location', 'Airport_Name', 'Aircraft_Category', 'Air_carrier',
                    'FAR_Description', 'Broad_phase_of_flight', 'Model', 'Report_Status',
                    'Purpose_of_flight', 'Make'
                    ]
    df = df.drop(drop_columns, axis=1)

    # Copy dataframe and create new dataframe that replaces unknown values with nan
    df_ = df.copy()
    df_.loc[df_['Weather_Condition'] == 'Unk', 'Weather_Condition'] = np.nan
    df_.loc[df_['Weather_Condition'] == 'UNK', 'Weather_Condition'] = np.nan
    df_.loc[df_['Aircraft_damage'] == 'Unknown', 'Aircraft_damage'] = np.nan
    df_.loc[df_['Number_of_Engines'] == '0', 'Number_of_Engines'] = np.nan
    df_.loc[df_['Engine_Type'] == 'Unknown', 'Engine_Type'] = np.nan
    df_.loc[df_['Engine_Type'] == 'UNK', 'Engine_Type'] = np.nan
    df_.loc[df_['Engine_Type'] == 'None', 'Engine_Type'] = np.nan

    # Clean up dataset to give areas accident happened meaningful spellings
    country_replacement = {
        'ATLANTIC OCEAN': 'Atlantic Ocean',
        'CARIBBEAN SEA': 'Caribbean Sea',
        "Cote D'ivoire": "Côte d'Ivoire",
        'Antigua And Barbuda': 'Antigua and Barbuda',
        'GULF OF MEXICO': 'Gulf of Mexico',
        'HIGH ISLAND': 'High Island',
        'PACIFIC OCEAN': 'Pacific Ocean',
        'Saint Vincent and the Grenadines': 'St Vincent And The Grenadines',
        'Turks And Caicos': 'Turks And Caicos Islands',
        'Korea, Republic Of': 'South Korea'
    }
    df_['Country'] = df_['Country'].replace(country_replacement)
    weather_na = df_['Weather_Condition'].isna().sum()
    print('=========================================================')
    print(f'There are {weather_na} missing values in the weather condition column')
    print('=========================================================')

    # dropping missing values
    df_ = df_.dropna(subset=['Weather_Condition', 'Number_of_Engines', 'Aircraft_damage', 'Engine_Type'])
    weather = df_['Weather_Condition'].unique()
    for i in weather:
        if i == 'IMC':
            print('=========================================================')
            print(f'The weather condition {i} stands for Instrument meteorological conditions. This basically means flying in cloudy or bad weather')
            print('=========================================================')
        else:
            print('=========================================================')
            print(f'The weather condition {i} stands for visual meteorological conditions. This means pilots ' +
                  f'have sufficient visibility to fly the aircraft maintaining visual separation from terrain ' +
                  f'and other aircraft.')
            print('=========================================================')

    weather_cond = df_['Weather_Condition'].isna().sum()
    print('=========================================================')
    print(f'After cleaning up the data, we have {weather_cond} missing values for the weather condition column')
    print('=========================================================')

    print('=========================================================')
    print(f'There are {len(df_)} observations in the cleaned up dataset, which is enough to carry out our analysis')
    print('=========================================================')
    print(df_.isna().sum())
    print('=========================================================')
    print('=========================================================')
    print(df_.dtypes)
    print('=========================================================')

    # Converting data types to correct data types
    df_['Total_Uninjured'] = df_['Total_Uninjured'].astype(int)
    df_['Total_Minor_Injuries'] = df_['Total_Minor_Injuries'].astype(int)
    df_['Total_Serious_Injuries'] = df_['Total_Serious_Injuries'].astype(int)
    df_['Total_Fatal_Injuries'] = df_['Total_Fatal_Injuries'].astype(int)
    df_['Number_of_Engines'] = df_['Number_of_Engines'].astype(int)
    print('=========================================================')
    print(df_.dtypes)
    print('=========================================================')

    #################################################
    #  CLEANED DATASET BEGINNING
    #################################################
    new_df = df_.reset_index(drop=True)
    new_df.to_csv('cleaned_dataframe.csv', index=False)
    print(new_df.head())

