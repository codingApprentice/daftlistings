import pandas as pd
from daftlistings import Daft, Location, SearchType, PropertyType, SortType, MapVisualization

 
daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_property_type(PropertyType.HOUSE)
daft.set_min_price(250000)
daft.set_max_price(425000)
daft.set_min_beds(3)
daft.set_min_baths(2)
# daft.set_min_floor_size(100)

listings = daft.search()

# cache the listings in the local file
with open("result.txt", "w") as fp:
  fp.writelines("%s\n" % listing.as_dict_for_mapping() for listing in listings)

# read from the local file
with open("result.txt") as fp:
  lines = fp.readlines()

properties = []
for line in lines:
  properties.append(eval(line))

df = pd.DataFrame(properties)
print(df)

df.to_excel("output.xlsx")

dublin_map = MapVisualization(df)
dublin_map.add_markers()
dublin_map.add_colorbar()
dublin_map.save("ireland_sale.html")
print("Done, please checkout the html file")