
chdir(path[0])
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from geopy.geocoders import Nominatim
from geopy import distance
import math
from geopy.distance import great_circle
import geopy

import csv
from geopy.point import Point
# c = csv.writer(open("MONFICHIER.csv", "w"))
# w_file=open(os.path.join('test.csv'), 'w') 
c = csv.writer(open("text.csv","w"), delimiter=';', lineterminator='\n')
# cities = ["Paris","Bruxelles","Londres","Berlin","Madrid","Dublin","Roma","Bucarest","Copenhagen","Luxemboug",
#           "Praha","Budapest"]
cities = [' Tirana',' Berlin',' Andorre-la-Vieille',' Vienne',' Bruxelles',' Minsk',' Sarajevo',' Sofia',' Nicosie',' Zagreb',' Copenhague',' Madrid',' Tallinn',' Helsinki',' Paris',' Athènes',' Budapest',' Dublin',' Reykjavik',' Roma',' Astana',' Pristina',' Riga',' Vaduz',' Vilnius',' Luxembourg',' Skopje',' La Valette',' Chisinau',' Monaco',' Podgorica',' Oslo',' Amsterdam',' Varsovie',' Lisbonne',' Bucarest',' Londres',' Moscou',' Belgrade',' Bratislava',' Ljubljana',' Berne',' Stockholm',' Prague',' Kiev',' Vatican'
]
villes={"Kabul":Point("34°28''N 69°11''E"),"Tirane":Point('41°18''N 19°49''E'),"Algiers":Point('36°42''N 03°08''E'),"Pago Pago":Point('14°16''S 170°43''W'),"Andorra la Vella":Point('42°31''N 01°32''E'),"Luanda":Point('08°50''S 13°15''E'),"W. Indies":Point('17°20''N 61°48''W'),"Buenos Aires":Point('36°30''S 60°00''W'),"Yerevan":Point('40°10''N 44°31''E'),"Oranjestad":Point('12°32''N 70°02''W'),"Canberra":Point('35°15''S 149°08''E'),"Vienna":Point('48°12''N 16°22''E'),"Baku":Point('40°29''N 49°56''E'),"Nassau":Point('25°05''N 77°20''W'),"Manama":Point('26°10''N 50°30''E'),"Dhaka":Point('23°43''N 90°26''E'),"Bridgetown":Point('13°05''N 59°30''W'),"Minsk":Point('53°52''N 27°30''E'),"Brussels":Point('50°51''N 04°21''E'),"Belmopan":Point('17°18''N 88°30''W'),"Porto-Novo (constitutional cotonou) (seat of gvnt)":Point('06°23''N 02°42''E'),"Thimphu":Point('27°31''N 89°45''E'),"La Paz (adm.)/sucre (legislative)":Point('16°20''S 68°10''W'),"Sarajevo":Point('43°52''N 18°26''E'),"Gaborone":Point('24°45''S 25°57''E'),"Brasilia":Point('15°47''S 47°55''W'),"Road Town":Point('18°27''N 64°37''W'),"Bandar Seri Begawan":Point('04°52''N 115°00''E'),"Sofia":Point('42°45''N 23°20''E'),"Ouagadougou":Point('12°15''N 01°30''W'),"Bujumbura":Point('03°16''S 29°18''E'),"Phnom Penh":Point('11°33''N 104°55''E'),"Yaounde":Point('03°50''N 11°35''E'),"Ottawa":Point('45°27''N 75°42''W'),"Praia":Point('15°02''N 23°34''W'),"George Town":Point('19°20''N 81°24''W'),"Bangui":Point('04°23''N 18°35''E'),"N'Djamena":Point('12°10''N 14°59''E'),"Santiago":Point('33°24''S 70°40''W'),"Beijing":Point('39°55''N 116°20''E'),"Bogota":Point('04°34''N 74°00''W'),"Moroni":Point('11°40''S 43°16''E'),"Brazzaville":Point('04°09''S 15°12''E'),"San Jose":Point('09°55''N 84°02''W'),"Yamoussoukro":Point('06°49''N 05°17''W'),"Zagreb":Point('45°50''N 15°58''E'),"Havana":Point('23°08''N 82°22''W'),"Nicosia":Point('35°10''N 33°25''E'),"Prague":Point('50°05''N 14°22''E'),"P'yongyang":Point('39°09''N 125°30''E'),"Kinshasa":Point('04°20''S 15°15''E'),"Copenhagen":Point('55°41''N 12°34''E'),"Djibouti":Point('11°08''N 42°20''E'),"Roseau":Point('15°20''N 61°24''W'),"Santo Domingo":Point('18°30''N 69°59''W'),"Dili":Point('08°29''S 125°34''E'),"Quito":Point('00°15''S 78°35''W'),"Cairo":Point('30°01''N 31°14''E'),"San Salvador":Point('13°40''N 89°10''W'),"Malabo":Point('03°45''N 08°50''E'),"Asmara":Point('15°19''N 38°55''E'),"Tallinn":Point('59°22''N 24°48''E'),"Addis Ababa":Point('09°02''N 38°42''E'),"Stanley":Point('51°40''S 59°51''W'),"Torshavn":Point('62°05''N 06°56''W'),"Suva":Point('18°06''S 178°30''E'),"Helsinki":Point('60°15''N 25°03''E'),"Paris":Point('48°50''N 02°20''E'),"Cayenne":Point('05°05''N 52°18''W'),"Papeete":Point('17°32''S 149°34''W'),"Libreville":Point('00°25''N 09°26''E'),"Banjul":Point('13°28''N 16°40''W'),"T'bilisi":Point('41°43''N 44°50''E'),"Berlin":Point('52°30''N 13°25''E'),"Accra":Point('05°35''N 00°06''W'),"Athens":Point('37°58''N 23°46''E'),"Nuuk":Point('64°10''N 51°35''W'),"Basse-Terre":Point('16°00''N 61°44''W'),"Guatemala":Point('14°40''N 90°22''W'),"St. Peter Port":Point('49°26''N 02°33''W'),"Conakry":Point('09°29''N 13°49''W'),"Bissau":Point('11°45''N 15°45''W'),"Georgetown":Point('06°50''N 58°12''W'),"Port-au-Prince":Point('18°40''N 72°20''W'),"Tegucigalpa":Point('14°05''N 87°14''W'),"Budapest":Point('47°29''N 19°05''E'),"Reykjavik":Point('64°10''N 21°57''W'),"New Delhi":Point('28°37''N 77°13''E'),"Jakarta":Point('06°09''S 106°49''E'),"Tehran":Point('35°44''N 51°30''E'),"Baghdad":Point('33°20''N 44°30''E'),"Dublin":Point('53°21''N 06°15''W'),"Jerusalem":Point('31°47''N 35°12''E'),"Rome":Point('41°54''N 12°29''E'),"Kingston":Point('18°00''N 76°50''W'),"Amman":Point('31°57''N 35°52''E'),"Astana":Point('51°10''N 71°30''E'),"Nairobi":Point('01°17''S 36°48''E'),"Tarawa":Point('01°30''N 173°00''E'),"Kuwait":Point('29°30''N 48°00''E'),"Bishkek":Point('42°54''N 74°46''E'),"Vientiane":Point('17°58''N 102°36''E'),"Riga":Point('56°53''N 24°08''E'),"Beirut":Point('33°53''N 35°31''E'),"Maseru":Point('29°18''S 27°30''E'),"Monrovia":Point('06°18''N 10°47''W'),"Tripoli":Point('32°49''N 13°07''E'),"Vaduz":Point('47°08''N 09°31''E'),"Vilnius":Point('54°38''N 25°19''E'),"Luxembourg":Point('49°37''N 06°09''E'),"Macau":Point('22°12''N 113°33''E'),"Antananarivo":Point('18°55''S 47°31''E'),"Lilongwe":Point('14°00''S 33°48''E'),"Kuala Lumpur":Point('03°09''N 101°41''E'),"Male":Point('04°00''N 73°28''E'),"Bamako":Point('12°34''N 07°55''W'),"Valletta":Point('35°54''N 14°31''E'),"Fort-de-France":Point('14°36''N 61°02''W'),"Nouakchott":Point('20°10''S 57°30''E'),"Mamoudzou":Point('12°48''S 45°14''E'),"Mexico":Point('19°20''N 99°10''W'),"Palikir":Point('06°55''N 158°09''E'),"Chisinau":Point('47°02''N 28°50''E'),"Maputo":Point('25°58''S 32°32''E'),"Yangon":Point('16°45''N 96°20''E'),"Windhoek":Point('22°35''S 17°04''E'),"Kathmandu":Point('27°45''N 85°20''E'),"Amsterdam/The Hague (seat of Gvnt)":Point('52°23''N 04°54''E'),"Willemstad":Point('12°05''N 69°00''W'),"Noumea":Point('22°17''S 166°30''E'),"Wellington":Point('41°19''S 174°46''E'),"Managua":Point('12°06''N 86°20''W'),"Niamey":Point('13°27''N 02°06''E'),"Abuja":Point('09°05''N 07°32''E'),"Kingston":Point('45°20''S 168°43''E'),"Saipan":Point('15°12''N 145°45''E'),"Oslo":Point('59°55''N 10°45''E'),"Masqat":Point('23°37''N 58°36''E'),"Islamabad":Point('33°40''N 73°10''E'),"Koror":Point('07°20''N 134°28''E'),"Panama":Point('09°00''N 79°25''W'),"Port Moresby":Point('09°24''S 147°08''E'),"Asuncion":Point('25°10''S 57°30''W'),"Lima":Point('12°00''S 77°00''W'),"Manila":Point('14°40''N 121°03''E'),"Warsaw":Point('52°13''N 21°00''E'),"Lisbon":Point('38°42''N 09°10''W'),"San Juan":Point('18°28''N 66°07''W'),"Doha":Point('25°15''N 51°35''E'),"Seoul":Point('37°31''N 126°58''E'),"Bucuresti":Point('44°27''N 26°10''E'),"Moskva":Point('55°45''N 37°35''E'),"Kigali":Point('01°59''S 30°04''E'),"Basseterre":Point('17°17''N 62°43''W'),"Castries":Point('14°02''N 60°58''W'),"Saint-Pierre":Point('46°46''N 56°12''W'),"Kingstown":Point('13°10''N 61°10''W'),"Apia":Point('13°50''S 171°50''W'),"San Marino":Point('43°55''N 12°30''E'),"Sao Tome":Point('00°10''N 06°39''E'),"Riyadh":Point('24°41''N 46°42''E'),"Dakar":Point('14°34''N 17°29''W'),"Freetown":Point('08°30''N 13°17''W'),"Bratislava":Point('48°10''N 17°07''E'),"Ljubljana":Point('46°04''N 14°33''E'),"Honiara":Point('09°27''S 159°57''E'),"Mogadishu":Point('02°02''N 45°25''E'),"Pretoria (adm.) / Cap Town (Legislative) / Bloemfontein (Judicial)":Point('25°44''S 28°12''E'),"Madrid":Point('40°25''N 03°45''W'),"Khartoum":Point('15°31''N 32°35''E'),"Paramaribo":Point('05°50''N 55°10''W'),"Mbabane (Adm.)":Point('26°18''S 31°06''E'),"Stockholm":Point('59°20''N 18°03''E'),"Bern":Point('46°57''N 07°28''E'),"Damascus":Point('33°30''N 36°18''E'),"Dushanbe":Point('38°33''N 68°48''E'),"Bangkok":Point('13°45''N 100°35''E'),"Skopje":Point('42°01''N 21°26''E'),"Lome":Point('06°09''N 01°20''E'),"Nuku'alofa":Point('21°10''S 174°00''W'),"Tunis":Point('36°50''N 10°11''E'),"Ankara":Point('39°57''N 32°54''E'),"Ashgabat":Point('38°00''N 57°50''E'),"Funafuti":Point('08°31''S 179°13''E'),"Kampala":Point('00°20''N 32°30''E'),"Kiev (Rus)":Point('50°30''N 30°28''E'),"Abu Dhabi":Point('24°28''N 54°22''E'),"London":Point('51°36''N 00°05''W'),"Dodoma":Point('06°08''S 35°45''E'),"Washington DC":Point('39°91''N 77°02''W'),"Charlotte Amalie":Point('18°21''N 64°56''W'),"Montevideo":Point('34°50''S 56°11''W'),"Tashkent":Point('41°20''N 69°10''E'),"Port-Vila":Point('17°45''S 168°18''E'),"Caracas":Point('10°30''N 66°55''W'),"Hanoi":Point('21°05''N 105°55''E'),"Belgrade":Point('44°50''N 20°37''E'),"Lusaka":Point('15°28''S 28°16''E'),"Harare":Point('17°43''S 31°02''E')}
from geopy.distance import great_circle
for v1 in villes:
    for v2 in villes:
        dist = great_circle(villes[v1],villes[v2]).km
        ligne = [v1,v2,dist]
        c.writerow(ligne)
# c.close()

#Get the location of each city and plot it
geolocator = Nominatim()
from LatLon import string2latlon
for v1 in cities:
    for v2 in cities:
        from geopy.point import Point
        Point("34°28''N 69°11''E")
        Point("36°30''S 60°00''W")


        #trace entre madrid et londres
        ville1 = geolocator.geocode(v1)
        ville2 = geolocator.geocode(v2)
        dist =great_circle((ville1.longitude,ville1.latitude),(ville2.latitude,ville2.latitude)).km
        ligne = [v1,v2,dist]
        c.writerow(ligne)

c.close()

    
    #avec l'algorithme GreatCircleDistance (fr.wikipedia.org/wiki/Distance_du_grand_cercle)
    distance.distance = distance.GreatCircleDistance
    #avec l'algorithme de Vincenty (en.wikipedia.org/wiki/Vincenty%27s_formulae)
    # distance.VincentyDistance.ELLIPSOID = 'wgs-84' 
    
    distance.distance(ville1, ville2).km
    long1,lat1 = map(loc1.longitude,loc1.latitude)
    
    map.plot(long1,lat1,marker='o',color=couleur,markersize=int(math.sqrt(10))*scale)
    plt.text(long1+1000,lat1+1000,listVilles[index])
    
    long2,lat2 = map(loc2.longitude,loc2.latitude)
    map.plot(long2,lat2,label="kkkkk",marker='o',color=couleur,markersize=int(math.sqrt(10))*scale)
    plt.text(long2+1000,lat2+1000,listVilles[index+1])
    
    map.drawgreat