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

  const tabs = [...document.querySelectorAll('.switch [role="tab"]')];
  if (tabs.length) {
    root.classList.add('js-tabs');
    const show = (id, focus) => {
      tabs.forEach((t) => {
        const on = t.getAttribute('aria-controls') === id;
        t.setAttribute('aria-selected', on);
        t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
        if (on && focus) t.focus();
      });
    };
    const fromHash = () => {
      const id = location.hash.slice(1);
      if (tabs.some((t) => t.getAttribute('aria-controls') === id)) {
        show(id);
        document.querySelector('.switch').scrollIntoView({ block: 'start' });
        return true;
      }
    };
    if (fromHash()) addEventListener('load', () => requestAnimationFrame(fromHash), { once: true });
    else show(tabs[0].getAttribute('aria-controls'));
    addEventListener('hashchange', fromHash);
    tabs.forEach((t, i) => {
      t.addEventListener('click', () => { show(t.getAttribute('aria-controls')); history.replaceState(null, '', '#' + t.getAttribute('aria-controls')); });
      t.addEventListener('keydown', (e) => {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        const n = tabs[(i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length];
        show(n.getAttribute('aria-controls'), true);
      });
    });
  }

  document.querySelectorAll('[data-steps]').forEach((wrap) => {
    root.classList.add('js-steps');
    const bs = [...wrap.querySelectorAll('[role="tab"]')];
    const pick = (b, focus) => bs.forEach((x) => {
      const on = x === b;
      x.setAttribute('aria-selected', on); x.tabIndex = on ? 0 : -1;
      document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
      if (on && focus) x.focus();
    });
    pick(bs[0]);
    bs.forEach((b, i) => {
      b.addEventListener('click', () => pick(b));
      b.addEventListener('keydown', (e) => {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        pick(bs[(i + (e.key === 'ArrowRight' ? 1 : bs.length - 1)) % bs.length], true);
      });
    });
  });

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
