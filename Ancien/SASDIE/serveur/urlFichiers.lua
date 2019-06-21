my=require("myapps")

email='bodin@irisa.fr'
passwd='141161'
my.connexion(email,passwd)
lf = my.fichiers()
mc =  my.macle()
print("Ma cle est : "..mc)
print("nombre de fichiers: " .. #lf-2)
for i= 3,#lf  do
   print("http://prototypel1.irisa.fr/files/"..mc.."/"..lf[i])
end
my.deconnexion()
