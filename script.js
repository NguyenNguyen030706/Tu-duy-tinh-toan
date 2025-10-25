// script.js

let map, directionsService, directionsRenderer;

function initMap() {
  const hcm = { lat: 10.762622, lng: 106.660172 }; // Vị trí mặc định TP.HCM
  map = new google.maps.Map(document.getElementById("map"), {
    center: hcm,
    zoom: 13
  });

  directionsService = new google.maps.DirectionsService();
  directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);

  // Khi người dùng nhập địa chỉ xong
  document.getElementById("start").addEventListener("change", calcRoute);
  document.getElementById("end").addEventListener("change", calcRoute);
}

function calcRoute() {
  const start = document.getElementById("start").value;
  const end = document.getElementById("end").value;

  if (!start || !end) return;

  directionsService.route(
    {
      origin: start,
      destination: end,
      travelMode: google.maps.TravelMode.DRIVING,
    },
    (result, status) => {
      if (status === "OK") {
        directionsRenderer.setDirections(result);
      } else {
        alert("Không tìm thấy đường đi: " + status);
      }
    }
  );
}