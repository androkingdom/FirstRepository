let hourBox = document.querySelector("#Hour");
let minuteBox = document.querySelector("#Minute");
let secBox = document.querySelector("#Sec");

setInterval(() => {
  let date = new Date();
  let hour = date.getHours();
  let minute = date.getMinutes();
  let sec = date.getSeconds();
  hourBox.textContent = hour;
  minuteBox.textContent = minute;
  secBox.textContent = sec;
}, 1000);