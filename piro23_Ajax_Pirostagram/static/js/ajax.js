document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.dataset.postId;
            const buttonElement = this;

            fetch(`like/${postId}/`, {
                method: 'POST',
                headers:{
                    'X-CSRFToken' : getCookie('csrftoken'),
                }})
            .then(response => {
                if(response.status === 401){
                    alert('로그인이 필요합니다.');
                    return;
                }
                return response.json();
                })
            .then(data => {
                if(!data) return;

                const likeCountSpan = document.getElementById(`like-count-${postId}`);
                likeCountSpan.textContent = data.likes_count;

                if(data.liked){
                    this.textContent = '좋아요 취소'
                }else {
                    this.textContent = '좋아요'
                }})
        });
    });
});

function getCookie(name){
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i=0; i < cookies.length; i++){
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
