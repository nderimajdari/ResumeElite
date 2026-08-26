/*
 * Consent, analytics and ad loading for ResumeElite.
 *
 * Order of events, which matters:
 *   1. Every page sets Consent Mode v2 defaults to "denied" inline in <head>,
 *      before this file runs. So the first paint is already compliant.
 *   2. This file reads any stored choice and calls gtag('consent','update').
 *   3. Only then does it load Google Analytics and AdSense.
 *
 * If Google's own certified CMP is present (the "Privacy & messaging" GDPR
 * message you enable inside AdSense), this file detects the TCF API and steps
 * out of the way rather than showing a second banner. That is the intended
 * production setup for EEA/UK traffic: a self-hosted banner is not a
 * Google-certified CMP and cannot legally substitute for one there.
 */
(function () {
  'use strict';

  var STORE_KEY = 're_consent_v1';
  var CONFIG = window.RE_CONFIG || {};
  var adsClient = (CONFIG.adsenseClient || '').trim();
  var gaId = (CONFIG.ga4Id || '').trim();

  // ------------------------------------------------------------------ storage
  function readChoice() {
    try {
      var raw = localStorage.getItem(STORE_KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      // A stored choice older than 13 months has to be asked again.
      if (!parsed || !parsed.at) return null;
      if (Date.now() - parsed.at > 1000 * 60 * 60 * 24 * 396) return null;
      return parsed;
    } catch (e) {
      return null;
    }
  }

  function saveChoice(state) {
    try {
      localStorage.setItem(STORE_KEY, JSON.stringify({
        ads: !!state.ads,
        analytics: !!state.analytics,
        at: Date.now()
      }));
    } catch (e) { /* private mode: session-only consent is acceptable */ }
  }

  // ------------------------------------------------------------------ signals
  function gtag() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  }

  function pushConsent(state) {
    gtag('consent', 'update', {
      ad_storage: state.ads ? 'granted' : 'denied',
      ad_user_data: state.ads ? 'granted' : 'denied',
      ad_personalization: state.ads ? 'granted' : 'denied',
      analytics_storage: state.analytics ? 'granted' : 'denied'
    });
  }

  // ------------------------------------------------------------------ loaders
  var loaded = { ga: false, ads: false };

  function loadScript(src, attrs) {
    var s = document.createElement('script');
    s.async = true;
    s.src = src;
    Object.keys(attrs || {}).forEach(function (k) { s.setAttribute(k, attrs[k]); });
    document.head.appendChild(s);
    return s;
  }

  function loadAnalytics() {
    if (loaded.ga || !gaId) return;
    loaded.ga = true;
    loadScript('https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(gaId));
    gtag('js', new Date());
    gtag('config', gaId, { anonymize_ip: true });
  }

  function loadAds() {
    if (loaded.ads || !adsClient) return;
    loaded.ads = true;
    loadScript(
      'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' +
      encodeURIComponent(adsClient),
      { crossorigin: 'anonymous' }
    );
    fillAdSlots();
  }

  // --------------------------------------------------------------- ad slots
  /*
   * Slots are reserved in the markup with a fixed min-height so filling one
   * causes no layout shift. Until AdSense is configured and consented they stay
   * collapsed, so a visitor never sees an empty box labelled "Advertisement".
   */
  function fillAdSlots() {
    if (!adsClient) return;
    var slots = document.querySelectorAll('.ad-slot:not([data-ad-filled])');
    Array.prototype.forEach.call(slots, function (slot) {
      slot.setAttribute('data-ad-filled', '1');
      slot.removeAttribute('aria-hidden');
      slot.classList.add('is-live');

      var ins = document.createElement('ins');
      ins.className = 'adsbygoogle';
      ins.style.display = 'block';
      ins.setAttribute('data-ad-client', adsClient);
      ins.setAttribute('data-ad-format', 'auto');
      ins.setAttribute('data-full-width-responsive', 'true');
      slot.appendChild(ins);

      try {
        (window.adsbygoogle = window.adsbygoogle || []).push({});
      } catch (e) { /* blocked or offline: the slot simply stays empty */ }
    });
  }

  // ------------------------------------------------------------------- banner
  var banner = null;

  function buildBanner() {
    if (banner) return banner;
    banner = document.createElement('div');
    banner.className = 'consent-bar';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-live', 'polite');
    banner.setAttribute('aria-label', 'Cookie consent');
    banner.innerHTML =
      '<div class="consent-inner">' +
        '<div class="consent-copy">' +
          '<h2>Cookies on this site</h2>' +
          '<p>Your resume never leaves your browser. Separately, we would like to use ' +
          'cookies for advertising and anonymous analytics so the site can stay free. ' +
          'You can change this at any time. ' +
          '<a href="/cookies.html">Cookie policy</a></p>' +
        '</div>' +
        '<div class="consent-actions">' +
          '<button type="button" class="btn-consent-ghost" data-consent="reject">Reject non-essential</button>' +
          '<button type="button" class="btn-consent-primary" data-consent="accept">Accept all</button>' +
        '</div>' +
      '</div>';
    document.body.appendChild(banner);

    banner.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-consent]');
      if (!btn) return;
      var accept = btn.getAttribute('data-consent') === 'accept';
      apply({ ads: accept, analytics: accept }, true);
      hideBanner();
    });
    return banner;
  }

  function showBanner() {
    buildBanner();
    requestAnimationFrame(function () { banner.classList.add('is-visible'); });
  }

  function hideBanner() {
    if (!banner) return;
    banner.classList.remove('is-visible');
    setTimeout(function () {
      if (banner && banner.parentNode) banner.parentNode.removeChild(banner);
      banner = null;
    }, 260);
  }

  // -------------------------------------------------------------------- apply
  function apply(state, persist) {
    pushConsent(state);
    if (persist) saveChoice(state);
    if (state.analytics) loadAnalytics();
    if (state.ads) loadAds();
  }

  // ------------------------------------------------------------------- public
  window.REConsent = {
    open: function () {
      // Re-opening always shows the banner so a choice can be changed.
      showBanner();
    },
    revoke: function () {
      try { localStorage.removeItem(STORE_KEY); } catch (e) {}
      pushConsent({ ads: false, analytics: false });
      showBanner();
    },
    state: readChoice
  };

  // ---------------------------------------------------------------- bootstrap
  function start() {
    // Footer "Cookie settings" links, on every page.
    document.addEventListener('click', function (e) {
      var opener = e.target.closest('[data-open-consent]');
      if (!opener) return;
      e.preventDefault();
      window.REConsent.open();
    });

    // A Google-certified CMP owns consent if it is present. Do not double-prompt.
    if (typeof window.__tcfapi === 'function') {
      window.__tcfapi('addEventListener', 2, function (data, success) {
        if (!success || !data) return;
        if (data.eventStatus === 'tcloaded' || data.eventStatus === 'useractioncomplete') {
          var purposes = (data.purpose && data.purpose.consents) || {};
          // Purpose 1 = store information; 3/4 = personalised ads profile/selection.
          var adsOk = !!purposes[1];
          apply({ ads: adsOk, analytics: adsOk }, false);
        }
      });
      return;
    }

    var stored = readChoice();
    if (stored) {
      apply(stored, false);
      return;
    }

    // Nothing stored: default stays denied and we ask.
    showBanner();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
