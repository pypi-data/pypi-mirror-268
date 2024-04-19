from AdDownloader import adlib_api
from AdDownloader.media_download import start_media_download

access_token = input() # your fb-access-token-here
ads_api = adlib_api.AdLibAPI(access_token, project_name = "test1")