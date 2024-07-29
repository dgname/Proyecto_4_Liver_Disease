$(document).ready(function() {
    // When the document is fully loaded and ready, execute this function
    
    // Event listener for the BMI input range slider
    $('#bmi').on('input', function() {
        // When the user changes the value of the BMI slider
        // Update the text content of the span with id 'bmi-value' to show the current value of the slider
        $('#bmi-value').text($(this).val());
    });

    // Event listener for the Physical Activity input range slider
    $('#physicalactivity').on('input', function() {
        // When the user changes the value of the Physical Activity slider
        // Update the text content of the span with id 'activity-value' to show the current value of the slider
        $('#activity-value').text($(this).val());
    });

    // Event listener for the Liver Function Test input range slider
    $('#liverfunctiontest').on('input', function() {
        // When the user changes the value of the Liver Function Test slider
        // Update the text content of the span with id 'liverfunction-value' to show the current value of the slider
        $('#liverfunction-value').text($(this).val());
    });

    // Event listener for the form submission
    $('#prediction-form').on('submit', function(e) {
        // Prevent the default form submission behavior (which would reload the page)
        e.preventDefault(); 

        // Collect the form data into an object
        var formData = {
            age: parseInt($('#age').val(), 10), // Convert the value from the age input field to integer
            gender: parseInt($('input[name="gender"]:checked').val(), 10), // Convert the selected value of the gender radio buttons to integer
            bmi: parseFloat($('#bmi').val()), // Convert the value from the BMI slider to float
            alcoholconsumption: parseFloat($('#alcoholconsumption').val()), // Convert the value from the alcohol consumption input field to float
            smoking: parseInt($('input[name="smoking"]:checked').val(), 10), // Convert the selected value of the smoking radio buttons to integer
            geneticrisk: parseInt($('input[name="geneticrisk"]:checked').val(), 10), // Convert the selected value of the genetic risk radio buttons to integer
            physicalactivity: parseFloat($('#physicalactivity').val()), // Convert the value from the physical activity slider to float
            diabetes: parseInt($('input[name="diabetes"]:checked').val(), 10), // Convert the selected value of the diabetes radio buttons to integer
            hypertension: parseInt($('input[name="hypertension"]:checked').val(), 10), // Convert the selected value of the hypertension radio buttons to integer
            liverfunctiontest: parseFloat($('#liverfunctiontest').val()) // Convert the value from the liver function test slider to float
        };

        // For debugging, log the collected data to the console
        console.log(formData);
    });
});
