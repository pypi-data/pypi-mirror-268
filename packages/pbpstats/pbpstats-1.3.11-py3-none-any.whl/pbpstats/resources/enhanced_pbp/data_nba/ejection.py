from pbpstats.resources.enhanced_pbp import Ejection
from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import (
    DataEnhancedPbpItem,
)


class DataEjection(Ejection, DataEnhancedPbpItem):
    """
    Class for Ejection events
    """

    event_type = 11

    def __init__(self, *args):
        super().__init__(*args)
