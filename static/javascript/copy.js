function CopyFunction() {
  let copyText = document.getElementById("src-to-site").innerHTML;
  navigator.clipboard.writeText(`${copyText}`)
  .then(() => {
    //console.log('yes');
  })
  .catch(err => {
    console.log('error', err);
  });
}

document.body.addEventListener("keydown", function (ev) {
  ev = ev || window.event;  // Event object 'ev'
  var key = ev.which || ev.keyCode; // Detecting keyCode
  var ctrl = ev.ctrlKey ? ev.ctrlKey : ((key === 17)
      ? true : false);
  if (key == 67 && ctrl) {
    let copyText = document.getElementById("src-to-site").innerHTML;
    navigator.clipboard.writeText(`${copyText}`)
    .then(() => {
      //
    })
    .catch(err => {
      console.log('error', err);
    });
  }
}, false);