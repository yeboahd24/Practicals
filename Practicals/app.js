const form = document.querySelector('form');
const timeInput = document.getElementById('time');
const fromSelect = document.getElementById('from');
const toSelect = document.getElementById('to');
const result = document.getElementById('result');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const date = new Date();
  const currentTime = timeInput.value;
  const currentOffSet = date.getTimezoneOffset();
  date.setUTCHours(currentTime.split(':')[0], currentTime.split(':')[1], 0, 0);
  let fromTimeZone = fromSelect.value;
  let toTimeZone = toSelect.value;
  fromTimeZone = fromTimeZone.slice(3);
  toTimeZone = toTimeZone.slice(3);

  const fromOffSet = fromTimeZone * 60;
  const toOffSet = toTimeZone * 60;

  date.setMinutes(date.getMinutes() + (toOffSet - fromOffSet));
  // update the result element with the converted time
  result.innerHTML = `Converted Time: ${date.toLocaleTimeString()}`;
});

