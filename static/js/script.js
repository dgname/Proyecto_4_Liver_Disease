document.addEventListener('DOMContentLoaded', function() {
    // Function to update the display of form values
    function updateDisplay() {
        d3.select('#bmi-value').text(d3.select('#bmi').property('value'));
        d3.select('#activity-value').text(d3.select('#physicalactivity').property('value'));
        d3.select('#liverfunction-value').text(d3.select('#liverfunctiontest').property('value'));
    }

    // Event listeners for form inputs
    d3.select('#bmi').on('input', updateDisplay);
    d3.select('#physicalactivity').on('input', updateDisplay);
    d3.select('#liverfunctiontest').on('input', updateDisplay);

    // Sets the initial display values when the page first loads
    updateDisplay();

    // Handle form submission with D3
    d3.select("#prediction-form").on("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = new FormData(this);
        const data = {};
        formData.forEach((value, key) => data[key] = value);

        // Send data to Flask using Fetch API
        fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams(data).toString() // Convert the data object to URL-encoded string
        })
        .then(response => response.json())
        .then(result => {
            // Display the prediction result
            const message = result.prediction === 1 ? 'You are at risk of liver disease.' : 'You are not at risk of liver disease.';
            d3.select("#modalBody").text(message);
            // Trigger the modal to show
            $('#resultModal').modal('show');
        })
        .catch(error => {
            console.error('Error:', error);
            d3.select("#modalBody").text('An error occurred. Please try again.');
            $('#resultModal').modal('show');
        });
    });

    // Ensure the modal can be closed with the close button
    $('#resultModal').on('hidden.bs.modal', function (e) {
        // Code to execute after the modal is closed, if needed
    });
});