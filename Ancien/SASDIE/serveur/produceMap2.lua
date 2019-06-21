my=require("myapps")

email='bodin@irisa.fr'
passwd='141161'
my.connexion(email,passwd)
w,n = my.position()
print(w,n)

lf = 'https://storage.googleapis.com/mapsdevsite/json/mapmarkers2.xml'
map = my.googlemap(n,w,lf)
my.enregistrer_html(map)
my.deconnexion()
