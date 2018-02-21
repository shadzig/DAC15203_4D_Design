
$(document).ready(function () {
  var ctx = document.getElementById("chart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: 'bar',
data: {
labels: ["7 days", "6 days", "5 days", "4 days", "3 days", "2 days","1 days"],
datasets: [{
    label: '7 days of past sleep',
    data: [100, 80, 74, 61, 20, 60, 92],
    backgroundColor: ['rgba(75, 192, 192, 0.2)','rgba(75, 192, 192, 0.2)','rgba(75, 192, 192, 0.2)','rgba(75, 192, 192, 0.2)','rgba(75, 192, 192, 0.2)','rgba(75, 192, 192, 0.2)','rgba(75, 192, 192, 0.2)'],
    borderColor: ['rgba(75, 192, 0, 1)','rgba(75, 192, 0, 1)','rgba(75, 192, 0, 1)','rgba(75, 192, 0, 1)','rgba(75, 192, 0, 1)','rgba(75, 192, 0, 1)','rgba(75, 192, 0, 1)', ],
            borderWidth: 4
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });

        console.log(myChart);
});
