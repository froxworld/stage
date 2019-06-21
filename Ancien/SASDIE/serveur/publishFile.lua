my=require("myapps")

if (arg[1] == nil) then
  os.exit()
end
email =  arg[1]

if (arg[2] == nil) then
  os.exit()
end
passwd =  arg[2]

my.connexion(email,passwd)

if (arg[3] == nil) then
  os.exit()
end
file1 = assert(io.open(arg[3], "r"))
content1 = file1:read("*all")

if (arg[4] == nil) then
  os.exit()
end
file2 = assert(io.open(arg[4], "r"))
content2 = file2:read("*all")

if (arg[5] == nil) then
  os.exit()
end
file3 = assert(io.open(arg[5], "r"))
content3 = file3:read("*all")

print("storing files: "..arg[3].." and "..arg[4].." and "..arg[5])

my.creer_fichier(arg[3],content1)
my.creer_fichier(arg[4],content2)
my.creer_fichier(arg[5],content3)
