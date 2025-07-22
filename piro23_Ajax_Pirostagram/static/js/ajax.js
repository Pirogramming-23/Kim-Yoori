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

document.addEventListener('DOMContentLoaded', function () {
    bindLikeButtons();
    bindCommentForms();
    bindDeleteCommentButtons();
    bindPostThumbnails();
    bindSearchInput();
});

function bindPostThumbnails() {
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
                    bindDeleteCommentButtons();

                    const closeButton = document.querySelector('.modal-close');
                    if (closeButton) {
                        closeButton.addEventListener('click', () => {
                            const modal = document.querySelector('.modal-wrapper');
                            if (modal) modal.remove();
                        });
                    }
                });
        });
    });
}

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

function bindDeleteCommentButtons() {
    const deleteButtons = document.querySelectorAll('.delete-comment');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const commentId = this.dataset.commentId;

            if (!confirm('정말 삭제하시겠습니까?')) return;

            fetch(`/comment/${commentId}/delete/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    this.closest('.comment').remove();
                } else {
                    alert(data.error || '삭제 실패');
                }
            });
        });
    });
}

function bindSearchInput() {
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            const keyword = searchInput.value;

            fetch(`/search/?q=${encodeURIComponent(keyword)}`)
                .then(response => response.text())
                .then(html => {
                    document.getElementById('search-results').innerHTML = html;
                    bindPostThumbnails();
                });
        });
    }
}

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const modal = document.querySelector('.modal-wrapper');
        if (modal) modal.remove();
    }
});