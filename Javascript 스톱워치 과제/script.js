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
    if(timerInterval !== null){
        clearInterval(timerInterval);
        timerInterval = null;        
    }

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

// 챌린지 1. 전체 선택 버튼 구현
const recordList = document.querySelector('.record-list');
const selectAllCheckbox = document.querySelector('.select-all');

recordList.addEventListener('change', (e) => {
    if(e.target.type === 'checkbox'){
        const allCheckboxes = document.querySelectorAll('.record-item input[type="checkbox"]');
        const checkedCheckboxes = document.querySelectorAll('.record-item input[type="checkbox"]:checked');

        selectAllCheckbox.checked = allCheckboxes.length > 0 && allCheckboxes.length === checkedCheckboxes.length;
    }
});

selectAllCheckbox.addEventListener('change', () => {
    const itemCheckboxes = document.querySelectorAll('.record-item input[type="checkbox"]');
    itemCheckboxes.forEach(cb => {
        cb.checked = selectAllCheckbox.checked;
    });
});

// 다크모드용 CSS 클래스 동적으로 생성 (선택)
const darkModeStyle = document.createElement("style");
darkModeStyle.textContent = `
  .dark-mode {
    background-color: #222;
    color: #f0f0f0;
  }

  .dark-mode .time-box{
    color: black;}
  .dark-mode .record-box,
  .dark-mode .record-list {
    background-color: #333;
    color: #f0f0f0;
    box-shadow: 2px 2px 6px rgba(255, 255, 255, 0.1);
  }

  .dark-mode .record-time {
    color: #ddd;
  }

  .dark-mode input[type="button"] {
    background-color: #555;
    color: white;
  }

  .dark-mode .checkmark {
    border-color: #ccc;
  }
`;
document.head.appendChild(darkModeStyle);
const container = document.querySelector(".container");

container.addEventListener("click", (e)=> {
    if (e.target === container){
        document.body.classList.toggle("dark-mode");
    }
})


// 버튼에 이벤트 연결
document.getElementById('startBtn').addEventListener('click', startTimer);
document.getElementById('stopbtn').addEventListener('click', () => {
  stopTimer();
  const time = document.getElementById('time').innerText;
  addRecord(time);
});
document.getElementById('resetBtn').addEventListener('click', resetTimer);

document.querySelector('.deleteBtn').addEventListener('click', hadleDelete)