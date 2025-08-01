  document.addEventListener('alpine:init', () => {
    Alpine.data('app', () => ({
      pn:'',
      getMask(input) {
        if(input.startsWith(0)) return '099 999 9999';
      }
    }))
  });