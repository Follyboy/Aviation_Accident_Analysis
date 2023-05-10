import numpy as np
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import normaltest


def calc_zscore(df, field=''):
    # select the column to detect outliers in
    col = df[field]

    # calculate the Z-score for each data point in the column
    z_scores = (col - np.mean(col)) / np.std(col)

    # define the threshold for outliers (Z-score > 3)
    threshold = 3

    # detect outliers using boolean indexing
    outliers = df[z_scores > threshold]
    outliers_df = df[~(z_scores > threshold)]

    # print the outliers
    print(f'Number of outliers for {field} is {len(outliers)}')
    return outliers_df


def da_k_squared_test(x, title):
    stats, p = normaltest(x)
    print('=' * 50)
    print(f'da_k_squared test: {title} dataset: statistics= {stats:.2f} p-value = {p:.2f}')

    alpha = 0.05 / len(x)
    if p > alpha:
        print(f'da_k_squared test:  {title} dataset looks Normal')
    else:
        print(f'da_k_squared test : {title} dataset does not look Normal')
    print('=' * 50)


def create_sub_line(df=[], field='', u=[], rows=3, cols=2, title='', fig_x=12, fig_y=8):
    # Create a row by col grid of subplots
    fig, axs = plt.subplots(rows, cols, figsize=(fig_x, fig_y))

    # Plot line graphs for each value in the subplots
    for i, value in enumerate(u):
        row = i // 2
        col = i % 2
        data = df[df[field] == value]
        grouped = data.groupby([field, 'Year']).size().reset_index(name='Count')
        if rows == 1:
            axs[col].plot(grouped['Year'], grouped['Count'])
            axs[col].set_title(value)
            axs[col].set_xlabel('Year')
            axs[col].set_ylabel('Count')
            axs[col].grid()
        else:
            axs[row, col].plot(grouped['Year'], grouped['Count'])
            axs[row, col].set_title(value)
            axs[row, col].set_xlabel('Year')
            axs[row, col].set_ylabel('Count')
            axs[row, col].grid()

    # Display the plot
    fig.suptitle(title)
    plt.tight_layout()
    plt.show()


class Toolbox:
    def __init__(self, df=[], length=0, fig_size_x=16, fig_size_y=8):
        self.df = df
        self.length = length
        self.fig_size_x = fig_size_x
        self.fig_size_y = fig_size_y

    def create_boxplot(self, x='', y='', title='', df=[], hue=None):
        fig_x = self.fig_size_x
        fig_y = self.fig_size_y

        fig, ax = plt.subplots(figsize=(fig_x, fig_y))
        sns.boxplot(x=x, y=y, hue=hue, data=df, ax=ax)
        plt.title(title)
        plt.show()

    def create_scatter(self, x='', y='', title=''):
        df = self.df
        sns.regplot(data=df, x=x, y=y)
        plt.title(title)
        plt.show()

    def create_qq(self, field=''):
        df = self.df
        sm.qqplot(df[field], line='s')
        plt.tight_layout()
        plt.show()

    def create_pie_count(self, field='', explode=0.01, num: bool = False, angle=0, title='', percentage='%1.2f%%',
                         loc=(.90, .8), capitalize: bool = True):
        df = self.df
        counts = df[field].value_counts()
        sum_ = df[field].count()
        sizes = counts.values.tolist()
        list_ = counts.index.tolist()
        labels = []
        for i in list_:
            if capitalize:
                c = i.capitalize()
                labels.append(c)
            else:
                labels.append(i)

        explode = [explode] * len(sizes)

        # Plot the pie chart
        fig, ax = plt.subplots(figsize=(8, 8))
        if num:
            ax.pie(sizes, labels=labels, autopct=lambda x: round((x / 100) * sum_), explode=explode, startangle=angle)
        else:
            ax.pie(sizes, labels=labels, autopct=percentage, explode=explode, startangle=angle)

        # Add title
        ax.set_title(title)
        ax.legend(loc=loc)

        # Show the chart
        plt.tight_layout()
        plt.show()

    def create_plot(self, x='', y=[], legend: bool = False, title='', x_label='', y_label='', date_index: bool = False):
        df = self.df

        plt.figure(figsize=(self.fig_size_x, self.fig_size_y))
        if date_index:
            if legend:
                df.plot(y=y)
            else:
                df.plot(y=y, legend=None)

        else:
            if legend:
                df.plot(x=x, y=y)
            else:
                df.plot(x=x, y=y, legend=None)

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.tight_layout()
        if legend:
            plt.legend()
        plt.grid()
        plt.show()

    def create_line_plot(self, field=[], title='', x_label='', y_label='', day: bool = False, month: bool = False,
                         head: bool = False, head_c=5):
        df = self.df

        count = df.groupby(field).size().reset_index(name='count')

        month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
                      'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
                      'November': 11, 'December': 12}

        day_dict = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5,
                    'Saturday': 6, 'Sunday': 7}

        # list
        if head:
            list_ = count.groupby(field[0])['count'].sum().sort_values(ascending=False).head(head_c).index.tolist()
        else:
            list_ = count.groupby(field[0])['count'].sum().sort_values(ascending=False).index.tolist()

        count_ = count[count[field[0]].isin(list_)]

        # create a line plot
        fig, ax = plt.subplots(figsize=(12, 6))
        for a in list_:
            data = count_[count_[field[0]] == a]
            ax.plot(data[field[1]], data['count'], label=a)

        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        if month:
            handles, labels = ax.get_legend_handles_labels()
            sorted_labels, sorted_handles = zip(
                *sorted(zip(labels, handles), key=lambda t: month_dict[t[0].split()[0]]))
            ax.legend(sorted_handles, sorted_labels, loc='center left', bbox_to_anchor=(1, 0.5))
        elif day:
            handles, labels = ax.get_legend_handles_labels()
            sorted_labels, sorted_handles = zip(*sorted(zip(labels, handles), key=lambda t: day_dict[t[0].split()[0]]))
            ax.legend(sorted_handles, sorted_labels, loc='center left', bbox_to_anchor=(1, 0.5))
        else:
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.grid()
        plt.tight_layout()
        plt.show()

    def create_catplot(self, x='', y='', title='', hue=None, width=2.5, kind='boxen', rotate_tick=90):
        df = self.df
        sns.catplot(x=x, y=y, kind=kind, data=df, aspect=width, hue=hue, legend_out=False)

        plt.title(title)
        plt.xticks(rotation=rotate_tick)

        plt.grid()
        plt.tight_layout()
        plt.show()

    def create_bar(self, df=[], stacked: bool = False, df_plot: bool = False, x=[], y=[], title='',
                   x_label='', y_label='', rotate_x: bool = False):
        fig_x = self.fig_size_x
        fig_y = self.fig_size_y

        if df_plot:
            df.plot(kind='bar', stacked=stacked, figsize=(fig_x, fig_y))
        else:
            plt.bar(x, y)

        # set the chart title and axis labels
        plt.title(title)
        if rotate_x:
            plt.xticks(rotation=90)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # show the chart
        plt.grid()
        plt.tight_layout()
        plt.show()

    def create_hist(self, bins='auto', field='', x_label='', y_label='', title='', style='', binwidth=None,
                    stat='count', hue=None):
        df = self.df

        sns.set_style(style)
        sns.histplot(data=df, x=field, bins=bins, binwidth=binwidth, stat=stat, hue=hue)

        # Set the plot title and axis labels
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)

        # Display the plot
        plt.tight_layout()
        plt.show()

    def create_countplot(self, field='', title='', style='', hue=None):
        df = self.df

        sns.set_style(style)
        sns.countplot(data=df, x=field, hue=hue)

        # Set the plot title and axis labels
        plt.title(title)

        # Display the plot
        plt.tight_layout()
        plt.show()

    def create_kdeplot(self, field_x='', field_y='', title='', style='', hue=None, subplot: bool = False,
                       rows=3, cols=2, array=[], fill: bool = True):
        df = self.df

        sns.set_style(style)
        if subplot:
            fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(self.fig_size_x, self.fig_size_y))
            k = 0
            for i in array:
                [x, y] = i
                sns.kdeplot(data=df, x=x, y=y, ax=axs[k], fill=fill, hue=hue)
                axs[k].set_title(f'Penguins {x} vs {y}')
                k += 1
            plt.tight_layout()
            plt.show()
        else:
            sns.kdeplot(data=df, x=field_x, y=field_y, hue=hue, fill=fill, warn_singular=False)

            # Set the plot title and axis labels
            plt.title(title)

            # Display the plot
            plt.tight_layout()
            plt.show()

    def create_displot(self, field='', x_label='', y_label='', title='', style='', hue=None, multiple='', element='',
                       dfs=[], rows=3, cols=2, subplot: bool = False, unique_field='', kind='hist', fill: bool = False,
                       both_fields: bool = False, field_x='', field_y=''):
        df = self.df

        sns.set_style(style)
        if both_fields:
            sns.displot(data=df, x=field_x, y=field_y, hue=hue)
            plt.show()
        else:
            if subplot:
                fig, axs = plt.subplots(nrows=rows, ncols=cols, figsize=(self.fig_size_x, self.fig_size_y))
                k = 0
                for i in dfs:
                    x = i[unique_field].unique()[0]
                    sns.histplot(data=i, x=field, ax=axs[k])
                    axs[k].set_title(f'Histogram of {x} Penguins Flipper length')
                    axs[k].set_ylabel(f'{y_label}')
                    k += 1
                plt.tight_layout()
                plt.show()
            else:
                if fill:
                    if multiple != '' and element == '':
                        sns.displot(data=df, x=field, hue=hue, multiple=multiple, kind=kind, fill=fill)
                    elif element != '' and multiple == '':
                        sns.displot(data=df, x=field, hue=hue, element=element, kind=kind, fill=fill)
                    elif multiple != '' and element != '':
                        sns.displot(data=df, x=field, hue=hue, multiple=multiple, element=element, kind=kind, fill=fill)
                    else:
                        sns.displot(data=df, x=field, hue=hue, kind=kind, fill=fill)
                else:
                    if multiple != '' and element == '':
                        sns.displot(data=df, x=field, hue=hue, multiple=multiple, kind=kind)
                    elif element != '' and multiple == '':
                        sns.displot(data=df, x=field, hue=hue, element=element, kind=kind)
                    elif multiple != '' and element != '':
                        sns.displot(data=df, x=field, hue=hue, multiple=multiple, element=element, kind=kind)
                    else:
                        sns.displot(data=df, x=field, hue=hue, kind=kind)

                # Set the plot title and axis labels
                plt.title(title, pad=1.50)
                plt.xlabel(x_label)
                plt.ylabel(y_label)

                # Display the plot
                if kind == 'kde':
                    plt.tight_layout()
                plt.show()
