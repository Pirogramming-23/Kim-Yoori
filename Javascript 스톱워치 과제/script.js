// 1. 스톱워치 기능
let startTime, timerInterval = null;
let elapsedTime = 0;

function startTimer() {
    if(timerInterval !== null) return;
    startTime = Date.now() - elapsedTime;
    timerInterval = setInterval(updateTime, 10);
}

function stopTimer() {
    if(timerInterval !== null) {
        clearInterval(timerInterval);
        timerInterval = null;
        elapsedTime = Date.now() - startTime;
    }
}

function resetTimer() {
    clearInterval(timerInterval);
    timerInterval = null;

    elapsedTime = 0;
    startTime = null;

    document.getElementById('time').innerText = "00 : 00";
}

function updateTime() {
    const now = Date.now();
    elapsedTime = now - startTime;

    const seconds = Math.floor(elapsedTime/1000);
    const milliseconds = Math.floor((elapsedTime % 1000) / 10);
    const formatted = `${String(seconds).padStart(2, '0')} : ${String(milliseconds).padStart(2, '0')}`;
    document.getElementById('time').innerText = formatted;
}

// 2. 기록 추가 기능
function addRecord(timeText) {
    const ul = document.querySelector(".record-list");
    const templateLi = document.querySelector(".record-item");
    
    const li = templateLi.cloneNode(true);
    const label = document.createElement('label');
    label.classList.add('custom-checkbox');

    const checkbox = document.createElement("input");
    checkbox.type = 'checkbox';

    const checkmark = document.createElement('span');
    checkmark.classList.add('checkmark');

    label.appendChild(checkbox);
    label.appendChild(checkmark);

    li.insertBefore(label, li.firstChild);

    const timeSpan = li.querySelector(".record-time");
    timeSpan.innerText = timeText;

    ul.appendChild(li);
}


// 3. 선택 삭제 기능 + 4. 전체 삭제 기능
function hadleDelete() {
    const records = document.querySelectorAll('.record-list .record-item');

    const checked = Array.from(records).filter(record => {
        const checkbox = record.querySelector('input[type="checkbox"]');
        return checkbox && checkbox.checked;
    });

    if(checked.length > 0) {
        checked.forEach(record => record.remove());
    } else {
        records.forEach(record => record.remove());
    }

    const selectAll = document.querySelector(".select-all");
    if (selectAll) selectAll.checked = false;
    
}

// 버튼에 이벤트 연결
document.getElementById('startBtn').addEventListener('click', startTimer);
document.getElementById('stopbtn').addEventListener('click', () => {
  stopTimer();
  const time = document.getElementById('time').innerText;
  addRecord(time);
});
document.querySelector('.deleteBtn').addEventListener('click', hadleDelete)

// 선택 삭제는 따로 버튼 만들거나 선택 후 바로 삭제해도 됨