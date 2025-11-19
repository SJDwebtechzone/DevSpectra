document.addEventListener('DOMContentLoaded', () => {
  const btn = document.querySelector('.hamburger');
  const nav = document.querySelector('#site-nav');

  function toggleNav() {
    const isOpen = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', isOpen);
    document.documentElement.style.overflow = isOpen ? 'hidden' : '';
  }

  btn.addEventListener('click', toggleNav);

  // Close nav on click outside
  document.addEventListener('click', (e) => {
    if (!nav.classList.contains('open')) return;
    if (e.target === btn || btn.contains(e.target) || nav.contains(e.target)) return;
    nav.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    document.documentElement.style.overflow = '';
  });

  // Close nav on escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('open')) {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      document.documentElement.style.overflow = '';
    }
  });

  // Close nav if resizing to desktop
  window.addEventListener('resize', () => {
    if (window.innerWidth > 980 && nav.classList.contains('open')) {
      nav.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
      document.documentElement.style.overflow = '';
    }
  });
});


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

document.getElementById('resumeInput').addEventListener('change', function() {
  const file = this.files[0];
  if (file && file.type !== "application/pdf") {
    alert("Please select a PDF file.");
    this.value = ""; // clear the invalid file
  }
});