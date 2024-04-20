# Imports.

from numbers_parser import Document

# Class definitions.

class Input_Parameters():

    def __init__( self ):

        self.datasets_to_read = []

        self.sample_mask = []

        self.read_files = False

        self.plot_global_features = False

        self.scatterplot = False

        self.correlation_heatmaps = False

        self.pca = False

        self.distance_to_virgin_analysis_based_on_pcas = False

        self.rank_resins_by_pp_content = False

        self.manual_ml = False

        self.pca_ml = False

        self.sandbox = False

# Function definitions.

def read_parameters_from_numbers_file( filename, ip ):

    doc = Document( filename )

    sheets = doc.sheets
    tables = sheets[0].tables
    rows = tables[0].rows()

    ip.datasets_to_read = [int( i.value ) for i in rows[0][1:] if i.value != None]

    ip.sample_mask = [int( i.value ) for i in rows[1][1:] if i.value != None]

    ip.read_files = bool( rows[2][1].value )

    ip.plot_global_features = bool( rows[3][1].value )

    ip.scatterplot = bool( rows[4][1].value )

    ip.correlation_heatmaps = bool( rows[5][1].value )

    ip.pca = bool( rows[6][1].value )

    ip.distance_to_virgin_analysis_based_on_pcas = bool( rows[7][1].value )

    ip.rank_resins_by_pp_content = bool( rows[8][1].value )

    ip.manual_ml = bool( rows[9][1].value )

    ip.pca_ml = bool( rows[10][1].value )

    ip.sandbox = bool( rows[11][1].value )
