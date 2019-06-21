my=require("myapps")
email='bodin@irisa.fr'
passwd='141161'

my.connexion(email,passwd)
lf = my.fichiers()
print("nombre de fichiers: " .. #lf-2)
for i= 3,#lf  do

if lf[i]:find("thumb") then
   print(lf[i])
end

end
