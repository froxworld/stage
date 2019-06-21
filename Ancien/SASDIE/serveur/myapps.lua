package.cpath = package.cpath .. ";/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/?.so"
local l=require("libmyapsistic")
local base64=require("ee5_base64")
local json = require('cjson')
local SLAXML = require 'slaxdom'
local readsensorscmd = "/home/pi/bin/readSensor.exe sensorsvalues.txt"

local function trim1(s)
  if (s == nil or s == '') then
    return ''
  end
  return (s:gsub("^%s*(.-)%s*$", "%1"))
end

local function split(s, delimiter)
    result = {};
    for match in (s..delimiter):gmatch("(.-)"..delimiter) do
        table.insert(result, match);
    end
    return result;
end

local function connex(mail,passw)
      assert((type(mail) == 'string'), "le mail doit être une chaîne de caractère")
      assert((type(passw) == 'string'), "le mot de passe doit être une chaîne de caractère")
      l.connect(mail,passw)
end

local function getkey()
      return l.getkeyid()
end

local function disco()
      l.disconnect()
end

local function filelist()
      local list
      list = l.listoffiles()
      list = json.decode(list)
      return list
end

local function xfilelist()
      local list
      list, update = l.xlistoffiles()
      list = json.decode(list)
      update = json.decode(update)
      return list, update
end

local function setact(la)
--      la = json.encode(la)
      la = base64.encode(la)
      l.addactions(la)
end

local function setmeta(m)
      m = base64.encode(m)
      l.addmenu(m)
end

local function getmetadataforfile(f)
      local c
      c = l.getmetadata(f)
      if c then      
         c = base64.decode(c)
         return c
      else
         return nil
      end
end

local function rmmetadataforfile(f)
       assert((type(f) == 'string'), "le nom du fichier est incorrect")
      l.rmmetadata(f)
end

local function setoutput(c)
      local pc
      assert((type(c) == 'string'), "le contenu doit être une chaîne de caractère")
      pc = "<html> <header><title>Réponse MyAppsIstic</title></header><body>";
      pc = pc .. c;
      pc = pc .. "</body></html>";
      pc = base64.encode(pc);
      l.generate("default.html",pc)
end

local function setoutputComplete(c)
      local pc
      assert((type(c) == 'string'), "le contenu doit être une chaîne de caractère")
      pc = base64.encode(c);
      l.generate("cams.html",pc)
end

local function pt(t)
      l.puttask(t)
end

local function gt()
      local t
       t = l.gettask()
       t = base64.decode(t)
      return t
end

local function pos()
      return l.position()
end

local function cf(f,c)
      c=base64.encode(c)
      l.putfile(f,c)
end

local function pf(f)
      local c
      local file = io.open(f,"rb");
      if (file ~= nil) then
        c = file:read("*all")         
        file:close()
        c=base64.encode(c)
        l.putfile(f,c)
      else
        print("Fichier non trouvé : "..f)
      end
end

local function addusr(p,n,e,w,c)
      l.adduser(p,n,e,w,c)
end

local function rmusr(e,c)
      l.rmuser(e,c)
end


local function chgpasswd(p,n,e,w,c)
      l.chgpasswd(p,n,e,w,c)
end

local function gf(f)
      local c, lf
      lf = filelist()
      c = l.getfile(f)
      c = base64.decode(c)
      return c
end

local function wait(s)
      os.execute("sleep " .. tonumber(s))
end

local function errfunc (x)
  print ("errfunc called", x)
  return "oh no!"
end

local function elementTextMD(para,field)
  for _,n in ipairs(para.kids) do
    if n.type=='element' then
        if n.name == field then
           --print("tag: "..n.name)
           --print("val: "..n.kids[1].value)
	   if field == 'comment' then
                if (n.kids[1] ~= nil) and  n.kids[1].value then
		   --print('decoding: '..n.kids[1].value)
		   local valmeta = n.kids[1].value
		   if valmeta:sub(1,1) == '{' then
 		       return json.decode(n.kids[1].value)
                   else 
		     print("Le format des métadata n'est pas le bon : "..valmeta)
                     return ''
                   end
                else
		return ''
                end
	   else 
	       return n.kids[1].value	   
           end
        end
     end
  end
  return ''
end

local  function metadata_field(md,field)
  local doc = SLAXML:dom(md)
  local para = doc.root
  if para then
     return elementTextMD(para,field)
  end
  return ''
end


local function genJsMap(n,w,lf)
local map=[[
<style>
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {
        height: 100%;
      }
      /* Optional: Makes the sample page fill the window. */
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
    </style>
    <div id="map"></div>

    <script>
      var customLabel = {
        restaurant: {
          label: 'R'
        },
        bar: {
          label: 'B'
        }
      };

        function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          center: new google.maps.LatLng(]]..n..','..w..[[),
          zoom: 12
        });
        var infoWindow = new google.maps.InfoWindow;

          // Change this depending on the name of your PHP or XML file
          downloadUrl(']]..lf..[[', function(data) {
            var xml = data.responseXML;
            var markers = xml.documentElement.getElementsByTagName('marker');
            Array.prototype.forEach.call(markers, function(markerElem) {
              var name = markerElem.getAttribute('name');
              var address = markerElem.getAttribute('address');
              var type = markerElem.getAttribute('type');
              var point = new google.maps.LatLng(
                  parseFloat(markerElem.getAttribute('lat')),
                  parseFloat(markerElem.getAttribute('lng')));

              var infowincontent = document.createElement('div');
              var strong = document.createElement('strong');
              strong.textContent = name
              infowincontent.appendChild(strong);
              infowincontent.appendChild(document.createElement('br'));

              var text = document.createElement('text');
              text.textContent = address
              infowincontent.appendChild(text);
              var icon = customLabel[type] || {};
              var marker = new google.maps.Marker({
                map: map,
                position: point,
                label: icon.label
              });
              marker.addListener('click', function() {
                infoWindow.setContent(infowincontent);
                infoWindow.open(map, marker);
              });
            });
          });
        }



      function downloadUrl(url, callback) {
        var request = window.ActiveXObject ?
            new ActiveXObject('Microsoft.XMLHTTP') :
            new XMLHttpRequest;

        request.onreadystatechange = function() {
          if (request.readyState == 4) {
            request.onreadystatechange = doNothing;
            callback(request, request.status);
          }
        };

        request.open('GET', url, true);
        request.send(null);
      }

      function doNothing() {}
    </script>
    <script async defer
    src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDtOIOCMZmY65ZvGmlS4Dw8vLqYWhyNwZI&callback=initMap">
    </script>
]]

return map
end


local cos = math.cos
local sin = math.sin
local pi = math.pi
local sqrt = math.sqrt
local min = math.min
local asin = math.asin
local abs = math.abs

local function distanceGPS(from_lat_s, from_long_s, to_lat_s, to_long_s)
  local distance = 0
  local radius = 6367000
  local radian = pi / 180

  from_lat = tonumber(from_lat_s)
  from_long = tonumber(from_long_s)
  to_lat = tonumber(to_lat_s)
  to_long = tonumber(to_long_s)

  local deltaLatitude = sin(radian * (from_lat - to_lat) /2)
  local deltaLongitude = sin(radian * (from_long - to_long) / 2)

  local circleDistance = 2 * asin(min(1, sqrt(deltaLatitude * deltaLatitude +
     cos(radian * from_lat) * cos(radian * to_lat) * deltaLongitude * deltaLongitude)))
  distance = abs(radius * circleDistance)
  return distance
 end


local function sensors()
      os.execute(readsensorscmd)
      local f = io.open("sensorsvalues.txt", "rb")
      for line in f:lines() do
         local fields = split(line,';')
         return fields
      end
      return
end

 -- take an HD picture
local function takePictureForTheWeb()
     local namefile = "image.jpg"
     local cmd = "raspistill -w 640 -h 480  -o "..namefile
     os.execute(cmd)
end


local function help()
      print("[[**************************************************************************]]")
      print("[[****************************** AIDE **************************************]]")
      print("[[**************************************************************************]]")
      print("connexion(mail,passwd) : établie la connexion avec le serveur")
      print("files() : liste les fichiers de l'utilisateur")
      print("[[**************************************************************************]]")
      print("[[**************************************************************************]]")
end


--[[**************************************************************************]]
--[[******************************  Module  **********************************]]
--[[**************************************************************************]]
return
{
    connexion			= connex,
    deconnexion 		= disco,
    definir_actions 		= setact,    
    definir_metadata 		= setmeta,
    lire_metadata		= getmetadataforfile,
    enregistrer_html		= setoutput,
    publierpage_html            = setoutputComplete,
    poster_action		= pt,
    lire_action			= gt,
    fichiers			= filelist,
    xfichiers			= xfilelist,
    obtenir_contenu_fichier 	= gf,
    creer_fichier 	    	= cf,
    position     	    	= pos,
    envoyer_fichier 	    	= pf,
    ajout_utilisateur		= addusr,
    efface_utilisateur		= rmusr,
    attendre     		= wait,
    macle                       = getkey,
    str_split                   = split,
    str_trim                    = trim1,
    chg_password                = chgpasswd,
    valeur_metadata             = metadata_field,
    efface_metadata		= rmmetadataforfile,
    googlemap			= genJsMap,
    distance_gps                = distanceGPS,
    capteurs			= sensors,
    prendrePhoto		= takePictureForTheWeb,
    aide       			= help
}

