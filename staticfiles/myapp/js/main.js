
console.log("Main JS loaded successfully");
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


  // Check if the URL has the success section in it

  // Check if the user is on the success section

  // If the current URL contains #success (after successful submission)

document.addEventListener("DOMContentLoaded", function () {
  console.log("JS running…");

  const messages = document.querySelectorAll(".django-message");
  console.log("Found messages:", messages);

  if (messages.length > 0) {
    messages.forEach(msg => {
      console.log("Message text:", msg.textContent.trim());
    });
  } else {
    console.log("No messages found in DOM.");
  }
});

