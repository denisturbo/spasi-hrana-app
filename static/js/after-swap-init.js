// функция да пуска flowbite js от cdn-a отновo,
// след смяна на елемент от htmx

document.body.addEventListener('htmx:afterSwap', () => {
  if (typeof initFlowbite === 'function') {
    initFlowbite();
  }
});
