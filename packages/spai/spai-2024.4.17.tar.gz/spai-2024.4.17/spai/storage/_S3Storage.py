import pandas as pd
import json
import io
from minio import Minio
import fnmatch

from .BaseStorage import BaseStorage
from .decorators import with_rio, with_geopandas


class S3Storage(BaseStorage):
    def __init__(self, url, access, secret, bucket, region=None):
        super().__init__()
        self.url = url
        self.access = access
        self.secret = secret
        self.region = region
        self.bucket = bucket

        if self.access and self.secret:
            # Create a client
            self.client = Minio(
                endpoint=self.url,
                access_key=self.access,
                secret_key=self.secret,
                secure=True if self.region else False,
                region=self.region,
            )  # because no certificate is used in the containerised version of minio
            if not self.client.bucket_exists(self.bucket):
                # Make a bucket with the credentials and the bucket_name given
                self.client.make_bucket(self.bucket)
                print(f"Bucket '{self.bucket}' created")
            else:
                print(f"'{self.bucket}' bucket ready to use")
        else:
            # TODO: create bucket in our minio server (we will need our credentials for that, do it with API request?
            print("Missing credentials")
            # Habría que preguntar si se quiere crear el bucket en nuestro cloud o decirles que introduzcan sus creds

    def list(self, pattern="*"):
        return fnmatch.filter(
            [
                obj.object_name
                for obj in self.client.list_objects(self.bucket, recursive=True)
            ],
            pattern,
        )

    def create_from_path(self, data, name):
        if data.endswith(".json"):
            content_type = "application/json"
            self.client.fput_object(self.bucket, name, data, content_type=content_type)
            return name
        elif data.endswith(".tiff") or data.endswith(".tif"):
            content_type = "image/tiff"
            # with rasterio.open(data) as src:
            #     self.client.put_object(self.bucket, dst_path, src, length=src.read().all(), content_type=content_type)
            self.client.fput_object(self.bucket, name, data, content_type=content_type)
            return name
        elif data.endswith(".geojson"):
            content_type = "application/geojson"
            self.client.fput_object(self.bucket, name, data, content_type=content_type)
            return name
        else:
            print(data)
            # self.client.put_object(self.bucket, prefix + name, data, length, content_type)

    def create_from_dict(self, data, name):
        if name.endswith(".json"):
            content_type = "application/json"
            content = json.dumps(data, ensure_ascii=False).encode("utf8")
            self.client.put_object(
                self.bucket,
                name,
                io.BytesIO(content),
                -1,
                part_size=50 * 1024 * 1024,
                content_type=content_type,
            )
            return name
        elif name.endswith(".geojson"):
            content_type = "application/geojson"
            content = json.dumps(data, ensure_ascii=False).encode("utf8")
            self.client.put_object(
                self.bucket,
                name,
                io.BytesIO(content),
                -1,
                part_size=50 * 1024 * 1024,
                content_type=content_type,
            )
            return name
        else:
            raise TypeError("Not a valid dict type extension")

    def create_from_string(self, data, name):
        content_type = "text/plain"
        prefix = "txt/"
        content = data.encode("utf8")
        self.client.put_object(
            self.bucket,
            name,
            io.BytesIO(content),
            -1,
            part_size=50 * 1024 * 1024,
            content_type=content_type,
        )
        return name

    def create_from_dataframe(self, data, name):
        if name.endswith(".csv"):
            content_type = "text/csv"
            content = data.to_csv().encode("utf8")
            self.client.put_object(
                self.bucket,
                name,
                io.BytesIO(content),
                -1,
                part_size=50 * 1024 * 1024,
                content_type=content_type,
            )
            return name
        elif name.endswith(".json"):
            content_type = "application/json"
            content = data.to_json().encode("utf8")
            self.client.put_object(
                self.bucket,
                name,
                io.BytesIO(content),
                -1,
                part_size=50 * 1024 * 1024,
                content_type=content_type,
            )
            return name
        else:
            raise TypeError("Not a valid dataframe type extension")

    def read_from_json(self, name):
        try:
            response = self.client.get_object(self.bucket, name)
            data = json.load(response)
        finally:
            response.close()
            response.release_conn()
        df = pd.DataFrame.from_dict(data)
        # Convert the index to integers (the timestamps) and then to datetime
        df.index = pd.to_datetime(df.index.astype(int), unit="ms")
        # Now your index is a datetime object and you can use strftime
        df.index = df.index.strftime("%Y-%m-%d")
        return df

    @with_geopandas
    def read_from_geojson(self, gpd, name):
        try:
            response = self.client.get_object(self.bucket, name)
            data = json.load(response)
        finally:
            response.close()
            response.release_conn()
        return gpd.GeoDataFrame.from_features(data)

    @with_rio
    def read_from_rasterio(self, rio, name):
        try:
            response = self.client.get_object(self.bucket, name)
            data = response
        finally:
            response.close()
            response.release_conn()
        return rio.open(data)
