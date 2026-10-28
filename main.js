(() => {
  const track = document.querySelector('.strip-track');
  if (track && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
    [...track.children].forEach((img) => {
      const c = img.cloneNode(true);
      c.setAttribute('aria-hidden', 'true');
      track.appendChild(c);
    });
  }

  const box = document.querySelector('.lightbox');
  const big = box.querySelector('img');
  document.querySelectorAll('[data-zoom] img').forEach((img) => {
    img.tabIndex = 0;
    const open = () => {
      big.src = img.currentSrc || img.src;
      big.alt = img.alt;
      box.showModal();
    };
    img.addEventListener('click', open);
    img.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
    });
  });
  box.querySelector('.lb-close').addEventListener('click', () => box.close());
  box.addEventListener('click', (e) => { if (e.target === box) box.close(); });
})();
