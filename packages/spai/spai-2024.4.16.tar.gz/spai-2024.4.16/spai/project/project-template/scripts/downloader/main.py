from spai.storage import Storage
from spai.data.satellite import explore_satellite_imagery, download_satellite_imagery

# explore available images
print("Looking for images in the last month")
bbox = (2.0052191, 41.38238988, 2.17002873, 41.48530451)  # Collserola
images = explore_satellite_imagery(bbox, cloud_cover=10)
if len(images) == 0:
    raise ValueError("No images found")

# download images and save locally
storage = Storage()
sensor = "sentinel-2-l2a"
existing_images = storage["data"].list(f"{sensor}*.tif")
dates = [image.split("_")[1].split(".")[0] for image in existing_images]
print("Found", len(images), f"image{'s' if len(images) > 1 else ''}")
new_images = []
for image in images:
    # check if image is already downloaded
    date = image["datetime"].split("T")[0]
    if date in dates or date in new_images:
        print("Image already downloaded:", date)
        continue
    new_images.append(date)
    print("Downloading new image:", date)
    path = download_satellite_imagery(storage["data"], bbox, date, sensor)
    print("Image saved at", path)
