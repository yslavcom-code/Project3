// Fetch data from Flask backend
fetch('/data')
    .then(response => response.json())
    .then(data => {
        const quarters = data.map(item => item['Unnamed: 0']); // Extract quarters
        const countries = Object.keys(data[0]).filter(key => key !== 'Unnamed: 0');

        // Example: Select one country
        const country = "United States";
        const values = data.map(item => item[country]);

        // Setup chart
        const ctx = document.getElementById('gdpChart').getContext('2d');
        new Chart(ctx, {
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
    })
    .catch(err => console.error("Error fetching data:", err));
