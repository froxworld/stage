my=require("myapps")
local json = require('cjson')

v = '{"titre":"2000","prix":"essesds sdsd","magasin":"manger ...","vendeuse":"c est elle","apprÃ©ciation":"pas terrible","origine":"webapps"}'

t = json.decode(v)
print(type(t))
print("champs1: " ..t["titre"])
print("champs2: " ..t["prix"])
print("champs3: " ..t["magasin"])
print("champs4: " ..t["vendeuse"])


