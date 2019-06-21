
/** check this at  https://facebook.github.io/react/docs/components-and-props.html**/

var DepotTP = React.createClass({
    getInitialState: function() {
	return {
	    email: 'email5',
	    uid: 'passwd5',
	    filename1: 'not a file name',
	    token: 'notatoken',
	};
    },
    
    handleInputChange: function(key, event) {
	var partialState = {};
	partialState[key] = event.target.value;
	this.setState(partialState);
	//console.log("input change: " + event.target.value);
    },

    handleSubmit: function(event) {
	var keyid  = localStorage.getItem("keyid");
	var status = localStorage.getItem("connected");
	if (status.localeCompare('Success') != 0){
	    alert("Vous devez vous connecter");
	    return;
	}
	if (this.state.filename1.localeCompare('not a file name') == 0){
	    alert("Vous devez selectionner un fichier");
	    return;
	}
	//To check the parameters  var url = 'http://prototypel1.irisa.fr/API/echo.php';
	var url = 'http://prototypel1.irisa.fr/API/putAFile.php';
	var xhr = new XMLHttpRequest();
	var fd = new FormData();
	xhr.open("POST", url, true);
	xhr.onreadystatechange = function() {
	    if (xhr.readyState == 4 && xhr.status == 200) {
		alert('Le fichier a été déposé');
		// maintenant, on charge la liste des fichiers
		var url1 = 'http://prototypel1.irisa.fr/API/listOfFiles.php';
		var xhr1 = new XMLHttpRequest();
		var fd1 = new FormData();
		xhr1.open("POST", url1, true);
		xhr1.onreadystatechange = function() {
		    if (xhr1.readyState == 4 && xhr1.status == 200) {
			//DISPLAY LIST OF FILE
			var node2 = document.getElementById('titreinfo');
			node2.innerHTML = '<h4> La liste de vos fichiers déposés</h4>';
			var node1 = document.getElementById('listefichiers');
			var jt1 = JSON.parse(xhr1.responseText);
                        var displayfileslist = '';
			var tab = jt1['list'];
			for(var i in tab){
                            var v = tab[i];
			    if (('.'.localeCompare(v) != 0) && ('..'.localeCompare(v) !=0)){
				displayfileslist = displayfileslist + '\n' + v;
			    }
			}
			node1.innerText = displayfileslist; 
		    }
		};
		var em = localStorage.getItem("email");
		var tok = localStorage.getItem("token");
		fd1.append('email',em+'@univ-rennes1.fr');
		fd1.append('token',tok);
		xhr1.send(fd1);
	    }
	};
	fd.append('email',this.state.email+'@univ-rennes1.fr');
	fd.append('token',this.state.token);
	fd.append('filename', this.state.filename1);
	var node = document.getElementById('contenufichier');
	fd.append('content', btoa(unescape(encodeURIComponent(node.innerText))));
	node.innerText = '';
	xhr.send(fd);    
    },
    
    //localStorage is used to store the 'email', the 'uid', the 'keyid', the 'connected' status 
    // and the 'token'
    handleConnect: function(filecontent,event) {
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
		localStorage.setItem("keyid",keyid);	
		localStorage.setItem("connected",status);	
		localStorage.setItem("token",'notatoken');	
		var node0 = document.getElementById('connected');
		node0.innerHTML = '<b>' + status + '</b>';
	    } else {
		//console.log(xhr.responseText); 
	    }
	};
	localStorage.setItem("email",this.state.email);
	localStorage.setItem("uid",this.state.uid);
	fd.append('usermail',this.state.email+'@univ-rennes1.fr');
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
	    console.log("openFile: " + input.files[0].name);
	    if (node && text){
		var node2 = document.getElementById('titreinfo');
		node2.innerHTML = '<h4>Le contenu du fichier qui sera déposé</h4>';
		node.innerText = text;
	    } else {
		alert('Le chargement du fichier a échoué');
	    }
	    //console.log(reader.result.substring(0, 200));
	};
	reader.readAsText(input.files[0]);
    },

    render: function() {
	var e = this.state.email;
	var u = this.state.uid;
	var f = this.state.filename1;
	return (
		<div>
		<p>
		<label>
		Email: <input type="text" value={e} onChange={this.handleInputChange.bind(null, 'email')} /> @univ-rennes1.fr
            </label>
		<br />
		<label>
		Numéro étudiant: <input type="text" value={u} onChange={this.handleInputChange.bind(null, 'uid')} />
		</label>
		<br />
		<button  onClick={this.handleConnect.bind(null)}>
		Se connecter
                </button>  <br />
		Statut de la connexion : <div id='connected'></div>
		<label>
		<input id="uploadfile" type='file' onChange={this.openFile.bind(null)} />
		</label>
		</p>
		<button  onClick={this.handleSubmit.bind(null)}>
		   Déposer
                </button>
		<h3>Information sur les fichiers</h3><br />
		<div id='titreinfo'> </div>
		<div id='contenufichier'> </div>
		<div id='listefichiers'> </div>
		</div>
	);
    }
});

ReactDOM.render(
	<DepotTP />,
    document.getElementById('container')
);
