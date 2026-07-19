// ===== AI · Perusteet — yhteinen sivulogiikka (v2) =====

// ---- GA4 (G-4ZLJF4THGV): basic consent mode, view-dimensio joka tapahtumaan ----
window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}
var GA_ID='G-4ZLJF4THGV';
function loadGA(){if(window.__gaLoaded)return;window.__gaLoaded=true;
  gtag('consent','default',{'analytics_storage':'granted','ad_storage':'denied','ad_user_data':'denied','ad_personalization':'denied'});
  gtag('js',new Date());gtag('config',GA_ID);
  var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+GA_ID;document.head.appendChild(s);}
function trackEvent(n,p){p=p||{};if(window.CI&&window.CI.view&&p.view==null)p.view=window.CI.view;
  if(window.__gaLoaded&&typeof gtag==='function')gtag('event',n,p);}
function consentChoice(v){try{localStorage.setItem('bcai-consent',v)}catch(e){}var b=document.getElementById('consent-banner');if(b)b.remove();if(v==='granted')loadGA();}
function initConsent(){var c=null;try{c=localStorage.getItem('bcai-consent')}catch(e){}
  if(c==='granted'){loadGA();}else if(c!=='denied'){var b=document.getElementById('consent-banner');if(b)b.style.display='flex';}}

// ---- Edistyminen (bcai-new): sama avain ja id-muoto (lesson-NN) kuin v1:ssä ----
function getDone(){try{return JSON.parse(localStorage.getItem('bcai-new')||'[]')}catch(e){return[]}}
function setDone(a){try{localStorage.setItem('bcai-new',JSON.stringify(a))}catch(e){}}
function isDone(id){return getDone().indexOf(id)>=0}
function toggleDone(id){var a=getDone(),i=a.indexOf(id);
  if(i>=0){a.splice(i,1);}else{a.push(id);var ai=(window.CI&&window.CI.allIds)?window.CI.allIds.indexOf(id):-1;trackEvent('lesson_complete',ai>=0?{lesson_id:id,lesson_num:ai+1}:{lesson_id:id});}
  setDone(a);updProg();updCards();updDoneBtn(id);}
function updDoneBtn(id){var btn=document.querySelector('.done-btn');if(!btn)return;var d=isDone(id);
  btn.classList.toggle('marked',d);btn.textContent=d?'✓ Suoritettu':'Merkitse suoritetuksi';}

function allIds(){
  if(window.CI&&window.CI.allIds)return window.CI.allIds;
  var els=document.querySelectorAll('[data-lessonid]');
  return Array.prototype.map.call(els,function(e){return e.getAttribute('data-lessonid')});
}
function updProg(){
  var ids=allIds();if(!ids.length)return;
  var done=getDone(),n=ids.filter(function(id){return done.indexOf(id)>=0}).length;
  var pb=document.getElementById('pb'),pt=document.getElementById('pt');
  if(pb)pb.style.width=(n/ids.length*100)+'%';
  if(pt)pt.textContent=n+'/'+ids.length;
  var dc=document.getElementById('done-cnt');if(dc)dc.textContent=Math.round(n/ids.length*100)+'%';
}
// Moduulikohtaiset edistymispalkit ja tuntirivien suoritusmerkit (yleiskuva/moduulisivut)
function updCards(){
  var done=getDone();
  document.querySelectorAll('[data-ospfill]').forEach(function(pf){
    var osp=pf.getAttribute('data-ospfill');
    var ids=(pf.getAttribute('data-ids')||'').split(',').filter(Boolean);
    var c=ids.filter(function(id){return done.indexOf(id)>=0}).length;
    pf.style.width=(ids.length?c/ids.length*100:0)+'%';
    var pt=document.querySelector('[data-osptxt="'+osp+'"]');
    if(pt)pt.textContent=c+' / '+ids.length;
  });
  document.querySelectorAll('[data-doneid]').forEach(function(el){
    el.classList.toggle('done',done.indexOf(el.getAttribute('data-doneid'))>=0);
  });
}

// ---- Välilehdet (ankkuri valitsee) ----
function showTab(name,pushHash){
  var panels=document.querySelectorAll('#lesson-panels .panel');
  var tabs=document.querySelectorAll('.lesson-tabs .tab-btn');
  var found=false;
  panels.forEach(function(p){var on=p.getAttribute('data-tab')===name;p.classList.toggle('active',on);if(on)found=true;});
  tabs.forEach(function(t){t.classList.toggle('active',t.getAttribute('data-tab')===name);});
  if(!found){return false;}
  if(pushHash!==false){try{history.replaceState(null,'','#'+name);}catch(e){location.hash=name;}}
  var lp=document.getElementById('lesson-panels');if(lp)lp.scrollTop=0;
  runMermaid();
  return true;
}
function tabFromHash(){
  var h=location.hash.replace(/^#/,'');
  if(h&&showTab(h,false))return;
  var first=document.querySelector('#lesson-panels .panel');
  if(first)showTab(first.getAttribute('data-tab'),false);
}

// ---- Näkymävaihtaja (bcai-view) ----
function rememberView(v){try{localStorage.setItem('bcai-view',v)}catch(e){}}
function initViewSwitch(){
  document.querySelectorAll('[data-view]').forEach(function(a){
    a.addEventListener('click',function(){rememberView(a.getAttribute('data-view'));});
  });
  // Valintasivu: korosta muistettu ovi
  var remembered=null;try{remembered=localStorage.getItem('bcai-view')}catch(e){}
  if(remembered){var door=document.querySelector('.door[data-view="'+remembered+'"]');if(door)door.classList.add('door--remembered');}
}

// ---- Diaesitys (koko näyttö) ----
function deckFull(btn){var w=btn.closest('.deck-wrap');if(!w)return;
  var fs=document.fullscreenElement||document.webkitFullscreenElement;
  if(!fs){(w.requestFullscreen||w.webkitRequestFullscreen).call(w);}
  else{(document.exitFullscreen||document.webkitExitFullscreen).call(document);}}
function deckFullSync(){var fs=document.fullscreenElement||document.webkitFullscreenElement;
  document.querySelectorAll('.deck-full-btn').forEach(function(b){b.textContent=fs?'⤢ Poistu koko näytöstä':'⛶ Koko näyttö';});}
document.addEventListener('fullscreenchange',deckFullSync);
document.addEventListener('webkitfullscreenchange',deckFullSync);
document.addEventListener('keydown',function(e){
  var fe=document.fullscreenElement||document.webkitFullscreenElement;
  if(!fe||!fe.classList||!fe.classList.contains('deck-wrap'))return;
  var d=fe.querySelector('.deck');if(!d)return;
  if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){d.scrollBy({left:d.clientWidth,behavior:'smooth'});e.preventDefault();}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){d.scrollBy({left:-d.clientWidth,behavior:'smooth'});e.preventDefault();}
});

// ---- Section-head-kortit + Suositeltu/Syventävä-pillit ----
function enhancePanels(){
  var root=document.getElementById('lesson-panels');if(!root)return;
  root.querySelectorAll('.task-card').forEach(function(c){
    var body=c.querySelector(':scope > .task-card-body');
    if(body&&body.children.length===0&&body.textContent.trim()===''){c.classList.add('is-sectionhead');}
  });
  root.querySelectorAll('h1,h2,h3,h4').forEach(function(h){
    if(!/SUOSITELTU|SYVENT[ÄA]V[ÄA]/.test(h.textContent))return;
    h.innerHTML=h.innerHTML
      .replace(/(?:🟢️?\s*)?SUOSITELTU/g,'<span class="pill pill--rec">Suositeltu</span>')
      .replace(/(?:🟣️?\s*)?SYVENT[ÄA]V[ÄA]/g,'<span class="pill pill--adv">Syventävä</span>');
  });
}

// ---- Mermaid ----
function runMermaid(){if(window.mermaid){try{mermaid.run({querySelector:'#lesson-panels .panel.active .mermaid'});}catch(e){}}}
function initMermaid(){if(!window.mermaid)return;
  mermaid.initialize({startOnLoad:false,theme:'base',fontFamily:'Hanken Grotesk, system-ui, sans-serif',
    themeVariables:{primaryColor:'#EEF1FD',primaryTextColor:'#15171E',primaryBorderColor:'#5B68C6',
      lineColor:'#6B5B73',secondaryColor:'#EFEAFB',tertiaryColor:'#E9F7F0',noteBkgColor:'#FFF6E6',
      noteTextColor:'#15171E',noteBorderColor:'#D9930B',fontSize:'14px',edgeLabelBackground:'#FDFCFA'}});}

// ---- Kopioi-linkki (opettaja: jaa opiskelijoille) ----
function copyShare(btn){var url=btn.getAttribute('data-url');var abs=location.origin+url;
  function ok(){var t=btn.textContent;btn.textContent='✓ Kopioitu';setTimeout(function(){btn.textContent=t;},1600);}
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(abs).then(ok,function(){prompt('Kopioi linkki:',abs);});}
  else{prompt('Kopioi linkki:',abs);}}

// ---- Skaalaa animoidut figuurit mahtumaan kapealle näytölle (ei leikkausta/vieritystä) ----
function fitAiDemos(){
  var stages=document.querySelectorAll('.ai-demo__stage');
  for(var i=0;i<stages.length;i++){(function(st){
    var fig=st.closest?st.closest('.ai-demo'):null;
    var fit=st.querySelector(':scope > .ai-demo__fit');
    if(!fit){
      var cs=st.style;
      fit=document.createElement('div'); fit.className='ai-demo__fit';
      fit.style.cssText='display:'+(cs.display||'flex')+';align-items:'+(cs.alignItems||'center')
        +';justify-content:'+(cs.justifyContent||'center')+';gap:'+(cs.gap||'0')
        +';padding:'+(cs.padding||'0')+';flex-shrink:0;box-sizing:border-box';
      while(st.firstChild){fit.appendChild(st.firstChild);}
      st.appendChild(fit);
      st.style.padding='0';
      var fr=fit.getBoundingClientRect();
      st.dataset.natw=Math.round(fr.width); st.dataset.nath=Math.round(fr.height);
      st.dataset.h0=parseFloat(cs.height)||Math.round(fr.height);
    }
    var natW=+st.dataset.natw, natH=+st.dataset.nath, h0=+st.dataset.h0, avail=st.clientWidth;
    var s=avail>0?Math.min(1, avail/natW):1;
    if(s<0.999){
      fit.style.transformOrigin='center center';
      fit.style.transform='scale('+s+')';
      st.style.height=Math.ceil(Math.max(natH,h0)*s)+'px';
    }else{
      fit.style.transform='none'; st.style.height=h0+'px';
    }
    if(fig)fig.classList.add('is-fitted');
  })(stages[i]);}
}
var __fitT; function fitAiDemosDebounced(){clearTimeout(__fitT);__fitT=setTimeout(fitAiDemos,120);}

// ---- Init ----
function ciInit(){
  initConsent();
  initMermaid();
  updProg();updCards();
  initViewSwitch();
  if(window.CI&&window.CI.lid){
    window.cid=window.CI.lid; // twReflect (practice.js) lukee bcai-reflect-avaimen tästä
    enhancePanels();
    tabFromHash();
    trackEvent('lesson_open',{lesson_id:window.CI.lid,lesson_num:window.CI.num,lesson_title:window.CI.title||window.CI.lid});
    if(window.CI.ptasks)initPractice(window.CI.lid,window.CI.ptasks);
    runMermaid();
  }
  fitAiDemos();
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',ciInit);}else{ciInit();}
window.addEventListener('load',fitAiDemos);
window.addEventListener('resize',fitAiDemosDebounced);
