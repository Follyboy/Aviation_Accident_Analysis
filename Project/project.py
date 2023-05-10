import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from toolbox import calc_zscore, da_k_squared_test, Toolbox, create_sub_line

if __name__ == '__main__':
    # Load Original Data
    url = 'https://raw.githubusercontent.com/Follyboy/Aviation_Accident_Analysis/main/Project/AviationData.csv'
    df = pd.read_csv(url, sep=",", encoding='cp1252', dtype='unicode')
    print(df.head())

    df['Event.Date'] = pd.to_datetime(df['Event.Date'])
    df['Year'] = df['Event.Date'].dt.year
    df['Month'] = df['Event.Date'].dt.month_name()
    df['Day'] = df['Event.Date'].dt.day_name()

    # Edit and Arrange names of columns
    df = df.rename(columns=lambda x: x.replace('.', '_'))
    arrange_col = ['Event_Date', 'Year', 'Month', 'Day', 'Investigation_Type', 'Location', 'Country',
                   'Airport_Name', 'Injury_Severity', 'Aircraft_damage',
                   'Aircraft_Category', 'Make', 'Model', 'Amateur_Built', 'Number_of_Engines',
                   'Engine_Type', 'FAR_Description', 'Purpose_of_flight', 'Air_carrier',
                   'Total_Fatal_Injuries', 'Total_Serious_Injuries', 'Total_Minor_Injuries',
                   'Total_Uninjured', 'Weather_Condition', 'Broad_phase_of_flight', 'Report_Status']
    df = df[arrange_col]

    # replace missing values with 0 because nana for these columns have values in other continuous variable columns
    df['Total_Serious_Injuries'].fillna(0, inplace=True)
    df['Total_Fatal_Injuries'].fillna(0, inplace=True)
    df['Total_Minor_Injuries'].fillna(0, inplace=True)
    df['Total_Uninjured'].fillna(0, inplace=True)
    df['Number_of_passengers'] = df.filter(like='Total').astype(int).sum(axis=1)

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
    df_.loc[df_['Number_of_passengers'] == 0, 'Number_of_passengers'] = np.nan

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
    df_ = df_.dropna(
        subset=['Weather_Condition', 'Number_of_Engines', 'Aircraft_damage', 'Engine_Type', 'Amateur_Built',
                'Number_of_passengers'])
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
    num_cols = ['Year', 'Total_Fatal_Injuries', 'Total_Serious_Injuries', 'Total_Minor_Injuries', 'Total_Uninjured', 'Number_of_passengers']
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
    print(new_df.head())

    # Display dataset dimensions
    print(new_df.shape)

    # Display summary statistics for numeric columns
    print(new_df.describe())

    skewness = new_df.skew(numeric_only=True)
    print('=' * 20 + 'SKEWNESS' + '=' * 20)
    print(skewness)
    print('=' * 48)

    ##############################
    # LINE PLOTS
    ##############################
    ############################################
    # LINE PLOT FOR CRASHES BY YEAR
    ############################################
    group_year = new_df.groupby('Year')['Event_Date'].count()
    tool = Toolbox(group_year)
    tool.create_plot(y='Event_Date', title='Number of Aviation Accidents by Year', y_label='Number of Accidents')

    ############################################
    # LINE PLOT FOR CRASHES VS YEAR BY COUNTRY
    ############################################
    tool_ = Toolbox(df=new_df)
    tool_.create_line_plot(field=['Country', 'Year'], title='Number of Aviation Accidents of top 10 Countries',
                           x_label='Year', y_label='Number of Accidents', head=True, head_c=10)

    ####################################################
    # LINE PLOT FOR CRASHES VS YEAR BY AIRCRAFT DAMAGE
    ####################################################
    tool_.create_line_plot(field=['Aircraft_damage', 'Year'], title='Number of Aviation Accidents by Aircraft Damage',
                           x_label='Year', y_label='Number of Accidents')

    ####################################################
    # LINE PLOT FOR CRASHES VS YEAR BY INJURY SEVERITY
    ####################################################
    tool_.create_line_plot(field=['Injury_Severity', 'Year'], title='Number of Aviation Accidents by Injury Severity',
                           x_label='Year', y_label='Number of Accidents')

    ####################################################
    # LINE PLOT FOR CRASHES VS YEAR BY MONTH
    ####################################################
    tool_.create_line_plot(field=['Month', 'Year'], title='Number of Aviation Accidents by Month',
                           x_label='Year', y_label='Number of Accidents', month=True)

    ####################################################
    # LINE PLOT FOR CRASHES VS YEAR BY DAY
    ####################################################
    tool_.create_line_plot(field=['Day', 'Year'], title='Number of Aviation Accidents by Day',
                           x_label='Year', y_label='Number of Accidents', day=True)

    ####################################################
    # LINE PLOT FOR CRASHES VS YEAR BY WEATHER
    ####################################################
    tool_.create_line_plot(field=['Weather_Condition', 'Year'],
                           title='Number of Aviation Accidents by Weather Condition',
                           x_label='Year', y_label='Number of Accidents')

    ##############################
    # BAR PLOTS
    ##############################
    ####################################################
    # BAR PLOT FOR CRASHES THAT ARE AMATEUR BUILT
    ####################################################
    # group the dataframe by year and 'Amateur_Built' column, and count the number of accidents in each group
    count_ab = new_df.groupby(['Year', 'Amateur_Built']).size().unstack()

    tool_bar = Toolbox(fig_size_x=12, fig_size_y=6)
    tool_bar.create_bar(df=count_ab, stacked=True, df_plot=True,
                        title='Number of Accidents by Year and Amateur-Built Status',
                        x_label='Year', y_label='Number of Accidents')

    ####################################################
    # BAR PLOT FOR AIRCRAFT THAT ARE AMATEUR BUILT
    ####################################################
    # create two dataframes, one for 'Yes' and one for 'No'
    yes_df = df[df['Amateur_Built'] == 'Yes']
    no_df = df[df['Amateur_Built'] == 'No']

    # count the number of accidents in each dataframe
    num_accidents_yes = len(yes_df)
    num_accidents_no = len(no_df)
    tool_bar.create_bar(title='Number of Amateur-Built Aircraft', x=['Yes', 'No'],
                        y=[num_accidents_yes, num_accidents_no],
                        x_label='Amateur Built', y_label='Number of Crashes')

    ####################################################
    # BAR PLOT FOR CRASHES AND THEIR ENGINE TYPES
    ####################################################
    # group the dataframe by year and 'Engine_Type' column, and count the number of accidents in each group
    count_et = new_df.groupby(['Year', 'Engine_Type']).size().unstack()

    tool_bar.create_bar(df=count_et, stacked=True, df_plot=True, title='Number of Accidents by Year and Engine Types',
                        x_label='Year', y_label='Number of Accidents')

    ####################################################
    # BAR PLOT FOR ENGINE TYPES
    ####################################################
    et_unique = new_df['Engine_Type'].unique()
    col_count_et = []
    for i in et_unique:
        df_et = new_df[new_df['Engine_Type'] == i]
        length = len(df_et)
        col_count_et.append(length)

    tool_bar.create_bar(title='Number of Engine Types', x=et_unique,
                        y=col_count_et,
                        x_label='Engine Types', y_label='Number of Crashes', rotate_x=True)

    ###################################################
    # BAR PLOT FOR CRASHES AND WEATHER CONDITION
    ###################################################
    # group the dataframe by year and 'Weather_Condition' column, and count the number of accidents in each group
    count_weather = new_df.groupby(['Year', 'Weather_Condition']).size().unstack()

    tool_bar.create_bar(df=count_weather, stacked=True, df_plot=True, title='Number of Accidents by Year and Weather Condition',
                        x_label='Year', y_label='Number of Accidents')

    ###################################################
    # BAR PLOT FOR WEATHER CONDITION
    ###################################################
    weather_unique = new_df['Weather_Condition'].unique()
    col_count_weather = []
    for i in weather_unique:
        df_weather = new_df[new_df['Weather_Condition'] == i]
        length = len(df_weather)
        col_count_weather.append(length)

    tool_bar.create_bar(title='Number of Weather Conditions', x=weather_unique,
                        y=col_count_weather,
                        x_label='Weather Condition', y_label='Number of Crashes', rotate_x=True)

    ##############################
    # COUNT PLOTS
    ##############################
    #####################################################################
    # COUNT PLOT FOR INJURY SEVERITY DURING DIFFERENT WEATHER CONDITIONS
    #####################################################################
    tool_count = Toolbox(df=new_df)
    tool_count.create_countplot(field='Injury_Severity', title='Number of Injury Severity with Weather Conditions',
                                style='darkgrid', hue='Weather_Condition')

    tool_count.create_countplot(field='Day', title='Number of Crashes on Days with Weather Conditions',
                                style='darkgrid', hue='Weather_Condition')

    ##############################
    # CAT PLOTS
    ##############################
    tool_cat = Toolbox(df=new_df)
    tool_cat.create_catplot(x='Day', y='Number_of_passengers', hue='Engine_Type')

    tool_cat.create_catplot(x='Month', y='Number_of_passengers', hue='Engine_Type')

    ##############################
    # PIE CHART PLOTS
    ##############################
    #######################################
    # PIE CHART OF DAY ACCIDENTS OCCUR
    #######################################
    explode = 0.01
    tool_pie = Toolbox(df=new_df)
    tool_pie.create_pie_count(field='Day', explode=explode, num=False, title='Accidents across days')
    #######################################
    # PIE CHART OF MONTH ACCIDENTS OCCUR
    #######################################
    tool_pie.create_pie_count(field='Month', explode=explode, num=False, title='Accidents across months')

    ##############################
    # DISPLOT
    ##############################
    ############################################################################################
    # DISPLOT OF TOTAL FATAL INJURIES PER WEATHER FOR COMMERCIAL, CHARTED AND PRIVATE PLANES
    ############################################################################################
    commercial_airlines = new_df[new_df['Number_of_passengers'] >= 200]
    tool_dis_comm = Toolbox(df=commercial_airlines)
    tool_dis_comm.create_displot(field='Total_Fatal_Injuries', x_label='Total_Fatal_Injuries', y_label='Frequency',
                                 title='Density plot of crash total fatal injuries per weather condition (commercial)',
                                 style='darkgrid',
                                 hue='Weather_Condition',
                                 kind='kde')

    chartered_planes = new_df[(new_df['Number_of_passengers'] >= 20) & (new_df['Number_of_passengers'] < 200)]
    tool_dis_char = Toolbox(df=chartered_planes)
    tool_dis_char.create_displot(field='Total_Fatal_Injuries', x_label='Total_Fatal_Injuries', y_label='Frequency',
                                 title='Density plot of crash total fatal injuries per weather condition (chartered)',
                                 style='darkgrid',
                                 hue='Weather_Condition',
                                 kind='kde')

    private_planes = new_df[new_df['Number_of_passengers'] < 20]
    tool_dis_pri = Toolbox(df=private_planes)
    tool_dis_pri.create_displot(field='Total_Fatal_Injuries', x_label='Total_Fatal_Injuries', y_label='Frequency',
                                title='Density plot of crash total fatal injuries per weather condition (private)',
                                style='darkgrid',
                                hue='Weather_Condition',
                                kind='kde')

    ############################################################################################
    # DISPLOT OF TOTAL UNINJURED PER WEATHER FOR COMMERCIAL, CHARTED AND PRIVATE PLANES
    ############################################################################################
    tool_dis_comm.create_displot(field='Total_Uninjured', x_label='Total_Uninjured', y_label='Frequency',
                                 title='Crash of total uninjured passengers per weather condition (commercial)',
                                 style='darkgrid',
                                 hue='Weather_Condition',
                                 kind='kde')

    tool_dis_char.create_displot(field='Total_Uninjured', x_label='Total_Uninjured', y_label='Frequency',
                                 title='Crash of total uninjured passengers per weather condition (chartered)',
                                 style='darkgrid',
                                 hue='Weather_Condition',
                                 kind='kde')

    tool_dis_pri.create_displot(field='Total_Uninjured', x_label='Total_Uninjured', y_label='Frequency',
                                title='Crash of total uninjured passengers per weather condition (private)',
                                style='darkgrid',
                                hue='Weather_Condition',
                                kind='kde')

    ############################################################################################
    # DISPLOT OF TOTAL SERIOUSLY INJURED PER WEATHER FOR COMMERCIAL, CHARTED AND PRIVATE PLANES
    ############################################################################################
    tool_dis_comm.create_displot(field='Total_Serious_Injuries', x_label='Total_Serious_Injuries', y_label='Frequency',
                                 title='Crash of total seriously injured passengers per weather condition (commercial)',
                                 style='darkgrid',
                                 hue='Weather_Condition',
                                 kind='kde')

    tool_dis_char.create_displot(field='Total_Serious_Injuries', x_label='Total_Serious_Injuries', y_label='Frequency',
                                 title='Crash of total seriously injured passengers per weather condition (chartered)',
                                 style='darkgrid',
                                 hue='Weather_Condition',
                                 kind='kde')

    tool_dis_pri.create_displot(field='Total_Serious_Injuries', x_label='Total_Serious_Injuries', y_label='Frequency',
                                title='Crash of total seriously injured passengers per weather condition (private)',
                                style='darkgrid',
                                hue='Weather_Condition',
                                kind='kde')

    ##############################
    # PAIR PLOT
    ##############################
    sns.pairplot(new_df[num_cols])
    plt.show()

    ##############################
    # QQ PLOT
    ##############################
    ######################################
    # QQ PLOT OF TOTAL SERIOUS INJURIES
    ######################################
    tool_qq = Toolbox(df=new_df)
    tool_qq.create_qq(field='Total_Serious_Injuries')

    #########################################
    # QQ PLOT OF TOTAL NUMBER OF PASSENGERS
    #########################################
    tool_qq.create_qq(field='Number_of_passengers')

    ##############################
    # KDE PLOT
    ##############################
    tool_kde_comm = Toolbox(df=commercial_airlines)
    tool_kde_char = Toolbox(df=chartered_planes)
    tool_kde_pri = Toolbox(df=private_planes)

    ################################################################
    # KDE PLOT FOR COMMERCIAL PLANE CRASH FOR TOTAL FATAL INJURIES
    ################################################################
    tool_kde_comm.create_kdeplot(field_y='Total_Fatal_Injuries', field_x='Year', style='darkgrid', hue='Amateur_Built',
                                 title='COMMERCIAL PLANE CRASH FOR TOTAL FATAL INJURIES')

    ################################################################
    # KDE PLOT FOR CHARTERED PLANE CRASH FOR TOTAL FATAL INJURIES
    ################################################################
    tool_kde_char.create_kdeplot(field_y='Total_Fatal_Injuries', field_x='Year', style='darkgrid', hue='Amateur_Built',
                                 title='CHARTERED PLANE CRASH FOR TOTAL FATAL INJURIES')

    ################################################################
    # KDE PLOT FOR PRIVATE PLANE CRASH FOR TOTAL FATAL INJURIES
    ################################################################
    tool_kde_pri.create_kdeplot(field_y='Total_Fatal_Injuries', field_x='Year', style='darkgrid', hue='Amateur_Built',
                                title='PRIVATE PLANE CRASH FOR TOTAL FATAL INJURIES')

    ##############################
    # SCATTER PLOT
    ##############################
    tool_scatter = Toolbox(df=new_df)
    tool_scatter.create_scatter(x='Total_Uninjured', y='Total_Minor_Injuries',
                                title='Scattered plot of Minor Injured vs Uninjured passengers')

    tool_scatter.create_scatter(y='Total_Uninjured', x='Number_of_passengers',
                                title='Scattered plot of Uninjured vs Total number of passengers')

    tool_scatter.create_scatter(y='Total_Fatal_Injuries', x='Number_of_passengers',
                                title='Scattered plot of Fatal Injured vs Total number of passengers')

    ##############################
    # MULTIVARIATE BOX PLOT
    ##############################
    tool_box = Toolbox(fig_size_x=12, fig_size_y=8)
    tool_box.create_boxplot(x='Day', y='Total_Uninjured',  hue='Weather_Condition',
                            df=chartered_planes, title='Box plot of Uninjured vs Day by Weather')

    tool_box.create_boxplot(x='Day', y='Total_Uninjured',  hue='Injury_Severity',
                            df=chartered_planes, title='Box plot of Uninjured vs Day by injury severity')

    ##############################
    # VIOLIN PLOT
    ##############################
    sns.violinplot(x="Day", y='Total_Uninjured', data=new_df)

    # add a title and y-axis label
    plt.title("Total Number of Uninjured passengers by Day")
    plt.ylabel("Number of Uninjured passengers")

    # show the plot
    plt.show()

    sns.violinplot(x='Weather_Condition', y='Total_Uninjured', data=new_df)

    # add a title and y-axis label
    plt.title("Total Number of Uninjured passengers by Weather")
    plt.ylabel("Number of Uninjured passengers")

    # show the plot
    plt.show()

    ###############################
    # SUBPLOTS
    ###############################
    ##############################################################
    # SUBPLOTS FOR COUNTRY
    ##############################################################
    countries = new_df['Country'].unique()[:6]
    create_sub_line(df=new_df, u=countries, field='Country', title='Number of Accidents by Year for first 6 Countries')

    ##############################################################
    # SUBPLOTS FOR WEATHER CONDITION
    ##############################################################
    weathers = new_df['Weather_Condition'].unique()
    create_sub_line(df=new_df, u=weathers, field='Weather_Condition', title='Number of Accidents by Year for Weather',
                    rows=1, cols=2, fig_y=4)
