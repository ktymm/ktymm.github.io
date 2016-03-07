// GALLERY namespace
var GALLERY = (function(containerId) {
  "use strict"

  // Any function/variable added to this dictionary will be exposed outside the script
  var nmspace = {};

  nmspace.genGallery = function(imgListFn) {
    // var container = d3.select(containerId);

    d3.json(imgListFn, function(error, imgData) {
      if(error) return console.error(error);

      d3.select(containerId)
        .selectAll("div")
        .data(imgData).enter()
        .append("div")
          .attr("class", "col-lg-3 col-md-3 col-sm-6 col-xs-12")
        .append("div")
          .attr("class", "img-thumb-outer aspect-100")
        .append("div")
          .attr("class", "img-thumb-inner")
        .append("a")
          .attr("href", function(d) { console.log(this); console.log(d.hires); return d.hires; })
        .append("img")
          .attr("src", function(d) { return d.thumb; })
          .attr("alt", "missing image");
    });
  };

  return nmspace;
})("#gallery");
