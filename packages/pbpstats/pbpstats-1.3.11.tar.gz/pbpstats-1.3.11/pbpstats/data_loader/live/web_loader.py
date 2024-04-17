import requests

from pbpstats import REQUEST_TIMEOUT
from pbpstats.data_loader.live.base import LiveLoaderBase


class LiveWebLoader(LiveLoaderBase):
    """
    Base class for loading data from live data API request.

    All live data data loader classes should inherit from this class.

    This class should not be instantiated directly.
    """

    def _load_request_data(self):
        response = requests.get(self.url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            self.source_data = response.json()
            self._save_data_to_file()
            return self.source_data
        else:
            response.raise_for_status()
