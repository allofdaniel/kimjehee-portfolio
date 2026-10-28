(() => {
  const box = document.querySelector('.lightbox');
  if (!box) return;
  const big = box.querySelector('img');
  document.querySelectorAll('img[data-zoom]').forEach((img) => {
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
