// static/js/map.js

// Define coordinates for all countries in our dataset
const countryCoordinates = {
    "Albania": { lat: 41.1533, lon: 20.1683 },
    "Argentina": { lat: -38.4161, lon: -63.6167 },
    "Australia": { lat: -25.2744, lon: 133.7751 },
    // ... add more countries as needed
};

// Function to initialize the map
function initializeMap() {
    // Create map centered on a middle point
    const map = L.map('mapContainer').setView([20, 0], 2);
    
    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    return map;
}

// Function to update map with economic data
function updateMap(map, data, indicator) {
    // Clear existing markers
    map.eachLayer((layer) => {
        if (layer instanceof L.CircleMarker) {
            map.removeLayer(layer);
        }
    });

    // Add markers for each country
    Object.keys(data).forEach(country => {
        if (countryCoordinates[country] && data[country]) {
            const coordinates = countryCoordinates[country];
            const value = data[country];
            
            // Create circle marker with size based on value
            const marker = L.circleMarker(
                [coordinates.lat, coordinates.lon],
                {
                    radius: Math.min(20, Math.max(5, value/10)),
                    fillColor: getColorForValue(value),
                    color: '#000',
                    weight: 1,
                    opacity: 1,
                    fillOpacity: 0.8
                }
            );

            // Add popup with country info
            marker.bindPopup(`
                <b>${country}</b><br>
                ${indicator}: ${value.toFixed(2)}
            `);

            marker.addTo(map);
        }
    });
}

// Helper function to get color based on value
function getColorForValue(value) {
    // Color scale from low (red) to high (green)
    return value > 100 ? '#1a9850' :
           value > 75  ? '#66bd63' :
           value > 50  ? '#a6d96a' :
           value > 25  ? '#fdae61' :
                        '#d73027';
}