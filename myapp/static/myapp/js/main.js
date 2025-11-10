document.addEventListener('DOMContentLoaded', function () {
  // === NAV TOGGLE ===
  const btn = document.querySelector('.hamburger');
  const nav = document.querySelector('#site-nav');
  if (btn && nav) {
    function closeNav() {
      btn.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      document.documentElement.style.overflow = '';
    }
    function openNav() {
      btn.setAttribute('aria-expanded', 'true');
      nav.classList.add('open');
      document.documentElement.style.overflow = 'hidden';
    }

    btn.addEventListener('click', function () {
      const expanded = btn.getAttribute('aria-expanded') === 'true';
      expanded ? closeNav() : openNav();
    });

    document.addEventListener('click', function (e) {
      if (!nav.classList.contains('open')) return;
      if (e.target === btn || btn.contains(e.target) || nav.contains(e.target)) return;
      closeNav();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') closeNav();
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 980 && nav.classList.contains('open')) {
        closeNav();
      }
    });
  }

  // === FORCE SCROLL TO TOP ON RELOAD ===
  if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
  }

  const urlParams = new URLSearchParams(window.location.search);
  const justSubmitted = urlParams.get('submitted') === 'true';

  if (!justSubmitted) {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // === FADE OUT SUCCESS MESSAGE ===
  // const messages = document.querySelectorAll('.django-message');
  // if (messages.length > 0) {
  //   setTimeout(() => {
  //     messages.forEach(msg => {
  //       msg.style.opacity = '0';
  //       msg.style.transition = 'opacity 0.5s ease';
  //     });
  //   }, 4000);
  // }
});
