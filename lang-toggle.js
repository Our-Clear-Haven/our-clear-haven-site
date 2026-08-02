(function(){
  var LANG_KEY='och_lang';
  function getLang(){try{return localStorage.getItem(LANG_KEY)||'en';}catch(e){return 'en';}}
  function setLang(l){try{localStorage.setItem(LANG_KEY,l);}catch(e){}}
  function apply(lang){
    document.querySelectorAll('[data-es]').forEach(function(el){
      if(el.dataset.enOrig===undefined) el.dataset.enOrig=el.textContent;
      el.textContent = lang==='es' ? el.dataset.es : el.dataset.enOrig;
    });
    document.querySelectorAll('[data-es-html]').forEach(function(el){
      if(el.dataset.enOrigHtml===undefined) el.dataset.enOrigHtml=el.innerHTML;
      el.innerHTML = lang==='es' ? el.dataset.esHtml : el.dataset.enOrigHtml;
    });
    document.querySelectorAll('[data-es-placeholder]').forEach(function(el){
      if(el.dataset.enOrigPlaceholder===undefined) el.dataset.enOrigPlaceholder=el.getAttribute('placeholder')||'';
      el.setAttribute('placeholder', lang==='es' ? el.dataset.esPlaceholder : el.dataset.enOrigPlaceholder);
    });
    document.documentElement.setAttribute('lang', lang);
    var btn=document.getElementById('langToggle');
    if(btn) btn.textContent = lang==='es' ? 'ENG' : 'ESP';
  }
  document.addEventListener('DOMContentLoaded', function(){
    apply(getLang());
    var btn=document.getElementById('langToggle');
    if(btn) btn.addEventListener('click', function(){
      var next = getLang()==='es' ? 'en' : 'es';
      setLang(next);
      apply(next);
    });
  });
})();
