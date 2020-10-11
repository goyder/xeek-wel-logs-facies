metadata_features = ["DEPTH_MD", "X_LOC", "Y_LOC", "Z_LOC", "GROUP", "FORMATION"]
continuous_metadata_features = ["DEPTH_MD", "X_LOC", "Y_LOC", "Z_LOC"]
well_log_features = ["BS", "CALI", "RDEP", "RHOB", "GR", "SGR", "RMED", "ROP", "NPHI", "PEF", "RSHA", "DTS", "DTC"]
interp_features = ["FORCE_2020_LITHOFACIES_LITHOLOGY", "FORCE_2020_LITHOFACIES_CONFIDENCE"]
target = ["FORCE_2020_LITHOFACIES_LITHOLOGY"]


def feature_presence_by_well(df, missing_data_threshold=0.5):
    """
    For a given dataframe, return the proportion of wells that a feature is present in.
    :param df: Dataframe to examine.
    :param missing_data_threshold: Proportion of missing data at which a feature is declared absent from well.
    :return: List of features that that meet thresholds.
    """
    return (df
            .groupby(["WELL"])
            .aggregate(lambda s: (s
                                  .isnull()
                                  .sum()) / len(s))
            .aggregate(lambda s: (s > missing_data_threshold).sum())
            .transform(lambda s: (1 - s / df["WELL"].nunique())))


def features_mostly_present(df, missing_data_threshold=0.5, presence_threshold=1) -> list:
    """
    For a given dataframe, return a list of features that are present in a given proportion of wells.
    :param df: Dataframe to examine.
    :param missing_data_threshold: Proportion of missing data at which a feature is declared absent from well.
    :param presence_threshold: Minimum presence to return a feature.
    :return: List of features.
    """
    f = feature_presence_by_well(df, missing_data_threshold)
    return ["WELL"] + (f
                       [f >= presence_threshold]
                       .index.to_list())

