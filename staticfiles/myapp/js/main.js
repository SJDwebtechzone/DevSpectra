document.addEventListener('DOMContentLoaded', function () {
  const btn = document.querySelector('.hamburger');
  const nav = document.getElementById('site-nav');
  if (!btn || !nav) return;

  function closeNav() {
    btn.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
  }
  function openNav() {
    btn.setAttribute('aria-expanded', 'true');
    nav.classList.add('open');
  }

  btn.addEventListener('click', function () {
    const expanded = btn.getAttribute('aria-expanded') === 'true';
    if (expanded) closeNav();
    else openNav();
  });

  document.addEventListener('click', function (e) {
    if (!nav.classList.contains('open')) return;
    if (e.target === btn || btn.contains(e.target) || nav.contains(e.target)) return;
    closeNav();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeNav();
  });
});