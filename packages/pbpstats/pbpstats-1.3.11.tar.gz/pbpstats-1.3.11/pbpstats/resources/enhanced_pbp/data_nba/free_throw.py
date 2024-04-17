from pbpstats.resources.enhanced_pbp import FreeThrow
from pbpstats.resources.enhanced_pbp.data_nba.enhanced_pbp_item import (
    DataEnhancedPbpItem,
)


class DataFreeThrow(FreeThrow, DataEnhancedPbpItem):
    """
    Class for free throw events
    """

    event_type = 3

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def is_made(self):
        """
        returns True if shot was made, False otherwise
        """
        return " Missed" not in self.description

    @property
    def is_ft_1_of_1(self):
        return self.event_action_type == 10 or self.event_action_type == 20

    @property
    def is_ft_1_of_2(self):
        return self.event_action_type == 11

    @property
    def is_ft_2_of_2(self):
        return self.event_action_type == 12

    @property
    def is_ft_1_of_3(self):
        return self.event_action_type == 13 or self.event_action_type == 27

    @property
    def is_ft_2_of_3(self):
        return self.event_action_type == 14

    @property
    def is_ft_3_of_3(self):
        return self.event_action_type == 15

    @property
    def is_technical_ft(self):
        return " Technical" in self.description

    @property
    def is_flagrant_ft(self):
        return " Flagrant" in self.description

    @property
    def is_ft_1pt(self):
        """
        returns True if free throw is a 1 point free throw, False otherwise
        Only used in g-league, starting in 2019-20 season
        """
        return self.event_action_type == 30 or self.event_action_type == 35

    @property
    def is_ft_2pt(self):
        """
        returns True if free throw is a 2 point free throw, False otherwise
        Only used in g-league, starting in 2019-20 season
        """
        return self.event_action_type == 31 or self.event_action_type == 36

    @property
    def is_ft_3pt(self):
        """
        returns True if free throw is a 3 point free throw, False otherwise
        Only used in g-league, starting in 2019-20 season
        """
        return self.event_action_type == 32 or self.event_action_type == 37
