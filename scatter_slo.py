import pandas as pd
#df = pd.read_csv('Koordinate.csv', index_col=0, names=['ZaporednaStevilkaOsebeVPN','GeoKoordinataX','GeoKoordinataY'])

import geopandas as gpd
from shapely.geometry import Point

slovenia = gpd.read_file('')
slovenia.plot()