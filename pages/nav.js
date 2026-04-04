(function () {
  const path = window.location.pathname;

  const links = [
    { href: '/index.html',     label: '홈',       match: ['/pages/', '/pages/index.html'] },
    { href: '/pages/problems.html',  label: '문제 모음', match: ['/pages/problems.html'] },
    { href: '/pages/summaries.html', label: '요약 모음', match: ['/pages/summaries.html'] },
  ];

  const style = document.createElement('style');
  style.textContent = `
    :root {
      --nav-h: 52px;
    }
    .site-nav {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      height: var(--nav-h);
      background: rgba(13,15,20,0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255,255,255,0.07);
      display: flex; align-items: center;
    }
    .site-nav-inner {
      max-width: 820px; width: 100%;
      margin: 0 auto; padding: 0 24px;
      display: flex; align-items: center; gap: 32px;
    }
    .nav-logo {
      font-family: 'Space Mono', monospace;
      font-size: 13px; font-weight: 700;
      color: #7bffc0; text-decoration: none;
      display: flex; align-items: center; gap: 8px;
      flex-shrink: 0;
    }
    .nav-logo-dot {
      width: 7px; height: 7px;
      background: #7bffc0; border-radius: 50%;
      animation: navblink 1.4s ease infinite;
    }
    .nav-links {
      display: flex; align-items: center; gap: 4px;
    }
    .nav-link {
      font-family: 'Space Mono', monospace;
      font-size: 11px; color: #7a7f8e;
      text-decoration: none;
      padding: 5px 12px; border-radius: 100px;
      border: 1px solid transparent;
      transition: color 0.2s, border-color 0.2s, background 0.2s;
    }
    .nav-link:hover {
      color: #e8eaf0;
      background: rgba(255,255,255,0.05);
    }
    .nav-link.active {
      color: #7bffc0;
      border-color: rgba(123,255,192,0.25);
      background: rgba(123,255,192,0.07);
    }
    body { padding-top: var(--nav-h) !important; }
    @keyframes navblink { 0%,100%{opacity:1} 50%{opacity:.2} }
  `;
  document.head.appendChild(style);

  const nav = document.createElement('nav');
  nav.className = 'site-nav';
  nav.innerHTML = `
    <div class="site-nav-inner">
      <a class="nav-logo" href="/pages/index.html"><span class="nav-logo-dot"></span>Do it! 알고리즘</a>
      <div class="nav-links">
        ${links.map(l => `
          <a class="nav-link ${l.match.includes(path) ? 'active' : ''}" href="${l.href}">${l.label}</a>
        `).join('')}
      </div>
    </div>
  `;
  document.body.insertAdjacentElement('afterbegin', nav);
})();
