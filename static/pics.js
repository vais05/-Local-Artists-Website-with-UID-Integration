var slideImages = [
  [
    { img_url: "static/6.png" },
    { img_url: "static/1.png" },
    { img_url: "static/2.png" },
    { img_url: "static/3.png" }
  ],

];

var z = null;

// script for media queries
var value = window.matchMedia("(max-width: 1000px)");

function mFunction(value) {
  if (value.matches) {
    z = slideImages[1];
  } else {
    z = slideImages[0];
  }

  z.map(function (ele, index) {
    var slideDiv = document.createElement('div');
    switch (index) {
      case 0:
        slideDiv.setAttribute('class', 'slide first');
        break;
      default:
        slideDiv.setAttribute('class', 'slide');
    }

    var images = document.createElement('img');
    images.src = ele.img_url;

    slideDiv.appendChild(images);
    document.getElementById('slides').appendChild(slideDiv);
  });
}

mFunction(value);
value.addListener(mFunction);
