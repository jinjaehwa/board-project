// 삭제 확인 팝업
function confirmDelete(postId) {
    if (confirm("정말 삭제하시겠습니까?")) {
        window.location.href = "/delete/" + postId;
    }
}

// 글자수 카운터
const textarea = document.querySelector('textarea[name="content"]');
if (textarea) {
    const counter = document.createElement('p');
    counter.style.fontSize = '13px';
    counter.style.color = '#888';
    counter.style.textAlign = 'right';
    counter.textContent = '0 글자';
    textarea.parentNode.insertBefore(counter, textarea.nextSibling);

    textarea.addEventListener('input', () => {
        counter.textContent = textarea.value.length + ' 글자';
    });
}