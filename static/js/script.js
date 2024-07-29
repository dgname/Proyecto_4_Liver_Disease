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
            age: $('#age').val(), // Get the value from the age input field
            gender: $('input[name="gender"]:checked').val(), // Get the selected value of the gender radio buttons
            bmi: $('#bmi').val(), // Get the value from the BMI slider
            alcoholconsumption: $('#alcoholconsumption').val(), // Get the value from the alcohol consumption input field
            smoking: $('input[name="smoking"]:checked').val(), // Get the selected value of the smoking radio buttons
            geneticrisk: $('input[name="geneticrisk"]:checked').val(), // Get the selected value of the genetic risk radio buttons
            physicalactivity: $('#physicalactivity').val(), // Get the value from the physical activity slider
            diabetes: $('input[name="diabetes"]:checked').val(), // Get the selected value of the diabetes radio buttons
            hypertension: $('input[name="hypertension"]:checked').val(), // Get the selected value of the hypertension radio buttons
            liverfunctiontest: $('#liverfunctiontest').val() // Get the value from the liver function test slider
        };

