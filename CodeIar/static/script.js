// Fetch data from Flask backend
fetch('/data')
    .then(response => response.json())
    .then(data => {
        const quarters = data.map(item => item['Unnamed: 0']); // Extract quarters
        const countries = Object.keys(data[0]).filter(key => key !== 'Unnamed: 0');

        // Populate the dropdown with countries
        const countrySelect = document.getElementById('countrySelect');
        countries.forEach(country => {
            const option = document.createElement('option');
            option.value = country;
            option.textContent = country;
            countrySelect.appendChild(option);
        });

        // Set the default selected country 
        const defaultCountry = "Australia";
        countrySelect.value = defaultCountry;

        // Store the chart instance globally
        let chart;

        // Function to update the chart with the selected country
        function updateChart(country) {

            const values = data.map(item => {
                const value = item[country];
                return (typeof value === 'number' && !isNaN(value)) ? value : null; // Replace NaN or invalid values with null
            }).filter(value => value !== null); // Filter out nulls

            if (values.length === 0) {
                console.warn(`No valid data available for ${country}`);
                return; // Do not render the chart if no valid data exists
            }


            // If chart exists, destroy it before creating a new one
            if (chart) {
                chart.destroy(); // Destroy the previous chart instance
            }

            // Create the new chart
            const ctx = document.getElementById('gdpChart').getContext('2d');
            chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: quarters,
                    datasets: [{
                        label: `${country} GDP Deflator`,
                        data: values,
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderWidth: 2,
                        fill: true,
                    }]
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

        // Update the chart with the default country (Australia)
        updateChart(defaultCountry);

        // Listen for changes in the dropdown
        countrySelect.addEventListener('change', function() {
            const selectedCountry = countrySelect.value;
            updateChart(selectedCountry);
        });
    })
    .catch(err => console.error("Error fetching data:", err));
