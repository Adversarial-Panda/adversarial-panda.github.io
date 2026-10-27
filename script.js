const dialog = document.querySelector('#image-dialog');
if (dialog && typeof dialog.showModal === 'function') {
  const expanded = dialog.querySelector('img');
  document.querySelectorAll('[data-zoom]').forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault();
      expanded.src = link.href;
      expanded.alt = link.querySelector('img').alt;
      dialog.showModal();
    });
  });
  dialog.querySelector('button').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => { if (event.target === dialog) { const r = dialog.getBoundingClientRect(); if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) dialog.close(); } });
}

const animationToggle = document.querySelector('#toggle-animations');
if (animationToggle) {
  const animations = document.querySelectorAll('[data-animation]');
  function setAnimations(playing) {
    animations.forEach(img => { img.src = playing ? img.dataset.animation : img.dataset.still; });
    animationToggle.textContent = playing ? 'Stop animations' : 'Play animations';
    animationToggle.setAttribute('aria-pressed', String(playing));
  }
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) setAnimations(false);
  animationToggle.addEventListener('click', () => {
    setAnimations(animationToggle.getAttribute('aria-pressed') !== 'true');
  });
}
