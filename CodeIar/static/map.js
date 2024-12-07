const map = L.map('map').setView([20, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

const countryCoordinates = {
    "Australia": [-25.2744, 133.7751],
    "United States": [37.0902, -95.7129],
    "Canada": [56.1304, -106.3468],
    "Germany": [51.1657, 10.4515],
    "China": [35.8617, 104.1954],
    "India": [20.5937, 78.9629]
};

const selectedCountries = ["Australia", "United States", "China"]; // Replace with dynamic data if available

selectedCountries.forEach(country => {
    if (countryCoordinates[country]) {
        const [lat, lon] = countryCoordinates[country];
        L.marker([lat, lon])
            .addTo(map)
            .bindPopup(`<b>${country}</b><br>GDP Deflator Data`)
            .openPopup();
    }
});