# Imports.

import sys
from pathlib import Path

sys.path.append( Path( __file__ ).absolute().parents[1].as_posix() )

from Global_Analysis import Preprocessing
from Global_Analysis import Utilities as util

sys.path.append( Path( __file__ ).absolute().parents[3].as_posix() )

from rHDPE_Data_Analysis import Global_Utilities as gu

# Main function definition.

def Global_Analysis_Main( directory, ip ):

    if ip.datasets_to_read == False:

        print( "Please select a dataset(s)" )

        return 0

    output_directory = directory + "Global/Output/"

    resin_data = gu.get_list_of_resins_data( directory ) # Obtain the spreadsheet of data for the resins.

    if ip.read_files:

        features_df, std_of_features_df, rank_features_df = Preprocessing.read_files_and_preprocess( directory, ip.datasets_to_read, ip.sample_mask )

    if ip.plot_global_features:

        gu.plot_global_features( output_directory, features_df.to_numpy(), features_df.columns, [resin_data.loc[i]["Label"] for i in features_df.index] )

    if ip.scatterplot:

        util.scatterplots( directory, features_df, std_of_features_df )

    if ip.correlation_heatmaps:

        spearman_rank_df = util.correlation_heatmap( rank_features_df, spearman = True )
        pearson_df = util.correlation_heatmap( features_df )

        gu.plot_df_heatmap( spearman_rank_df, savefig = True, filename = output_directory + "Correlations/Spearman.pdf" )
        gu.plot_df_heatmap( pearson_df, savefig = True, filename = output_directory + "Correlations/Pearson.pdf" )

    if ip.pca:

        util.pca( directory, features_df, std_of_features_df )

    if ip.distance_to_virgin_analysis_based_on_pcas:

        util.distance_to_virgin_analysis_based_on_pcas( directory, features_df )

    if ip.rank_resins_by_pp_content:

        util.rank_resins_by_pp_content( directory, features_df, rank_features_df )

    if ip.manual_ml:

        util.manual_ml( directory, ip, features_df )

    if ip.pca_ml:

        util.pca_ml( directory, ip, features_df )

    if ip.sandbox:

        util.sandbox( directory, features_df, std_of_features_df )
