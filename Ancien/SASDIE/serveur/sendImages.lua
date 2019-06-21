my=require("myapps")

  email='bodin@etudiant.univ-rennes1.fr'
  passwd='141161'
  my.connexion(email,passwd)

  cssname = "info.css"
  filecss = io.open(cssname, "rb")
  ccss = filecss:read "*a"
  filecss:close()

  mc = my.macle()
  my.creer_fichier(cssname,ccss)
  print("Pour une visualisation directe, la page est à l'adresse : ","http://prototypel1.irisa.fr/"..mc.."/cams.html")
  -- création de la page HTML
  pageStatusSalle=[[
  <html>
  <header>
  <meta  http-equiv="refresh" content="10" />
  <meta charset="UTF-8">
  <link href="info.css" rel="stylesheet" type="text/css">
  <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0" />
  <title>Drone</title>
  </header>
   <body>
   <img src="../files/]]..mc..[[/image2_calib.jpg" alt="Drone2" style="height:720px;">
   <img src="../files/]]..mc..[[/image1_calib.jpg" alt="Drone1" style="height:720px;">
   <img src="../files/]]..mc..[[/image3.jpg" alt="Drone3" style="height:720px;">
   <p>Dernière mise à jour : ]]..os.date( "!%a %b %d, %H:%M", os.time() + 2 * 60 * 60 )..[[
      <p>
      <form>
      <input type="button" onClick="history.go(0)" value="recharger">
      </form>
   </body>
   </html>
  ]]
  my.publierpage_html(pageStatusSalle)

  -- take an HD picture
  function takePicture(num)
  local namefile = "HD_Images/"..os.time().."_image"..num ..".jpg"
     local cmd = "raspistill -o "..namefile
     os.execute(cmd)
     my.attendre(2)
  end

  -- take an HD picture
  function takePictureForTheWeb()
     local namefile = "image1.jpg"
     local namefile2 = "image2.jpg"
     local namefile3 = "image3.jpg"
     local nf = "image1_calib.jpg"
     local nf2 = "image2_calib.jpg"
     local cmd = "python3 take_pictures.py --img1 "..namefile.." --img2 "..namefile2.." --img3 "..namefile3
     os.execute(cmd)
     local cmd = "python3 calib_right.py --input "..namefile2.." --output "..nf2
     os.execute(cmd)
     local cmd = "python3 calib_left.py --input "..namefile.." --output "..nf
     os.execute(cmd)
     file = io.open(nf, "rb")
     image = file:read "*a"
     file:close()
     my.creer_fichier(nf,image)
     file = io.open(nf2, "rb")
     image2 = file:read "*a"
     file:close()
     my.creer_fichier(nf2,image2)
     file = io.open(namefile3, "rb")
     image3 = file:read "*a"
     file:close()
     my.creer_fichier(namefile3,image3)
     --my.attendre(30)
     my.attendre(1)
  end

  -- send images about 30 minutes numImages=360
  i = 0
  numImages = 360
  while i < numImages do
       start_time = os.time()
       -- send image to the Web
       takePictureForTheWeb()
       end_time = os.time()
       elapsed_time = os.difftime(end_time-start_time)
       print('time elapsed: ' .. elapsed_time .. 's')
       -- Now store high resolution images
--     takePicture(i)
       i = i+1
  end
  my.deconnexion()

		
