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

        // Function to update chart with selected country
        function updateChart(country) {
            const values = data.map(item => item[country]);

            // Setup chart
            const ctx = document.getElementById('gdpChart').getContext('2d');
            const chart = new Chart(ctx, {
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

        // Update the chart with the default country (United States)
        updateChart(defaultCountry);

        // Listen for changes in the dropdown
        countrySelect.addEventListener('change', function() {
            const selectedCountry = countrySelect.value;
            updateChart(selectedCountry);
        });
    })
    .catch(err => console.error("Error fetching data:", err));
