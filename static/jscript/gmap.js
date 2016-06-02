var map, latLng, marker, infoWindow;
var geocoder = new google.maps.Geocoder();

function showAddress(val) {
infoWindow.close();
geocoder.geocode( { 'address': val }, function(results, status) {
  if (status == google.maps.GeocoderStatus.OK) {
	 marker.setPosition(results[0].geometry.location);
	 geocode(results[0].geometry.location);
  } else {
	 alert("Sorry but Google Maps could not find this location.");
  }
});
}

function geocode(position) {
geocoder.geocode({
   latLng: position
}, function(responses) {
	 var html = '';
	 if (responses && responses.length > 0) {
		html += '<strong>Postal Address:</strong><hr/>' + responses[0].formatted_address;
	 } else {
		html += 'Sorry but Google Maps could not determine the approximate postal address of this location.';
	 }

	 html += '<br /><br /><strong>Geo Co-ordinates</strong><hr />' + 'Latitude : ' + marker.getPosition().lat() + '<br/>Longitude: ' + marker.getPosition().lng();
	 map.panTo(marker.getPosition());
	 infoWindow.setContent("<div id='iw'>" + html + "</div>");
	 infoWindow.open(map, marker);
 });
}

	function initialize() {
	  var mapOptions = {
		zoom: 5,
		center: new google.maps.LatLng(42.000325,-75.926513),
		mapTypeControl: true,
		mapTypeControlOptions: {
		  style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
		},
		zoomControl: true,
		zoomControlOptions: {
		  style: google.maps.ZoomControlStyle.SMALL
		},
		mapTypeId: google.maps.MapTypeId.ROADMAP
	  }
	  map = new google.maps.Map(document.getElementById("map"), mapOptions);
	  
		if (!latLng) latLng = new google.maps.LatLng(38.8977, -77.0366);																
		map.setCenter(latLng);
		
		marker = new google.maps.Marker({ 
			position: latLng, map: map, draggable: true, animation: google.maps.Animation.DROP
		});								
		infoWindow = new google.maps.InfoWindow({
			content: '<div id="iw"><strong>Instructions:</strong><br />Click and drag this red marker <br />anywhere to know the approximate <br />postal address of that location.</div>'		});
		infoWindow.open(map, marker);								
		google.maps.event.addListener(marker, 'dragstart', function (e) { infoWindow.close();	});								
		google.maps.event.addListener(marker, 'dragend', function (e) {
			var point = marker.getPosition();
			map.panTo(point);
			geocode(point);
		});							
	}							
	google.maps.event.addDomListener(window, 'load', initialize);
					 