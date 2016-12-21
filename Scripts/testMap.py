from tkinter import * 

fenetre = Tk()
# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()
label = Label(fenetre, text="Hello World")
label.pack()

fenetre.mainloop()

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
# create new figure, axes instances.
fig=plt.figure()
ax=fig.add_axes([0.1,0.1,0.8,0.8])
# setup mercator map projection.
m = Basemap(llcrnrlon=-100.,llcrnrlat=20.,urcrnrlon=20.,urcrnrlat=60.,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',projection='merc',\
            lat_0=40.,lon_0=-20.,lat_ts=20.)
# nylat, nylon are lat/lon of New York
nylat = 40.78; nylon = -73.98
# lonlat, lonlon are lat/lon of London.
lonlat = 51.53; lonlon = 0.08
# draw great circle route between NY and London
m.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
m.drawcoastlines()
m.fillcontinents()
# draw parallels
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
ax.set_title('Great Circle from New York to London')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
 
### PARAMETERS FOR MATPLOTLIB :
import matplotlib as mpl
mpl.rcParams['font.size'] = 10.
mpl.rcParams['font.family'] = 'Comic Sans MS'
mpl.rcParams['axes.labelsize'] = 8.
mpl.rcParams['xtick.labelsize'] = 6.
mpl.rcParams['ytick.labelsize'] = 6.
 
fig = plt.figure(figsize=(11.7,8.3))
#Custom adjust of the subplots
plt.subplots_adjust(left=0.05,right=0.95,top=0.90,bottom=0.05,wspace=0.15,hspace=0.05)
ax = plt.subplot(111)
#Let's create a basemap of Europe
x1 = -5.0
x2 = 15.
y1 = 45.
y2 = 54.
 
m = Basemap(resolution='i',projection='merc', llcrnrlat=y1,urcrnrlat=y2,llcrnrlon=x1,urcrnrlon=x2,lat_ts=(x1+x2)/2)
m.drawcountries(linewidth=0.5)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(y1,y2,2.),labels=[1,0,0,0],color='black',dashes=[1,0],labelstyle='+/-',linewidth=0.2) # draw parallels
m.drawmeridians(np.arange(x1,x2,2.),labels=[0,0,0,1],color='black',dashes=[1,0],labelstyle='+/-',linewidth=0.2) # draw meridians
 
from matplotlib.collections import LineCollection
from matplotlib import cm

import shapefile
 
r = shapefile.Reader(r"C:/Users/Joe/Downloads/gadm/MyEurope")
shapes = r.shapes()
records = r.records()

for record, shape in zip(records,shapes):
    lons,lats = zip(*shape.points)
    data = np.array(m(lons, lats)).T
 
    if len(shape.parts) == 1:
        segs = [data,]
    else:
        segs = []
        for i in range(1,len(shape.parts)):
            index = shape.parts[i-1]
            index2 = shape.parts[i]
            segs.append(data[index:index2])
        segs.append(data[index2:])
 
    lines = LineCollection(segs,antialiaseds=(1,))
    lines.set_facecolors(cm.jet(np.random.rand(1)))
    lines.set_edgecolors('k')
    lines.set_linewidth(0.1)
    ax.add_collection(lines)
 
plt.savefig('tutorial10.png',dpi=300)
plt.show()



import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
import math

# cities = [["Paris",10],
#           ["Bruxelles",10],
#           ["Londres",5],
#           ["Berlin",25]]
cities = [["Paris",10],
          ["Bruxelles",10],
          ["Londres",10],
          ["Berlin",10],
          ["Madrid",10],
          ["Dublin",10],
          ["Roma",10],
          ["Bucarest",10],
          ["Copenhagen",10],
          ["Luxemboug",10],
          ["Praha",10],
          ["Budapest",10]]
# cities = [["Chicago",10],
#           ["Boston",10],
#           ["New York",5],
#           ["San Francisco",25]]
scale = 1#5
map = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
             llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
map = Basemap(projection='merc',llcrnrlat=30,urcrnrlat=65,\
             llcrnrlon=-15,urcrnrlon=60,lat_ts=20,resolution='c')
# m.drawcoastlines()
# m.fillcontinents(color='coral',lake_color='aqua')
 # map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='lcc',lat_1=0,lat_2=60,lon_0=-95)
# map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
#          projection='lcc',lat_1=32,lat_2=45,lon_0=-95)
# map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
#          projection='lcc',lat_1=32,lat_2=45,lon_0=20)
# 
# # load the shapefile, use the name 'states'
# map.readshapefile('C:/Users/Joe/Downloads/gadm/MyEurope', name='states', drawbounds=True)
# map.drawcoastlines()
# map.fillcontinents(color='coral',lake_color='aqua')

# map = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,\
#             llcrnrlon=-180,urcrnrlon=180,lat_ts=20,resolution='c')
map.drawcoastlines()
map.fillcontinents(color='coral',lake_color='aqua')
# draw parallels and meridians.
# map.drawparallels(np.arange(-90.,91.,30.))
# map.drawmeridians(np.arange(-180.,181.,60.))
map.drawmapboundary(fill_color='aqua')
plt.title("Mercator Projection")

#Get the location of each city and plot it
geolocator = Nominatim()
for (city,count) in cities:
    loc = geolocator.geocode(city)
    print("lat=",loc.latitude,"long=",loc.longitude)
    x, y = map(loc.longitude, loc.latitude)
    map.plot(x,y,marker='o',color='Red',markersize=int(math.sqrt(count))*scale)
    plt.text(x+1000,y+1000,city)

#trace entre madrid et londres
locMad = geolocator.geocode("Madrid")
locLond = geolocator.geocode("Londres")
longMad,latMad = map(locMad.longitude,locMad.latitude)
longLon,latLon = map(locLond.longitude,locLond.latitude)

map.drawgreatcircle(locMad.longitude,locMad.latitude,locLond.longitude,locLond.latitude,linewidth=2,color='b')

plt.show()