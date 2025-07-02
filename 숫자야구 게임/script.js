
// 1. 초기화 단계
let answer = [];
let attempts = 9;

function resetInput(){
    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';
}

function resetGame(){
    // 시도 횟수는 총 9번
    attempts = 9;

    // 정답 숫자 3개 랜덤 생성
    answer = [];
    while(answer.length < 3){
        let num = Math.floor(Math.random() * 10);
        //includes는 배열에 특정 값이 이미 있는지 확인하는 함수
        if(!answer.includes(num)) { 
            //push는 배열의 맨 끝에 새로운 값을 추가하는 함수
            answer.push(num);
        }
    }
    
    // input 창 및 결과창 초기화
    resetInput();
    
    document.getElementById('results').innerHTML = '';
    document.getElementById('attempts').innerText = attempts;
    document.getElementById('game-result-img').src = '';
   
    //submit_button 활성화
    document.querySelector('.submit-button').disabled = false;
}

// 2. 입력
// 사용자는 3개의 숫자를 각 input 칸에 입력
// #submit_button 클릭 시 check_numbers() 실행 --> 이거 이벤트 리스너로 연결해줘야함 !!!!

// 3. 유효성 검사
// 입력칸 중 하나라도 비어 있으면 input만 비우고 넘어감

function check_numbers(){
    let n1 = document.getElementById('number1').value;
    let n2 = document.getElementById('number2').value;
    let n3 = document.getElementById('number3').value;

    if(n1 ===''|| n2 === ''|| n3 ===''){
        resetInput();
        return;
    }

    // 4. 숫자 판정
    // 컴퓨터 정답과 비교하기
    // 숫자와 위치 일치하면 스트라이크(S)
    // 숫자만 일지하면 볼(b)
    // 아무것도 일치하지 않으면 "O" 아웃

    let input = [parseInt(n1), parseInt(n2), parseInt(n3)];
    let strikes = 0;
    let balls = 0;

    for(let i=0; i < 3; i++){
        if (input[i] === answer[i]) {
            strikes ++;
        }
        else if (answer.includes(input[i])) {
            balls ++;
        }
        
    }
    
    // 5. 결과 출력
    // 결과 메시지 출력 (예: 1S 2B /또는 O)
    // 시도 횟수 -1
    if (strikes === 0 && balls === 0){
       resultText = `${out}`;
    }
    else {
        resultText = `${strikes}S ${balls}B`;
    }
    
    document.getElementById('results').innerHTML += resultText + "<br>";
    attempts --;
    document.getElementById('attempts').innerText = attempts;

    // 6. 게임 종료 판단
    // 3 스트라이크 시 승리 이미지 
    // 시도 횟수 0이면 패배 이미지
    // 종료 시 이미지 출력 및 버튼 활성화

    if(strikes === 3){
        document.getElementById('game-result-img').src = 'success.png';
        document.querySelector('.submit-button').disabled = true;
    }
    else if(attempts === 0){
        document.getElementById('game-result-img').src = 'fail.png';
        document.querySelector('.submit-button').disabled = true;
    }
}

