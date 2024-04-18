# from .download import download_satellite_image, download_dem, download_cloud_mask
# from .explore import explore_satellite_images

from .stac import (
    AWSS2L2ADownloader,
    PCS1GRDDownloader,
    AWSDEM30Downloader,
    AWSDEM90Downloader,
)

DOWNLOADERS = {
    "sentinel-2-l2a": AWSS2L2ADownloader,
    "sentinel-1-grd": PCS1GRDDownloader,
    "cop-dem-glo-30": AWSDEM30Downloader,
    "cop-dem-glo-90": AWSDEM90Downloader,
}
AVAILABLE_COLLECTIONS = list(DOWNLOADERS.keys())

from .download_stac import (
    download_satellite_imagery,
    load_satellite_imagery,
    explore_satellite_imagery,
)
