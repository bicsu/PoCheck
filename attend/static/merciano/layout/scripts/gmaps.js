/*
Template Name: Merciano
Author: <a href="https://www.os-templates.com/">OS Templates</a>
Author URI: https://www.os-templates.com/
Licence: Free to use under our free template licence terms
Licence URI: https://www.os-templates.com/template-terms
File: Google Maps Setup js
*/

google.maps.visualRefresh = true; // Enable the visual refresh
function initialize() {
    // Set up your geolocation latitude and longtitude
    var latlang = new google.maps.LatLng(51.51121, -0.11982);
    var mapOptions = {
        // This will always position your loction in the middle of the displayed map, using your "latlang" settings
        center: latlang,
        // Initial display resolution, zoom 0 corresponds to a map of the Earth fully zoomed out, and higher zoom levels zoom in at a higher resolution.
        zoom: 12,
        // true or false => enables or disables the Zoom control. By default, this control is visible and appears in the top left corner of the map
        zoomControl: true,
        zoomControlOptions: {
            style: google.maps.ZoomControlStyle.SMALL
        },
        // true or false => enables or disables the Scale control that provides a simple map scale
        scaleControl: true,
        // true or false => enables or disables the Pan control. By default, this control is visible and appears in the top left corner of the map
        panControl: true,
        // true or false => If false, prevents the map from being dragged. Dragging is enabled by default
        draggable: true,
        // true or false => If false, scrollwheel zooming is disabled on the map. The scrollwheel is enabled by default.
        scrollwheel: false,
        // Set the basic map type here, choice of: ROADMAP, SATELLITE, HYBRID or TERRAIN
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        // Set up the colour coding for the map and its elements
        styles: [{
            stylers: [{
                saturation: -100
            }, {
                gamma: 1
            }]
        }, {
            featureType: "road",
            elementType: "geometry",
            stylers: [{
                visibility: "simplified"
            }]
        }, {
            featureType: "water",
            elementType: "geometry.fill",
            stylers: [{
                saturation: 50
            }, {
                gamma: 0
            }, {
                hue: "#56AED4"
            }]
        }, {
            featureType: "road.local",
            elementType: "labels.text",
            stylers: [{
                weight: 0.5
            }, {
                color: "#666666"
            }]
        }, {
            featureType: "transit.station",
            elementType: "labels.icon",
            stylers: [{
                saturation: 50
            }, {
                gamma: 0
            }, {
                hue: "#FF0000"
            }]
        }]
    };
    var map = new google.maps.Map(document.getElementById('gmapcanvas'), mapOptions);
    var marker = new google.maps.Marker({
        position: latlang,
        map: map,
        // This is the title text that is shown when you hover over the marker on the map - change it to your text
        title: 'We Are Here'
    });
    var infowindow = new google.maps.InfoWindow();
    // Write the content that you wish to be displayed here e.g. Your Companies Address
    infowindow.setContent('<address>Name<br>Address<br>Post Code / Zip<br>Tel: xxxx xxxxxx</address>');
    google.maps.event.addListener(marker, 'click', function() {
        infowindow.open(map, marker);
    });
}
google.maps.event.addDomListener(window, 'load', initialize);