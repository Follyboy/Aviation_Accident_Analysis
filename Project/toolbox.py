import seaborn as sns
import matplotlib.pyplot as plt


class Toolbox:
    def __init__(self, df=[], length=0, fig_size_x=16, fig_size_y=8):
        self.df = df
        self.length = length
        self.fig_size_x = fig_size_x
        self.fig_size_y = fig_size_y

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
            sns.kdeplot(data=df, x=field_x, y=field_y, hue=hue, fill=fill)

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
