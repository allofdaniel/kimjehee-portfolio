(() => {
  const root = document.documentElement;
  const sysDark = matchMedia('(prefers-color-scheme: dark)');
  const btn = document.querySelector('.theme');
  if (btn) {
    btn.addEventListener('click', () => {
      const cur = root.dataset.theme || (sysDark.matches ? 'dark' : 'light');
      const next = cur === 'dark' ? 'light' : 'dark';
      root.dataset.theme = next;
      try { localStorage.setItem('theme', next); } catch (e) {}
    });
  }

  const els = document.querySelectorAll('[data-reveal]');
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach((el) => el.classList.add('in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.35 });
    els.forEach((el) => io.observe(el));
  }

  const box = document.querySelector('.lightbox');
  if (!box) return;
  const big = box.querySelector('img');
  document.querySelectorAll('img[data-zoom]').forEach((img) => {
    img.tabIndex = 0;
    const open = () => { big.src = img.currentSrc || img.src; big.alt = img.alt; box.showModal(); };
    img.addEventListener('click', open);
    img.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
  });
  box.querySelector('.lb-close').addEventListener('click', () => box.close());
  box.addEventListener('click', (e) => { if (e.target === box) box.close(); });
})();
