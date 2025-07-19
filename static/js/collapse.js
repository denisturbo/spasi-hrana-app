document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('[data-collapse-toggle]').forEach((btn) => {
        const targetId = btn.getAttribute('data-collapse-toggle');
        const target = document.getElementById(targetId);
        if (localStorage.getItem(targetId) === 'open') {
            target.classList.remove('hidden');
        }
        btn.addEventListener('click', () => {
            const isHidden = target.classList.contains('hidden');
            localStorage.setItem(targetId, isHidden ? 'open' : 'closed');
        });
    });
});