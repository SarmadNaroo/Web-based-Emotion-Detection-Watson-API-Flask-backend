function RunSentimentAnalysis() {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            if (response.error) {
                document.getElementById("system_response").innerHTML = response.error;
            } else {
                // Extract emotion scores and dominant emotion from the response
                let emotionScores = {
                    anger: response.anger,
                    disgust: response.disgust,
                    fear: response.fear,
                    joy: response.joy,
                    sadness: response.sadness
                };

                let dominantEmotion = response.dominant_emotion;

                // Create a bar graph using Chart.js
                createBarGraph(emotionScores);

                // Display the dominant emotion
                document.getElementById("dominantEmotion").innerHTML = "Dominant Emotion: " + dominantEmotion;

                // Optionally, update the HTML to display the scores
                document.getElementById("system_response").innerHTML = "Emotion scores received and graph created.";
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + textToAnalyze, true);
    xhttp.send();
}

function createBarGraph(emotionScores) {
    // Use Chart.js or any other library to create a bar graph
    // Example code to create a simple bar graph using Chart.js:
    let ctx = document.getElementById("emotionChart").getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(emotionScores),
            datasets: [{
                label: 'Emotion Scores',
                data: Object.values(emotionScores),
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
