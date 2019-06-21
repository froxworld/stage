my=require("myapps")
local SLAXML = require 'slaxdom'
email='bodin@irisa.fr'
passwd='141161'

my.connexion(email,passwd)
md = my.lire_metadata("5846c1c4310a4.jpg")
if (md ~=nil) then
   print(md)
   my.efface_metadata("5846c1c4310a4.jpg")
end
my.deconnexion()
