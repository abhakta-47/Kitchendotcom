"use strict";

var tinderContainer6 = document.querySelector(".tinder6");
var allCards6 = document.querySelectorAll(".tinder--card6");
var nope6 = document.getElementById("nope6");
var love6 = document.getElementById("love6");

function initCards6(card, index) { 
  var newCards = document.querySelectorAll(".tinder--card6:not(.removed)");

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards6.length - index;
    card.style.transform =
      "scale(" + (20 - index) / 20 + ") translateY(-" + 30 * index + "px)";
    card.style.opacity = (10 - index) / 10;
  });

  tinderContainer6.classList.add("loaded");
}

initCards6();

allCards6.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on("pan", function (event) {
    el.classList.add("moving");
  });

  hammertime.on("pan", function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    tinderContainer6.classList.toggle("tinder_love6", event.deltaX > 0);
    tinderContainer6.classList.toggle("tinder_nope6", event.deltaX < 0);

    var xMulti = event.deltaX * 0.03;
    var yMulti = event.deltaY / 80;
    var rotate = xMulti * yMulti;

    event.target.style.transform =
      "translate(" +
      event.deltaX +
      "px, " +
      event.deltaY +
      "px) rotate(" +
      rotate +
      "deg)";
  });

  hammertime.on("panend", function (event) {
    el.classList.remove("moving");
    tinderContainer6.classList.remove("tinder_love6");
    tinderContainer6.classList.remove("tinder_nope6");

    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;

    event.target.classList.toggle("removed", !keep);

    if (keep) {
      event.target.style.transform = "";
    } else {
      var endX = Math.max(
        Math.abs(event.velocityX) * moveOutWidth,
        moveOutWidth
      );
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform =
        "translate(" +
        toX +
        "px, " +
        (toY + event.deltaY) +
        "px) rotate(" +
        rotate +
        "deg)";
      initCards6();
    }
  });
});

function createButtonListener(love6) {
  return function (event) {
    var cards = document.querySelectorAll(".tinder--card6:not(.removed)");
    var moveOutWidth = document.body.clientWidth * 1.5;

    if (!cards.length) return false;

    var card = cards[0];

    card.classList.add("removed");

    if (love6) {
      card.style.transform =
        "translate(" + moveOutWidth + "px, -100px) rotate(-30deg)";
    } else {
      card.style.transform =
        "translate(-" + moveOutWidth + "px, -100px) rotate(30deg)";
    }

    initCards6();

    event.preventDefault();
  };
}

var nope6Listener = createButtonListener(false);
var love6Listener = createButtonListener(true);

nope6.addEventListener("click", nope6Listener);
love6.addEventListener("click", love6Listener);
