import sys

def must_replace(path, old, new, count=1):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    actual = content.count(old)
    if actual != count:
        print(f"MISMATCH in {path}: expected {count}, found {actual}")
        sys.exit(1)
    content = content.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"OK: {path}")

EMAIL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'

# 1. style.css - add .foot-email rules
must_replace(
    'style.css',
    '.foot-social a svg{width:16px;height:16px}',
    '.foot-social a svg{width:16px;height:16px}\n.foot-email{color:var(--gold);font-weight:700;font-size:15px;display:inline-flex;align-items:center;gap:8px;margin:18px 0}\n.foot-email svg{width:18px;height:18px;flex-shrink:0}'
)

# 2. shared pages
SHARED_PAGES = ['index.html', 'get-involved.html', 'our-story.html', 'resources.html', 'grande-grand.html']
old_shared = '''    </div>
    <div class="foot-bottom">
      <span data-es-html="Contacto: <a href=&quot;mailto:contact@ourclearhaven.org&quot;>contact@ourclearhaven.org</a>">Contact: <a href="mailto:contact@ourclearhaven.org">contact@ourclearhaven.org</a></span>
      <span>&copy; 2026 <span class="logo-text">Our Clear Haven</span> &middot; Bend, Oregon</span>'''
new_shared = f'''    </div>
    <a class="foot-email" href="mailto:contact@ourclearhaven.org">{EMAIL_SVG}<span>contact@ourclearhaven.org</span></a>
    <div class="foot-bottom">
      <span>&copy; 2026 <span class="logo-text">Our Clear Haven</span> &middot; Bend, Oregon</span>'''

for page in SHARED_PAGES:
    must_replace(page, old_shared, new_shared)

# 3. crystal-clear-app.html
must_replace(
    'crystal-clear-app.html',
    '.cca-foot-social a svg{width:16px;height:16px}',
    '.cca-foot-social a svg{width:16px;height:16px}\n.cca-foot-email{color:var(--teal);font-weight:700;font-size:15px;display:inline-flex;align-items:center;gap:8px;margin:18px 0}\n.cca-foot-email svg{width:18px;height:18px;flex-shrink:0}'
)
old_cca = '''    </div>
    <div class="cca-foot-bottom">
      <span data-es-html="Contacto: <a href=&quot;mailto:contact@ourclearhaven.org&quot;>contact@ourclearhaven.org</a>">Contact: <a href="mailto:contact@ourclearhaven.org">contact@ourclearhaven.org</a></span>
      <span>&copy; 2026 <span class="logo-text">Our Clear Haven</span> &middot; Bend, Oregon</span>'''
new_cca = f'''    </div>
    <a class="cca-foot-email" href="mailto:contact@ourclearhaven.org">{EMAIL_SVG}<span>contact@ourclearhaven.org</span></a>
    <div class="cca-foot-bottom">
      <span>&copy; 2026 <span class="logo-text">Our Clear Haven</span> &middot; Bend, Oregon</span>'''
must_replace('crystal-clear-app.html', old_cca, new_cca)

# 4. dual-board.html
must_replace(
    'dual-board.html',
    '.db-foot-social a svg{width:16px;height:16px}',
    '.db-foot-social a svg{width:16px;height:16px}\n.db-foot-email{color:var(--gold);font-weight:700;font-size:15px;display:inline-flex;align-items:center;gap:8px;margin:18px 0}\n.db-foot-email svg{width:18px;height:18px;flex-shrink:0}'
)
old_db = '''    </div>
    <div class="db-foot-bottom">
      <span data-es-html="Contacto: <a href=&quot;mailto:contact@ourclearhaven.org&quot;>contact@ourclearhaven.org</a>">Contact: <a href="mailto:contact@ourclearhaven.org">contact@ourclearhaven.org</a></span>
      <span>&copy; 2026 <span class="logo-text">Our Clear Haven</span> &middot; Bend, Oregon</span>'''
new_db = f'''    </div>
    <a class="db-foot-email" href="mailto:contact@ourclearhaven.org">{EMAIL_SVG}<span>contact@ourclearhaven.org</span></a>
    <div class="db-foot-bottom">
      <span>&copy; 2026 <span class="logo-text">Our Clear Haven</span> &middot; Bend, Oregon</span>'''
must_replace('dual-board.html', old_db, new_db)

print("ALL DONE")
