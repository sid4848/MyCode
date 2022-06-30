var spinInterval = 0;
function timeSpin() {
  var loop = setInterval(function () {
    let spin = Math.round(Math.random() * 100);
    spinInterval += spin;
    let rotate = `rotate(${spinInterval}deg)`;
    document.querySelector(".box").style.transform = rotate;
    // console.log(rotate);
    rotation = spinInterval;
  }, 100);

  setTimeout(function () {
    clearInterval(loop);
    console.clear();
    // inline style.transform
    console.log(document.querySelector(".box").style.transform);

    // full computed transform matrix
    const rotation= window.getComputedStyle(document.querySelector(".box")).getPropertyValue('transform');
    console.log(rotation);
  }, 5000);
}

document.querySelector('.spin').addEventListener('click', timeSpin);