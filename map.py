import os
import ee
import folium
from folium import plugins
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account
from google.cloud import storage






root_dir = "/Users/acarite/Desktop/capstone/GPPDataPortal"
cred_dir = root_dir + os.sep + '.cred'
cred_file = cred_dir + os.sep + 'ee_creds.json'

# Add custom basemaps to folium
basemaps = {
    'Google Maps': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Maps',
        overlay = True,
        control = True
    ),
    'Google Satellite': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Google Terrain': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Terrain',
        overlay = True,
        control = True
    ),
    'Google Satellite Hybrid': folium.TileLayer(
        tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
        attr = 'Google',
        name = 'Google Satellite',
        overlay = True,
        control = True
    ),
    'Esri Satellite': folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = True,
        control = True
    )
}

class GCSStorageClient:
    def __init__(self, cred_file):
        self.blob_svc_client = None

        if os.path.exists(cred_file):

            self.blob_svc_client = storage.Client.from_service_account_json(cred_file)

        else:
            print(f"ERROR: {cred_file} not found")

    def selectBucket(self, bucket_name):
        self.bucket_name = bucket_name
        return f"Current selected bucket: {self.bucket_name}"

    # def listBlobs(self, bucket_name):
    #     if self.blob_svc_client:
    #         if not self.bucket_client_list[bucket_name]:
    #             self.bucket_client_list[bucket_name] = self.blob_svc_client.get_bucket(bucket_name)
    #         blob_list = self.bucket_client_list[bucket_name].list_blobs()
    #         return blob_list
    #     else:
    #         print("ERROR: GCS Storage Blob Client does not exist.")
    
    def downloadBlob(self, bucket_name, blob_name):
        if self.blob_svc_client:
            if not self.bucket_client_list[bucket_name]:
                self.bucket_client_list[bucket_name] = self.blob_svc_client.get_bucket(bucket_name)
            
            return self.bucket_client_list[bucket_name].blob(blob_name).download_as_bytes()
        else:
            print("ERROR: GCS Storage Blob Client does not exist.")


# class ee_client:
#     SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

#     def __init__(self, cred_folder):
#         self.creds = None
#         self.client = None
#         if os.path.exists(cred_folder+'/ee_creds.json'):
#             self.creds = Credentials.from_authorized_user_file(cred_folder+'/token.json', self.SCOPES)

# def map_init(creds = cred_file):
    
#     credentials = service_account.Credentials.from_service_account_file(cred_file)
#     scoped_credentials = credentials.with_scopes(
#         ['https://www.googleapis.com/auth/cloud-platform'])

#     session = AuthorizedSession(scoped_credentials)

#     ee_creds = ee.ServiceAccountCredentials(SERVICE_ACCOUNT, KEY)
#     ee.Initialize(ee_creds)

#     return session

# Define a method for displaying Earth Engine image tiles on a folium map.
def add_ee_layer(self, ee_object, vis_params, name):
    
    try:    
        # display ee.Image()
        if isinstance(ee_object, ee.image.Image):    
            map_id_dict = ee.Image(ee_object).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
            ).add_to(self)
        # display ee.ImageCollection()
        elif isinstance(ee_object, ee.imagecollection.ImageCollection):    
            ee_object_new = ee_object.mosaic()
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
            ).add_to(self)
        # display ee.Geometry()
        elif isinstance(ee_object, ee.geometry.Geometry):    
            folium.GeoJson(
            data = ee_object.getInfo(),
            name = name,
            overlay = True,
            control = True
        ).add_to(self)
        # display ee.FeatureCollection()
        elif isinstance(ee_object, ee.featurecollection.FeatureCollection):  
            ee_object_new = ee.Image().paint(ee_object, 0, 2)
            map_id_dict = ee.Image(ee_object_new).getMapId(vis_params)
            folium.raster_layers.TileLayer(
            tiles = map_id_dict['tile_fetcher'].url_format,
            attr = 'Google Earth Engine',
            name = name,
            overlay = True,
            control = True
        ).add_to(self)
    
    except:
        print("Could not display {}".format(name))
    
# Add EE drawing method to folium.
# folium.Map.add_ee_layer = add_ee_layer

def get_map():
    dem = ee.Image()
    # Set visualization parameters.
    vis_params = {
    'min': 0,
    'max': 4000,
    'palette': ['006633', 'E5FFCC', '662A00', 'D8D8D8', 'F5F5F5']}

    # Create a folium map object.
    my_map = folium.Map(location=[40.33, -99.42], zoom_start=4, height=500)

    # Add custom basemaps
    basemaps['Google Maps'].add_to(my_map)
    basemaps['Google Satellite Hybrid'].add_to(my_map)

    # Add the elevation model to the map object.
    my_map.add_ee_layer(dem.updateMask(dem.gt(0)), vis_params, 'DEM')

    # Display ee.Image
    dataset = ee.Image('JRC/GSW1_1/GlobalSurfaceWater')
    occurrence = dataset.select('occurrence');
    occurrenceVis = {'min': 0.0, 'max': 100.0, 'palette': ['ffffff', 'ffbbbb', '0000ff']}
    my_map.add_ee_layer(occurrence, occurrenceVis, 'JRC Surface Water')

    # Display ee.Geometry
    holePoly = ee.Geometry.Polygon(coords = [[[-35, -10], [-35, 10], [35, 10], [35, -10], [-35, -10]]],
                                proj= 'EPSG:4326',
                                geodesic = True,
                                maxError= 1.,
                                evenOdd = False)
    my_map.add_ee_layer(holePoly, {}, 'Polygon')

    # Display ee.FeatureCollection
    fc = ee.FeatureCollection('TIGER/2018/States')
    my_map.add_ee_layer(fc, {}, 'US States')

    return my_map
    # # Add a layer control panel to the map.
    # my_map.add_child(folium.LayerControl())
    # plugins.Fullscreen().add_to(my_map)

    # # Display the map.
    # display(my_map)