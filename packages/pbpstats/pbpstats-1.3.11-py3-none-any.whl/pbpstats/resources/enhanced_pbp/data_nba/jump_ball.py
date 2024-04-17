from pbpstats.resources.enhanced_pbp import JumpBall
from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import (
    DataEnhancedPbpItem,
)


class DataJumpBall(JumpBall, DataEnhancedPbpItem):
    """
    Class for jump ball events
    """

    event_type = 10

    def __init__(self, *args):
        super().__init__(*args)
