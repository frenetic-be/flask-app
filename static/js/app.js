
function buildPlot() {
    var url = '/api/pals';
    Plotly.d3.json(url, function(error, response){
        if (error) {
            return console.warn(error);
        }
        var layout = {
            title: "Pet Pals",
            xaxis: {
                title: "Pet type"
            },
            yaxis: {
                title: "Number of pets"
            }
        };
        Plotly.newPlot('plot', [response], layout);
    });
}

buildPlot();