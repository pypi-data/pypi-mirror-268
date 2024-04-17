import requests

from pbpstats import HEADERS, REQUEST_TIMEOUT
from pbpstats.data_loader.stats_nba.base import StatsNbaLoaderBase


class StatsNbaWebLoader(StatsNbaLoaderBase):
    """
    Base class for loading data from data.nba.com API request.

    All stats.nba.com data loader classes should inherit from this class.

    This class should not be instantiated directly.
    """

    def _load_request_data(self):
        # If endpoint requires different headers they can be set in the web loader for the endpoint
        # Otherwise use the default headers
        if not hasattr(self, "headers"):
            self.headers = HEADERS
        response = requests.get(
            self.base_url,
            self.parameters,
            headers=self.headers,
            timeout=REQUEST_TIMEOUT,
        )
        if response.status_code == 200:
            self.source_data = response.json()
            self._save_data_to_file()
            return response.json()
        else:
            response.raise_for_status()
