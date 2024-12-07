// Fetch country list from the server
fetch('/data')
    .then(response => response.json())
    .then(async data => {
        // Extract the list of countries (excluding 'Unnamed: 0')
        const countries = Object.keys(data[0]).filter(key => key !== 'Unnamed: 0');
        console.log("Countries fetched:", countries);

        const countryCoordinates = {
            "Albania": { lat: 41.1533, lon: 20.1683 },
            "Argentina": { lat: -38.4161, lon: -63.6167 },
            "Australia": { lat: -25.2744, lon: 133.7751 },
            "Austria": { lat: 47.5162, lon: 14.5501 },
            "Bahrain": { lat: 26.0667, lon: 50.5577 },
            "Belarus": { lat: 53.9006, lon: 27.5590 },
            "Belgium": { lat: 50.8503, lon: 4.3517 },
            "Bolivia": { lat: -16.2902, lon: -63.5887 },
            "Bosnia and Herzegovina": { lat: 43.9159, lon: 17.6791 },
            "Botswana": { lat: -22.3285, lon: 24.6849 },
            "Brazil": { lat: -14.2350, lon: -51.9253 },
            "Bulgaria": { lat: 42.7339, lon: 25.4858 },
            "Cameroon": { lat: 7.3697, lon: 12.3547 },
            "Canada": { lat: 56.1304, lon: -106.3468 },
            "Chile": { lat: -35.6751, lon: -71.5430 },
            "China": { lat: 35.8617, lon: 104.1954 },
            "Colombia": { lat: 4.5709, lon: -74.2973 },
            "Costa Rica": { lat: 9.7489, lon: -83.7534 },
            "Croatia": { lat: 45.1000, lon: 15.2000 },
            "Cyprus": { lat: 35.1264, lon: 33.4299 },
            "Czech Republic": { lat: 49.8175, lon: 15.4730 },
            "Denmark": { lat: 56.2639, lon: 9.5018 },
            "Ecuador": { lat: -1.8312, lon: -78.1834 },
            "Egypt, Arab Rep.": { lat: 26.8206, lon: 30.8025 },
            "Estonia": { lat: 58.5953, lon: 25.0136 },
            "Finland": { lat: 61.9241, lon: 25.7482 },
            "France": { lat: 46.6034, lon: 1.8883 },
            "Germany": { lat: 51.1657, lon: 10.4515 },
            "Ghana": { lat: 7.9465, lon: -1.0232 },
            "Greece": { lat: 39.0742, lon: 21.8243 },
            "Guatemala": { lat: 15.7835, lon: -90.2308 },
            "Honduras": { lat: 15.1999, lon: -86.2419 },
            "Hong Kong SAR, China": { lat: 22.3193, lon: 114.1694 },
            "Hungary": { lat: 47.1625, lon: 19.5033 },
            "Iceland": { lat: 64.9631, lon: -19.0208 },
            "India": { lat: 20.5937, lon: 78.9629 },
            "Indonesia": { lat: -0.7893, lon: 113.9213 },
            "Ireland": { lat: 53.4129, lon: -8.2439 },
            "Israel": { lat: 31.0461, lon: 34.8516 },
            "Italy": { lat: 41.8719, lon: 12.5674 },
            "Japan": { lat: 36.2048, lon: 138.2529 },
            "Jordan": { lat: 30.5852, lon: 36.2384 },
            "Kazakhstan": { lat: 48.0196, lon: 66.9237 },
            "Kenya": { lat: -1.2864, lon: 36.8172 },
            "Korea, Rep.": { lat: 35.9078, lon: 127.7669 },
            "Kuwait": { lat: 29.3759, lon: 47.9774 },
            "Latvia": { lat: 56.8796, lon: 24.6032 },
            "Lithuania": { lat: 55.1694, lon: 23.8813 },
            "Luxembourg": { lat: 49.8153, lon: 6.1296 },
            "Malaysia": { lat: 4.2105, lon: 101.9758 },
            "Malta": { lat: 35.9375, lon: 14.3754 },
            "Mexico": { lat: 23.6345, lon: -102.5528 },
            "Mongolia": { lat: 46.8625, lon: 103.8467 },
            "Morocco": { lat: 31.7917, lon: -7.0926 },
            "Netherlands": { lat: 52.1326, lon: 5.2913 },
            "New Zealand": { lat: -40.9006, lon: 174.8860 },
            "Nicaragua": { lat: 12.8654, lon: -85.2072 },
            "Nigeria": { lat: 9.0820, lon: 8.6753 },
            "North Macedonia": { lat: 41.6086, lon: 21.7453 },
            "Norway": { lat: 60.4720, lon: 8.4689 },
            "Paraguay": { lat: -23.4425, lon: -58.4438 },
            "Peru": { lat: -9.1900, lon: -75.0152 },
            "Philippines": { lat: 12.8797, lon: 121.7740 },
            "Poland": { lat: 51.9194, lon: 19.1451 },
            "Portugal": { lat: 39.3999, lon: -8.2245 },
            "Romania": { lat: 45.9432, lon: 24.9668 },
            "Russian Federation": { lat: 61.5240, lon: 105.3188 },
            "Saudi Arabia": { lat: 23.8859, lon: 45.0792 },
            "Serbia": { lat: 44.0165, lon: 21.0059 },
            "Singapore": { lat: 1.3521, lon: 103.8198 },
            "Slovakia": { lat: 48.6690, lon: 19.6990 },
            "Slovenia": { lat: 46.1512, lon: 14.9955 },
            "South Africa": { lat: -30.5595, lon: 22.9375 },
            "Spain": { lat: 40.4637, lon: -3.7492 },
            "Sri Lanka": { lat: 7.8731, lon: 80.7718 },
            "Sweden": { lat: 60.1282, lon: 18.6435 },
            "Switzerland": { lat: 46.8182, lon: 8.2275 },
            "Taiwan, China": { lat: 23.6978, lon: 120.9605 },
            "Thailand": { lat: 15.8700, lon: 100.9925 },
            "Tunisia": { lat: 33.8869, lon: 9.5375 },
            "Turkey": { lat: 38.9637, lon: 35.2433 },
            "Ukraine": { lat: 48.3794, lon: 31.1656 },
            "United Kingdom": { lat: 55.3781, lon: -3.4360 },
            "United States": { lat: 37.0902, lon: -95.7129 },
            "Uruguay": { lat: -32.5228, lon: -55.7658 },
        };


        const map = L.map('map',{
            attributionControl: false
        }).setView([20, 0], 2);

        // Add OpenStreetMap tiles
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 18,
            attribution: '© OpenStreetMap contributors'
        }).addTo(map);

        countries.forEach(country => {
            if (countryCoordinates[country]) {
                const { lat, lon } = countryCoordinates[country];
                L.marker([lat, lon])
                    .addTo(map)
                    .bindPopup(`<strong>${country}</strong>`)
                    .openPopup();
            }
        });
    })
    .catch(err => console.error("Error fetching data:", err));
