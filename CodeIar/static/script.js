// Fetch data from Flask backend
fetch('/data')
    .then(response => response.json())
    .then(data => {
        const quarters = data.map(item => item['Unnamed: 0']); // Extract quarters
        const countries = Object.keys(data[0]).filter(key => key !== 'Unnamed: 0');

        // Populate the dropdown with countries
        const countrySelect = document.getElementById('countrySelect');
        countrySelect.setAttribute('multiple', true); // Allow multiple selections
        countrySelect.setAttribute('size', 10); // Display 10 options at once in the dropdown

        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.textContent = country;
            countrySelect.appendChild(option);
        });

        // Set the default selected countries (up to 5)
        const defaultCountries = ["Australia"];
        defaultCountries.forEach(country => {
            const option = countrySelect.querySelector(`option[value="${country}"]`);
            if (option) option.selected = true;
        });

        // Store the chart instance globally
        let chart;

        // Map to store country-color assignments
        const countryColorMap = {};

        // Function to generate or reuse a color for a country
        function getCountryColor(country) {
            // If a color is already assigned to this country, return it
            if (countryColorMap[country]) {
                return countryColorMap[country];
            }
            
            // Otherwise, generate a new color and store it
            const color = randomColor();
            countryColorMap[country] = color;
            return color;
        }

        // Function to generate random color (for variety)
        function randomColor() {
            const letters = '0123456789ABCDEF';
            let color = '#';
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }

        // Function to generate a semi-transparent color
        function semiTransparentColor(color) {
            return color.replace('rgb', 'rgba').replace(')', ', 0.3)'); // Convert to RGBA and set opacity to 0.3
        }

        // Function to update the chart with the selected countries
        function updateChart(selectedCountries) {
            // Generate datasets for the selected countries
            const datasets = selectedCountries.map(country => {
                const values = data.map(item => {
                    const value = item[country];
                    return (typeof value === 'number' && !isNaN(value)) ? value : null; // Replace NaN or invalid values with null
                }).filter(value => value !== null); // Filter out nulls

                const color = getCountryColor(country); // Get or generate the color for this country
                const borderColor = color;
                const backgroundColor = semiTransparentColor(color); // Make background semi-transparent

                return {
                    label: `${country} GDP Deflator`,
                    data: values,
                    borderColor: borderColor, // Assign the color for the border
                    backgroundColor: backgroundColor, // Semi-transparent color for the background
                    borderWidth: 2,
                    fill: true,
                };
            });

            // If chart exists, destroy it before creating a new one
            if (chart) {
                chart.destroy();
            }

            // Create the new chart
            const ctx = document.getElementById('gdpChart').getContext('2d');
            chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: quarters.slice(0, datasets[0].data.length), // Ensure labels match the number of values
                    datasets: datasets, // Add all datasets for the selected countries
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top',
                        }
                    },
                    scales: {
                        x: {
                            title: {
                                display: true,
                                text: 'Quarter'
                            }
                        },
                        y: {
                            title: {
                                display: true,
                                text: 'GDP Deflator'
                            },
                            beginAtZero: false
                        }
                    }
                }
            });
        }

        // Update the chart with the default selected countries
        updateChart(defaultCountries);

        // Listen for changes in the dropdown
        countrySelect.addEventListener('change', function() {
            const selectedCountries = Array.from(countrySelect.selectedOptions).map(option => option.value);
            
            // Ensure the number of selected countries doesn't exceed 5
            if (selectedCountries.length > 5) {
                alert('You can only select up to 5 countries.');
                return; 
            }

            updateChart(selectedCountries);
        });
    })
    .catch(err => console.error("Error fetching data:", err));
