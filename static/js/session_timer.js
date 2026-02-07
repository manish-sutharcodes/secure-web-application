let seconds = 0;

setInterval(() => {
    seconds++;

    const hrs = String(Math.floor(seconds / 3600)).padStart(2, '0');
    const mins = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0');
    const secs = String(seconds % 60).padStart(2, '0');

    const timer = document.getElementById("session-timer");
    if (timer) timer.innerText = `${hrs}:${mins}:${secs}`;
}, 1000);