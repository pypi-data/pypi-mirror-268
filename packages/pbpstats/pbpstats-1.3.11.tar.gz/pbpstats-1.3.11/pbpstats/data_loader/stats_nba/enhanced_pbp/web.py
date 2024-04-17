from pbpstats.data_loader.stats_nba.pbp.web import StatsNbaPbpWebLoader
from pbpstats.data_loader.stats_nba.shots.web import StatsNbaShotsWebLoader


class StatsNbaEnhancedPbpWebLoader(StatsNbaPbpWebLoader):
    """
    A ``StatsNbaEnhancedPbpWebLoader`` object should be instantiated and passed into ``StatsNbaEnhancedPbpLoader`` when loading data directly from the NBA Stats API

    :param str file_directory: (optional, use it if you want to store the response data on disk)
        Directory in which data should be either stored.
        The specific file location will be `stats_<game_id>.json` in the `/pbp` subdirectory.
        If not provided response data will not be saved on disk.
    """

    def __init__(self, file_directory=None):
        self.file_directory = file_directory
        self.shots_source_loader = StatsNbaShotsWebLoader(file_directory)
