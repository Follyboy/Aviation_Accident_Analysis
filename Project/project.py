import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from toolbox import calc_zscore, da_k_squared_test

if __name__ == '__main__':
    # Load Original Data
    url = 'https://raw.githubusercontent.com/Follyboy/Aviation_Accident_Analysis/main/Project/AviationData.csv'
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
    print(f'There are {len(df)} and {len(df.columns)} columns observations in the original dataset')
    print('=========================================================')
    print(df.isna().sum())
    print('=========================================================')

    # Remove or replace values that do not make sense in different columns
    country_values_to_drop = ['AY', 'BLOCK 651A', 'MISSING', 'UN']
    injury_values_to_drop = ['Unavailable']
    df = df[~df['Country'].isin(country_values_to_drop)]
    df = df[~df['Injury_Severity'].isin(injury_values_to_drop)]
    df = df.dropna(subset=['Aircraft_damage', 'Country', 'Engine_Type', 'Number_of_Engines', 'Injury_Severity',
                           'Total_Serious_Injuries', 'Total_Fatal_Injuries', 'Total_Minor_Injuries', 'Total_Uninjured',
                           'Weather_Condition'])
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
            print(
                f'The weather condition {i} stands for Instrument meteorological conditions. This basically means flying in cloudy or bad weather')
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

    df_['Event_Date'] = pd.to_datetime(df_['Event_Date'])
    df_['Year'] = df_['Event_Date'].dt.year
    df_['Month'] = df_['Event_Date'].dt.month_name()
    df_['Day'] = df_['Event_Date'].dt.day_name()

    print('=========================================================')
    print(
        f'There are {len(df_)} observations and {len(df_.columns)} columns in the cleaned up dataset, which is enough to carry out our analysis')
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

    ########################################
    # OUTLIER DETECTION AND REMOVAL
    ########################################
    print('=========================================================')
    calc_zscore(new_df, 'Total_Fatal_Injuries')
    calc_zscore(new_df, 'Total_Serious_Injuries')
    calc_zscore(new_df, 'Total_Minor_Injuries')
    calc_zscore(new_df, 'Total_Uninjured')
    print('=========================================================')
    print('=========================================================')
    print(
        'Because of the nature of our dataset, the outliers are mostly going to be too large or have zero number of passengers.\n' +
        'This is imperative to getting the right results. These outliers makes sense because we might have commercial airlines\n' +
        'that have a large number of passengers due to the size of the plane and might have little number of passengers due to the plane being small.\n' +
        'Another reason might be these columns that have zero as the outlier probably have the numbers in other columns. This means air crashes that had\n' +
        'passengers with fatal injuries probably did not have passengers that were uninjured and vice versa')
    print('=========================================================')

    ########################################
    # PCA ANALYSIS
    ########################################
    num_cols = new_df.select_dtypes(include=np.number).columns.tolist()
    X = new_df[num_cols].values

    # Standardize the data
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(X)

    # Perform PCA with two components
    # Instantiate PCA with the desired number of components
    pca = PCA(n_components=None)

    # Fit PCA on the scaled features
    pca.fit(scaled_features)

    # Get the explained variance ratio of each component
    explained_variance_ratio = pca.explained_variance_ratio_

    # Computes cumulative explained variance
    cumulative_explained_variance = np.cumsum(explained_variance_ratio) * 100

    # Find the number of components that explain 95% of the variance
    num_components_95 = np.argmax(cumulative_explained_variance >= 95) + 1

    # Display the number of components to be removed
    num_components_to_remove = pca.n_components_ - num_components_95
    print("Number of components to be removed:", num_components_to_remove)

    # Display the explained variance ratio of the original feature space vs reduced feature space
    print("Explained variance ratio of original feature space:", explained_variance_ratio)
    print("Explained variance ratio of reduced feature space:", explained_variance_ratio[:num_components_95])

    # Check the singular values of the PCA results
    sv = pca.singular_values_
    condition_number = np.max(sv) / np.min(sv)
    print('Singular values:', sv)
    print('Condition number:', condition_number)

    plt.plot(np.arange(1, pca.n_components_ + 1), cumulative_explained_variance, color='black')
    plt.axvline(x=num_components_95, color='black', linestyle='--')
    plt.axhline(y=95, color='red', linestyle='--')
    plt.xlabel('Number of components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('Cumulative Explained Variance vs Number of Components')
    plt.grid()
    plt.show()

    print('=========================================================')
    print(
        'After carrying out PCA Analysis, the conclusion is that we are not going to be removing any feature to further our analysis.\n' +
        'This is the decision because these components explains 95% of the variance')
    print('=========================================================')

    ########################################
    # NORMALITY TEST
    ########################################
    # D’AGOSTINO’S K2 TEST
    da_k_squared_test(new_df['Total_Fatal_Injuries'], 'Total_Fatal_Injuries')
    da_k_squared_test(new_df['Total_Serious_Injuries'], 'Total_Serious_Injuries')
    da_k_squared_test(new_df['Total_Minor_Injuries'], 'Total_Minor_Injuries')
    da_k_squared_test(new_df['Total_Uninjured'], 'Total_Uninjured')

    ####################################################
    # Heatmap & Pearson correlation coefficient matrix
    ####################################################
    corr = new_df[num_cols].corr()
    print(corr)

    sns.heatmap(corr, center=0, annot=True, fmt='.2f')
    plt.title('Correlation Coefficient between numerical features')
    plt.tight_layout()
    plt.show()

    #####################################
    # STATISTICAL ANALYSIS
    #####################################
    pd.options.display.max_columns = 10
    print(new_df.describe())

    group_year = new_df.groupby('Year')['Event_Date'].count()
    group_year.plot()
    plt.grid()
    plt.show()
