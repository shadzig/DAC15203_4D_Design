var width = 500;
var height = 500;

var Gauge_percentage = 50;

var margin = {
  top: 42,
  right: 1,
  bottom: 0,
  left: -250
};

var config = {
  minAngle: -90,
  maxAngle: 90,
  innerTickRingOffset: -30,
  innerTickCounterclockSpin: 0,
  innerTickNumber: 10,
  outerTickRingOffset: 30,
  outerTickCounterclockSpin: 5,
  outerTickBorderLength: 20
};

var radius = Math.min(width, height) / 2;

var percentToDeg = function percentToDeg(percent) {
  return percent * 180 / 100;
};

var element = d3.select('.gauge');

var arc = d3.svg.arc().innerRadius(radius).outerRadius(radius - 10).startAngle(-90 * (Math.PI / 180)).endAngle(90 * (Math.PI / 180));

var scale = d3.scale.linear().domain([0, 10]).range([0, 1]);

var innerTicks = scale.ticks(config.innerTickNumber).map(function (tick) {
  return {
    value: tick,
    label: tick
  };
});

var outerTicks = [{
  value: 4,
  label: 'Angry'
}, {
  value: 6.85,
  borderAt: 6,
  label: 'Sad'
}, {
  value: 8.3,
  borderAt: 7.5,
  label: 'Neutral'
}, {
  value: 9.85,
  borderAt: 9,
  label: 'Happy'
}];

console.log('outerTicks', outerTicks);

var svg = element.append('svg').attr('width', "100%").attr('height', height + margin.top + margin.bottom);

var gradient = svg.append("defs").append("linearGradient").attr("id", "gradient").attr("x1", "0%").attr("y1", "20%").attr("x2", "100%").attr("y2", "100%").attr("spreadMethod", "pad");

gradient.append("stop").attr("offset", "20%").attr("stop-color", "#c00").attr("stop-opacity", 0.7);

gradient.append("stop").attr("offset", "95%").attr("stop-color", "#0c0").attr("stop-opacity", 1);

// Add layer for the panel
var chart = svg.append('g').attr('transform', 'translate(' + (width / 1 + margin.left) + ',' + (height / 2 + margin.top) + ')');

chart.append('path').attr('class', "arc").style("fill", "url(#gradient)").attr("d", arc);

chart.append('circle').attr('class', 'needle-center').attr('cx', 0).attr('cy', 0).attr('r', 30);

chart.append('line').attr('class', 'needle').style("stroke", "black").style("stroke-width", "7").attr("x1", 0).attr("y1", 0).attr("x2", -170).attr("y2", 0).transition().delay(500).ease('bounce').duration(1000).attr("transform", function () {
  return "rotate(" + percentToDeg(Gauge_percentage) + ")";
});

var innerTicksGroup = chart.append('g').attr('class', 'inner-ticks');

innerTicksGroup.selectAll('text').data(innerTicks).enter().append('text').attr('class', 'tick').attr('text-anchor', 'middle').attr('transform', function (d) {
  var ratio = scale(d.value);
  var newAngle = config.minAngle + ratio * 180;
  return 'rotate(' + newAngle + ') translate(0, ' + -(radius + config.innerTickRingOffset) + ')';
}).text(function (d) {
  return d.label;
});

var outerTicksGroup = chart.append('g').attr('class', 'outer-ticks');

outerTicksGroup.selectAll('text').data(outerTicks).enter().append('text').attr('class', 'tick').attr('text-anchor', 'middle').attr('transform', function (d, i) {
  var ratio = scale(d.value);
  var newAngle = config.minAngle + ratio * 180 - (d.counterNotch ? d.counterNotch : 15);
  return 'rotate(' + newAngle + ') translate(0, ' + -(radius + config.outerTickRingOffset) + ')';
}).text(function (d) {
  return d.label;
});

outerTicksGroup.selectAll('line').data(outerTicks).enter().append('line').filter(function (d) {
  return !!d.borderAt;
}).attr('class', 'line').attr("x1", -0).attr("y1", -radius + 10).attr("x2", -0).attr("y2", -(radius + config.outerTickBorderLength)).style("stroke", 'red').attr('transform', function (d) {
  var ratio = scale(d.borderAt);
  var newAngle = config.minAngle + ratio * 180;
  return 'rotate(' + newAngle + ')';
});
