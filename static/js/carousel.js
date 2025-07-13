document.querySelectorAll('.carousel-container').forEach(container => {
    const carousel = container.querySelector('.carousel');
    const scrollLeftBtn = container.querySelector('.scroll-left');
    const scrollRightBtn = container.querySelector('.scroll-right');

    const scrollAmount = () => {
        const firstEl = carousel.querySelector('.carousel-card');
        return firstEl.offsetWidth + 16;
    };

    scrollLeftBtn.addEventListener('click', () => {
        carousel.scrollBy({left: -scrollAmount(), behavior: 'smooth'});
    });

    scrollRightBtn.addEventListener('click', () => {
        carousel.scrollBy({left: scrollAmount(), behavior: 'smooth'});
    });
});
