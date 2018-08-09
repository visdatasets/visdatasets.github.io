---
layout: default
title: Datasets for Visualization Construction
---

<h2 id="title"></h2>
<p><a id="download-link" href="#">Download</a></p>
<p id="loading">Loading...</p>
<table id="table" class="data-table"></table>

<script src="https://d3js.org/d3.v5.min.js"></script>
<script type="text/javascript">
function showFileContents(url) {
    d3.select("#download-link").attr("href", url);
    d3.select("#title").text(url.match(/\/([0-9a-zA-Z\_\-]+.csv)$/)[1]);
    d3.csv(url).then(function(data) {
        let columns = data.columns;
        d3.select("#loading").remove();
        let thead = d3.select("#table").append("thead");
        thead.append("tr").selectAll("th").data(columns).enter().append("th").text(d => d);
        let tbody = d3.select("#table").append("tbody");
        data.forEach(function(row) {
            tbody.append("tr").selectAll("td").data(columns).enter().append("td").text(d => row[d]);
        });
    });
}

let hash = document.location.hash;
let m = hash.match(/\#\!((.*)\.csv)/i);
if(m) {
    showFileContents(m[1]);
}
</script>