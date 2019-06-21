my=require("myapps")

email='commande.2@laorans.com'
passwd='23456'
my.connexion(email,passwd)
w,n = my.position()
print(w,n)
my.deconnexion()
