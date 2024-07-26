$(document).ready(function() {
    // Update the BMI and Physical Activity value displays
    $('#bmi').on('input', function() {
        $('#bmi-value').text($(this).val());
    });

    $('#activity').on('input', function() {
        $('#activity-value').text($(this).val());
    });

    // Handle form submission
    $('#prediction-form').on('submit', function(e) {
        e.preventDefault();

        var formData = {
            age: $('#age').val(),
            gender: $('input[name="gender"]:checked').val(),
            bmi: $('#bmi').val(),
            alcohol: $('#alcohol').val(),
            smoking: $('input[name="smoking"]:checked').val(),
            genetic: $('input[name="genetic"]:checked').val(),
            activity: $('#activity').val(),
            diabetes: $('input[name="diabetes"]:checked').val(),
            hypertension: $('input[name="hypertension"]:checked').val()
        };

        $.ajax({
            url: '/predict',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                $('#prediction-result').text(`The prediction result is: ${response.prediction}`);
            },
            error: function(response) {
                $('#prediction-result').text('An error occurred while making the prediction.');
            }
        });
    });
});