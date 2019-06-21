my=require("myapps")
email='bodin@etudiant.univ-rennes1.fr'
passwd='141161'

my.connexion(email,passwd)
lf = my.fichiers()
print("nombre de fichiers: " .. #lf-2)
for i= 3,#lf  do
   print(lf[i])
end
