"""
PCDownloader class for downloading data from the Planetary Computer STAC API.
"""

from ..STACDownloader import STACDownloader
from typing import Optional, Dict


class PCDownloader(STACDownloader):
    def __init__(self, aoi, datetime, query: Optional[Dict[str, Dict]] = None):
        try:
            from planetary_computer import sign_inplace
        except ImportError:
            raise ImportError(
                "The planetary_computer package is required. Please install it with 'pip install planetary-computer' and try again."
            )

        self.url = "https://planetarycomputer.microsoft.com/api/stac/v1"
        self.modifier = sign_inplace
        super().__init__(aoi, datetime, query)
