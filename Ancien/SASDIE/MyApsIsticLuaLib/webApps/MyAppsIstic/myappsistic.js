
/** check this at  https://facebook.github.io/react/docs/components-and-props.html**/
class Welcome extends React.Component {
    render() {
	return <h2>Hello, {this.props.name}</h2>;
    }
}

var MyAppsIstic = React.createClass({
    getInitialState: function() {
	return {
	    email: 'bodin@irisa.fr',
	    uid: '141161',
	    filename1: 'not a file name',
	    content1: 'not a content',
	    token: 'notatoken',
	    gpsw: '-1.639845',
	    gpsn: '48.116336',
	    metadata: '',
	    photofile: '', 
	    imagePreviewUrl: '',
	    imagePreviewBin: ''
	};
    },
    
    /**
     * This function will be re-bound in render multiple times. Each .bind() will
     * create a new function that calls this with the appropriate key as well as
     * the event. The key is the key in the state object that the value should be
     * mapped from.
     */
    handleInputChange: function(key, event) {
	var partialState = {};
	partialState[key] = event.target.value;
	this.setState(partialState);
	console.log("input change: " + event.target.value);
    },

    handleMetadata: function(event) {
        var keyid  = sessionStorage.getItem('keyid');
        var flag  =  sessionStorage.getItem('connected');
        //alert("flag is " + flag);                                                                                                         
        if (flag.localeCompare('Success') != 0){
            alert("Vous devez vous connecter");
            return;
        }
	if (this.state.filename1.localeCompare('not a file name') == 0){
            alert("Vous devez selectionner un fichier");
            return;
        }
	var md  = sessionStorage.getItem("metadata");
        var jmd = JSON.parse(md);
	var param = '{';
        for(var i in jmd){
	    var f = jmd[i];
	    var metanode =  document.getElementById(f);
	    var val = metanode.value;
	    param = param + "'"+f+"':"+"'"+val+"',";
        }
	param = param + '}';
	alert('metadata '+param);
	// let send the meta data
	var url = 'http://prototypel1.irisa.fr/API/putFileMetaData.php';
        var xhr = new XMLHttpRequest();
        var fd = new FormData();
        xhr.open("POST", url, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                //console.log(xhr.responseText); // handle response.                                                                        
                alert('Metatdata sending: Server response OK (' + xhr.responseText+')');
            }
        };
        fd.append('email',sessionStorage.getItem('email'));
        fd.append('token',sessionStorage.getItem('token'));
	fd.append('filename', this.state.filename1);
        fd.append('metadata', btoa(unescape(encodeURIComponent(param))));
        xhr.send(fd);
    },    

    handleSubmit: function(event) {
	var keyid  = sessionStorage.getItem('keyid');
	var flag  =  sessionStorage.getItem('connected');
	//alert("flag is " + flag);
	if (flag.localeCompare('Success') != 0){
	    alert("Vous devez vous connecter");
	    return;
	}

	if ((this.state.filename1.localeCompare('not a file name') == 0) && !(this.state.imagePreviewUrl)){
	    alert("Vous devez selectionner un fichier");
	    return;
	}

	// let send a text file
	if (this.state.filename1.localeCompare('not a file name') != 0){
	    var url = 'http://prototypel1.irisa.fr/API/putAFile.php';
	    var xhr = new XMLHttpRequest();
	    var fd = new FormData();
	    xhr.open("POST", url, true);
	    xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
		    //console.log(xhr.responseText); // handle response.
		    alert('Server response: ' + xhr.responseText);
		} 
	    };
	    fd.append('email',sessionStorage.getItem('email'));
	    fd.append('token',sessionStorage.getItem('token'));
	    fd.append('filename', this.state.filename1);
	    var node = document.getElementById('contenufichier');
	    fd.append('content', btoa(unescape(encodeURIComponent(node.innerText))));
	    xhr.send(fd);
	}
	//let send a photo
	if (this.state.imagePreviewUrl){
	    var url = 'http://prototypel1.irisa.fr/API/myappsistic_dld.php';
	    var xhr = new XMLHttpRequest();
	    var fd = new FormData();
	    xhr.open("POST", url, true);
	    xhr.onreadystatechange = function() {
		if (xhr.readyState == 4 && xhr.status == 200) {
		    //console.log(xhr.responseText); // handle response.
		    alert('Server response: ' + xhr.responseText);
		} 
	    };
	    fd.append('email',sessionStorage.getItem('email'));
	    fd.append('token',sessionStorage.getItem('token'));
	    fd.append('arg_keyid',sessionStorage.getItem('keyid'));
	    fd.append('arg_latitude',this.state.gpsn);
	    fd.append('arg_longitude',this.state.gpsw);
	    fd.append('arg_rotation','90.0');
	    fd.append('arg_orientation','6.0');
	    //fd.append('arg_photopath','');
	    //fd.append('arg_message','');
	    //fd.append('arg_author','');
	    fd.append('identifier',this.state.photofile.name);
	    fd.append('arg_image',btoa(this.state.imagePreviewBin));
	    //deal with metata data
	    var md  = sessionStorage.getItem("metadata");
            var jmd = JSON.parse(md);
	    var param = '{';
            for(var i in jmd){
		var f = jmd[i];
		var metanode =  document.getElementById(f);
		var val = metanode.value;
		param = param + '"'+f+'":"'+val+'",';
            }
	    param = param + '"origine":"webapps"}';
	    fd.append('arg_comment', unescape(encodeURIComponent(param)));
	    xhr.send(fd);
	}
	    
    },
    
    handleConnect: function(event) {
	var url = 'http://prototypel1.irisa.fr/API/userConnect.php';
        var xhr = new XMLHttpRequest();
        var fd = new FormData();
        xhr.open("POST", url, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var servsession = xhr.responseText;
                var jt = JSON.parse(servsession);
                var keyid  = jt['keyid'];
                var status  = jt['flag'];
                sessionStorage.setItem("keyid",keyid);
                sessionStorage.setItem("connected",status);
                sessionStorage.setItem("token",'notatoken');
                var node0 = document.getElementById('connected');
                node0.innerHTML = '<b>' + status + '</b>';
		/*** now we need to get the meta data ***/
		if (jt['metadata']){
     		    var md  = decodeURIComponent(escape(window.atob(jt['metadata'])));
		    sessionStorage.setItem("metadata",md);
		    var mdn = document.getElementById('metadata');
		    var jmd = JSON.parse(md);
		    var textMetada = '';
		    for(var i in jmd){
			var v = jmd[i];
			textMetada = textMetada + v+ ': <input type="text" id="'+v+'"/> <br />'
		    }
		    mdn.innerHTML = textMetada;
		}
		/*** now we need to get the actions ***/
		if (jt['action']) {
		    var act  = decodeURIComponent(escape(window.atob(jt['action'])));
		    sessionStorage.setItem("action",act);
		    var actn = document.getElementById('action');
		    var jact = JSON.parse(act);
		    var textAction = '';
		    for(var j in jact){
			var a = jact[j];
			textAction = textAction + "<button onclick='window.myFunction(\""+a+"\")' id='"+a+"'>"+a+"</button> <br />";
			//alert(textAction);
		    }
		    actn.innerHTML = textAction;
		}
            } else {
                //console.log(xhr.responseText);                                                                                            
            }
        };
        sessionStorage.setItem("email",this.state.email);
        sessionStorage.setItem("uid",this.state.uid);
        fd.append('usermail',this.state.email);
        fd.append('mdp',this.state.uid);
        xhr.send(fd);
    },
    
    /** from http://stackoverflow.com/questions/14446447/javascript-read-local-text-file**/
    openFile: function(event) {
	var input = event.target;
	var reader = new FileReader();
	var partialState = {};
	partialState['filename1'] = input.files[0].name;
	this.setState(partialState);	
	
	reader.onload = function(){
	    var text = reader.result;
	    var node = document.getElementById('contenufichier');
	    //node.innerText = btoa(text);
	    node.innerText = text;
	    //console.log(reader.result.substring(0, 200));
	    console.log("openFile: " + input.files[0].name);
	};

	reader.readAsText(input.files[0]);
    },
    
    handleResponse: function(event) {
	var keyid  = sessionStorage.getItem('keyid');
	var node1 = document.getElementById('response');
	var location = 'http://prototypel1.irisa.fr/'+keyid+'/default.html';
	var response =  '<iframe id="idFrame" width="800" height="600" src="'+location+'"></iframe>';
	node1.innerHTML = response;
	//need to reload
	document.getElementById('idFrame').src = document.getElementById('idFrame').src
    },

    _handleImageChange(e) {
        e.preventDefault();
        let reader = new FileReader();
        let file = e.target.files[0];
	this.setState({photofile: file});
        reader.onloadend = ()=> {
            this.setState({
                imagePreviewUrl: reader.result
            });
        }
        reader.readAsDataURL(file);
	//need also to read it as binary to send it
	let binreader = new FileReader();
	binreader.onloadend = ()=> {
            this.setState({
                imagePreviewBin: binreader.result
            });
        }
	binreader.readAsBinaryString(file);
    },

    render: function() {
	var t = this.state.token;
	var e = this.state.email;
	var u = this.state.uid;
	var f = this.state.filename1;
	var w = this.state.gpsw;
	var n = this.state.gpsn;
	let {imagePreviewUrl}=this.state;
        let $imagePreview = null;
        
	if (imagePreviewUrl) {
            $imagePreview = (<img src={imagePreviewUrl} width={300}/>);
        } else {
            $imagePreview = (<div>Please select an Image for Preview </div>);
        }
	sessionStorage.setItem("gpsw",w);
	sessionStorage.setItem("gpsn",n);

	/*** functions for the action button */
	window.myFunction = function (a) { 
	  var url = 'http://prototypel1.irisa.fr/API/putTask.php';
  	  var xhr = new XMLHttpRequest();
  	  var fd = new FormData();
  	  xhr.open("POST", url, true);
	  xhr.onreadystatechange = function() {
	    if (xhr.readyState == 4 && xhr.status == 200) {
		alert('OK Server response: ' + xhr.responseText);
	    } 
	  };
	  var t = sessionStorage.getItem("token");
	  var e = sessionStorage.getItem("email");
	  fd.append('email',e);
	  fd.append('token',t);
	  fd.append('task', a);
	  xhr.send(fd);
	  //alert(a+ "sent to "+e+" with token "+t);
	  //envoi des coordonnées GPS
	  var url2 = 'http://prototypel1.irisa.fr/API/putPosition.php';
	  var xhr2 = new XMLHttpRequest();
  	  var fd2 = new FormData();
  	  xhr2.open("POST", url2, true);
	  xhr2.onreadystatechange = function() {
	    if (xhr2.readyState == 4 && xhr2.status == 200) {
		alert('OK Server response: ' + xhr2.responseText);
	    } 
	  };
	  fd2.append('email',e);
	  fd2.append('token',t);
	  fd2.append('GPSN', sessionStorage.getItem('gpsn'));
	  fd2.append('GPSW', sessionStorage.getItem('gpsw'));
	  xhr2.send(fd2);
	};

	return (
		<div>
		<label>
		email: <input type="text" value={e} onChange={this.handleInputChange.bind(null, 'email')} />
		</label>
		<br />
		<label>
		mot de passe: <input type="text" value={u} onChange={this.handleInputChange.bind(null, 'uid')} />
		</label>
		<br />
	        <button  onClick={this.handleConnect.bind(null)}>
		Se connecter
                </button>  <br />
         	Statut de la connexion : <div id='connected'></div>
		<br />
		<label>
		fichier image: <input id="uploadPhoto" type='file' accept="image/*" onChange={(e)=>this._handleImageChange(e)} />
		</label>
		<br />
		<label>
		coordonnées GPS W: <input type="text" value={w} onChange={this.handleInputChange.bind(null, 'gpsw')} />
		</label>
		<br />
		<label>
		coordonnées GPS N: <input type="text" value={n} onChange={this.handleInputChange.bind(null, 'gpsn')} />
		</label>
		<br />
		
		<div id='metadata'> </div> <br />

		<div id='action'> </div> <br />

		<button  onClick={() =>{this.handleSubmit(null)}}>Publier le fichier sur le serveur</button><br />

		<button  onClick={() =>{this.handleResponse(null)}}>Réponse du serveur</button> <br />

		<div id='response'> </div> <br />
		<div id='contenufichier'> </div> <br />
		<div id='listefichiers'> </div>
                <div className="imgPreview"> {$imagePreview}</div>
		</div>
	);
    }
});

ReactDOM.render(
	<MyAppsIstic />,
    document.getElementById('container')
);
