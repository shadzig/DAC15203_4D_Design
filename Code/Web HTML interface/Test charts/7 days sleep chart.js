
$(document).ready(function () {
    var ctx = document.getElementById("chart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: 'bar',
data: {
  labels: ["7 days", "6 days", "5 days", "4 days", "3 days", "2 days","1 days"],
  datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: [
        if data
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
      ],
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
