document.addEventListener('DOMContentLoaded', function () {
    bindLikeButtons();
    bindCommentForms();

    const thumbnails = document.querySelectorAll('.post-thumbnail');
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function () {
            const postId = this.dataset.postId;

            fetch(`/${postId}/detail/`)
                .then(response => response.text())
                .then(html => {
                    const oldModal = document.querySelector('.modal-wrapper');
                    if (oldModal) oldModal.remove();

                    const modalContainer = document.createElement('div');
                    modalContainer.innerHTML = html;
                    document.body.appendChild(modalContainer);

                    // 모달 내에 바인딩 다시 설정
                    bindLikeButtons();
                    bindCommentForms();
                });
        });
    });

    function bindLikeButtons() {
        const likeButtons = document.querySelectorAll('.like-button');
        likeButtons.forEach(button => {
            button.addEventListener('click', function () {
                const postId = this.dataset.postId;

                fetch(`/like/${postId}/`, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('좋아요 요청 실패');
                        }
                        return response.json();
                    })
                    .then(data => {
                        const likeCountSpan = document.getElementById(`like-count-${postId}`);
                        if (likeCountSpan) likeCountSpan.textContent = data.likes_count;

                        this.textContent = data.liked ? '❤️' : '🤍';
                    })
                    .catch(error => {
                        alert(error.message);
                    });
            });
        });
    }

    function bindCommentForms() {
        const commentForms = document.querySelectorAll('.comment-form');

        commentForms.forEach(form => {
            form.addEventListener('submit', function (e) {
                e.preventDefault();

                const postId = this.dataset.postId;
                const input = this.querySelector('input[name="content"]');
                const content = input.value.trim();

                if (!content) return;

                fetch(`/${postId}/comment/`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                    body: JSON.stringify({ content }),
                })
                    .then(response => {
                        if (!response.ok) {
                            return response.json().then(data => {
                                throw new Error(data.error || '댓글 등록 실패');
                            });
                        }
                        return response.json();
                    })
                    .then(data => {
                        const commentList = document.querySelector('.modal-comments');
                        const username = document.querySelector('.modal-header strong')?.textContent || '익명';

                        // 기존 '댓글 없음' 메시지 제거
                        const emptyMsg = commentList.querySelector('.no-comment');
                        if (emptyMsg) emptyMsg.remove();

                        const newComment = document.createElement('div');
                        newComment.classList.add('comment');
                        newComment.innerHTML = `<strong>${username}</strong> ${content}`;
                        commentList.appendChild(newComment);
                        input.value = '';
                    })
                    .catch(error => {
                        alert(error.message);
                    });
            });
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
