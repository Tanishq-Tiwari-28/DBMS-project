// var main_data = {
//         loc_name: "",
//         distance: 0
//     };  

//     mapboxgl.accessToken = 'pk.eyJ1IjoidGFuaXNocS0yOCIsImEiOiJjbGY2a245Z2Mxbm52NDBzOTAzd21lOXdoIn0.t54Xj-liRz-dB8fCEoPW5A';

//     navigator.geolocation.getCurrentPosition(function (position) {
//         var currentLocation = [position.coords.longitude, position.coords.latitude];
//         var map = new mapboxgl.Map({
//             container: 'map',
//             style: 'mapbox://styles/mapbox/streets-v11',
//             center: currentLocation,
//             zoom: 12
//         });

//         // Add current location marker
//         var marker = new mapboxgl.Marker()
//             .setLngLat(currentLocation)
//             .addTo(map);

//         // Add click event listener to map
//         map.on('click', function (event) {
//             var newLocation = [event.lngLat.lng, event.lngLat.lat];
//             console.log(newLocation)
//             var lngLat = event.lngLat;
//             var url1 = 'https://api.mapbox.com/geocoding/v5/mapbox.places/' + lngLat.lng + ',' + lngLat.lat + '.json?access_token=' + mapboxgl.accessToken;
//             // Remove previous marker

//             fetch(url1)
//                 .then(response => response.json())
//                 .then(data => {
//                     var locationName = data.features[0].place_name;
//                     console.log(locationName);
//                     const s = document.getElementById("location-input");
//                     s.value = locationName
//                     main_data.loc_name = locationName;
//                 });

//             if (marker) {
//                 marker.remove();
//             }

//             // Add new marker
//             marker = new mapboxgl.Marker()
//                 .setLngLat(newLocation)
//                 .addTo(map);

//             // Store location string in variable
//             var locationString = JSON.stringify(newLocation);
//             console.log(locationString)
//             // Draw driving path from current location to new location
//             var url = 'https://api.mapbox.com/directions/v5/mapbox/driving/' + currentLocation[0] + ',' + currentLocation[1] + ';' + newLocation[0] + ',' + newLocation[1] + '?steps=true&geometries=geojson&access_token=' + mapboxgl.accessToken;
//             console.log(currentLocation[0], currentLocation[1]);
//             console.log(newLocation[0], newLocation[1]);
//             var url1 = 'https://api.mapbox.com/directions/v5/mapbox/driving/' + currentLocation[0] + ',' + currentLocation[1] + ';' + newLocation[0] + ',' + newLocation[1] + '?geometries=geojson&access_token=pk.eyJ1Ijoib20yMTQ4MSIsImEiOiJjbGRobTBreDUxM2w1M3F0NTd4ZG01ZXEzIn0.l7-GFstLQOdYhnkUMbHukQ';
//             console.log(url1);
//             var req = new XMLHttpRequest();
//             req.open('GET', url, true);
//             req.onload = function () {
//                 var json = JSON.parse(req.response);
//                 var data = json.routes[0];
//                 var route = data.geometry.coordinates;
//                 var geojson = {
//                     type: 'Feature',
//                     properties: {},
//                     geometry: {
//                         type: 'LineString',
//                         coordinates: route
//                     }
//                 };
//                 req.open('GET', url1, true);
//                 req.onload = function () {
//                     if (req.status == 200) {
//                         var response = JSON.parse(req.response);
//                         var distance = response.routes[0].distance;

//                         // distance stored here
//                         console.log(distance);

//                         const s1 = document.getElementById("dist");
//                         s1.value = distance
//                         main_data.distance = distance;

//                         const s2 = document.getElementById("final_d");
//                         s2.value = JSON.stringify(main_data)

//                     }
//                 };

//                 req.send();
//                 // If the route already exists on the map, reset it using setData
//                 if (map.getSource('route')) {
//                     map.getSource('route').setData(geojson);
//                 } else { // Otherwise, create a new source and add it to the map
//                     map.addSource('route', {
//                         type: 'geojson',
//                         data: geojson
//                     });

//                     // Add layer for route
//                     map.addLayer({
//                         id: 'route',
//                         type: 'line',
//                         source: 'route',
//                         layout: {
//                             'line-join': 'round',
//                             'line-cap': 'round'
//                         },
//                         paint: {
//                             'line-color': '#3887be',
//                             'line-width': 5,
//                             'line-opacity': 0.75
//                         }
//                     });
//                 }
//             };
//             req.send();

//             // Center map on new location
//             map.flyTo({
//                 center: newLocation,
//                 zoom: 12
//             });

//         });
//     });
