my=require("myapps")
local SLAXML = require 'slaxdom'
email='bodin@irisa.fr'
passwd='141161'

my.connexion(email,passwd)
lf = my.fichiers()
print("nombre de fichiers: " .. #lf-2)
for i= 3,#lf  do
   print(lf[i])
   md = my.lire_metadata(lf[i])
   if md ~= nil then
      print("Metadata pour le ficher :" ..md)
      print("Champs longitude :" .. my.valeur_metadata(md,'longitude'))
      tablemetadata =  my.valeur_metadata(md,'comment')
      if (tablemetadata ~= nil) and (tablemetadata['magasin'] ~= nil) then
         print("Champs metadata magasin :" .. tablemetadata['magasin'])
      end
   end
end
