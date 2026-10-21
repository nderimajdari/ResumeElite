/* ===== ResumeElite app.js ===== */

// ---- State ----
const state = {
  template: 'classic',
  accentColor: '#2563eb',
  accentCustom: false,
  photo: null,
  showJobTitle: true,
  personal: { 
    firstName: '', lastName: '', jobTitle: '', email: '', phone: '', 
    city: '', country: '', linkedin: '', website: '', 
    dob: '', pob: '', driverLicense: '', gender: '', nationality: '', 
    civilStatus: '', customField: '' 
  },
  summary: '',
  experience: [],
  education: [],
  skills: [],
  languages: [],
  projects: [],
  certifications: [],
  internships: [],
  activities: [],
  hobbies: '',
  courses: [],
  references: [],
  qualities: [],
  achievements: [],
  signature: { text: '', image: null },
  footer: '',
  custom: { title: 'Custom Section', content: '' },
  sectionOrder: [
    'summary', 'experience', 'education', 'skills', 'languages', 
    'projects', 'certifications', 'internships', 'activities', 
    'hobbies', 'courses', 'references', 'qualities', 'achievements', 
    'signature', 'footer', 'custom'
  ],
  visibleSections: ['summary', 'experience', 'education', 'skills']
};

const defaultState = JSON.parse(JSON.stringify(state));
const personalFieldKeys = Object.keys(defaultState.personal);
const defaultVisibleSections = ['summary', 'experience', 'education', 'skills', 'languages', 'projects', 'certifications'];

let zoom = 1;

// ---- Section Drag & Drop ----
let draggedSection = null;

// ---- Item Drag & Drop ----
let draggedItem = null;
let draggedType = null;
let draggedIndex = null;

function initSectionDragging() {
  const container = document.querySelector('.form-scroll');
  const sections = document.querySelectorAll('.form-section:not(#section-personal)');

  sections.forEach(section => {
    const header = section.querySelector('.section-header');
    header.setAttribute('draggable', 'true');

    header.addEventListener('dragstart', (e) => {
      draggedSection = section;
      section.classList.add('section-dragging');
      e.dataTransfer.effectAllowed = 'move';
    });

    header.addEventListener('dragend', () => {
      section.classList.remove('section-dragging');
      draggedSection = null;
      document.querySelectorAll('.form-section').forEach(s => s.classList.remove('section-drag-over'));
    });

    section.addEventListener('dragover', (e) => {
      e.preventDefault();
      if (!draggedSection || draggedSection === section) return;
      section.classList.add('section-drag-over');
    });

    section.addEventListener('dragleave', () => {
      section.classList.remove('section-drag-over');
    });

    section.addEventListener('drop', (e) => {
      e.preventDefault();
      section.classList.remove('section-drag-over');
      if (!draggedSection || draggedSection === section) return;

      const allSections = Array.from(document.querySelectorAll('.form-section'));
      const fromIndex = allSections.indexOf(draggedSection);
      const toIndex = allSections.indexOf(section);

      if (fromIndex < toIndex) {
        section.after(draggedSection);
      } else {
        section.before(draggedSection);
      }

      updateSectionOrder();
      renderPreview();
      saveToStorage();
    });
  });
}

function updateSectionOrder() {
  const sections = document.querySelectorAll('.form-section:not(#section-personal)');
  state.sectionOrder = Array.from(sections).map(s => s.id.replace('section-', ''));
}

// ---- Init ----
document.addEventListener('DOMContentLoaded', () => {
  ensureCvFonts();
  if (!document.getElementById('resume-preview')) {
    // Landing page
    initLanding();
    return;
  }
  loadFromStorage();
  initFromUrl();
  bindTemplateButtons();
  bindTemplateToggle();
  bindAccentColor();
  bindPersonalFields();
  bindJobTitleToggle();
  bindSummaryField();
  bindSimpleFields();
  bindPhotoUpload();
  bindDownloadBtn();
  bindAccentSwatches();
  renderAllDynamic();
  syncTemplateButtons();
  renderTemplateThumbnails();
  renderPreview();
  bindClearBtn();
  initSectionDragging();
  initTemplateDrawer();
  initEditorTabs();
  window.addEventListener('resize', debounce(applyZoom, 120));
  window.addEventListener('orientationchange', () => setTimeout(applyZoom, 200));
});

function debounce(fn, wait) {
  let t;
  return function (...args) {
    clearTimeout(t);
    t = setTimeout(() => fn.apply(this, args), wait);
  };
}

// ---- Landing ----
function initLanding() {
  document.querySelectorAll('.template-card').forEach(card => {
    card.addEventListener('click', (e) => {
      if (e.target.closest('a')) return;
      const t = card.dataset.template;
      if (t) window.location.href = `editor.html?template=${t}`;
    });
  });
  initMobileNav();
  initGalleryFilters();
  initFaq();
  initReveal();
  initLiveThumbnails();
  initHeroShowcase();
  initShelf();
}

// Homepage hero: the front sheet cycles through templates to show that one set of
// content can take many designs. Pauses on hover/focus, when the tab is hidden, and
// never auto-plays for people who ask for reduced motion.
function initHeroShowcase() {
  const root = document.getElementById('lp-show');
  if (!root) return;
  const slides = Array.from(root.querySelectorAll('.lp-slide'));
  const label = document.getElementById('lp-show-name');
  const dots = document.getElementById('lp-show-dots');
  if (slides.length < 2) return;

  if (dots) dots.innerHTML = slides.map(() => '<i></i>').join('');
  const dotEls = dots ? Array.from(dots.children) : [];
  let index = 0;
  let timer = null;

  const go = (n) => {
    index = (n + slides.length) % slides.length;
    slides.forEach((s, i) => s.classList.toggle('is-active', i === index));
    dotEls.forEach((d, i) => d.classList.toggle('on', i === index));
    const slide = slides[index];
    if (label) {
      label.textContent = slide.dataset.label || slide.dataset.liveThumb;
      label.href = `editor.html?template=${slide.dataset.liveThumb}`;
    }
  };
  go(0);

  root.querySelector('.lp-show-front')?.addEventListener('click', () => {
    window.location.href = `editor.html?template=${slides[index].dataset.liveThumb}`;
  });

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const start = () => { if (!timer) timer = setInterval(() => go(index + 1), 2600); };
  const stop = () => { clearInterval(timer); timer = null; };
  root.addEventListener('mouseenter', stop);
  root.addEventListener('mouseleave', start);
  root.addEventListener('focusin', stop);
  root.addEventListener('focusout', start);
  document.addEventListener('visibilitychange', () => (document.hidden ? stop() : start()));
  start();
}

function initShelf() {
  const shelf = document.getElementById('lp-shelf');
  if (!shelf) return;
  document.querySelectorAll('[data-shelf]').forEach(btn => {
    btn.addEventListener('click', () => {
      const dir = btn.dataset.shelf === 'next' ? 1 : -1;
      shelf.scrollBy({ left: dir * shelf.clientWidth * 0.8, behavior: 'smooth' });
    });
  });
}

function initFromUrl() {
  const params = new URLSearchParams(window.location.search);
  const t = params.get('template');
  if (t && getTemplateIds().includes(t)) {
    state.template = t;
  }
}

// ---- Storage ----
function saveToStorage() {
  try { localStorage.setItem('rf_state', JSON.stringify(state)); } catch (e) { }
}
function loadFromStorage() {
  try {
    const s = localStorage.getItem('rf_state');
    if (s) Object.assign(state, JSON.parse(s));
    normalizeState();
    if (state.accentColor) {
      document.getElementById('accent-color').value = state.accentColor;
    }
    if (state.sectionOrder) {
      reorderFormSections();
    }
  } catch (e) { }
}

function normalizeState() {
  state.personal = { ...defaultState.personal, ...(state.personal || {}) };
  state.signature = { ...defaultState.signature, ...(state.signature || {}) };
  // Saves from before per-template colours: anything but the old default blue
  // was a deliberate choice and should keep applying.
  if (typeof state.accentCustom !== 'boolean') {
    state.accentCustom = !!state.accentColor && state.accentColor.toLowerCase() !== '#2563eb';
  }
  state.custom = { ...defaultState.custom, ...(state.custom || {}) };
  if (typeof state.showJobTitle !== 'boolean') state.showJobTitle = true;

  [
    'experience', 'education', 'skills', 'languages', 'projects', 'certifications',
    'internships', 'activities', 'courses', 'references', 'qualities', 'achievements'
  ].forEach(key => {
    if (!Array.isArray(state[key])) state[key] = [];
  });

  if (!Array.isArray(state.sectionOrder)) {
    state.sectionOrder = [...defaultState.sectionOrder];
  } else {
    state.sectionOrder = [
      ...state.sectionOrder.filter(id => defaultState.sectionOrder.includes(id)),
      ...defaultState.sectionOrder.filter(id => !state.sectionOrder.includes(id))
    ];
  }

  const storedVisible = Array.isArray(state.visibleSections) ? state.visibleSections : [];
  state.visibleSections = [
    ...defaultVisibleSections,
    ...storedVisible.filter(id => defaultState.sectionOrder.includes(id))
  ].filter((id, index, arr) => arr.indexOf(id) === index);
}

function reorderFormSections() {
  const container = document.querySelector('.form-scroll');
  if (!container || !state.sectionOrder) return;

  state.sectionOrder.forEach(id => {
    const el = document.getElementById(`section-${id}`);
    if (el) container.appendChild(el);
  });
}

// ---- Template Buttons ----
function bindTemplateButtons() {
  document.querySelectorAll('.tmpl-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      state.template = btn.dataset.tmpl;
      syncTemplateButtons();
      renderPreview();
      saveToStorage();
    });
  });
}

function bindTemplateToggle() {
  const toggle = document.getElementById('template-toggle');
  const group = document.querySelector('.template-toolbar-group');
  if (!toggle || !group) return;

  toggle.addEventListener('click', () => {
    group.classList.toggle('is-collapsed');
    const open = !group.classList.contains('is-collapsed');
    toggle.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('drawer-open', open);
    if (open) {
      updateTemplateToggleLabel();
      requestAnimationFrame(syncThumbScales);
      const search = document.getElementById('template-search');
      if (search && !window.matchMedia('(max-width: 900px)').matches) search.focus();
    }
  });
}

function getTemplateIds() {
  return Array.from(document.querySelectorAll('.tmpl-btn')).map(btn => btn.dataset.tmpl);
}

function syncTemplateButtons() {
  document.querySelectorAll('.tmpl-btn').forEach(btn => {
    const on = btn.dataset.tmpl === state.template;
    btn.classList.toggle('active', on);
    btn.setAttribute('aria-pressed', String(on));
  });
  updateTemplateToggleLabel();
}

// ---- Accent Color ----
function bindAccentColor() {
  const input = document.getElementById('accent-color');
  if (!input) return;
  input.addEventListener('input', () => {
    state.accentColor = input.value;
    state.accentCustom = true;
    renderTemplateThumbnails();
    renderPreview();
    saveToStorage();
  });
}

// ---- Personal Fields ----
function bindPersonalFields() {
  document.querySelectorAll('[data-field]').forEach(el => {
    const field = el.dataset.field;
    if (el.id === 'summary' || !field || field.includes('.') || !personalFieldKeys.includes(field)) return;
    
    // Set initial value from state
    el.value = state.personal[field] || '';
    
    // If field has data, show its container if it's hidden
    if (el.value) {
      const row = el.closest('.form-row, .form-group');
      if (row && (row.id.startsWith('row-') || row.classList.contains('hidden'))) {
        row.classList.remove('hidden');
      }
    }
    
    el.addEventListener('input', () => {
      state.personal[field] = el.value;
      renderPreview();
      saveToStorage();
    });
  });
}

// The job title can be switched off without deleting it, for people who would rather
// let the summary position them or who are applying across several kinds of role.
function bindJobTitleToggle() {
  const toggle = document.getElementById('jobTitle-toggle');
  const input = document.getElementById('jobTitle');
  if (!toggle) return;
  const sync = () => {
    toggle.checked = state.showJobTitle !== false;
    input?.closest('.form-group')?.classList.toggle('is-field-off', !toggle.checked);
  };
  sync();
  toggle.addEventListener('change', () => {
    state.showJobTitle = toggle.checked;
    sync();
    renderPreview();
    saveToStorage();
  });
}

function toggleExtraField(id) {
  const row = document.getElementById(`row-${id}`);
  if (row) {
    row.classList.toggle('hidden');
  }
}

function bindSummaryField() {
  const el = document.getElementById('summary');
  if (!el) return;
  el.value = state.summary;
  el.addEventListener('input', () => { state.summary = el.value; renderPreview(); saveToStorage(); });
}

function bindSimpleFields() {
  const mappings = [
    { id: 'hobbies', stateKey: 'hobbies' },
    { id: 'footer', stateKey: 'footer' },
    { id: 'signatureText', stateKey: 'signature', subKey: 'text' },
    { id: 'customTitle', stateKey: 'custom', subKey: 'title' },
    { id: 'customContent', stateKey: 'custom', subKey: 'content' }
  ];

  mappings.forEach(m => {
    const el = document.getElementById(m.id);
    if (!el) return;
    if (m.subKey) {
      el.value = state[m.stateKey][m.subKey] || '';
      el.addEventListener('input', () => {
        state[m.stateKey][m.subKey] = el.value;
        renderPreview();
        saveToStorage();
      });
    } else {
      el.value = state[m.stateKey] || '';
      el.addEventListener('input', () => {
        state[m.stateKey] = el.value;
        renderPreview();
        saveToStorage();
      });
    }
  });
}

// ---- Photo Upload ----
function bindPhotoUpload() {
  const input = document.getElementById('photo-input');
  const removeBtn = document.getElementById('remove-photo-btn');
  if (!input) return;
  input.addEventListener('change', () => {
    const file = input.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (e) => {
      state.photo = e.target.result;
      updatePhotoPreview();
      renderPreview();
      saveToStorage();
    };
    reader.readAsDataURL(file);
  });

  if (removeBtn) {
    removeBtn.addEventListener('click', () => {
      state.photo = null;
      input.value = '';
      updatePhotoPreview();
      renderPreview();
      saveToStorage();
    });
  }

  updatePhotoPreview();
}

function updatePhotoPreview() {
  const preview = document.getElementById('photo-preview');
  const removeBtn = document.getElementById('remove-photo-btn');
  if (!preview) return;

  if (state.photo) {
    preview.innerHTML = `<img src="${state.photo}" alt="Photo" />`;
    if (removeBtn) removeBtn.classList.remove('hidden');
    return;
  }

  preview.innerHTML = `
    <svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
      <circle cx="12" cy="8" r="4" />
      <path d="M4 20c0-4 3.6-7 8-7s8 3 8 7" />
    </svg>
  `;
  if (removeBtn) removeBtn.classList.add('hidden');
}

// ---- Section toggle ----
function toggleSection(id) {
  const body = document.getElementById(`body-${id}`);
  const icon = document.getElementById(`collapse-${id}`);
  if (!body) return;
  body.classList.toggle('hidden');
  icon.classList.toggle('collapsed');
}

// ---- Clear ----
function bindClearBtn() {
  const btn = document.getElementById('clear-btn');
  if (!btn) return;
  btn.addEventListener('click', () => {
    if (!confirm('Clear all resume data?')) return;
    localStorage.removeItem('rf_state');
    location.reload();
  });
}

// ---- Zoom ----
function zoomIn() { zoom = Math.min(zoom + 0.1, 1.6); applyZoom(); }
function zoomOut() { zoom = Math.max(zoom - 0.1, 0.4); applyZoom(); }
function resetZoom() { zoom = 1; applyZoom(); }

// The A4 page is a fixed 794px wide. Scale it down to whatever the preview
// column can actually show, then multiply by the user's zoom on top of that.
function applyZoom() {
  const w = document.getElementById('preview-wrapper');
  const page = document.getElementById('resume-preview');
  const scroll = document.querySelector('.preview-scroll');
  if (w && page && scroll) {
    const pageWidth = page.offsetWidth || 794;
    const pageHeight = page.offsetHeight || 1122;
    const gutter = window.matchMedia('(max-width: 900px)').matches ? 24 : 48;
    const available = Math.max(200, scroll.clientWidth - gutter);
    const fitScale = Math.min(1, Math.max(0.24, available / pageWidth));
    const scale = fitScale * zoom;

    // Always scale from the top-left corner. The wrapper reserves exactly the
    // scaled page size as layout space and is centred with auto margins, so a
    // centre origin would shift the 794px child sideways out of its own box.
    w.style.transform = `scale(${scale})`;
    w.style.transformOrigin = 'top left';
    w.style.width = `${Math.round(pageWidth * scale)}px`;
    w.style.height = `${Math.round(pageHeight * scale)}px`;
  }
  const lbl = document.getElementById('zoom-level');
  if (lbl) lbl.textContent = Math.round(zoom * 100) + '%';
}

// ============================================================
// ---- DYNAMIC ENTRIES ----
// ============================================================

function renderAllDynamic() {
  renderList('experience', renderExperienceForm, state.experience);
  renderList('education', renderEducationForm, state.education);
  renderList('skills', renderSkillForm, state.skills);
  renderList('languages', renderLanguageForm, state.languages);
  renderList('projects', renderProjectForm, state.projects);
  renderList('certifications', renderCertificationForm, state.certifications);
}

function renderList(type, renderer, list) {
  const container = document.getElementById(`${type}-list`);
  if (!container) return;
  container.innerHTML = '';
  list.forEach((item, i) => {
    container.appendChild(renderer(item, i));
  });
}

function makeEntry(title, subtitle, content, removeCallback, type, index) {
  const card = document.createElement('div');
  card.className = 'entry-card collapsed';
  card.setAttribute('draggable', 'true');

  const render = () => {
    if (card.classList.contains('collapsed')) {
      card.innerHTML = `
        <div class="entry-summary">
          <div class="entry-summary-text">
            <div class="entry-summary-title">${esc(title) || 'Untitled'}</div>
            <div class="entry-summary-subtitle">${esc(subtitle) || 'Click to edit'}</div>
          </div>
          <button class="btn-edit-entry">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/></svg>
          </button>
        </div>
      `;
      card.onclick = () => { card.classList.remove('collapsed'); card.classList.add('expanded'); render(); };
    } else {
      card.innerHTML = '';
      card.onclick = null;
      const form = document.createElement('div');
      form.className = 'entry-form';
      form.appendChild(content);

      const footer = document.createElement('div');
      footer.className = 'entry-footer';
      
      const btnDel = document.createElement('button');
      btnDel.className = 'btn-delete-card';
      btnDel.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><line x1="10" y1="11" x2="10" y2="17"/><line x1="14" y1="11" x2="14" y2="17"/></svg>';
      btnDel.onclick = (e) => { e.stopPropagation(); removeCallback(); };

      const btnDone = document.createElement('button');
      btnDone.className = 'btn-done';
      btnDone.innerHTML = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Done';
      btnDone.onclick = (e) => { 
        e.stopPropagation(); 
        card.classList.remove('expanded'); 
        card.classList.add('collapsed'); 
        renderAllDynamic();
      };

      footer.appendChild(btnDel);
      footer.appendChild(btnDone);
      form.appendChild(footer);
      card.appendChild(form);
    }
  };

  render();

  // Drag Events
  card.addEventListener('dragstart', (e) => {
    draggedItem = card;
    draggedType = type;
    draggedIndex = index;
    card.classList.add('dragging');
    e.dataTransfer.effectAllowed = 'move';
    setTimeout(() => card.style.opacity = '0.4', 0);
  });
  card.addEventListener('dragend', () => { card.style.opacity = '1'; card.classList.remove('dragging'); document.querySelectorAll('.entry-card').forEach(c => c.classList.remove('drag-over')); });
  card.addEventListener('dragover', (e) => { e.preventDefault(); if (draggedType !== type) return; card.classList.add('drag-over'); e.dataTransfer.dropEffect = 'move'; });
  card.addEventListener('dragleave', () => { card.classList.remove('drag-over'); });
  card.addEventListener('drop', (e) => {
    e.preventDefault();
    card.classList.remove('drag-over');
    if (draggedType !== type || draggedIndex === index) return;
    const list = state[type];
    const itemToMove = list.splice(draggedIndex, 1)[0];
    list.splice(index, 0, itemToMove);
    renderAllDynamic();
    renderPreview();
    saveToStorage();
  });

  return card;
}

function makeInput(label, val, onInput, placeholder = '') {
  const g = document.createElement('div');
  g.className = 'form-group';
  g.innerHTML = `<label>${label}</label><input type="text" value="${esc(val)}" placeholder="${placeholder}" />`;
  g.querySelector('input').addEventListener('input', e => onInput(e.target.value));
  return g;
}
function makeDateDropdowns(label, value, onInput, includePresent = false) {
  const g = document.createElement('div');
  g.className = 'form-group';

  const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const years = [];
  const currYear = new Date().getFullYear();
  for (let y = currYear + 10; y >= 1950; y--) years.push(y);

  let mVal = '', yVal = '', isPresent = (value === 'Present');
  if (!isPresent && value) {
    const pts = String(value).split(' ');
    if (pts.length === 2) { mVal = pts[0]; yVal = pts[1]; }
    else if (pts.length === 1 && !isNaN(pts[0])) { yVal = pts[0]; }
  }

  const update = () => {
    if (includePresent && isPresent) onInput('Present');
    else if (mVal && yVal) onInput(`${mVal} ${yVal}`);
    else if (yVal) onInput(yVal);
    else onInput('');
  };

  g.innerHTML = `
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
      <label style="margin:0;">${label}</label>
      ${includePresent ? `
        <div class="present-toggle">
          <label class="switch">
            <input type="checkbox" ${isPresent ? 'checked' : ''} />
            <span class="slider"></span>
          </label>
          <span>Present</span>
        </div>
      ` : ''}
    </div>
    <div class="date-select-row">
      <select class="m-select"><option value="">Month</option>${months.map(m => `<option value="${m}" ${m === mVal ? 'selected' : ''}>${m}</option>`).join('')}</select>
      <select class="y-select"><option value="">Year</option>${years.map(y => `<option value="${y}" ${String(y) === String(yVal) ? 'selected' : ''}>${y}</option>`).join('')}</select>
    </div>
  `;

  const mSel = g.querySelector('.m-select');
  const ySel = g.querySelector('.y-select');
  
  const setDisabled = (dis) => {
    mSel.disabled = ySel.disabled = dis;
    mSel.style.opacity = ySel.style.opacity = dis ? '0.5' : '1';
  };
  setDisabled(isPresent);

  mSel.onchange = e => { mVal = e.target.value; update(); };
  ySel.onchange = e => { yVal = e.target.value; update(); };

  if (includePresent) {
    g.querySelector('input').onchange = e => {
      isPresent = e.target.checked;
      setDisabled(isPresent);
      if (isPresent) { mSel.value = ''; ySel.value = ''; mVal = ''; yVal = ''; }
      update();
    };
  }

  return g;
}

function makeRichText(label, val, onInput, placeholder = '') {
  const g = document.createElement('div');
  g.className = 'form-group';
  g.innerHTML = `
    <label>${label}</label>
    <div class="rt-toolbar">
      <button class="rt-btn" title="Bold"><b>B</b></button>
      <button class="rt-btn" title="Italic" style="font-style:italic">I</button>
      <button class="rt-btn" title="Underline" style="text-decoration:underline">U</button>
      <div class="rt-divider"></div>
      <button class="rt-btn" title="Link">🔗</button>
      <div class="rt-divider"></div>
      <button class="rt-btn" title="Bulleted List">⁝≡</button>
      <button class="rt-btn" title="Numbered List">1≡</button>
      <div class="rt-divider"></div>
      <button class="rt-btn" title="Align Left">≡</button>
      <button class="rt-btn" title="Align Center">⌄</button>
      <button class="rt-btn btn-ai-spark">✨ AI Suggestions</button>
    </div>
    <textarea class="rt-area" rows="4" placeholder="${placeholder}">${esc(val)}</textarea>
  `;
  g.querySelector('textarea').addEventListener('input', e => onInput(e.target.value));
  return g;
}
function makeTextarea(label, val, onInput, placeholder = '', rows = 3) {
  const g = document.createElement('div');
  g.className = 'form-group';
  g.innerHTML = `<label>${label}</label><textarea rows="${rows}" placeholder="${placeholder}">${esc(val)}</textarea>`;
  g.querySelector('textarea').addEventListener('input', e => onInput(e.target.value));
  return g;
}
function makeRow(...children) {
  const row = document.createElement('div');
  row.className = 'form-row';
  children.forEach(c => row.appendChild(c));
  return row;
}
function makeSelect(label, val, options, onInput) {
  const g = document.createElement('div');
  g.className = 'form-group';
  const sel = document.createElement('select');
  options.forEach(o => { const opt = document.createElement('option'); opt.value = o; opt.textContent = o; if (o === val) opt.selected = true; sel.appendChild(opt); });
  sel.addEventListener('change', e => onInput(e.target.value));
  g.innerHTML = `<label>${label}</label>`;
  g.appendChild(sel);
  return g;
}

// --- Experience ---
function addExperience() {
  state.experience.push({ company: '', position: '', location: '', startDate: '', endDate: '', current: false, description: '' });
  renderListClean('experience', buildExperienceCard, state.experience);
  renderPreview(); saveToStorage();
}
function removeExperience(i) {
  state.experience.splice(i, 1);
  renderListClean('experience', buildExperienceCard, state.experience);
  renderPreview(); saveToStorage();
}
function buildExperienceCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Position', item.position, v => { item.position = v; rp(); saveToStorage(); }, 'Job title'));
  wrap.appendChild(makeRow(
    makeInput('Employer', item.company, v => { item.company = v; rp(); saveToStorage(); }, 'Company name'),
    makeInput('City', item.location || '', v => { item.location = v; rp(); saveToStorage(); }, 'City, Country')
  ));
  wrap.appendChild(makeRow(
    makeDateDropdowns('Start date', item.startDate, v => { item.startDate = v; rp(); saveToStorage(); }),
    makeDateDropdowns('End date', item.endDate, v => { item.endDate = v; rp(); saveToStorage(); }, true)
  ));
  wrap.appendChild(makeRichText('Description', item.description, v => { item.description = v; rp(); saveToStorage(); }, 'Start typing here...'));
  
  const title = item.position || 'Job Title';
  const sub = [item.company, item.location].filter(Boolean).join(', ') || 'Employer, City';
  return makeEntry(title, sub, wrap, () => removeExperience(i), 'experience', i);
}

// --- Education ---
function addEducation() {
  state.education.push({ institution: '', degree: '', field: '', location: '', startDate: '', endDate: '', description: '' });
  renderListClean('education', buildEducationCard, state.education);
  renderPreview(); saveToStorage();
}
function removeEducation(i) {
  state.education.splice(i, 1);
  renderListClean('education', buildEducationCard, state.education);
  renderPreview(); saveToStorage();
}
function buildEducationCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Education', item.degree, v => { item.degree = v; rp(); saveToStorage(); }, 'Degree / Field of study'));
  wrap.appendChild(makeRow(
    makeInput('School', item.institution, v => { item.institution = v; rp(); saveToStorage(); }, 'University name'),
    makeInput('City', item.location || '', v => { item.location = v; rp(); saveToStorage(); }, 'City, Country')
  ));
  wrap.appendChild(makeRow(
    makeDateDropdowns('Start date', item.startDate, v => { item.startDate = v; rp(); saveToStorage(); }),
    makeDateDropdowns('End date', item.endDate, v => { item.endDate = v; rp(); saveToStorage(); }, true)
  ));
  wrap.appendChild(makeRichText('Description', item.description, v => { item.description = v; rp(); saveToStorage(); }, 'Start typing here...'));
  
  const title = item.degree || 'Degree';
  const sub = [item.institution, item.location].filter(Boolean).join(', ') || 'School, City';
  return makeEntry(title, sub, wrap, () => removeEducation(i), 'education', i);
}

// --- Skills ---
function addSkill() {
  state.skills.push({ name: '', level: 'Proficient' });
  renderListClean('skills', buildSkillCard, state.skills);
  renderPreview(); saveToStorage();
}
function removeSkill(i) {
  state.skills.splice(i, 1);
  renderListClean('skills', buildSkillCard, state.skills);
  renderPreview(); saveToStorage();
}
function buildSkillCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeRow(
    makeInput('Skill', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'JavaScript'),
    makeSelect('Level', item.level, ['Beginner', 'Elementary', 'Intermediate', 'Advanced', 'Expert', 'Proficient'], v => { item.level = v; rp(); saveToStorage(); })
  ));
  return makeEntry(item.name || 'Skill', item.level || 'Level', wrap, () => removeSkill(i), 'skills', i);
}

// --- Languages ---
function addLanguage() {
  state.languages.push({ name: '', proficiency: 'Fluent' });
  renderListClean('languages', buildLanguageCard, state.languages);
  renderPreview(); saveToStorage();
}
function removeLanguage(i) {
  state.languages.splice(i, 1);
  renderListClean('languages', buildLanguageCard, state.languages);
  renderPreview(); saveToStorage();
}
function buildLanguageCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeRow(
    makeInput('Language', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'English'),
    makeSelect('Proficiency', item.proficiency, ['Native', 'Fluent', 'Advanced', 'Intermediate', 'Beginner'], v => { item.proficiency = v; rp(); saveToStorage(); })
  ));
  return makeEntry(item.name || 'Language', item.proficiency || 'Proficiency', wrap, () => removeLanguage(i), 'languages', i);
}

// --- Projects ---
function addProject() {
  state.projects.push({ name: '', url: '', description: '', tech: '' });
  renderListClean('projects', buildProjectCard, state.projects);
  renderPreview(); saveToStorage();
}
function removeProject(i) {
  state.projects.splice(i, 1);
  renderListClean('projects', buildProjectCard, state.projects);
  renderPreview(); saveToStorage();
}
function buildProjectCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeRow(
    makeInput('Project Name', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'My App'),
    makeInput('URL / Link', item.url, v => { item.url = v; rp(); saveToStorage(); }, 'github.com/...')
  ));
  wrap.appendChild(makeInput('Technologies', item.tech, v => { item.tech = v; rp(); saveToStorage(); }, 'React, Node.js, PostgreSQL'));
  wrap.appendChild(makeRichText('Description', item.description, v => { item.description = v; rp(); saveToStorage(); }, 'What the project does...'));
  return makeEntry(item.name || 'Project Name', item.tech || 'Technologies', wrap, () => removeProject(i), 'projects', i);
}

// --- Certifications ---
function addCertification() {
  state.certifications.push({ name: '', issuer: '', date: '', url: '' });
  renderListClean('certifications', buildCertCard, state.certifications);
  renderPreview(); saveToStorage();
}
function removeCertification(i) {
  state.certifications.splice(i, 1);
  renderListClean('certifications', buildCertCard, state.certifications);
  renderPreview(); saveToStorage();
}
function buildCertCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeRow(
    makeInput('Certification', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'AWS Certified'),
    makeInput('Issuing Org', item.issuer, v => { item.issuer = v; rp(); saveToStorage(); }, 'Amazon')
  ));
  wrap.appendChild(makeRow(
    makeDateDropdowns('Date', item.date, v => { item.date = v; rp(); saveToStorage(); }),
    makeInput('URL', item.url, v => { item.url = v; rp(); saveToStorage(); }, 'credential link')
  ));
  return makeEntry(item.name || 'Certification', item.issuer || 'Issuing Org', wrap, () => removeCertification(i), 'certifications', i);
}

// Helper to render list directly with card builder
function renderListClean(type, builder, list) {
  const container = document.getElementById(`${type}-list`);
  if (!container) return;
  container.innerHTML = '';
  list.forEach((item, i) => container.appendChild(builder(item, i)));
}

// --- Internships ---
function addInternship() {
  state.internships.push({ company: '', position: '', location: '', startDate: '', endDate: '', description: '' });
  renderListClean('internships', buildInternshipCard, state.internships);
  rp(); saveToStorage();
}
function removeInternship(i) {
  state.internships.splice(i, 1);
  renderListClean('internships', buildInternshipCard, state.internships);
  rp(); saveToStorage();
}
function buildInternshipCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Position', item.position, v => { item.position = v; rp(); saveToStorage(); }, 'Intern title'));
  wrap.appendChild(makeRow(
    makeInput('Employer', item.company, v => { item.company = v; rp(); saveToStorage(); }, 'Company name'),
    makeInput('City', item.location || '', v => { item.location = v; rp(); saveToStorage(); }, 'City, Country')
  ));
  wrap.appendChild(makeRow(
    makeDateDropdowns('Start date', item.startDate, v => { item.startDate = v; rp(); saveToStorage(); }),
    makeDateDropdowns('End date', item.endDate, v => { item.endDate = v; rp(); saveToStorage(); }, true)
  ));
  wrap.appendChild(makeRichText('Description', item.description, v => { item.description = v; rp(); saveToStorage(); }, 'What you did...'));
  return makeEntry(item.position || 'Internship', item.company || 'Company', wrap, () => removeInternship(i), 'internships', i);
}

// --- Activities ---
function addActivity() {
  state.activities.push({ name: '', organization: '', date: '', description: '' });
  renderListClean('activities', buildActivityCard, state.activities);
  rp(); saveToStorage();
}
function removeActivity(i) {
  state.activities.splice(i, 1);
  renderListClean('activities', buildActivityCard, state.activities);
  rp(); saveToStorage();
}
function buildActivityCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Activity Name', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'Volunteer, Member...'));
  wrap.appendChild(makeInput('Organization', item.organization, v => { item.organization = v; rp(); saveToStorage(); }, 'Club, Non-profit...'));
  wrap.appendChild(makeDateDropdowns('Date', item.date, v => { item.date = v; rp(); saveToStorage(); }));
  wrap.appendChild(makeRichText('Description', item.description, v => { item.description = v; rp(); saveToStorage(); }, 'Details...'));
  return makeEntry(item.name || 'Activity', item.organization || 'Organization', wrap, () => removeActivity(i), 'activities', i);
}

// --- Courses ---
function addCourse() {
  state.courses.push({ name: '', institution: '', date: '' });
  renderListClean('courses', buildCourseCard, state.courses);
  rp(); saveToStorage();
}
function removeCourse(i) {
  state.courses.splice(i, 1);
  renderListClean('courses', buildCourseCard, state.courses);
  rp(); saveToStorage();
}
function buildCourseCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Course Name', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'Computer Science 101'));
  wrap.appendChild(makeInput('Institution', item.institution, v => { item.institution = v; rp(); saveToStorage(); }, 'Coursera, University...'));
  wrap.appendChild(makeDateDropdowns('Date', item.date, v => { item.date = v; rp(); saveToStorage(); }));
  return makeEntry(item.name || 'Course', item.institution || 'Institution', wrap, () => removeCourse(i), 'courses', i);
}

// --- References ---
function addReference() {
  state.references.push({ name: '', company: '', email: '', phone: '' });
  renderListClean('references', buildReferenceCard, state.references);
  rp(); saveToStorage();
}
function removeReference(i) {
  state.references.splice(i, 1);
  renderListClean('references', buildReferenceCard, state.references);
  rp(); saveToStorage();
}
function buildReferenceCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeRow(
    makeInput('Full Name', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'John Smith'),
    makeInput('Company', item.company, v => { item.company = v; rp(); saveToStorage(); }, 'Company X')
  ));
  wrap.appendChild(makeRow(
    makeInput('Email', item.email, v => { item.email = v; rp(); saveToStorage(); }, 'john@example.com'),
    makeInput('Phone', item.phone, v => { item.phone = v; rp(); saveToStorage(); }, '+1 234...')
  ));
  return makeEntry(item.name || 'Reference', item.company || 'Company', wrap, () => removeReference(i), 'references', i);
}

// --- Qualities ---
function addQuality() {
  state.qualities.push({ name: '' });
  renderListClean('qualities', buildQualityCard, state.qualities);
  rp(); saveToStorage();
}
function removeQuality(i) {
  state.qualities.splice(i, 1);
  renderListClean('qualities', buildQualityCard, state.qualities);
  rp(); saveToStorage();
}
function buildQualityCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Quality', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'Problem Solver'));
  return makeEntry(item.name || 'Quality', '', wrap, () => removeQuality(i), 'qualities', i);
}

// --- Achievements ---
function addAchievement() {
  state.achievements.push({ name: '', description: '' });
  renderListClean('achievements', buildAchievementCard, state.achievements);
  rp(); saveToStorage();
}
function removeAchievement(i) {
  state.achievements.splice(i, 1);
  renderListClean('achievements', buildAchievementCard, state.achievements);
  rp(); saveToStorage();
}
function buildAchievementCard(item, i) {
  const wrap = document.createElement('div');
  wrap.appendChild(makeInput('Achievement', item.name, v => { item.name = v; rp(); saveToStorage(); }, 'Employee of the Month'));
  wrap.appendChild(makeTextarea('Description', item.description, v => { item.description = v; rp(); saveToStorage(); }, 'Short description...'));
  return makeEntry(item.name || 'Achievement', '', wrap, () => removeAchievement(i), 'achievements', i);
}

function toggleAddSectionPopover() {
  const popover = document.getElementById('add-section-popover');
  const btn = document.getElementById('add-section-toggle-btn');
  if (popover) {
    popover.classList.toggle('hidden');
    if (btn) {
      btn.querySelector('svg').style.transform = popover.classList.contains('hidden') ? 'rotate(0deg)' : 'rotate(180deg)';
    }
  }
}

// Section Toggling
function toggleVisibleSection(id) {
  const section = document.getElementById(`section-${id}`);
  const btn = document.querySelector(`.btn-popover-item[onclick="toggleVisibleSection('${id}')"]`);
  
  if (state.visibleSections.includes(id)) {
    state.visibleSections = state.visibleSections.filter(sid => sid !== id);
    if (section) section.classList.add('hidden');
    if (btn) btn.classList.remove('active');
  } else {
    state.visibleSections.push(id);
    if (section) section.classList.remove('hidden');
    if (btn) btn.classList.add('active');
    if (section) section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    
    // Close popover after adding
    setTimeout(() => {
      const popover = document.getElementById('add-section-popover');
      if (popover) popover.classList.add('hidden');
      const toggleBtn = document.getElementById('add-section-toggle-btn');
      if (toggleBtn) toggleBtn.querySelector('svg').style.transform = 'rotate(0deg)';
    }, 300);
  }
  renderPreview();
  saveToStorage();
}

// Override renderAllDynamic to use clean builders
function renderAllDynamic() {
  renderListClean('experience', buildExperienceCard, state.experience);
  renderListClean('education', buildEducationCard, state.education);
  renderListClean('skills', buildSkillCard, state.skills);
  renderListClean('languages', buildLanguageCard, state.languages);
  renderListClean('projects', buildProjectCard, state.projects);
  renderListClean('certifications', buildCertCard, state.certifications);
  
  // New sections
  renderListClean('internships', buildInternshipCard, state.internships);
  renderListClean('activities', buildActivityCard, state.activities);
  renderListClean('courses', buildCourseCard, state.courses);
  renderListClean('references', buildReferenceCard, state.references);
  renderListClean('qualities', buildQualityCard, state.qualities);
  renderListClean('achievements', buildAchievementCard, state.achievements);

  // Simple text fields
  const hobbiesEl = document.getElementById('hobbies');
  if (hobbiesEl) hobbiesEl.value = state.hobbies || '';
  
  const footerEl = document.getElementById('footer');
  if (footerEl) footerEl.value = state.footer || '';

  const sigTextEl = document.getElementById('signatureText');
  if (sigTextEl) sigTextEl.value = state.signature.text || '';

  const customTitleEl = document.getElementById('customTitle');
  if (customTitleEl) customTitleEl.value = state.custom.title || '';

  const customContentEl = document.getElementById('customContent');
  if (customContentEl) customContentEl.value = state.custom.content || '';

  // Update visible sections buttons and sidebar
  updateSectionVisibilityUI();
}

function updateSectionVisibilityUI() {
  defaultState.sectionOrder.forEach(id => {
    const section = document.getElementById(`section-${id}`);
    if (section) section.classList.toggle('hidden', !state.visibleSections.includes(id));
    const btn = document.querySelector(`.btn-popover-item[onclick="toggleVisibleSection('${id}')"]`);
    if (btn) btn.classList.toggle('active', state.visibleSections.includes(id));
  });
}

// shorthand
function rp() { renderPreview(); }

// ============================================================
// ---- RESUME PREVIEW RENDERER ----
// ============================================================

function renderPreview() {
  const preview = document.getElementById('resume-preview');
  if (!preview) return;
  const tmpl = state.template;
  const accent = effectiveAccent(tmpl);
  const accentLight = hexToRgba(accent, 0.12);
  preview.style.setProperty('--resume-accent', accent);
  preview.style.setProperty('--resume-accent-light', accentLight);
  syncAccentInputs();

  const html = buildTemplateHtml(tmpl);

  preview.className = `resume-page ${templateRootClass(tmpl)}`;
  preview.innerHTML = html;
  preview.style.setProperty('--resume-accent', accent);
  preview.style.setProperty('--resume-accent-light', accentLight);
  requestAnimationFrame(() => {
    paginateResume(preview);
    applyZoom();
  });
  if (document.fonts?.ready) {
    document.fonts.ready.then(() => {
      paginateResume(preview);
      applyZoom();
    });
  }
}

function paginateResume(root, options = {}) {
  if (!root) return;
  const pageHeight = options.pageHeight || 1122;
  const pageGap = options.gap ?? 14;
  const bottomGuard = options.bottomGuard || 24;
  const rootStyle = getComputedStyle(root);
  const rootTopPadding = parseFloat(rootStyle.paddingTop) || 0;
  const pagePitch = pageHeight + pageGap;
  const selector = [
    '.r-section',
    '.prof-section',
    '.cv-keep'
  ].join(',');

  root.querySelectorAll('.resume-page-spacer').forEach(el => el.remove());
  root.querySelectorAll('.resume-page-gap-visual').forEach(el => el.remove());
  root.querySelectorAll('.resume-page-break-before').forEach(el => el.classList.remove('resume-page-break-before'));
  root.style.removeProperty('min-height');

  const getTop = (el) => el.getBoundingClientRect().top - root.getBoundingClientRect().top;
  const candidates = Array.from(root.querySelectorAll(selector))
    // We now ALLOW sidebar elements to be paginated, so they break correctly!
    .filter(el => el.offsetParent !== null && el.offsetHeight > 0)
    .sort((a, b) => {
      const aTop = getTop(a);
      const bTop = getTop(b);
      return aTop - bTop;
    });

  const visualGapsAdded = new Set();

  candidates.forEach(el => {
    // The first entry of a cv section moves together with the section heading,
    // so a heading is never left alone at the foot of a page.
    let target = el;
    if (el.classList.contains('cv-item') && !el.previousElementSibling) {
      target = el.closest('.cv-sec') || el;
    }
    const top = getTop(target);
    const bottom = getTop(el) + el.getBoundingClientRect().height;
    const height = bottom - top;
    if (height >= pageHeight - 120) return;

    const pageStart = Math.floor(top / pagePitch) * pagePitch;
    const pageEnd = pageStart + pageHeight;
    if (top > pageStart + bottomGuard && bottom > pageEnd - bottomGuard) {
      const parentTopPadding = parseFloat(getComputedStyle(target.parentElement).paddingTop) || 0;
      const nextPageTopPadding = Math.max(rootTopPadding, parentTopPadding, 34);
      const remainingPageSpace = Math.max(0, pageEnd - top);
      const spacerHeight = remainingPageSpace + pageGap + nextPageTopPadding;
      
      // 1. Physical spacer (pushes content inside the specific template column)
      const spacer = document.createElement('div');
      spacer.className = 'resume-page-spacer';
      spacer.style.height = `${Math.ceil(spacerHeight)}px`;
      target.classList.add('resume-page-break-before');
      target.parentNode.insertBefore(spacer, target);
      
      // 2. Visual gap overlay (attached to root to span the entire paper width)
      // We only want ONE visual gap per physical page boundary to avoid dark overlapping shadows.
      if (!visualGapsAdded.has(pageEnd)) {
        visualGapsAdded.add(pageEnd);
        const visualGap = document.createElement('div');
        visualGap.className = 'resume-page-gap-visual';
        visualGap.style.setProperty('--resume-page-gap', `${pageGap}px`);
        visualGap.style.setProperty('--resume-page-remainder', `${Math.ceil(remainingPageSpace)}px`);
        visualGap.style.setProperty('--spacer-y', `${Math.ceil(top)}px`);
        visualGap.style.height = `${Math.ceil(spacerHeight)}px`;
        root.appendChild(visualGap);
      }
    }
  });

  // Sub-pixel layout rounding routinely leaves a few stray pixels past the page
  // edge. Counting those as a new page produced an entirely blank trailing sheet
  // in the preview and in the exported PDF, so ignore anything under the guard.
  // Engine templates measure where the content ends instead: a sidebar's bottom
  // padding alone could otherwise push scrollHeight past the page and add an
  // empty sheet. Professional keeps the scrollHeight rule it was tuned against.
  const totalHeight = root.classList.contains('cv2')
    ? Math.max(cvContentBottom(root), pageHeight)
    : Math.max(root.scrollHeight, pageHeight);
  const pageCount = Math.max(1, Math.ceil((totalHeight - bottomGuard) / pagePitch));
  root.style.minHeight = `${(pageCount * pageHeight) + ((pageCount - 1) * pageGap)}px`;
}

function cvContentBottom(root) {
  const top = root.getBoundingClientRect().top;
  let bottom = 0;
  root.querySelectorAll('.cv-head, .cv-photo, .cv-sec, .cv-signature, .cv-footer').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.height) bottom = Math.max(bottom, r.bottom - top);
  });
  return Math.ceil(bottom);
}

function buildTemplateHtml(tmpl) {
  if (tmpl === 'professional') return buildProfessional();
  return buildCvTemplate(CV_TEMPLATES[tmpl] ? tmpl : 'classic');
}

// The page element's class. Professional keeps its original markup and CSS; every
// other template is drawn by the cv engine below and styled under .cv2, so none of
// the older .tmpl-* rules can reach it.
function templateRootClass(tmpl) {
  if (tmpl === 'professional') return 'tmpl-professional';
  return `cv2 cv-${CV_TEMPLATES[tmpl] ? tmpl : 'classic'}`;
}

// Each template has its own signature colour. It is used until the person picks
// a colour themselves, after which their choice applies to every template.
function effectiveAccent(tmpl) {
  if (tmpl === 'professional' || state.accentCustom) return state.accentColor || '#2563eb';
  return CV_TEMPLATES[tmpl]?.accent || state.accentColor || '#2563eb';
}

function accentStyle(tmpl) {
  const accent = effectiveAccent(tmpl);
  return `--resume-accent:${accent};--resume-accent-light:${hexToRgba(accent, 0.12)};`;
}

// ============================================================
// ---- Template engine (every template except Professional) ----
// ============================================================
// A template is a config: where the sidebar sits and what goes in it, how the
// header is arranged, and how dates, skills and languages are drawn. The markup is
// shared and uses only cv-* classes; each template's look is its .cv-<id> block at
// the end of styles.css.
//
//   layout   single | left | right | split (full-width header, side column right)
//   head     top (full width) | main (top of main column) | side (top of sidebar)
//   contact  header | side            contactStyle  icons | plain | labels
//   dates    right | left | above | inline
//   skills / langs / quals            chips | bars | dots | list | grid | inline
//   side     section ids that go in the sidebar
//   first    section ids pulled to the front of the main column
//   orgFirst company line above the role (Harvard / consulting convention)
//   decor    static markup placed first inside the page (terminal window bar)

const CV_SIDE = ['skills', 'languages', 'qualities', 'hobbies', 'certifications', 'courses', 'references'];

const CV_TEMPLATES = {
  'classic':           { accent: '#1f4e79', layout: 'single', skills: 'grid', langs: 'list', quals: 'inline' },
  'modern':            { accent: '#0f766e', layout: 'left', head: 'main', contact: 'side', photoIn: 'side', skills: 'bars', langs: 'dots', quals: 'list' },
  'creative':          { accent: '#f2545b', layout: 'split', skills: 'chips', langs: 'bars', side: ['skills', 'languages', 'qualities', 'hobbies', 'certifications', 'courses'] },
  'minimal':           { accent: '#111111', layout: 'single', photo: false, contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'executive':         { accent: '#8a6d3b', layout: 'split', contactStyle: 'plain', skills: 'list', langs: 'list', quals: 'list' },
  'tech':              { accent: '#0891b2', layout: 'split', first: ['projects'], skills: 'chips', langs: 'list' },
  'software-engineer': { accent: '#4f46e5', layout: 'left', head: 'side', contact: 'side', photoIn: 'side', skills: 'bars', langs: 'list', side: ['skills', 'certifications', 'languages', 'courses', 'qualities', 'hobbies'] },
  'qa-engineer':       { accent: '#15803d', layout: 'split', dates: 'above', skills: 'grid', langs: 'dots', quals: 'grid' },
  'elegant':           { accent: '#8c6d62', layout: 'single', contactStyle: 'plain', dates: 'left', skills: 'inline', langs: 'inline', quals: 'inline' },
  'bold':              { accent: '#f59e0b', layout: 'split', solidIcons: true, skills: 'chips', langs: 'bars' },
  'startup':           { accent: '#7c3aed', layout: 'split', first: ['projects'], dates: 'above', skills: 'chips', langs: 'list' },
  'corporate':         { accent: '#1e3a5f', layout: 'single', contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'modern-dark':       { accent: '#10b981', layout: 'left', head: 'top', solidIcons: true, skills: 'dots', langs: 'dots', quals: 'list' },
  'classic-blue':      { accent: '#1d4ed8', layout: 'single', skills: 'grid', langs: 'list', quals: 'inline' },
  'minimal-formal':    { accent: '#334155', layout: 'single', contactStyle: 'plain', dates: 'left', skills: 'grid', langs: 'list', quals: 'inline' },
  'traditional-serif': { accent: '#6b1d2a', layout: 'single', contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'europass':          { accent: '#0e4194', layout: 'single', contactStyle: 'labels', dates: 'left', kicker: 'Curriculum Vitae', skills: 'grid', langs: 'list', quals: 'inline',
                         titles: { summary: 'About Myself', experience: 'Work Experience', education: 'Education and Training', languages: 'Language Skills', skills: 'Digital and Job-related Skills' } },
  'modern-right':      { accent: '#0284c7', layout: 'right', head: 'main', contact: 'side', photoIn: 'side', skills: 'bars', langs: 'dots', quals: 'list' },
  'nordic':            { accent: '#5b7553', layout: 'split', skills: 'list', langs: 'list', quals: 'list' },
  'timeline':          { accent: '#c026d3', layout: 'single', dates: 'left', skills: 'chips', langs: 'inline', quals: 'inline' },
  'mono':              { accent: '#9a3412', layout: 'single', contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'compact':           { accent: '#155e75', layout: 'single', contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'portfolio':         { accent: '#fca311', layout: 'left', head: 'side', contact: 'side', photoIn: 'side', first: ['projects'], skills: 'chips', langs: 'bars', quals: 'list' },
  'graduate':          { accent: '#14532d', layout: 'single', photo: false, contactStyle: 'plain', first: ['education', 'courses'], skills: 'grid', langs: 'inline', quals: 'inline' },
  'student':           { accent: '#6366f1', layout: 'single', first: ['education', 'courses', 'projects'], skills: 'chips', langs: 'chips', quals: 'chips' },
  'freelancer':        { accent: '#c2410c', layout: 'right', head: 'main', contact: 'side', photoIn: 'side', kicker: 'Available for projects', first: ['projects'], skills: 'list', langs: 'list', quals: 'list',
                         titles: { skills: 'Services', projects: 'Selected Work', summary: 'About' } },
  'clean-sidebar':     { accent: '#2563eb', layout: 'right', head: 'main', contact: 'side', photoIn: 'side', contactStyle: 'plain', skills: 'list', langs: 'list', quals: 'list' },
  'editorial':         { accent: '#b91c1c', layout: 'single', contactStyle: 'plain', kicker: 'Résumé', skills: 'inline', langs: 'inline', quals: 'inline' },
  'ats-friendly':      { accent: '#111111', layout: 'single', photo: false, contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'latex-style':       { accent: '#2e5c8a', layout: 'single', photo: false, contactStyle: 'plain', dates: 'left', skills: 'inline', langs: 'inline', quals: 'inline' },
  'harvard-style':     { accent: '#111111', layout: 'single', photo: false, contactStyle: 'plain', orgFirst: true, skills: 'inline', langs: 'inline', quals: 'inline' },
  'federal-style':     { accent: '#1e3a8a', layout: 'single', photo: false, contactStyle: 'labels', skills: 'grid', langs: 'list', quals: 'inline' },
  'functional':        { accent: '#0d9488', layout: 'single', first: ['skills', 'qualities', 'achievements'], skills: 'grid', langs: 'inline', quals: 'chips',
                         titles: { skills: 'Core Competencies', experience: 'Employment History' } },
  'chronological':     { accent: '#be123c', layout: 'single', dates: 'left', skills: 'chips', langs: 'inline', quals: 'inline' },
  'consulting-style':  { accent: '#7f1d1d', layout: 'single', photo: false, contactStyle: 'plain', orgFirst: true, skills: 'inline', langs: 'inline', quals: 'inline' },
  'academic-cv':       { accent: '#1e3a8a', layout: 'single', photo: false, contactStyle: 'plain', dates: 'left', skills: 'inline', langs: 'inline', quals: 'inline' },
  'infographic':       { accent: '#f97316', layout: 'left', head: 'main', contact: 'side', photoIn: 'side', numbered: true, skills: 'dots', langs: 'bars', quals: 'chips' },
  'modern-executive':  { accent: '#0f3d3e', layout: 'split', contactStyle: 'plain', skills: 'list', langs: 'list', quals: 'list' },
  'elite':             { accent: '#c9a227', layout: 'left', head: 'top', contact: 'side', photoIn: 'side', skills: 'dots', langs: 'list', quals: 'list' },
  'aurora':            { accent: '#8b5cf6', layout: 'split', skills: 'chips', langs: 'bars', quals: 'chips', side: ['skills', 'languages', 'qualities', 'hobbies', 'courses', 'references'] },
  'swiss':             { accent: '#e30613', layout: 'single', photo: false, contactStyle: 'plain', numbered: true, skills: 'grid', langs: 'list', quals: 'inline' },
  'brutalist':         { accent: '#ff5c00', layout: 'single', skills: 'chips', langs: 'chips', quals: 'chips' },
  'vogue':             { accent: '#be185d', layout: 'split', contactStyle: 'plain', kicker: 'Curriculum Vitae', dropcap: true, skills: 'inline', langs: 'list', quals: 'inline' },
  'luxe':              { accent: '#b08d4f', layout: 'single', contactStyle: 'plain', dates: 'above', skills: 'inline', langs: 'inline', quals: 'inline' },
  'impact':            { accent: '#dc2626', layout: 'split', skills: 'bars', langs: 'list', quals: 'chips' },
  'atelier':           { accent: '#4d7c0f', layout: 'single', contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'spectrum':          { accent: '#db2777', layout: 'split', skills: 'chips', langs: 'dots', quals: 'chips' },
  'metro':             { accent: '#0ea5e9', layout: 'split', skills: 'bars', langs: 'list', quals: 'chips' },
  'terminal':          { accent: '#22c55e', layout: 'split', contactStyle: 'plain', decor: '<div class="cv-window"><i></i><i></i><i></i></div>', skills: 'chips', langs: 'list', quals: 'chips' },

  // ---- 2026 trend set ----
  'bento':             { accent: '#6366f1', layout: 'split', skills: 'chips', langs: 'dots', quals: 'chips', side: ['skills', 'languages', 'qualities', 'hobbies', 'certifications', 'courses'] },
  'glass':             { accent: '#22d3ee', layout: 'split', skills: 'chips', langs: 'bars', quals: 'chips' },
  'notion':            { accent: '#0f7b6c', layout: 'single', skills: 'chips', langs: 'chips', quals: 'chips' },
  'docs-style':        { accent: '#e8615a', layout: 'single', photo: false, contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'simple':            { accent: '#2563eb', layout: 'single', photo: false, contactStyle: 'plain', skills: 'inline', langs: 'inline', quals: 'inline' },
  'pastel':            { accent: '#ec4899', layout: 'split', skills: 'chips', langs: 'dots', quals: 'chips' },
  'midnight':          { accent: '#a78bfa', layout: 'left', head: 'main', contact: 'side', photoIn: 'side', skills: 'bars', langs: 'dots', quals: 'chips' },
  'retro':             { accent: '#d9480f', layout: 'split', skills: 'chips', langs: 'list', quals: 'chips' },
  'gradient':          { accent: '#ec4899', layout: 'left', head: 'side', contact: 'side', photoIn: 'side', skills: 'bars', langs: 'list', quals: 'chips' },
  'two-column':        { accent: '#0f766e', layout: 'split', skills: 'list', langs: 'dots', quals: 'list' },
  'bauhaus':           { accent: '#d62828', layout: 'split', decor: '<div class="cv-geo"><i></i><i></i><i></i><i></i><i></i><i></i></div>', skills: 'chips', langs: 'list', quals: 'chips' },
  'zen':               { accent: '#c0392b', layout: 'single', contactStyle: 'plain', dates: 'left', skills: 'inline', langs: 'inline', quals: 'inline' },
  'gazette':           { accent: '#8b0000', layout: 'split', photoIn: 'side', contactStyle: 'plain', kicker: 'The Professional Record', dropcap: true, skills: 'list', langs: 'list', quals: 'list' },
  'blueprint':         { accent: '#0b5ed7', layout: 'split', numbered: true, skills: 'bars', langs: 'list', quals: 'chips' },
  'profile':           { accent: '#0a66c2', layout: 'split', skills: 'chips', langs: 'list', quals: 'chips', titles: { summary: 'About' } },

  // ---- Job-specific set: section names and order follow each field's conventions ----
  'nurse':             { accent: '#0e7490', layout: 'left', head: 'main', contact: 'side', photoIn: 'side', skills: 'list', langs: 'dots', quals: 'list',
                         side: ['skills', 'certifications', 'languages', 'qualities', 'courses', 'hobbies', 'references'],
                         titles: { experience: 'Clinical Experience', certifications: 'Licenses & Certifications', skills: 'Clinical Skills' } },
  'teacher':           { accent: '#f59e0b', layout: 'split', skills: 'chips', langs: 'list', quals: 'chips',
                         titles: { summary: 'Teaching Profile', experience: 'Teaching Experience', skills: 'Classroom Skills', certifications: 'Certification & Licensure' } },
  'sales':             { accent: '#16a34a', layout: 'single', first: ['summary', 'achievements'], skills: 'chips', langs: 'inline', quals: 'chips',
                         titles: { achievements: 'Key Wins', experience: 'Sales Experience', skills: 'Sales Skills' } },
  'marketing':         { accent: '#e11d48', layout: 'right', head: 'main', contact: 'side', photoIn: 'side', first: ['summary', 'projects'], skills: 'bars', langs: 'list', quals: 'chips',
                         titles: { projects: 'Campaigns', skills: 'Marketing Skills' } },
  'data-analyst':      { accent: '#2563eb', layout: 'left', head: 'main', contact: 'side', photoIn: 'side', first: ['summary', 'projects'], skills: 'bars', langs: 'list', quals: 'list',
                         titles: { projects: 'Analytics Projects', skills: 'Tools & Methods' } },
  'product-manager':   { accent: '#7c3aed', layout: 'split', first: ['summary', 'achievements'], skills: 'chips', langs: 'list', quals: 'chips',
                         titles: { achievements: 'Product Impact', projects: 'Launches' } },
  'accountant':        { accent: '#065f46', layout: 'single', contactStyle: 'plain', dates: 'left', skills: 'grid', langs: 'inline', quals: 'inline',
                         titles: { experience: 'Professional Experience', certifications: 'Certifications & Licences' } },
  'customer-service':  { accent: '#f97316', layout: 'left', head: 'main', contact: 'side', photoIn: 'side', skills: 'list', langs: 'dots', quals: 'chips',
                         titles: { skills: 'Service Skills', qualities: 'Soft Skills' } },
  'project-manager':   { accent: '#1d4ed8', layout: 'split', dates: 'above', skills: 'list', langs: 'list', quals: 'chips',
                         side: ['skills', 'certifications', 'languages', 'qualities', 'courses', 'hobbies', 'references'],
                         titles: { experience: 'Project Leadership', skills: 'Core Competencies' } },
  'ux-designer':       { accent: '#ff4f81', layout: 'single', first: ['summary', 'projects'], kicker: 'Frame 01 — Résumé', skills: 'chips', langs: 'inline', quals: 'chips',
                         titles: { projects: 'Case Studies' } },
  'engineering':       { accent: '#eab308', layout: 'left', head: 'top', skills: 'list', langs: 'list', quals: 'list',
                         titles: { skills: 'Technical Skills', projects: 'Engineering Projects' } },
  'legal':             { accent: '#a16207', layout: 'single', photo: false, contactStyle: 'plain', orgFirst: true, skills: 'inline', langs: 'inline', quals: 'inline',
                         titles: { experience: 'Legal Experience', education: 'Education & Admissions' } },
  'hospitality':       { accent: '#b45309', layout: 'right', head: 'top', skills: 'list', langs: 'dots', quals: 'list',
                         titles: { skills: 'Guest Service Skills' } },
  'entry-level':       { accent: '#10b981', layout: 'single', numbered: true, first: ['summary', 'education', 'internships', 'projects'], skills: 'chips', langs: 'chips', quals: 'chips',
                         titles: { summary: 'Profile' } },
  'admin-assistant':   { accent: '#4f46e5', layout: 'single', skills: 'grid', langs: 'list', quals: 'inline',
                         titles: { skills: 'Office & Software Skills' } }
};

// Thumbnail sample content for the job-specific templates, so a nurse sees a nurse's
// resume in the gallery rather than the product designer every other card shows.
// Only what differs from the shared sample is listed; see applyThumbnailState().
const CV_SAMPLES = {
  'nurse': {
    name: ['Amelia', 'Brooks'], title: 'Registered Nurse, ICU',
    summary: 'ICU nurse with six years of acute-care experience, trusted with ventilated patients and the preceptor for new graduates on a 32-bed unit.',
    exp: [['ICU Registered Nurse', "St. Mary's Hospital", 'Cared for 2–3 critical patients per shift; cut central-line infections to zero for 14 months.'],
          ['Staff Nurse, Med-Surg', 'City General Hospital', 'Led discharge teaching that lowered 30-day readmissions on the unit.']],
    edu: ['BSc Nursing', 'Boston College'],
    skills: [['Critical Care', 95], ['Patient Assessment', 90], ['IV Therapy', 85]],
    certs: [['Registered Nurse Licence', 'State Board of Nursing'], ['BLS & ACLS', 'American Heart Association']]
  },
  'teacher': {
    name: ['Daniel', 'Okafor'], title: 'Secondary English Teacher',
    summary: 'English teacher with eight years in mixed-ability classrooms; raised GCSE pass rates 18 points through structured feedback and reading programmes.',
    exp: [['English Teacher', 'Riverside High School', 'Teach five classes across Years 9–13; designed the department reading curriculum.'],
          ['Teaching Assistant', 'Oak Park Academy', 'Supported SEN learners and ran small-group literacy interventions.']],
    edu: ['PGCE Secondary English', 'University of Leeds'],
    skills: [['Curriculum Design', 90], ['Classroom Management', 92], ['Differentiation', 85]]
  },
  'sales': {
    name: ['Marcus', 'Reed'], title: 'Senior Account Executive',
    summary: 'B2B SaaS seller who builds pipeline as well as closing it. Five years over quota in mid-market and enterprise.',
    exp: [['Senior Account Executive', 'Northwind SaaS', 'Closed $3.4M new ARR in 2025 across 41 mid-market accounts.'],
          ['Sales Development Rep', 'Brightline', 'Booked 210 qualified meetings; promoted in 11 months.']],
    edu: ['BA Business', 'University of Texas'],
    skills: [['Pipeline Generation', 90], ['Negotiation', 88], ['Salesforce', 85]],
    achievements: [['142% of annual quota', 'Top performer of 28 AEs in 2025.'], ["President's Club ×2", 'Awarded in 2024 and 2025.']]
  },
  'marketing': {
    name: ['Sofia', 'Marin'], title: 'Growth Marketing Manager',
    summary: 'Full-funnel marketer who pairs brand instinct with experiment discipline. Grew paid acquisition 3× at a flat CAC.',
    exp: [['Growth Marketing Manager', 'Lumen Apps', 'Own a $1.2M paid budget across Meta, Google and TikTok.'],
          ['Marketing Specialist', 'Fable & Co', 'Launched lifecycle email that drove 22% of revenue.']],
    edu: ['BA Marketing', 'Bocconi University'],
    skills: [['Paid Social', 92], ['SEO & Content', 84], ['Analytics', 80]],
    projects: [['Spring Relaunch Campaign', 'Paid social, CRM', 'Integrated campaign that lifted trial sign-ups 41% in six weeks.']]
  },
  'data-analyst': {
    name: ['Priya', 'Nair'], title: 'Data Analyst',
    summary: 'Analyst who turns messy product data into decisions. SQL-first, comfortable owning a dashboard from query to stakeholder review.',
    exp: [['Data Analyst', 'Kite Commerce', 'Built the weekly revenue model used by finance and leadership.'],
          ['Junior Analyst', 'Metric Labs', 'Automated reporting, saving the team ten hours a week.']],
    edu: ['BSc Statistics', 'University of Toronto'],
    skills: [['SQL', 95], ['Python', 82], ['Tableau', 88]],
    projects: [['Churn Prediction Dashboard', 'SQL, Python, Tableau', 'Flagged at-risk accounts two months earlier, saving $400K ARR.']]
  },
  'product-manager': {
    name: ['Jonas', 'Weber'], title: 'Senior Product Manager',
    summary: 'Product manager for B2B platforms. Ships in small increments, measures everything, and writes the spec people actually read.',
    exp: [['Senior Product Manager', 'Atlas Cloud', 'Lead a 9-person squad on billing and onboarding.'],
          ['Product Manager', 'Shiftly', 'Launched mobile scheduling, now 60% of weekly active use.']],
    edu: ['MSc Computer Science', 'TU Munich'],
    skills: [['Discovery', 90], ['Roadmapping', 88], ['SQL & Analytics', 80]],
    achievements: [['+31% activation', 'Rebuilt onboarding around the first key action.'], ['$2.1M new ARR', 'From usage-based pricing launched in Q2.']]
  },
  'accountant': {
    name: ['Grace', 'Holloway'], title: 'Senior Accountant, CPA',
    summary: 'CPA with seven years in audit and corporate accounting. Closes the month in four days and leaves a clean audit trail behind.',
    exp: [['Senior Accountant', 'Harbor Logistics', 'Own the month-end close for three entities and $90M revenue.'],
          ['Audit Associate', 'Baker & Lowe LLP', 'Audited manufacturing and retail clients up to $250M revenue.']],
    edu: ['BSc Accounting', 'University of Illinois'],
    skills: [['GAAP & IFRS', 92], ['Month-End Close', 95], ['NetSuite', 85]],
    certs: [['Certified Public Accountant', 'State Board of Accountancy']]
  },
  'customer-service': {
    name: ['Lena', 'Morales'], title: 'Customer Success Specialist',
    summary: 'Support specialist with a 97% satisfaction score across 9,000+ tickets. Calm on the phone, fast in chat, and good at fixing the cause.',
    exp: [['Customer Success Specialist', 'Brightdesk', 'Handle 60+ chats and calls a day across billing and technical issues.'],
          ['Customer Service Associate', 'Urban Retail', 'Resolved in-store escalations and trained four new hires.']],
    edu: ['Associate Degree, Business', 'Miami Dade College'],
    skills: [['Zendesk', 90], ['De-escalation', 92], ['Product Knowledge', 85]]
  },
  'project-manager': {
    name: ['Omar', 'Haddad'], title: 'Project Manager, PMP',
    summary: 'PMP-certified project manager delivering infrastructure and software programmes up to $8M, on schedule and on budget.',
    exp: [['Project Manager', 'Vertex Engineering', 'Run four concurrent projects with teams of up to 25.'],
          ['Project Coordinator', 'Cobalt Systems', 'Kept 30+ milestones on track across a CRM rollout.']],
    edu: ['BEng Civil Engineering', 'University of Manchester'],
    skills: [['Agile & Scrum', 90], ['Risk Management', 88], ['MS Project', 85]],
    certs: [['PMP', 'Project Management Institute']]
  },
  'ux-designer': {
    title: 'UX/UI Designer',
    projects: [['Checkout Redesign', 'Case study · Figma', 'Cut checkout drop-off 23% through research-led simplification.'],
               ['Design System 2.0', 'Case study · Tokens', 'Unified 4 products on one component library.']]
  },
  'engineering': {
    name: ['Ethan', 'Clarke'], title: 'Mechanical Engineer',
    summary: 'Chartered mechanical engineer with eight years in product design and manufacturing, from CAD model to production line.',
    exp: [['Mechanical Engineer', 'Kestrel Robotics', 'Designed drive assemblies for a 40,000-unit production run.'],
          ['Graduate Engineer', 'Aston Motors', 'Ran FEA studies that cut bracket weight 18%.']],
    edu: ['MEng Mechanical Engineering', 'Imperial College London'],
    skills: [['SolidWorks', 92], ['FEA / ANSYS', 85], ['GD&T', 88]]
  },
  'legal': {
    name: ['Charlotte', 'Avery'], title: 'Corporate Associate',
    summary: 'Corporate associate focused on M&A and venture financings, with deal experience from seed rounds to $400M acquisitions.',
    exp: [['Corporate Associate', 'Whitmore & Lane LLP', 'Drafted and negotiated purchase agreements on 20+ transactions.'],
          ['Judicial Law Clerk', 'Court of Appeals', 'Drafted bench memoranda and opinions for a sitting judge.']],
    edu: ['Juris Doctor', 'Columbia Law School'],
    skills: [['M&A', 90], ['Due Diligence', 92], ['Contract Drafting', 90]]
  },
  'hospitality': {
    name: ['Isabella', 'Conti'], title: 'Front Office Manager',
    summary: 'Hospitality manager from five-star hotels, known for calm service recovery and front desks that guests mention in reviews.',
    exp: [['Front Office Manager', 'The Grand Riviera', 'Lead a 22-person team across reception, concierge and reservations.'],
          ['Guest Relations Supervisor', 'Hotel Belvedere', 'Raised review scores from 8.6 to 9.3.']],
    edu: ['BA Hospitality Management', 'Les Roches'],
    skills: [['Guest Relations', 95], ['Opera PMS', 88], ['Revenue Management', 80]]
  },
  'entry-level': {
    name: ['Mia', 'Johnson'], title: 'Business Graduate',
    summary: 'Business graduate with two internships and a final-year project on retail pricing. Quick to learn, organised, and comfortable with data.',
    exp: [['Sales Assistant (part-time)', 'Target', 'Served 150+ customers a day during peak trading.']],
    edu: ['BA Business Administration', 'Ohio State University'],
    skills: [['Excel', 85], ['Research', 80], ['Presentation', 82]]
  },
  'admin-assistant': {
    name: ['Hannah', 'Price'], title: 'Executive Assistant',
    summary: 'Executive assistant to C-level leaders for six years. Runs complex calendars, travel and board packs so nothing slips.',
    exp: [['Executive Assistant to the CEO', 'Meridian Group', 'Manage calendar, travel and board materials for the CEO.'],
          ['Office Administrator', 'Clearwater Partners', 'Ran office operations for a team of 40.']],
    edu: ['Diploma, Business Administration', 'Pitman Training'],
    skills: [['Microsoft 365', 95], ['Calendar Management', 92], ['Minute Taking', 88]]
  }
};

const CV_DEFAULTS = {
  layout: 'single', head: 'top', contact: 'header', contactStyle: 'icons', photo: true, photoIn: 'header',
  dates: 'right', skills: 'chips', langs: 'list', quals: 'chips', side: CV_SIDE, first: [], titles: {}
};

const CV_TITLES = {
  summary: 'Professional Summary', experience: 'Work Experience', education: 'Education', skills: 'Skills',
  languages: 'Languages', projects: 'Projects', certifications: 'Certifications', internships: 'Internships',
  activities: 'Activities', hobbies: 'Interests', courses: 'Courses', references: 'References',
  qualities: 'Strengths', achievements: 'Achievements', contact: 'Contact'
};

const CV_LEVELS = {
  beginner: 1, elementary: 2, intermediate: 3, advanced: 4, proficient: 4, expert: 5,
  native: 5, fluent: 4, a1: 1, a2: 2, b1: 3, b2: 3, c1: 4, c2: 5
};

// Skills are stored as words ("Advanced") from the editor, or as 0–100 numbers
// in older saves and the thumbnail sample. Both map onto a 1–5 scale.
function cvLevel(value) {
  if (value === undefined || value === null || value === '') return 0;
  const n = Number(value);
  if (!Number.isNaN(n)) return Math.max(1, Math.min(5, Math.round(n / 20)));
  return CV_LEVELS[String(value).trim().toLowerCase()] || 0;
}

function cvLevelLabel(value) {
  if (value === undefined || value === null || value === '') return '';
  return Number.isNaN(Number(value)) ? esc(value) : '';
}

function cvRange(start, end) {
  if (!start && !end) return '';
  if (!start) return esc(end);
  return `${esc(start)} – ${esc(end) || 'Present'}`;
}

function cvDesc(str) {
  const html = formatBullets(str);
  if (!html) return '';
  if (html.startsWith('<ul>')) return `<div class="cv-desc">${html.replace('<ul>', '<ul class="cv-bullets">')}</div>`;
  return `<div class="cv-desc"><p>${html}</p></div>`;
}

function cvItem({ role = '', org = '', loc = '', date = '', desc = '', orgFirst = false }) {
  if (!role && !org) return '';
  const top = role || org;
  const second = role ? org : '';
  const orgLine = (second || loc)
    ? `<div class="cv-org">${second ? `<span class="cv-org-name">${second}</span>` : ''}${loc ? `<span class="cv-loc">${loc}</span>` : ''}</div>`
    : '';
  // Harvard and consulting CVs lead with the employer for jobs and schools
  // (orgFirst is only passed by those sections); the role sits under it.
  const roleHtml = `<div class="cv-role">${top}</div>`;
  const lead = orgFirst && second;
  return `<div class="cv-item cv-keep${lead ? ' cv-org-first' : ''}">
      ${date ? `<div class="cv-date">${date}</div>` : ''}
      ${lead ? orgLine + roleHtml : roleHtml + orgLine}
      ${desc}
    </div>`;
}

function cvTitle(id, cfg) {
  if (id === 'custom') return esc(state.custom.title || 'Custom Section');
  return cfg.titles[id] || CV_TITLES[id] || id;
}

function cvSec(id, cfg, body, num, keep = false) {
  if (!body) return '';
  const n = num ? `<span class="cv-num">${String(num).padStart(2, '0')}</span>` : '';
  return `<section class="cv-sec cv-sec-${id}${keep ? ' cv-keep' : ''}">
      <h2 class="cv-h">${n}<span class="cv-h-t">${cvTitle(id, cfg)}</span></h2>
      <div class="cv-sec-body">${body}</div>
    </section>`;
}

function cvLevelList(list, mode, levelKey) {
  if (!list.length) return '';
  const lvl = item => cvLevel(item[levelKey]);
  const label = item => cvLevelLabel(item[levelKey]);
  switch (mode) {
    case 'bars':
      return `<div class="cv-bars">${list.map(it => `
        <div class="cv-bar-row"><span class="cv-bar-name">${esc(it.name)}</span>${lvl(it)
          ? `<span class="cv-bar"><i style="width:${lvl(it) * 20}%"></i></span>` : ''}</div>`).join('')}</div>`;
    case 'dots':
      return `<div class="cv-dotlist">${list.map(it => `
        <div class="cv-dot-row"><span class="cv-dot-name">${esc(it.name)}</span>${lvl(it)
          ? `<span class="cv-dots">${[1, 2, 3, 4, 5].map(i => `<i class="${i <= lvl(it) ? 'on' : ''}"></i>`).join('')}</span>` : ''}</div>`).join('')}</div>`;
    case 'list':
    case 'grid':
      return `<ul class="cv-list${mode === 'grid' ? ' cv-list-grid' : ''}">${list.map(it => `
        <li><span class="cv-li-name">${esc(it.name)}</span>${label(it) ? `<span class="cv-li-lvl">${label(it)}</span>` : ''}</li>`).join('')}</ul>`;
    case 'inline':
      return `<p class="cv-inline">${list.map(it => `<span class="cv-in">${esc(it.name)}${label(it) && levelKey === 'proficiency' ? ` <em>(${label(it)})</em>` : ''}</span>`).join('<span class="cv-in-sep"> · </span>')}</p>`;
    default:
      return `<div class="cv-chips">${list.map(it => `<span class="cv-chip">${esc(it.name)}</span>`).join('')}</div>`;
  }
}

function cvSectionHtml(id, cfg, num) {
  const s = state;
  switch (id) {
    case 'summary':
      if (!s.summary) return '';
      if (cfg.dropcap) {
        const text = esc(s.summary.trim());
        return cvSec(id, cfg, `<p class="cv-summary"><span class="cv-dropcap">${text.charAt(0)}</span>${text.slice(1)}</p>`, num, true);
      }
      return cvSec(id, cfg, `<p class="cv-summary">${esc(s.summary)}</p>`, num, true);
    case 'experience':
    case 'internships': {
      const list = s[id].filter(e => e.position || e.company);
      return cvSec(id, cfg, list.map(e => cvItem({
        role: esc(e.position), org: esc(e.company), loc: esc(e.location),
        date: cvRange(e.startDate, e.endDate), desc: cvDesc(e.description), orgFirst: cfg.orgFirst
      })).join(''), num);
    }
    case 'education': {
      const list = s.education.filter(e => e.degree || e.institution);
      return cvSec(id, cfg, list.map(e => cvItem({
        role: esc(e.degree) + (e.field ? ` in ${esc(e.field)}` : ''), org: esc(e.institution), loc: esc(e.location),
        date: cvRange(e.startDate, e.endDate), desc: cvDesc(e.description), orgFirst: cfg.orgFirst
      })).join(''), num);
    }
    case 'projects': {
      const list = s.projects.filter(pr => pr.name && pr.name.trim());
      return cvSec(id, cfg, list.map(pr => cvItem({
        role: esc(pr.name) + (pr.url ? ` <span class="cv-url">${linkify('website', pr.url)}</span>` : ''),
        org: esc(pr.tech), desc: cvDesc(pr.description)
      })).join(''), num);
    }
    case 'certifications': {
      const list = s.certifications.filter(c => c.name && c.name.trim());
      return cvSec(id, cfg, list.map(c => cvItem({
        role: esc(c.name), org: esc(c.issuer), date: esc(c.date), desc: cvDesc(c.description)
      })).join(''), num);
    }
    case 'activities': {
      const list = s.activities.filter(a => a.name || a.organization);
      return cvSec(id, cfg, list.map(a => cvItem({
        role: esc(a.name), org: esc(a.organization), date: esc(a.date), desc: cvDesc(a.description)
      })).join(''), num);
    }
    case 'courses': {
      const list = s.courses.filter(c => c.name || c.institution);
      return cvSec(id, cfg, list.map(c => cvItem({ role: esc(c.name), org: esc(c.institution), date: esc(c.date) })).join(''), num);
    }
    case 'references': {
      const list = s.references.filter(r => r.name || r.company);
      return cvSec(id, cfg, list.map(r => cvItem({
        role: esc(r.name), org: esc(r.company),
        desc: (r.email || r.phone) ? `<div class="cv-desc"><p>${[r.email ? linkify('email', r.email) : '', r.phone ? linkify('phone', r.phone) : ''].filter(Boolean).join(' · ')}</p></div>` : ''
      })).join(''), num);
    }
    case 'achievements': {
      const list = s.achievements.filter(a => a.name && a.name.trim());
      return cvSec(id, cfg, list.map(a => cvItem({ role: esc(a.name), desc: cvDesc(a.description) })).join(''), num);
    }
    case 'skills':
      return cvSec(id, cfg, cvLevelList(s.skills.filter(x => x.name && x.name.trim()), cfg.skills, 'level'), num, true);
    case 'languages':
      return cvSec(id, cfg, cvLevelList(s.languages.filter(x => x.name && x.name.trim()), cfg.langs, 'proficiency'), num, true);
    case 'qualities':
      return cvSec(id, cfg, cvLevelList(s.qualities.filter(x => x.name && x.name.trim()), cfg.quals, ''), num, true);
    case 'hobbies':
      if (!s.hobbies) return '';
      return cvSec(id, cfg, `<p class="cv-summary">${esc(s.hobbies)}</p>`, num, true);
    case 'custom':
      if (!s.custom.content) return '';
      return cvSec(id, cfg, cvDesc(s.custom.content), num, true);
    case 'signature': {
      const sig = s.signature || {};
      if (!sig.text && !sig.image) return '';
      return `<div class="cv-signature cv-keep">
          ${sig.image ? `<img class="cv-sig-img" src="${sig.image}" alt="Signature" />` : `<div class="cv-sig-text">${esc(sig.text)}</div>`}
          <div class="cv-sig-label">Signature</div>
        </div>`;
    }
    case 'footer':
      if (!s.footer) return '';
      return `<div class="cv-footer cv-keep">${esc(s.footer)}</div>`;
    default:
      return '';
  }
}

const CV_CONTACT_LABELS = {
  email: 'Email', phone: 'Phone', location: 'Address', linkedin: 'LinkedIn', website: 'Website',
  dob: 'Date of birth', pob: 'Place of birth', license: 'Driving licence', gender: 'Gender',
  nationality: 'Nationality', civil: 'Marital status', custom: 'Other'
};

function cvContactEntries() {
  const p = state.personal;
  return [
    ['email', p.email ? linkify('email', p.email) : ''],
    ['phone', p.phone ? linkify('phone', p.phone) : ''],
    ['location', (p.city || p.country) ? esc([p.city, p.country].filter(Boolean).join(', ')) : ''],
    ['linkedin', p.linkedin ? linkify('linkedin', p.linkedin) : ''],
    ['website', p.website ? linkify('website', p.website) : ''],
    ['dob', esc(p.dob)], ['pob', esc(p.pob)], ['license', esc(p.driverLicense)], ['gender', esc(p.gender)],
    ['nationality', esc(p.nationality)], ['civil', esc(p.civilStatus)], ['custom', esc(p.customField)]
  ].filter(([, v]) => v);
}

function cvContacts(cfg) {
  const entries = cvContactEntries();
  if (!entries.length) return '';
  if (cfg.contactStyle === 'plain') {
    return `<div class="cv-contacts cv-contacts-plain">${entries.map(([k, v]) => `<span class="cv-c cv-c-${k}">${v}</span>`).join('<span class="cv-c-sep"> | </span>')}</div>`;
  }
  if (cfg.contactStyle === 'labels') {
    return `<div class="cv-contacts cv-contacts-labels">${entries.map(([k, v]) => `<div class="cv-c cv-c-${k}"><span class="cv-cl">${CV_CONTACT_LABELS[k]}</span><span class="cv-cv">${v}</span></div>`).join('')}</div>`;
  }
  const iconTmpl = cfg.solidIcons ? 'bold' : 'modern';
  const iconKey = { license: 'license', civil: 'civil' };
  return `<div class="cv-contacts cv-contacts-icons">${entries.map(([k, v]) => `<span class="cv-c cv-c-${k}"><span class="cv-ic">${getIcon(iconKey[k] || k, iconTmpl)}</span><span class="cv-cv">${v}</span></span>`).join('')}</div>`;
}

function cvPhoto(cfg, where) {
  if (cfg.photo === false || !state.photo || cfg.photoIn !== where) return '';
  return `<div class="cv-photo"><img class="cv-img" src="${state.photo}" alt="Profile photo" /></div>`;
}

function cvHeader(cfg) {
  const p = state.personal;
  const first = esc(p.firstName), last = esc(p.lastName);
  const name = (first || last)
    ? `<span class="cv-first">${first}</span>${first && last ? ' ' : ''}<span class="cv-last">${last}</span>`
    : '<span class="cv-first">Your</span> <span class="cv-last">Name</span>';
  const title = state.showJobTitle === false ? '' : esc(p.jobTitle);
  return `<header class="cv-head">
      ${cvPhoto(cfg, 'header')}
      <div class="cv-id">
        ${cfg.kicker ? `<div class="cv-kicker">${cfg.kicker}</div>` : ''}
        <h1 class="cv-name">${name}</h1>
        ${title ? `<div class="cv-title">${title}</div>` : ''}
      </div>
      ${cfg.contact === 'header' ? cvContacts(cfg) : ''}
    </header>`;
}

function buildCvTemplate(tmpl) {
  const cfg = { ...CV_DEFAULTS, ...CV_TEMPLATES[tmpl] };
  const ordered = orderedVisibleSectionIds(state.sectionOrder);
  const ids = [...cfg.first.filter(id => ordered.includes(id)), ...ordered.filter(id => !cfg.first.includes(id))];
  const hasSide = cfg.layout !== 'single';
  const tail = ['signature', 'footer'];
  const sideIds = hasSide ? ids.filter(id => cfg.side.includes(id)) : [];
  const mainIds = ids.filter(id => !sideIds.includes(id) && !tail.includes(id));

  let n = 0;
  const main = mainIds.map(id => {
    const html = cvSectionHtml(id, cfg, cfg.numbered ? n + 1 : 0);
    if (html) n += 1;
    return html;
  }).join('') + tail.filter(id => ids.includes(id)).map(id => cvSectionHtml(id, cfg, 0)).join('');

  const header = cvHeader(cfg);
  const side = hasSide ? `<aside class="cv-side">
      ${cvPhoto(cfg, 'side')}
      ${cfg.head === 'side' ? header : ''}
      ${cfg.contact === 'side' ? cvSec('contact', cfg, cvContacts(cfg), 0, true) : ''}
      ${sideIds.map(id => cvSectionHtml(id, cfg, 0)).join('')}
    </aside>` : '';

  const classes = ['cv', `cv-L-${cfg.layout}`, `cv-D-${cfg.dates}`, `cv-H-${cfg.head}`, state.photo && cfg.photo !== false ? 'cv-has-photo' : 'cv-no-photo'];
  return `<div class="${classes.join(' ')}">
      ${cfg.decor || ''}
      ${cfg.head === 'top' || !hasSide ? header : ''}
      <div class="cv-body">
        ${side}
        <main class="cv-main">
          ${hasSide && cfg.head === 'main' ? header : ''}
          ${main}
        </main>
      </div>
    </div>`;
}

const CV_FONT_FAMILIES = [
  'Lato:ital,wght@0,300;0,400;0,700;0,900;1,400', 'Merriweather:ital,wght@0,400;0,700;1,400',
  'Roboto:ital,wght@0,400;0,500;0,700;1,400', 'Playfair:ital,wght@0,400..900;1,400..900',
  'Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500', 'DM+Sans:ital,wght@0,400;0,500;0,700;1,400',
  'Outfit:wght@300..900', 'Work+Sans:ital,wght@0,300..700;1,400', 'Source+Sans+3:ital,wght@0,400..800;1,400',
  'Space+Grotesk:wght@400..700', 'IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400', 'IBM+Plex+Mono:wght@400;500;600',
  'Manrope:wght@400..800', 'Lora:ital,wght@0,400..700;1,400..700', 'Archivo:ital,wght@0,400..900;1,400',
  'Archivo+Black', 'Plus+Jakarta+Sans:ital,wght@0,400..800;1,400', 'Libre+Baskerville:ital,wght@0,400;0,700;1,400',
  'Montserrat:wght@400..900', 'Open+Sans:ital,wght@0,400..800;1,400', 'PT+Serif:ital,wght@0,400;0,700;1,400',
  'Spectral:ital,wght@0,400;0,500;0,600;0,700;1,400', 'EB+Garamond:ital,wght@0,400..800;1,400..800',
  'Raleway:wght@400..900', 'DM+Serif+Display:ital@0;1', 'Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400',
  'Courier+Prime:ital,wght@0,400;0,700;1,400', 'Barlow:ital,wght@0,400;0,500;0,600;0,700;1,400',
  'Barlow+Condensed:wght@500;600;700;800', 'Fraunces:ital,wght@0,400..900;1,400..900', 'Crimson+Pro:ital,wght@0,400..800;1,400',
  'Nunito:ital,wght@0,400..900;1,400', 'STIX+Two+Text:ital,wght@0,400..700;1,400..700', 'JetBrains+Mono:wght@400..700',
  'Sora:wght@400..800', 'Bodoni+Moda:ital,wght@0,400..900;1,400..900', 'Syne:wght@400..800', 'Rubik:ital,wght@0,400..800;1,400'
];

// Templates use a wider range of typefaces than the site chrome, so the families
// are requested once, from script, on any page that renders a resume. Inter and
// Playfair Display are left out on purpose: every page already loads them, and a
// second declaration with other weights changes how Professional renders.
function ensureCvFonts() {
  if (document.getElementById('cv-fonts')) return;
  const link = document.createElement('link');
  link.id = 'cv-fonts';
  link.rel = 'stylesheet';
  link.href = `https://fonts.googleapis.com/css2?${CV_FONT_FAMILIES.map(f => `family=${f}`).join('&')}&display=swap`;
  document.head.appendChild(link);
}

function renderTemplateThumbnails() {
  const thumbs = document.querySelectorAll('.tmpl-thumb');
  if (!thumbs.length) return;

  thumbs.forEach(thumb => {
    const btn = thumb.closest('.tmpl-btn');
    if (!btn) return;
    const tmpl = btn.dataset.tmpl;
    const html = buildTemplateThumbnailHtml(tmpl);
    thumb.innerHTML = thumbnailPageHtml(tmpl, html);
    setThumbScale(thumb);
  });
}

function thumbnailPageHtml(tmpl, html) {
  const style = tmpl === 'professional' ? '' : ` style="${accentStyle(tmpl)}"`;
  return `<div class="thumbnail-page resume-page ${templateRootClass(tmpl)}"${style}>${html}</div>`;
}

function buildTemplateThumbnailHtml(tmpl) {
  const original = snapshotThumbnailState();
  const originalTemplate = state.template;
  applyThumbnailState(tmpl);

  let html = '';
  try {
    html = buildTemplateHtml(tmpl);
  } finally {
    restoreThumbnailState(original, originalTemplate);
  }
  return demoteThumbnailHeadings(html);
}

// A thumbnail is decorative: it is a picture of a template, not page content.
// Several templates mark the person's name as <h1>, which is right in the live
// editor preview but would give a gallery page twenty competing <h1> elements.
// Styling is entirely class-based, so swapping the tag changes nothing visually.
function demoteThumbnailHeadings(html) {
  return html
    .replace(/<h1(\s|>)/g, '<div$1')
    .replace(/<\/h1>/g, '</div>');
}

function snapshotThumbnailState() {
  return {
    accentColor: state.accentColor,
    photo: state.photo,
    showJobTitle: state.showJobTitle,
    personal: { ...state.personal },
    summary: state.summary,
    experience: state.experience,
    education: state.education,
    skills: state.skills,
    languages: state.languages,
    projects: state.projects,
    certifications: state.certifications,
    internships: state.internships,
    activities: state.activities,
    hobbies: state.hobbies,
    courses: state.courses,
    references: state.references,
    qualities: state.qualities,
    achievements: state.achievements,
    signature: { ...state.signature },
    footer: state.footer,
    custom: { ...state.custom },
    visibleSections: state.visibleSections
  };
}

function applyThumbnailState(tmpl) {
  state.template = tmpl;
  state.accentColor = state.accentColor || '#2563eb';
  state.showJobTitle = true;
  state.photo = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 120'%3E%3Crect width='120' height='120' fill='%23dbeafe'/%3E%3Ccircle cx='60' cy='44' r='24' fill='%2393c5fd'/%3E%3Cpath d='M20 118c6-30 28-48 40-48s34 18 40 48' fill='%232563eb'/%3E%3C/svg%3E";
  Object.assign(state.personal, {
    firstName: 'Josephine',
    lastName: 'Fournier',
    jobTitle: 'Product Designer',
    email: 'josephine@email.com',
    phone: '+1 555 0199',
    city: 'Paris',
    country: 'France',
    linkedin: 'linkedin.com/in/josephine'
  });
  state.summary = 'Creative professional with experience building clear, elegant products and leading cross-functional projects.';
  state.experience = [
    { position: 'Senior Designer', company: 'Studio North', location: 'Paris', startDate: '2022', endDate: 'Present', description: 'Led product design systems and improved user workflows across web and mobile platforms.' },
    { position: 'Designer', company: 'Blue Labs', location: 'Lyon', startDate: '2019', endDate: '2022', description: 'Created brand, UX and visual design assets for SaaS and editorial teams.' }
  ];
  state.education = [
    { institution: 'Design Academy', degree: 'BA Visual Design', field: '', location: 'Paris', startDate: '2015', endDate: '2019', description: '' }
  ];
  state.skills = [
    { name: 'Product Design', level: 90 },
    { name: 'Brand Systems', level: 82 },
    { name: 'Research', level: 76 }
  ];
  state.languages = [
    { name: 'French', proficiency: 'Native' },
    { name: 'English', proficiency: 'Fluent' }
  ];
  state.projects = [
    { name: 'Portfolio Platform', tech: 'Figma, Web', url: '', description: 'Designed a modular profile builder.' }
  ];
  state.certifications = [
    { name: 'UX Strategy', issuer: 'Design Guild', date: '2023', description: '' }
  ];
  state.internships = [
    { position: 'Design Intern', company: 'Atelier UI', location: 'Paris', startDate: '2018', endDate: '2019', description: 'Supported research and visual design delivery.' }
  ];
  state.activities = [
    { name: 'Design Club Mentor', organization: 'Local University', date: '2021', description: 'Mentored students on portfolio projects.' }
  ];
  state.hobbies = 'Photography, typography, travel';
  state.courses = [
    { name: 'Design Systems Foundations', institution: 'Interaction School', date: '2024' }
  ];
  state.references = [
    { name: 'Marie Laurent', company: 'Studio North', email: 'marie@example.com', phone: '+1 555 0100' }
  ];
  state.qualities = [
    { name: 'Detail-oriented' },
    { name: 'Collaborative' }
  ];
  state.achievements = [
    { name: 'Design Excellence Award', description: 'Recognized for improving onboarding clarity.' }
  ];
  state.signature = { text: 'Josephine Fournier', image: null };
  state.footer = 'ResumeElite sample resume';
  state.custom = { title: 'Selected Work', content: 'Available portfolio case studies on request.' };
  state.visibleSections = ['summary', 'experience', 'education', 'skills', 'languages', 'projects', 'certifications'];
  applyThumbnailSample(CV_SAMPLES[tmpl]);
}

function applyThumbnailSample(sample) {
  if (!sample) return;
  if (sample.name) Object.assign(state.personal, { firstName: sample.name[0], lastName: sample.name[1] });
  if (sample.title) state.personal.jobTitle = sample.title;
  if (sample.summary) state.summary = sample.summary;
  if (sample.exp) {
    state.experience = sample.exp.map(([position, company, description], i) => ({
      position, company, location: '', description,
      startDate: i === 0 ? '2021' : '2017', endDate: i === 0 ? 'Present' : '2021'
    }));
  }
  if (sample.edu) {
    state.education = [{ degree: sample.edu[0], institution: sample.edu[1], field: '', location: '', startDate: '2013', endDate: '2017', description: '' }];
  }
  if (sample.skills) state.skills = sample.skills.map(([name, level]) => ({ name, level }));
  if (sample.certs) state.certifications = sample.certs.map(([name, issuer]) => ({ name, issuer, date: '2022', description: '' }));
  if (sample.projects) state.projects = sample.projects.map(([name, tech, description]) => ({ name, tech, url: '', description }));
  if (sample.achievements) {
    state.achievements = sample.achievements.map(([name, description]) => ({ name, description }));
    state.visibleSections = [...state.visibleSections, 'achievements'];
  }
}

function restoreThumbnailState(original, originalTemplate) {
  state.template = originalTemplate;
  state.accentColor = original.accentColor;
  state.photo = original.photo;
  state.showJobTitle = original.showJobTitle;
  Object.assign(state.personal, original.personal);
  state.summary = original.summary;
  state.experience = original.experience;
  state.education = original.education;
  state.skills = original.skills;
  state.languages = original.languages;
  state.projects = original.projects;
  state.certifications = original.certifications;
  state.internships = original.internships;
  state.activities = original.activities;
  state.hobbies = original.hobbies;
  state.courses = original.courses;
  state.references = original.references;
  state.qualities = original.qualities;
  state.achievements = original.achievements;
  state.signature = original.signature;
  state.footer = original.footer;
  state.custom = original.custom;
  state.visibleSections = original.visibleSections;
}

// ---- Shared helpers ----
const p = state.personal;
function esc(str = '') { return String(str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
function linkify(type, val) {
  if (!val) return '';
  let href = val;
  if (type === 'email') href = `mailto:${val}`;
  if (type === 'phone') href = `tel:${val.replace(/\s+/g, '')}`;
  if (type === 'website' || type === 'linkedin') {
    if (!/^https?:\/\//i.test(val)) href = `https://${val}`;
  }
  return `<a href="${href}" target="_blank" style="color:inherit;text-decoration:none;">${esc(val)}</a>`;
}
function hexToRgba(hex, a) {
  const r = parseInt(hex.slice(1, 3), 16), g = parseInt(hex.slice(3, 5), 16), b = parseInt(hex.slice(5, 7), 16);
  return `rgba(${r},${g},${b},${a})`;
}
function getName() { const f = state.personal.firstName, l = state.personal.lastName; return (f || l) ? esc(f) + ' ' + esc(l) : 'Your Name'; }
function getTitle() { return esc(state.personal.jobTitle) || 'Job Title'; }
function formatBullets(str = '') {
  if (!str) return '';
  // Split by newline and filter empty
  const lines = str.split('\n').map(l => l.trim()).filter(Boolean);
  if (lines.length === 0) return '';
  
  // If it's just one line and doesn't look like a bullet, just return escaped text
  if (lines.length === 1 && !lines[0].startsWith('•') && !lines[0].startsWith('-') && !lines[0].startsWith('*')) {
    return esc(str);
  }

  // Convert to UL/LI
  const listItems = lines.map(line => {
    // Remove existing bullet characters from the start
    const clean = line.replace(/^[•\-\*\u2022]\s*/, '');
    return `<li>${esc(clean)}</li>`;
  }).join('');
  
  return `<ul>${listItems}</ul>`;
}
function avatarHtml(cls = 'r-avatar', phClass = 'r-avatar-placeholder') {
  if (state.photo) return `<img src="${state.photo}" class="${cls}" alt="Profile" />`;
  return `<div class="${phClass}"><svg width="36" height="36" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="8" r="4"/><path d="M4 20c0-4 3.6-7 8-7s8 3 8 7"/></svg></div>`;
}

function getIcon(type, tmpl) {
  const isSolid = (tmpl === 'modern-dark' || tmpl === 'bold');
  const svgIcons = ['modern', 'tech', 'software-engineer', 'qa-engineer', 'student', 'freelancer', 'professional', 'corporate', 'modern-dark', 'elegant', 'executive', 'startup', 'classic-blue', 'minimal-formal', 'traditional-serif', 'europass', 'modern-right', 'nordic', 'timeline', 'mono', 'compact', 'portfolio', 'graduate', 'clean-sidebar', 'editorial', 'ats-friendly', 'latex-style', 'harvard-style', 'federal-style', 'functional', 'chronological', 'consulting-style', 'academic-cv', 'infographic', 'modern-executive', 'elite', 'aurora', 'swiss', 'brutalist', 'vogue', 'terminal', 'metro', 'luxe', 'impact', 'atelier', 'spectrum'];
  
  const outlinePaths = {
    email: '<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/>',
    phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
    location: '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    linkedin: '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/>',
    website: '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    dob: '<rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    pob: '<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>',
    license: '<rect x="1" y="3" width="22" height="18" rx="2" ry="2"/><path d="M7 8h10"/><path d="M7 12h10"/><path d="M7 16h6"/>',
    gender: '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    nationality: '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
    civil: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/>',
    calendar: '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>',
    star: '<polygon points="12 2 15 8.5 22 9.3 16.8 14 18.2 21 12 17.3 5.8 21 7.2 14 2 9.3 9 8.5 12 2"/>',
    quality: '<path d="M9 12l2 2 4-5"/><path d="M12 2l2.4 2.2 3.2-.4.5 3.2 2.7 1.7-1.4 2.9 1.4 2.9-2.7 1.7-.5 3.2-3.2-.4L12 22l-2.4-2.2-3.2.4-.5-3.2-2.7-1.7 1.4-2.9-1.4-2.9 2.7-1.7.5-3.2 3.2.4L12 2z"/>',
    flag: '<path d="M4 22V4"/><path d="M4 4c3-2 6 2 9 0s5 0 7 1v10c-2-1-4-3-7-1s-6-2-9 0"/>',
    idea: '<path d="M9 18h6"/><path d="M10 22h4"/><path d="M8.5 14.5A6 6 0 1 1 15.5 14.5c-.8.6-1.2 1.4-1.2 2.5H9.7c0-1.1-.4-1.9-1.2-2.5z"/>',
    custom: '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>'
  };

  const solidPaths = {
    email: '<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="currentColor" stroke="none"/>',
    phone: '<path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-2.2 2.2a15.045 15.045 0 01-6.59-6.59l2.2-2.21a.96.96 0 00.24-1.01c-.36-1.11-.56-2.3-.56-3.53 0-.55-.45-1-1-1H4.03c-.55 0-1 .45-1 1 0 9.39 7.63 17.02 17.02 17.02.55 0 1-.45 1-1v-3.52c0-.55-.45-1-1.02-1z" fill="currentColor" stroke="none"/>',
    location: '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z" fill="currentColor" stroke="none"/>',
    linkedin: '<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a2.7 2.7 0 0 0-2.7-2.7c-1.1 0-1.9.6-2.2 1.2v-1h-2.5v7.8h2.5v-4.1c0-.7.6-1.3 1.3-1.3a1.3 1.3 0 0 1 1.3 1.3v4.1h2.5M6.7 8.3a1.4 1.4 0 1 0 0-2.8 1.4 1.4 0 0 0 0 2.8m1.2 10.2V10.7H5.5v7.8h2.4z" fill="currentColor" stroke="none"/>',
    website: '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z" fill="currentColor" stroke="none"/>',
    dob: '<path d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z" fill="currentColor" stroke="none"/>',
    pob: '<path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" fill="currentColor" stroke="none"/>',
    license: '<path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm-8 12H5v-2h7v2zm8-4H5V8h15v4z" fill="currentColor" stroke="none"/>',
    gender: '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z" fill="currentColor" stroke="none"/>',
    nationality: '<path d="M14.4 6L14 4H5v17h2v-7h5.6l.4 2h7V6z" fill="currentColor" stroke="none"/>',
    civil: '<path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm0-12c-2.21 0-4 1.79-4 4s1.79 4 4 4 4-1.79 4-4-1.79-4-4-4z" fill="currentColor" stroke="none"/>',
    custom: '<path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04a.996.996 0 0 0 0-1.41l-2.34-2.34a.996.996 0 0 0-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z" fill="currentColor" stroke="none"/>'
  };

  const emojis = {
    email: '✉', phone: '📞', location: '📍', linkedin: 'in', website: '🌐', dob: '📅', pob: '🏠', license: '🚗', gender: '👤', nationality: '🏳️', civil: '💍', custom: '📝'
  };

  if (svgIcons.includes(tmpl)) {
    const p = isSolid ? solidPaths : outlinePaths;
    const style = isSolid ? `fill="currentColor"` : `fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"`;
    let pathContent = p[type] || '';
    // Use a safety margin by scaling the path down and centering it
    const safePath = `<g transform="translate(2, 2) scale(0.833)">${pathContent}</g>`;
    const svgStr = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" class="r-icon-svg" viewBox="0 0 24 24" ${style} style="display:inline-block; flex-shrink:0; overflow:visible;">${safePath}</svg>`;
    if (tmpl === 'modern-right') {
      return `<span class="mr-icon-bg">${svgStr}</span>`;
    }
    return svgStr;
  }
  return emojis[type] || '';
}

function sectionTitle(label) { return `<div class="r-section-title">${label}</div>`; }

function orderedVisibleSectionIds(ids) {
  const requested = Array.isArray(ids) ? ids : [];
  const order = Array.isArray(state.sectionOrder) ? state.sectionOrder : requested;
  const visible = Array.isArray(state.visibleSections) ? state.visibleSections : requested;
  return order
    .filter((id, index) => order.indexOf(id) === index)
    .filter(id => requested.includes(id) && visible.includes(id));
}

function summarySection() {
  if (!state.summary) return '';
  return `<div class="r-section">${sectionTitle('Professional Summary')}<p class="r-summary">${esc(state.summary)}</p></div>`;
}

// ---- Professional (Refined High-Fidelity) ----
function buildProfessional() {
  const p = state.personal;
  const tmpl = state.template;
  const contacts = [
    p.email ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('email', tmpl)}</span> ${linkify('email', p.email)}</span>` : '',
    p.phone ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('phone', tmpl)}</span> ${linkify('phone', p.phone)}</span>` : '',
    (p.city || p.country) ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('location', tmpl)}</span> ${esc([p.city, p.country].filter(Boolean).join(', '))}</span>` : '',
    p.linkedin ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('linkedin', tmpl)}</span> ${linkify('linkedin', p.linkedin)}</span>` : '',
    p.website ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('website', tmpl)}</span> ${linkify('website', p.website)}</span>` : '',
    p.dob ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('dob', tmpl)}</span> ${esc(p.dob)}</span>` : '',
    p.pob ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('pob', tmpl)}</span> ${esc(p.pob)}</span>` : '',
    p.driverLicense ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('license', tmpl)}</span> ${esc(p.driverLicense)}</span>` : '',
    p.gender ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('gender', tmpl)}</span> ${esc(p.gender)}</span>` : '',
    p.nationality ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('nationality', tmpl)}</span> ${esc(p.nationality)}</span>` : '',
    p.civilStatus ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('civil', tmpl)}</span> ${esc(p.civilStatus)}</span>` : '',
    p.customField ? `<span class="r-contact-item"><span class="r-prof-icon">${getIcon('custom', tmpl)}</span> ${esc(p.customField)}</span>` : ''
  ].filter(Boolean);

  const profSectionMap = {
    summary: summarySection,
    education: profEduSection,
    experience: profExpSection,
    skills: profSkillsSection,
    certifications: profCertSection,
    languages: profLangSection,
    projects: profProjSection,
    internships: profInternshipSection,
    activities: profActivitySection,
    hobbies: profHobbySection,
    courses: profCourseSection,
    references: profReferenceSection,
    qualities: profQualitySection,
    achievements: profAchievementSection,
    signature: profSignatureSection,
    footer: profFooterSection,
    custom: profCustomSection
  };

  const sections = orderedVisibleSectionIds(state.sectionOrder)
    .map(id => profSectionMap[id] ? profSectionMap[id]() : '')
    .join('');

  return `
    <div class="prof-pg">
      <div class="prof-header">
        <div class="prof-header-content">
          <div class="prof-name">${getName()}</div>
          ${state.showJobTitle === false ? '' : `<div class="prof-job-title">${getTitle()}</div>`}
          <div class="prof-contacts">${contacts.join('')}</div>
        </div>
        ${state.photo ? `<div class="prof-photo">${avatarHtml('prof-img', 'prof-ph')}</div>` : ''}
      </div>
      <div class="prof-body">
        ${sections}
      </div>
    </div>
  `;
}

function profSectionWrapper(label, content, extraClass = '') {
  if (!content) return '';
  return `
    <div class="prof-section ${extraClass}">
      <div class="prof-section-label">${label}</div>
      ${content}
    </div>
  `;
}

function profExpSection() {
  const list = state.experience.filter(e => e.position || e.company);
  if (!list.length) return '';
  const rows = list.map(e => `
    <div class="prof-item-row">
      <div class="prof-date-side">${e.startDate ? esc(e.startDate) + ' - ' + (esc(e.endDate) || 'Present') : ''}</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(e.position)}</div>
        <div class="prof-item-sub">${esc(e.company)}${e.location ? ' • ' + esc(e.location) : ''}</div>
        ${e.description ? `<div class="prof-item-desc">${esc(e.description)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Employment', rows);
}

function profEduSection() {
  const list = state.education.filter(e => e.degree || e.institution);
  if (!list.length) return '';
  const rows = list.map(e => `
    <div class="prof-item-row">
      <div class="prof-date-side">${e.startDate ? esc(e.startDate) + ' - ' + (esc(e.endDate) || 'Present') : ''}</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(e.degree)}${e.field ? ', ' + esc(e.field) : ''}</div>
        <div class="prof-item-sub">${esc(e.institution)}${e.location ? ' • ' + esc(e.location) : ''}</div>
        ${e.description ? `<div class="prof-item-desc">${esc(e.description)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Education', rows);
}

function profSkillsSection() {
  const list = state.skills.filter(s => s.name && s.name.trim());
  if (!list.length) return '';
  const rows = `<div class="prof-skills-grid">${list.map(s => `<div class="prof-skill-item">${esc(s.name)}</div>`).join('')}</div>`;
  return profSectionWrapper('Skills', rows, 'prof-no-timeline');
}

function profLangSection() {
  const list = state.languages.filter(l => l.name && l.name.trim());
  if (!list.length) return '';
  const rows = `<div class="prof-skills-grid">${list.map(l => `<div class="prof-skill-item">${esc(l.name)}</div>`).join('')}</div>`;
  return profSectionWrapper('Languages', rows, 'prof-no-timeline');
}

function profCertSection() {
  const list = state.certifications.filter(c => c.name && c.name.trim());
  if (!list.length) return '';
  const rows = list.map(c => `
    <div class="prof-item-row">
      <div class="prof-date-side">${esc(c.date || '')}</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(c.name)}</div>
        ${c.issuer ? `<div class="prof-item-sub">${esc(c.issuer)}</div>` : ''}
        ${c.url ? `<div class="prof-item-desc">${linkify('website', c.url)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Certificates', rows);
}

function profProjSection() {
  const list = state.projects.filter(p => p.name && p.name.trim());
  if (!list.length) return '';
  const rows = list.map(p => `
    <div class="prof-item-row">
      <div class="prof-date-side"></div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(p.name)}</div>
        ${p.tech ? `<div class="prof-item-sub">${esc(p.tech)}</div>` : ''}
        ${p.url ? `<div class="prof-item-desc">${linkify('website', p.url)}</div>` : ''}
        ${p.description ? `<div class="prof-item-desc">${formatBullets(p.description)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Projects', rows);
}

function profInternshipSection() {
  const list = state.internships.filter(e => e.position || e.company);
  if (!list.length) return '';
  const rows = list.map(e => `
    <div class="prof-item-row">
      <div class="prof-date-side">${e.startDate ? esc(e.startDate) + ' - ' + (esc(e.endDate) || 'Present') : ''}</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(e.position)}</div>
        <div class="prof-item-sub">${esc(e.company)}${e.location ? ' • ' + esc(e.location) : ''}</div>
        ${e.description ? `<div class="prof-item-desc">${esc(e.description)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Internships', rows);
}

function profActivitySection() {
  const list = state.activities.filter(a => a.name || a.organization);
  if (!list.length) return '';
  const rows = list.map(a => `
    <div class="prof-item-row">
      <div class="prof-date-side">${esc(a.date || '')}</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(a.name)}</div>
        <div class="prof-item-sub">${esc(a.organization)}</div>
        ${a.description ? `<div class="prof-item-desc">${esc(a.description)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Activities', rows);
}

function profHobbySection() {
  if (!state.hobbies) return '';
  const list = state.hobbies.split(/[,\n]/).map(s => s.trim()).filter(Boolean);
  if (!list.length) return '';
  const rows = `<div class="prof-hobby-grid">${list.map(h => `<div class="prof-hobby-item"><span class="prof-hobby-bullet"></span> ${esc(h)}</div>`).join('')}</div>`;
  return profSectionWrapper('Hobbies', rows, 'prof-no-timeline');
}

function profCourseSection() {
  const list = state.courses.filter(c => c.name || c.institution);
  if (!list.length) return '';
  const rows = list.map(c => `
    <div class="prof-item-row">
      <div class="prof-date-side">${esc(c.date || '')}</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(c.name)}</div>
        <div class="prof-item-sub">${esc(c.institution)}</div>
      </div>
    </div>`).join('');
  return profSectionWrapper('Courses', rows);
}

function profReferenceSection() {
  const list = state.references.filter(r => r.name || r.company);
  if (!list.length) return '';
  const rows = list.map(r => `
    <div class="prof-item-row">
      <div class="prof-date-side">Reference</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(r.name)}</div>
        <div class="prof-item-sub">${esc(r.company)}</div>
        <div class="prof-item-desc">${[r.email, r.phone].filter(Boolean).join(' • ')}</div>
      </div>
    </div>`).join('');
  return profSectionWrapper('References', rows);
}

function profQualitySection() {
  const list = state.qualities.filter(q => q.name && q.name.trim());
  if (!list.length) return '';
  // No .prof-skills-full rule exists, and the extra wrapper landed in the parent
  // grid's column 3 with no width, collapsing every quality to one letter per line.
  const rows = `<div class="prof-skills-grid">${list.map(q => `<div class="prof-skill-item">${esc(q.name)}</div>`).join('')}</div>`;
  return profSectionWrapper('Qualities', rows, 'prof-no-timeline');
}

function profAchievementSection() {
  const list = state.achievements.filter(a => a.name && a.name.trim());
  if (!list.length) return '';
  const rows = list.map(a => `
    <div class="prof-item-row">
      <div class="prof-date-side">Award</div>
      <div class="prof-bullet-side"><span class="prof-sq"></span></div>
      <div class="prof-content-side">
        <div class="prof-item-title">${esc(a.name)}</div>
        ${a.description ? `<div class="prof-item-desc">${esc(a.description)}</div>` : ''}
      </div>
    </div>`).join('');
  return profSectionWrapper('Achievements', rows);
}

function profSignatureSection() {
  if (!state.signature.text) return '';
  const content = `<div class="prof-content-side" style="grid-column:3;text-align:right;margin-top:20px;">
    <div style="font-family:'Playfair Display', serif;font-size:1.8rem;font-style:italic;color:#3b82f6;">${esc(state.signature.text)}</div>
    <div style="border-top:1px solid #e2e8f0;display:inline-block;padding-top:4px;margin-top:4px;min-width:150px;font-size:0.8rem;text-transform:uppercase;">Signature</div>
  </div>`;
  return profSectionWrapper('Signature', content);
}

function profFooterSection() {
  if (!state.footer) return '';
  return `<div style="margin-top:30px;padding-top:15px;border-top:1px solid #f1f5f9;text-align:center;color:#94a3b8;font-size:0.75rem;grid-column:1/4;">${esc(state.footer)}</div>`;
}

function profCustomSection() {
  if (!state.custom.content) return '';
  const content = `<div class="prof-content-side" style="grid-column:3"><div class="prof-item-desc">${esc(state.custom.content)}</div></div>`;
  return profSectionWrapper(state.custom.title || 'Custom', content, 'prof-no-timeline');
}

function collectPdfLinks(root, pageWidthMm, pageHeightMm) {
  const rootRect = root.getBoundingClientRect();
  const pxToMm = pageWidthMm / rootRect.width;
  const links = [];

  root.querySelectorAll('a[href]').forEach(anchor => {
    const href = anchor.getAttribute('href');
    if (!href || href === '#') return;

    anchor.getClientRects && Array.from(anchor.getClientRects()).forEach(rect => {
      if (!rect.width || !rect.height) return;

      const x = (rect.left - rootRect.left) * pxToMm;
      const y = (rect.top - rootRect.top) * pxToMm;
      const width = rect.width * pxToMm;
      const height = rect.height * pxToMm;
      const firstPage = Math.floor(y / pageHeightMm);
      const lastPage = Math.floor((y + height) / pageHeightMm);

      for (let page = firstPage; page <= lastPage; page += 1) {
        const pageTop = page * pageHeightMm;
        const clippedTop = Math.max(y, pageTop);
        const clippedBottom = Math.min(y + height, pageTop + pageHeightMm);
        if (clippedBottom <= clippedTop) continue;

        links.push({
          page,
          href,
          x,
          y: clippedTop - pageTop,
          width,
          height: clippedBottom - clippedTop
        });
      }
    });
  });

  return links;
}

function applyPdfLinks(pdf, links) {
  const pageCount = pdf.getNumberOfPages ? pdf.getNumberOfPages() : 0;
  links.forEach(link => {
    const pageNumber = link.page + 1;
    if (pageNumber < 1 || (pageCount && pageNumber > pageCount)) return;
    if (pdf.setPage) pdf.setPage(pageNumber);
    pdf.link(link.x, link.y, link.width, Math.max(link.height, 3), { url: link.href });
  });
}

// The PDF page itself is a picture (html2canvas), so on its own it has no text for an
// applicant tracking system to read, copy or search. Every visible line is therefore
// also written as invisible PDF text, laid exactly over its picture and stretched to
// the same width so a selection highlights the right words. Lines are emitted in
// document order, which keeps each section together for parsers even in two-column
// layouts.
//
// jsPDF's built-in Helvetica has no Unicode map, so anything beyond ASCII (ë, ç, ü,
// –, ·) extracts as garbage. The text layer therefore uses a subset of Noto Sans
// (fonts/pdf-text.ttf: Latin, Greek, Cyrillic and punctuation, ~105 KB, OFL), fetched
// on the first export. If it cannot load, the layer falls back to ASCII Helvetica.
const PDF_TEXT_FONT_URL = '/fonts/pdf-text.ttf';
let pdfTextFontData = null;

async function loadPdfTextFont(pdf) {
  try {
    if (!pdfTextFontData) {
      const res = await fetch(PDF_TEXT_FONT_URL);
      if (!res.ok) throw new Error(res.status);
      const bytes = new Uint8Array(await res.arrayBuffer());
      let bin = '';
      for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
      pdfTextFontData = btoa(bin);
    }
    pdf.addFileToVFS('pdf-text.ttf', pdfTextFontData);
    pdf.addFont('pdf-text.ttf', 'PdfText', 'normal');
    return 'PdfText';
  } catch (err) {
    return null;
  }
}

function pdfSafeText(str, unicode) {
  str = str.replace(/[   ]/g, ' ').replace(/[​-‍﻿]/g, '');
  if (unicode) return str;
  return str
    .normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[‐-―−]/g, '-')
    .replace(/[·•]/g, '|')
    .replace(/[‘’]/g, "'").replace(/[“”]/g, '"')
    .replace(/[^\x20-\x7e]/g, '');
}

function collectPdfText(root, pageWidthMm, pageHeightMm) {
  const rootRect = root.getBoundingClientRect();
  const pxToMm = pageWidthMm / rootRect.width;
  const lines = [];
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      if (!node.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
      const el = node.parentElement;
      if (!el || !el.getClientRects().length) return NodeFilter.FILTER_REJECT;
      const cs = getComputedStyle(el);
      if (cs.visibility === 'hidden' || cs.opacity === '0') return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT;
    }
  });

  const range = document.createRange();
  for (let node = walker.nextNode(); node; node = walker.nextNode()) {
    const cs = getComputedStyle(node.parentElement);
    const fontPx = parseFloat(cs.fontSize) || 12;
    const transform = cs.textTransform;
    const text = node.nodeValue;
    let line = null;

    const flush = () => {
      if (!line) return;
      let str = text.slice(line.start, line.end).replace(/\s+/g, ' ');
      if (transform === 'uppercase') str = str.toUpperCase();
      else if (transform === 'lowercase') str = str.toLowerCase();
      if (str.trim()) {
        const top = (line.top - rootRect.top) * pxToMm;
        const page = Math.floor(top / pageHeightMm);
        lines.push({
          page,
          x: (line.left - rootRect.left) * pxToMm,
          y: top - page * pageHeightMm + (line.bottom - line.top) * pxToMm * 0.8,
          width: (line.right - line.left) * pxToMm,
          sizePt: fontPx * pxToMm * (72 / 25.4),
          text: str
        });
      }
      line = null;
    };

    for (const m of text.matchAll(/\S+/g)) {
      range.setStart(node, m.index);
      range.setEnd(node, m.index + m[0].length);
      const r = range.getClientRects()[0];
      if (!r || !r.width) continue;
      if (line && Math.abs(r.top - line.top) < fontPx * 0.5 && r.left >= line.right - 1) {
        line.end = m.index + m[0].length;
        line.right = r.right;
        line.bottom = Math.max(line.bottom, r.bottom);
      } else {
        flush();
        line = { start: m.index, end: m.index + m[0].length, left: r.left, right: r.right, top: r.top, bottom: r.bottom };
      }
    }
    flush();
  }
  range.detach();
  return lines;
}

// Each line is stretched with horizontal scaling rather than character spacing:
// added spacing makes extractors read letter-spaced headings as "M A N A G E R".
function applyPdfText(pdf, lines, fontName) {
  const pageCount = pdf.getNumberOfPages ? pdf.getNumberOfPages() : 0;
  pdf.setFont(fontName || 'helvetica', 'normal');
  lines.forEach(line => {
    const pageNumber = line.page + 1;
    if (pageNumber < 1 || (pageCount && pageNumber > pageCount)) return;
    const text = pdfSafeText(line.text, !!fontName);
    if (!text.trim()) return;
    pdf.setPage(pageNumber);
    pdf.setFontSize(line.sizePt);
    const natural = pdf.getTextWidth(text);
    const horizontalScale = natural > 0 ? Math.min(4, Math.max(0.25, line.width / natural)) : 1;
    pdf.text(text, line.x, line.y, { renderingMode: 'invisible', horizontalScale });
  });
}

// html2canvas 1.4 has no object-fit support: it draws every <img> stretched to its
// box, which squashed any photo that was not already the box's shape. Before the
// capture, each cover/contain image in the export copy is redrawn at the size it is
// shown, cropped exactly as the browser crops it, so nothing is left to stretch.
async function flattenImagesForPdf(root) {
  const imgs = Array.from(root.querySelectorAll('img'));
  await Promise.all(imgs.map(async img => {
    const cs = getComputedStyle(img);
    const fit = cs.objectFit;
    if (fit !== 'cover' && fit !== 'contain' && fit !== 'scale-down') return;
    const w = img.clientWidth, h = img.clientHeight;
    const nw = img.naturalWidth, nh = img.naturalHeight;
    if (!w || !h || !nw || !nh) return;
    const [px, py] = (cs.objectPosition || '50% 50%').split(' ').map(v => {
      if (v === 'left' || v === 'top') return 0;
      if (v === 'right' || v === 'bottom') return 1;
      return v.endsWith('%') ? parseFloat(v) / 100 : 0.5;
    });
    const scale = 3;
    const canvas = document.createElement('canvas');
    canvas.width = Math.round(w * scale);
    canvas.height = Math.round(h * scale);
    const ctx = canvas.getContext('2d');
    try {
      if (fit === 'cover') {
        const s = Math.max(w / nw, h / nh);
        const sw = w / s, sh = h / s;
        ctx.drawImage(img, (nw - sw) * px, (nh - sh) * (py ?? 0.5), sw, sh, 0, 0, canvas.width, canvas.height);
      } else {
        const s = Math.min(w / nw, h / nh, fit === 'scale-down' ? 1 : Infinity);
        const dw = nw * s, dh = nh * s;
        ctx.drawImage(img, (w - dw) * px * scale, (h - dh) * (py ?? 0.5) * scale, dw * scale, dh * scale);
      }
      const url = canvas.toDataURL('image/png');
      await new Promise(resolve => {
        img.onload = resolve;
        img.onerror = resolve;
        img.src = url;
      });
      img.style.objectFit = 'fill';
    } catch (err) {
      // A cross-origin image taints the canvas; leave it as it was.
    }
  }));
}

// ---- Download PDF ----
function bindDownloadBtn() {
  const btn = document.getElementById('download-btn');
  if (!btn) return;
  btn.addEventListener('click', async () => {
    let fn = 'Resume.pdf';
    if (state.personal.firstName || state.personal.lastName) {
      fn = `${state.personal.firstName || ''}_${state.personal.lastName || ''}_ResumeElite`.replace(/_+/g, '_').trim() + '.pdf';
    }

    const oldZoom = zoom;
    if (zoom !== 1) {
      zoom = 1;
      applyZoom();
    }

    btn.innerHTML = `<span style="display:inline-block;animation:spin 1s linear infinite;">⏳</span> Generating...`;
    btn.disabled = true;

    const element = document.getElementById('resume-preview');
    const exportRoot = document.createElement('div');
    const exportElement = element.cloneNode(true);
    exportRoot.className = 'pdf-export-root';
    exportElement.id = 'resume-preview-pdf';
    exportElement.classList.add('pdf-exporting');
    exportRoot.appendChild(exportElement);
    document.documentElement.classList.add('is-pdf-exporting');
    document.body.classList.add('is-pdf-exporting');
    document.body.appendChild(exportRoot);
    paginateResume(exportElement, { gap: 0, bottomGuard: 24 });

    const resetDownloadButton = () => {
      if (exportRoot.parentNode) exportRoot.parentNode.removeChild(exportRoot);
      document.documentElement.classList.remove('is-pdf-exporting');
      document.body.classList.remove('is-pdf-exporting');
      if (oldZoom !== 1) {
        zoom = oldZoom;
        applyZoom();
      }
      btn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3" /></svg> Download PDF`;
      btn.disabled = false;
    };

    try {
      await new Promise(resolve => requestAnimationFrame(resolve));
      if (document.fonts?.ready) {
        await document.fonts.ready;
      }
      await Promise.all(Array.from(exportElement.querySelectorAll('img')).map(img => {
        if (img.complete) return Promise.resolve();
        return new Promise(resolve => {
          img.onload = resolve;
          img.onerror = resolve;
        });
      }));
      await flattenImagesForPdf(exportElement);
      paginateResume(exportElement, { gap: 0, bottomGuard: 24 });
      if (!window.html2canvas) {
        throw new Error('html2canvas library is not loaded');
      }
      const PDFCtor = window.jspdf?.jsPDF || window.jsPDF;
      if (!PDFCtor) {
        throw new Error('jsPDF library is not loaded');
      }
      const exportBounds = exportElement.getBoundingClientRect();
      // Engine pages are sized by paginateResume() to whole sheets; their scrollHeight
      // can include clipped sidebar padding, which must not become an extra page.
      const exportHeight = exportElement.classList.contains('cv2')
        ? Math.ceil(Math.max(parseFloat(exportElement.style.minHeight) || exportBounds.height, 1122))
        : Math.ceil(Math.max(exportBounds.height, exportElement.scrollHeight, 1122));
      const canvas = await html2canvas(exportElement, {
        scale: 2,
        useCORS: true,
        logging: false,
        width: 794,
        height: exportHeight,
        windowWidth: 1200,
        windowHeight: exportHeight,
        scrollX: 0,
        scrollY: 0
      });

      const pdf = new PDFCtor('p', 'mm', 'a4');
      const pageWidth = 210;
      const pageHeight = 297;
      const pdfLinks = collectPdfLinks(exportElement, pageWidth, pageHeight);
      const pdfText = collectPdfText(exportElement, pageWidth, pageHeight);
      const imgData = canvas.toDataURL('image/jpeg', 0.98);
      const imgHeight = (canvas.height * pageWidth) / canvas.width;
      let position = 0;
      let heightLeft = imgHeight;

      pdf.addImage(imgData, 'JPEG', 0, position, pageWidth, imgHeight);
      heightLeft -= pageHeight;

      while (heightLeft > 0) {
        position -= pageHeight;
        pdf.addPage();
        pdf.addImage(imgData, 'JPEG', 0, position, pageWidth, imgHeight);
        heightLeft -= pageHeight;
      }

      applyPdfText(pdf, pdfText, await loadPdfTextFont(pdf));
      applyPdfLinks(pdf, pdfLinks);
      pdf.save(fn);
    } catch (err) {
      console.error('PDF export failed', err);
      alert(`PDF export failed: ${err.message || 'Please refresh the page and try again.'}`);
    } finally {
      resetDownloadButton();
    }
  });
}

// ============================================================
// ---- MODERN UI LAYER (2026): editor drawer, mobile views,
//      accent presets, landing gallery, live thumbnails
// ============================================================

// ---- Template drawer: search, category filter, close, current label ----
function initTemplateDrawer() {
  const group = document.querySelector('.template-toolbar-group');
  const drawer = document.getElementById('template-selector');
  if (!group || !drawer) return;

  const search = document.getElementById('template-search');
  const cats = document.getElementById('template-cats');
  const empty = document.getElementById('template-empty');
  const closeBtn = document.getElementById('template-drawer-close');
  const buttons = Array.from(drawer.querySelectorAll('.tmpl-btn'));
  let activeCat = 'all';

  function applyFilter() {
    const q = (search?.value || '').trim().toLowerCase();
    let shown = 0;
    buttons.forEach(btn => {
      const name = (btn.dataset.name || '').toLowerCase();
      const id = (btn.dataset.tmpl || '').toLowerCase();
      const cat = (btn.dataset.cat || '');
      const matchesCat = activeCat === 'all' || cat.split(/\s+/).includes(activeCat);
      const matchesText = !q || name.includes(q) || id.includes(q);
      const show = matchesCat && matchesText;
      btn.hidden = !show;
      if (show) shown++;
    });
    if (empty) empty.hidden = shown > 0;
  }

  search?.addEventListener('input', applyFilter);

  cats?.addEventListener('click', (e) => {
    const chip = e.target.closest('.tcat');
    if (!chip) return;
    activeCat = chip.dataset.cat || 'all';
    cats.querySelectorAll('.tcat').forEach(c => c.classList.toggle('is-active', c === chip));
    applyFilter();
  });

  closeBtn?.addEventListener('click', () => closeTemplateDrawer());

  document.addEventListener('click', (e) => {
    if (group.classList.contains('is-collapsed')) return;
    if (!group.contains(e.target)) closeTemplateDrawer();
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !group.classList.contains('is-collapsed')) closeTemplateDrawer();
  });

  // Pick a template, then close on small screens so the preview is visible
  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      updateTemplateToggleLabel();
      if (window.matchMedia('(max-width: 900px)').matches) closeTemplateDrawer();
    });
  });

  applyFilter();
  updateTemplateToggleLabel();
}

function closeTemplateDrawer() {
  const group = document.querySelector('.template-toolbar-group');
  const toggle = document.getElementById('template-toggle');
  if (!group) return;
  group.classList.add('is-collapsed');
  toggle?.setAttribute('aria-expanded', 'false');
  document.body.classList.remove('drawer-open');
}

function updateTemplateToggleLabel() {
  const label = document.getElementById('template-toggle-current');
  if (!label) return;
  const active = document.querySelector(`.tmpl-btn[data-tmpl="${state.template}"]`);
  label.textContent = active?.dataset.name || state.template || 'Classic';
}

// ---- Accent colour presets ----
// The picker shows the colour actually in use: the template's own until the
// person chooses one.
function syncAccentInputs() {
  const current = effectiveAccent(state.template).toLowerCase();
  const input = document.getElementById('accent-color');
  if (input && input.value.toLowerCase() !== current) input.value = current;
  document.querySelectorAll('#accent-swatches .accent-swatch').forEach(sw => {
    sw.classList.toggle('is-active', (sw.dataset.color || '').toLowerCase() === current);
    sw.setAttribute('aria-pressed', String(sw.classList.contains('is-active')));
  });
}

function bindAccentSwatches() {
  const wrap = document.getElementById('accent-swatches');
  const input = document.getElementById('accent-color');
  if (!wrap) return;

  const syncActive = syncAccentInputs;

  wrap.addEventListener('click', (e) => {
    const sw = e.target.closest('.accent-swatch');
    if (!sw) return;
    state.accentColor = sw.dataset.color;
    state.accentCustom = true;
    if (input) input.value = state.accentColor;
    syncActive();
    renderTemplateThumbnails();
    renderPreview();
    saveToStorage();
  });

  input?.addEventListener('input', syncActive);
  syncActive();
}

// ---- Mobile editor view switcher (Edit / Preview) ----
function initEditorTabs() {
  const tabs = document.getElementById('editor-tabs');
  if (!tabs) return;
  tabs.addEventListener('click', (e) => {
    const tab = e.target.closest('.editor-tab');
    if (!tab) return;
    setEditorView(tab.dataset.view);
  });
  setEditorView('edit');
}

function setEditorView(view) {
  const tabs = document.getElementById('editor-tabs');
  if (!tabs) return;
  const target = view === 'preview' ? 'preview' : 'edit';
  document.body.dataset.editorView = target;
  tabs.querySelectorAll('.editor-tab').forEach(t => {
    const on = t.dataset.view === target;
    t.classList.toggle('is-active', on);
    t.setAttribute('aria-pressed', String(on));
  });
  requestAnimationFrame(() => {
    const preview = document.getElementById('resume-preview');
    if (preview) paginateResume(preview);
    applyZoom();
  });
}

// ---- Live template thumbnails ----
// The templates only exist at a fixed 794px A4 width, so a thumbnail is the real
// markup scaled down. The scale factor depends on the tile width, which changes
// with the viewport, so it is measured here rather than hard-coded in CSS.
const THUMB_PAGE_WIDTH = 794;

function setThumbScale(el) {
  const width = el.clientWidth;
  if (!width) return;
  el.style.setProperty('--thumb-scale', String(width / THUMB_PAGE_WIDTH));
}

function syncThumbScales() {
  document.querySelectorAll('[data-live-thumb], .tmpl-thumb').forEach(setThumbScale);
}

function paintLiveThumb(el) {
  if (el.dataset.thumbPainted === '1') return;
  const tmpl = el.dataset.liveThumb;
  if (!tmpl) return;
  el.dataset.thumbPainted = '1';
  try {
    el.innerHTML = thumbnailPageHtml(tmpl, buildTemplateThumbnailHtml(tmpl));
    setThumbScale(el);
  } catch (err) {
    el.classList.add('thumb-failed');
  }
}

// IntersectionObserver only reports a *change* in intersection state. A fast
// scroll (End key, a flick on mobile) can carry an element from below the fold to
// above it without a single intersecting frame in between, so the callback never
// runs and the element is left untouched forever. Every lazy behaviour therefore
// pairs the observer with a debounced scroll sweep that catches the stragglers.
function watchLazy(targets, apply, rootMargin) {
  if (!targets.length) return;

  const pending = new Set(targets);
  const run = (el) => {
    if (!pending.has(el)) return;
    pending.delete(el);
    apply(el);
  };

  if (!('IntersectionObserver' in window)) {
    targets.forEach(run);
    return;
  }

  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      io.unobserve(entry.target);
      run(entry.target);
    });
  }, { rootMargin });

  targets.forEach(el => io.observe(el));

  const sweep = () => {
    if (!pending.size) {
      window.removeEventListener('scroll', onScroll);
      return;
    }
    const limit = window.innerHeight + 600;
    Array.from(pending).forEach(el => {
      if (el.getBoundingClientRect().top < limit) {
        io.unobserve(el);
        run(el);
      }
    });
  };

  const onScroll = debounce(sweep, 140);
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
}

function initLiveThumbnails() {
  const targets = Array.from(document.querySelectorAll('[data-live-thumb]'));
  if (!targets.length) return;
  window.addEventListener('resize', debounce(syncThumbScales, 150));
  watchLazy(targets, paintLiveThumb, '500px 0px');
}

// ---- Landing page: template gallery filter + search ----
function initGalleryFilters() {
  const bar = document.getElementById('template-filters');
  const grid = document.getElementById('templates-grid');
  if (!grid) return;

  const search = document.getElementById('gallery-search');
  const empty = document.getElementById('gallery-empty');
  const count = document.getElementById('gallery-count');
  const cards = Array.from(grid.querySelectorAll('.template-card'));
  let activeCat = 'all';

  function applyFilter() {
    const q = (search?.value || '').trim().toLowerCase();
    let shown = 0;
    cards.forEach(card => {
      const name = (card.dataset.name || '').toLowerCase();
      const id = (card.dataset.template || '').toLowerCase();
      const cat = (card.dataset.cat || '');
      const matchesCat = activeCat === 'all' || cat.split(/\s+/).includes(activeCat);
      const matchesText = !q || name.includes(q) || id.includes(q);
      const show = matchesCat && matchesText;
      card.hidden = !show;
      if (show) shown++;
    });
    if (empty) empty.hidden = shown > 0;
    if (count) count.textContent = String(shown);
  }

  bar?.addEventListener('click', (e) => {
    const chip = e.target.closest('.tfilter');
    if (!chip) return;
    activeCat = chip.dataset.cat || 'all';
    bar.querySelectorAll('.tfilter').forEach(c => c.classList.toggle('is-active', c === chip));
    applyFilter();
  });

  search?.addEventListener('input', applyFilter);
  applyFilter();
}

// ---- Landing page: mobile navigation ----
function initMobileNav() {
  const toggle = document.getElementById('nav-toggle');
  const panel = document.getElementById('nav-links');
  if (!toggle || !panel) return;

  const close = () => {
    document.body.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
  };

  toggle.addEventListener('click', () => {
    const open = !document.body.classList.contains('nav-open');
    document.body.classList.toggle('nav-open', open);
    toggle.setAttribute('aria-expanded', String(open));
  });

  panel.addEventListener('click', (e) => {
    if (e.target.closest('a')) close();
  });

  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  window.addEventListener('resize', () => { if (window.innerWidth > 900) close(); });
}

// ---- Landing page: FAQ accordion ----
function initFaq() {
  document.querySelectorAll('.faq-item').forEach(item => {
    const btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', () => {
      const open = item.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', String(open));
    });
  });
}

// ---- Landing page: reveal-on-scroll (respects reduced motion) ----
function initReveal() {
  const items = Array.from(document.querySelectorAll('[data-reveal]'));
  if (!items.length) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) {
    items.forEach(el => el.classList.add('is-revealed'));
    return;
  }
  // Opt in only now that we know the observer will run, so a script failure
  // earlier in the file can never leave the page invisible.
  document.documentElement.classList.add('js-reveal');
  watchLazy(items, (el) => el.classList.add('is-revealed'), '0px 0px -40px 0px');
}
