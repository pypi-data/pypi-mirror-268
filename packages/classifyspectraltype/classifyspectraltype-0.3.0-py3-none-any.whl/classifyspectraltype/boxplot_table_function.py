import matplotlib.pyplot as plt


def make_boxplot_and_table(data, column_name, csv_dir, box_plot_dir):
    """
    Purpose: 
    creates a boxplot and a csv file given the dataframe the desired column name
    of which we want to investigate. Our function will also save all of these figures to the given
    file directory path.

    Requirements: Must have a column called st_spectype to group by. This is project specific in our
    case and can be easily altered if using other data.

    Parameters:
    - data: Dataframe used to select our desired column from
    - column_name: Name of the column as a string
    - csv_dir: Path to the directory in which we want the csv files to live
    - box_plot_dir: Path to the directory in which we want the box plot figures to live

    Returns:
    - A csv with the quantitative descriptions (mean, std, min) for the four bands (FGKM) loaded into
    the corresponding directory
    - A boxplot of each of the four bands loaded into the corresponding directory
    """

    # create and save csv for given column provided
    column_csv = data[["st_spectype", column_name]].groupby("st_spectype").describe()
    column_csv2 = column_csv.round(2)
    column_csv2.to_csv(f"{csv_dir}/{column_name}.csv")

    # create and save png for given column provided
    data[["st_spectype", column_name]].groupby("st_spectype").boxplot()
    plt.savefig(f"{box_plot_dir}/{column_name}.png")
