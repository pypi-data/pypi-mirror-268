def clean_confidence_intervals(exoplanet_data):
    """
    Purpose:
    Processes a pandas DataFrame containing exoplanet data by removing confidence
    intervals from the data, retaining only the mean values for further analysis.
    This function is intended for columns that contain string representations
    of statistical measurements where the mean and confidence intervals are combined.

    Parameters:
    - exoplanet_data: DataFrame where each cell in object-type columns contains a string
    with the mean value and its confidence intervals separated by an ampersand (&).

    Returns:
    - A DataFrame with the same structure as exoplanet_data, but with confidence intervals
    removed from all object-type columns, leaving only the mean values as strings.
    """
    return exoplanet_data.apply(
        lambda col: col.str.split("&").str[0] if col.dtype == "object" else col
    )
