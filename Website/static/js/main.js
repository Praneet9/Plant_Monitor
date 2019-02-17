jQuery.get('/data').done(function(results) {
        plot(results);
});

function plot(data) {
    var plant1 = document.getElementById("plant1").getContext('2d');
    // var plant2 = document.getElementById("plant2").getContext('2d');
    // var plant3 = document.getElementById("plant3").getContext('2d');
    // var plant4 = document.getElementById("plant4").getContext('2d');
    // var plant5 = document.getElementById("plant5").getContext('2d');
    // var plant6 = document.getElementById("plant6").getContext('2d');

    var temp1 = document.getElementById("temp1").getContext('2d');
    // var temp2 = document.getElementById("temp2").getContext('2d');

    var humidity1 = document.getElementById("humidity1").getContext('2d');
    // var humidity2 = document.getElementById("humidity2").getContext('2d');

    myChart(plant1, data.moisture_1, data.plot_labels, 'Plant 1');
    // myChart(plant2, data.results, data.plot_labels, 'Plant 2');
    // myChart(plant3, data.results, data.plot_labels, 'Plant 3');
    // myChart(plant4, data.results, data.plot_labels, 'Plant 4');
    // myChart(plant5, data.results, data.plot_labels, 'Plant 5');
    // myChart(plant6, data.results, data.plot_labels, 'Plant 6');

    myChart(temp1, data.temperature_1, data.plot_labels, 'Temperature 1');
    // myChart(temp2, data.results, data.plot_labels, 'Temperature 2');

    myChart(humidity1, data.humidity_1, data.plot_labels, 'Humidity 1');
    // myChart(humidity2, data.results, data.plot_labels, 'Humidity 2');

}

function myChart(context, plot_data, plot_labels, label) {
    new Chart(context, {
        type: 'bar',
        data: {
            labels: plot_labels,
            datasets: [{
                label: label,
                data: plot_data,
                backgroundColor: [
                    '#26A69A'
                ],
                borderColor: [
                   'green'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:false
                    }
                }]
            }
        }
    });
}