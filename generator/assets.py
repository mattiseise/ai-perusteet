"""Yhteiset asset-tiedostot: site.js (edistyminen, tabit, consent/GA, näkymävaihtaja,
mermaid-init) ja practice.js (Harjoittele-moottori). assets/site.css on erillinen
committoitu lähde (siirretty v1:n f-string-CSS:stä).

Nämä kirjoitetaan tiedostoiksi write_assets():ssä. Merkkijonot ovat tavallisia
(yksinkertaiset aaltosulkeet) — niitä ei interpoloida f-stringeihin.
"""

import os

# ===== Harjoittele-tehtävämoottori (siirretty v1:n PRACTICE_JS:stä; initPractice
# ottaa nyt tehtävälistan parametrina yksittäisen sivun globaalin L:n sijaan) =====
PRACTICE_JS = r"""// ===== Harjoittele-tehtävämoottori =====
function prGet(){try{return JSON.parse(localStorage.getItem('bcai-practice')||'{}')}catch(e){return{}}}
function prSet(o){try{localStorage.setItem('bcai-practice',JSON.stringify(o))}catch(e){}}
function prKey(lid,ti){return lid+'/'+ti}
function twShuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function twEl(tag,cls,html){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;
  if(cls&&cls.split(' ').indexOf('tw-fb')>=0){e.setAttribute('role','status');e.setAttribute('aria-live','polite');e.setAttribute('aria-atomic','true');}
  return e}
function initPractice(lid,tasks){
  if(!tasks||!tasks.length)return;
  document.querySelectorAll('#lesson-panels .task-widget').forEach(w=>{
    const ti=+w.dataset.ti,task=tasks[ti];
    if(!task||w.dataset.init)return;w.dataset.init='1';
    renderTask(w,task,lid,ti);
  });
  updatePracticeGuide();
}
// ---- Harjoittele-ohjaus: silta teoriassa, footer-chip, tab-laskuri ja
// valmistumiskortti elävät bcai-practice-tilan mukaan. Pehmeä ohjaus:
// mitään ei disabloida, vain visuaalinen hierarkia vaihtuu. ----
function practiceGuideState(){
  var ci=window.CI||{};var t=ci.ptasks;
  if(!t||!t.length||!ci.lid)return null;
  var st=prGet(),n=t.length,d=0;
  for(var i=0;i<n;i++){if(st[prKey(ci.lid,i)])d++;}
  return{n:n,done:d,all:d>=n};
}
function updatePracticeGuide(){
  var s=practiceGuideState();if(!s)return;
  var txt=document.querySelector('[data-practice-bridge-txt]');
  if(txt)txt.textContent=s.all?('Kaikki '+s.n+' tehtävää tehty ✓')
    :(s.done>0?(s.done+' / '+s.n+' tehtävää tehty'):(s.n+' tehtävää'));
  var br=document.querySelector('[data-practice-bridge]');
  if(br)br.classList.toggle('all-done',s.all);
  var chip=document.querySelector('[data-practice-chip]');
  if(chip){chip.hidden=s.all;
    var c=chip.querySelector('[data-practice-chip-count]');
    if(c)c.textContent=s.done+' / '+s.n;}
  var ft=document.getElementById('lesson-footer');
  if(ft)ft.classList.toggle('guide-practice',!s.all);
  var tc=document.querySelector('[data-practice-tabcount]');
  if(tc){tc.hidden=false;tc.textContent=s.done+' / '+s.n;}
  var pc=document.querySelector('[data-practice-complete]');
  if(pc)pc.hidden=!s.all;
}
function renderTask(w,task,lid,ti){
  w.innerHTML='';
  const typeNames={quiz:'Monivalinta',classify:'Luokittelu',order:'Järjestäminen',match:'Yhdistä parit',scenario:'Skenaario',spot:'Etsi kohdat',reflect:'Omin sanoin'};
  const head=twEl('div','tw-head');
  head.appendChild(twEl('div','tw-type',typeNames[task.type]||'Tehtävä'));
  head.appendChild(twEl('h3',null,task.title||''));
  if(task.intro)head.appendChild(twEl('p','tw-intro',task.intro));
  w.appendChild(head);
  const st=prGet()[prKey(lid,ti)];
  if(st)head.appendChild(twEl('div','tw-prev','✓ Tehty aiemmin'+(st.m?(' · '+st.s+' / '+st.m):'')));
  const body=twEl('div','tw-body');w.appendChild(body);
  let started=false;
  const api={
    mark:function(){if(!started){started=true;trackEvent('task_start',{lesson_id:lid,task_id:prKey(lid,ti),task_type:task.type});}},
    done:function(s,m){
      const o=prGet();o[prKey(lid,ti)]={s:s,m:m,t:Date.now()};prSet(o);
      trackEvent('task_complete',{lesson_id:lid,task_id:prKey(lid,ti),task_type:task.type,score:s,max:m});
      updatePracticeGuide();
      const f=twEl('div','tw-foot');
      f.appendChild(twEl('span','tw-score',m!=null?('Tulos: '+s+' / '+m):'Valmis'));
      const rb=twEl('button','tw-redo','Tee uudelleen');
      rb.onclick=function(){renderTask(w,task,lid,ti)};
      f.appendChild(rb);w.appendChild(f);
    }
  };
  const renderers={quiz:twQuiz,classify:twClassify,order:twOrder,match:twMatch,scenario:twScenario,spot:twSpot,reflect:twReflect};
  if(renderers[task.type])renderers[task.type](body,task,api);
}
function twClassify(body,task,api){
  let i=0,score=0;
  const prog=twEl('div','tw-prog'),card=twEl('div','tw-card'),cats=twEl('div','tw-opts'),fb=twEl('div','tw-fb'),nxt=twEl('button','tw-next','Seuraava');
  body.append(prog,card,cats,fb,nxt);nxt.style.display='none';
  function show(){
    fb.className='tw-fb';fb.innerHTML='';nxt.style.display='none';
    prog.textContent=(i+1)+' / '+task.items.length;
    card.innerHTML=task.items[i].text;cats.innerHTML='';
    task.categories.forEach(function(c,ci){
      const b=twEl('button','tw-opt',c);
      b.onclick=function(){api.mark();answer(ci,b)};
      cats.appendChild(b);
    });
  }
  function answer(ci,btn){
    const it=task.items[i],ok=ci===it.answer;
    cats.querySelectorAll('button').forEach(function(b){b.disabled=true});
    btn.classList.add(ok?'ok':'no');
    if(ok)score++;else cats.children[it.answer].classList.add('ok');
    fb.className='tw-fb show '+(ok?'ok':'no');
    fb.innerHTML=(ok?'<strong>Oikein.</strong> ':'<strong>Ei aivan — oikea vastaus: '+task.categories[it.answer]+'.</strong> ')+(it.explain||'');
    nxt.style.display='inline-block';
    nxt.textContent=i<task.items.length-1?'Seuraava':'Näytä tulos';
    nxt.onclick=function(){i++;if(i<task.items.length)show();else finish()};
  }
  function finish(){
    prog.remove();card.remove();cats.remove();nxt.remove();
    fb.className='tw-fb show '+(score===task.items.length?'ok':'mid');
    fb.innerHTML='<strong>'+score+' / '+task.items.length+' oikein.</strong>'+(task.summary?('<br>'+task.summary):'');
    api.done(score,task.items.length);
  }
  show();
}
function twQuiz(body,task,api){
  let i=0,score=0;
  const prog=twEl('div','tw-prog'),q=twEl('div','tw-card'),opts=twEl('div','tw-opts tw-vert'),fb=twEl('div','tw-fb'),nxt=twEl('button','tw-next','Seuraava');
  body.append(prog,q,opts,fb,nxt);nxt.style.display='none';
  let shOpts=[];
  function show(){
    fb.className='tw-fb';fb.innerHTML='';nxt.style.display='none';
    prog.textContent=(i+1)+' / '+task.items.length;
    q.innerHTML=task.items[i].q;opts.innerHTML='';
    shOpts=twShuffle(task.items[i].options.slice());
    shOpts.forEach(function(o){
      const b=twEl('button','tw-opt',o.text);
      b.onclick=function(){api.mark();ans(o,b)};
      opts.appendChild(b);
    });
  }
  function ans(o,btn){
    const ok=!!o.correct;
    opts.querySelectorAll('button').forEach(function(b){b.disabled=true});
    btn.classList.add(ok?'ok':'no');
    if(ok)score++;else shOpts.forEach(function(so,x){if(so.correct)opts.children[x].classList.add('ok')});
    fb.className='tw-fb show '+(ok?'ok':'no');
    fb.innerHTML=(ok?'<strong>Oikein.</strong> ':'<strong>Ei aivan.</strong> ')+(o.explain||'');
    nxt.style.display='inline-block';
    nxt.textContent=i<task.items.length-1?'Seuraava':'Näytä tulos';
    nxt.onclick=function(){i++;if(i<task.items.length)show();else fin()};
  }
  function fin(){
    prog.remove();q.remove();opts.remove();nxt.remove();
    fb.className='tw-fb show '+(score===task.items.length?'ok':'mid');
    fb.innerHTML='<strong>'+score+' / '+task.items.length+' oikein.</strong>'+(task.summary?('<br>'+task.summary):'');
    api.done(score,task.items.length);
  }
  show();
}
function twOrder(body,task,api){
  let pos=0,miss=0;
  const seq=twEl('ol','tw-seq'),pool=twEl('div','tw-opts'),fb=twEl('div','tw-fb');
  body.append(seq,pool,fb);
  twShuffle(task.steps.map(function(s,si){return{s:s,si:si}})).forEach(function(o){
    const b=twEl('button','tw-opt',o.s);
    b.onclick=function(){
      api.mark();
      if(o.si===pos){
        b.remove();seq.appendChild(twEl('li',null,o.s));pos++;
        fb.className='tw-fb';fb.innerHTML='';
        if(pos===task.steps.length){
          const perfect=miss===0;
          fb.className='tw-fb show '+(perfect?'ok':'mid');
          fb.innerHTML='<strong>Järjestys valmis'+(perfect?' — ensimmäisellä yrityksellä!':' ('+miss+' hutia).')+'</strong>'+(task.summary?('<br>'+task.summary):'');
          api.done(Math.max(task.steps.length-miss,0),task.steps.length);
        }
      }else{
        miss++;b.classList.add('shake');setTimeout(function(){b.classList.remove('shake')},400);
        fb.className='tw-fb show no';fb.innerHTML=task.missHint||'Ei vielä — mieti, mikä vaihe tulee seuraavaksi.';
      }
    };
    pool.appendChild(b);
  });
}
function twMatch(body,task,api){
  let selA=null,got=0,miss=0;
  const wrap=twEl('div','tw-match'),colA=twEl('div','tw-col'),colB=twEl('div','tw-col'),fb=twEl('div','tw-fb');
  wrap.append(colA,colB);body.append(wrap,fb);
  task.pairs.forEach(function(p,pi){
    const b=twEl('button','tw-opt',p.a);b.dataset.pi=pi;
    b.onclick=function(){api.mark();colA.querySelectorAll('button').forEach(function(x){x.classList.remove('sel')});selA=b;b.classList.add('sel')};
    colA.appendChild(b);
  });
  twShuffle(task.pairs.map(function(p,pi){return{t:p.b,pi:pi}})).forEach(function(o){
    const b=twEl('button','tw-opt',o.t);
    b.onclick=function(){
      api.mark();
      if(!selA){fb.className='tw-fb show';fb.textContent='Valitse ensin käsite vasemmalta.';return}
      if(+selA.dataset.pi===o.pi){
        const p=task.pairs[o.pi];
        selA.classList.remove('sel');selA.classList.add('ok');b.classList.add('ok');
        selA.disabled=true;b.disabled=true;selA=null;got++;
        if(got===task.pairs.length){
          fb.className='tw-fb show '+(miss===0?'ok':'mid');
          fb.innerHTML='<strong>Kaikki parit löytyivät'+(miss?' ('+miss+' hutia).':' — ensimmäisellä yrityksellä!')+'</strong>'+(task.summary?('<br>'+task.summary):'');
          api.done(Math.max(task.pairs.length-miss,0),task.pairs.length);
        }else{
          fb.className='tw-fb show ok';fb.innerHTML='<strong>'+p.a+'</strong> — '+(p.explain||'oikein.');
        }
      }else{
        miss++;b.classList.add('shake');setTimeout(function(){b.classList.remove('shake')},400);
        fb.className='tw-fb show no';fb.textContent='Ei pari. Kokeile uudelleen.';
      }
    };
    colB.appendChild(b);
  });
}
function twScenario(body,task,api){
  const card=twEl('div','tw-card'),opts=twEl('div','tw-opts tw-vert'),fb=twEl('div','tw-fb');
  body.append(card,opts,fb);
  function go(idn){
    const n=task.nodes[idn];if(!n)return;
    card.innerHTML=n.text;opts.innerHTML='';fb.className='tw-fb';fb.innerHTML='';
    if(n.end){
      fb.className='tw-fb show '+(n.verdict||'mid');fb.innerHTML=n.feedback||'';
      const rb=twEl('button','tw-next','Aloita alusta');
      rb.onclick=function(){renderTaskRestart()};
      opts.appendChild(rb);
      api.done(n.score!=null?n.score:1,task.max!=null?task.max:1);
      return;
    }
    (n.choices||[]).forEach(function(c){
      const b=twEl('button','tw-opt',c.label);
      b.onclick=function(){
        api.mark();
        opts.querySelectorAll('button').forEach(function(x){x.disabled=true});
        b.classList.add('sel');
        if(c.feedback){
          fb.className='tw-fb show '+(c.tone||'');fb.innerHTML=c.feedback;
          const cont=twEl('button','tw-next','Jatka');
          cont.onclick=function(){go(c.next)};
          opts.appendChild(cont);cont.disabled=false;
        }else{
          go(c.next);
        }
      };
      opts.appendChild(b);
    });
  }
  function renderTaskRestart(){go(task.start)}
  go(task.start);
}
function twSpot(body,task,api){
  const info=twEl('div','tw-prog','Napauta epäilyttävät kohdat — valinta korostuu. Tarkista lopuksi.');
  const txt=twEl('div','tw-spottext'),fb=twEl('div','tw-fb'),chk=twEl('button','tw-next','Tarkista');
  body.append(info,txt,fb,chk);
  const segs=task.segments.map(function(sg){
    const b=twEl('button','tw-seg',sg.text);
    b.onclick=function(){api.mark();b.classList.toggle('sel')};
    txt.appendChild(b);txt.appendChild(document.createTextNode(' '));
    return{sg:sg,b:b};
  });
  chk.onclick=function(){
    let hits=0,misses=0,fas=0;const notes=[];
    segs.forEach(function(o){
      const sel=o.b.classList.contains('sel');o.b.disabled=true;o.b.classList.remove('sel');
      if(o.sg.flag&&sel){hits++;o.b.classList.add('ok');notes.push('<li><strong>Löysit:</strong> '+(o.sg.explain||'')+'</li>');}
      else if(o.sg.flag&&!sel){misses++;o.b.classList.add('miss');notes.push('<li><strong>Jäi huomaamatta:</strong> '+(o.sg.explain||'')+'</li>');}
      else if(!o.sg.flag&&sel){fas++;o.b.classList.add('fa');notes.push('<li><strong>Turha epäily:</strong> '+(o.sg.explain||'Tämä kohta oli kunnossa.')+'</li>');}
    });
    chk.remove();info.remove();
    const max=segs.filter(function(o){return o.sg.flag}).length;
    fb.className='tw-fb show '+(hits===max&&fas===0?'ok':(hits>0?'mid':'no'));
    fb.innerHTML='<strong>'+hits+' / '+max+' löydetty'+(fas?', '+fas+' turhaa epäilyä':'')+'.</strong><ul class="tw-notes">'+notes.join('')+'</ul>'+(task.summary?('<div>'+task.summary+'</div>'):'');
    api.done(hits,max);
  };
}
function twReflect(body,task,api){
  const KEY='bcai-reflect';
  function rGet(){try{return JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){return{}}}
  function rSet(o){try{localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}}
  const rid=(cid||'')+'/'+(task.title||'');
  const minc=task.min_chars||60;
  const p=twEl('label','tw-card',task.prompt||'');
  const ta=twEl('textarea','tw-ta');ta.rows=5;ta.placeholder='Kirjoita tähän omin sanoin...';
  ta.id='tw-reflect-'+Math.random().toString(36).slice(2);p.htmlFor=ta.id;
  ta.value=(rGet()[rid]||'');
  const cnt=twEl('div','tw-prog'),rev=twEl('button','tw-next','Näytä asiantuntijan näkökulma'),fb=twEl('div','tw-fb');
  body.append(p,ta,cnt,rev,fb);
  function upd(){const n=ta.value.trim().length;cnt.textContent=n+' / '+minc+' merkkiä';rev.disabled=n<minc;}
  ta.oninput=function(){api.mark();const o=rGet();o[rid]=ta.value;rSet(o);upd();};
  upd();
  rev.onclick=function(){
    rev.remove();ta.readOnly=true;
    fb.className='tw-fb show';
    let h='<strong>Asiantuntijan näkökulma:</strong><br>'+(task.expert||'');
    if(task.checklist&&task.checklist.length){
      h+='<div class="tw-checkwrap"><strong>Vertaa omaan vastaukseesi:</strong>';
      task.checklist.forEach(function(c,ci){h+='<label class="tw-check"><input type="checkbox" data-ci="'+ci+'"> '+c+'</label>'});
      h+='</div>';
    }
    fb.innerHTML=h;
    const fin=twEl('button','tw-next','Valmis');
    fb.appendChild(fin);
    fin.onclick=function(){
      const n=fb.querySelectorAll('input:checked').length;
      fin.remove();fb.querySelectorAll('input').forEach(function(x){x.disabled=true});
      api.done(n,(task.checklist||[]).length||null);
    };
  };
}
"""


# ===== Yhteinen sivulogiikka =====
# window.CI on per-sivu-konfiguraatio (view, lid, num, total, ptasks) — asetetaan
# tuntisivujen inline-skriptissä. Muut sivut jättävät sen määrittelemättä.
SITE_JS = r"""// ===== AI · Perusteet — yhteinen sivulogiikka (v2) =====

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
function updDoneBtn(id){var d=isDone(id);
  document.querySelectorAll('.done-btn').forEach(function(btn){
    btn.classList.toggle('marked',d);btn.textContent=d?'✓ Suoritettu':'Merkitse suoritetuksi';});}

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
  panels.forEach(function(p){var on=p.getAttribute('data-tab')===name;p.classList.toggle('active',on);p.hidden=!on;if(on)found=true;});
  tabs.forEach(function(t){var on=t.getAttribute('data-tab')===name;t.classList.toggle('active',on);t.setAttribute('aria-selected',on?'true':'false');t.tabIndex=on?0:-1;});
  if(!found){return false;}
  if(pushHash!==false){try{history.replaceState(null,'','#'+name);}catch(e){location.hash=name;}
    scrollToTabs();}
  var lp=document.getElementById('lesson-panels');if(lp)lp.scrollTop=0;
  runMermaid();
  return true;
}
// Välilehden vaihto vierittää uuden sisällön alkuun. Sivu vierittyy dokumentti-
// tasolla (lesson-panels ei ole vieritysalue), joten pelkkä scrollTop=0 ei riitä:
// alalaidasta (esim. teorian lopun Harjoittele-sillasta) vaihtava jäi katsomaan
// uuden paneelin loppua. Vieritetään VAIN ylöspäin, ettei sivun yläosassa oleva
// käyttäjä hyppää alaspäin tabia vaihtaessaan. Sticky-yläpalkin korkeus vähennetään.
function scrollToTabs(){
  var tabs=document.getElementById('lesson-tabs');if(!tabs||!window.scrollTo)return;
  var bar=document.querySelector('.topbar');
  var off=(bar&&getComputedStyle(bar).position==='sticky')?bar.getBoundingClientRect().height:0;
  var y=window.scrollY+tabs.getBoundingClientRect().top-off;
  if(y<0)y=0;
  if(y>=window.scrollY)return;
  var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  try{window.scrollTo({top:y,behavior:rm?'auto':'smooth'});}catch(e){window.scrollTo(0,y);}
}
function initTabs(){var list=document.querySelector('.lesson-tabs[role="tablist"]');if(!list)return;
  list.addEventListener('keydown',function(e){var tabs=Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));var i=tabs.indexOf(document.activeElement);if(i<0)return;var n=i;
    if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;else return;
    e.preventDefault();tabs[n].focus();showTab(tabs[n].getAttribute('data-tab'));
  });
}
function initDemoKeyboard(){document.querySelectorAll('.ai-demo[data-demo-kind="interactive"] label[for]').forEach(function(label){
  var input=document.getElementById(label.htmlFor);if(input){input.addEventListener('focus',function(){label.classList.add('demo-focus');});input.addEventListener('blur',function(){label.classList.remove('demo-focus');});}
  });
}
function initL20Quiz(){
  var wrap=document.querySelector('.l20q-wrap');if(!wrap)return;
  var rounds=[1,2,3].map(function(i){return wrap.querySelector('.l20q-round.r'+i);});
  var prog=wrap.querySelector('.l20q-prog');
  var live=document.createElement('span');live.className='sr-only';live.setAttribute('role','status');live.setAttribute('aria-live','polite');wrap.appendChild(live);
  function show(i,focus){
    rounds.forEach(function(r,ix){if(!r)return;if(ix+1===i){r.removeAttribute('hidden');}else{r.setAttribute('hidden','');}});
    if(prog)prog.textContent='tilanne '+i+'/3';
    live.textContent='';
    if(focus){var sc=rounds[i-1]&&rounds[i-1].querySelector('.l20q-sc');if(sc)sc.focus();}
  }
  rounds.forEach(function(r,ix){
    if(!r)return;
    var btn=r.querySelector('.l20q-next');
    r.querySelectorAll('.l20q-in').forEach(function(inp){
      inp.addEventListener('change',function(){
        if(btn)btn.disabled=false;
        var lab=r.querySelector('label[for="'+inp.id+'"]');
        var cls=inp.id.replace('l20q-','f');
        var fb=r.querySelector('.l20q-fb.'+cls);
        live.textContent=fb?fb.textContent:'';
      });
    });
    if(btn)btn.addEventListener('click',function(){
      if(btn.classList.contains('l20q-restart')){
        wrap.querySelectorAll('.l20q-in').forEach(function(inp){inp.checked=false;});
        rounds.forEach(function(rr){var b=rr&&rr.querySelector('.l20q-next');if(b)b.disabled=true;});
        show(1,true);
      }else{
        show(ix+2,true);
      }
    });
  });
  show(1,false);
}
function initScrollableRegions(){document.querySelectorAll('.panel table').forEach(function(table){table.tabIndex=0;});}
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
  document.querySelectorAll('.deck-full-btn').forEach(function(b){b.textContent=fs?'⤢ Poistu koko näytöstä':'⛶ Koko näyttö';b.setAttribute('aria-label',fs?'Poistu diaesityksen koko näytön tilasta':'Avaa diaesitys koko näytön tilaan');});}
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
// Fallback reflow-järjestelmän rinnalla: interaktiivisilla demoilla (data-demo-kind=
// "interactive") on oma aito mobiilitaitto ja ne ohitetaan; staattisilla skaalaus
// kattaa 431-680 px -välin, ja <=430 px reflow-kortti (.ai-demo__mobile-model, joka
// jätetään stagen suoraksi lapseksi) korvaa skaalatun sisällön kokonaan.
function fitAiDemos(){
  var stages=document.querySelectorAll('.ai-demo__stage');
  for(var i=0;i<stages.length;i++){(function(st){
    var fig=st.closest?st.closest('.ai-demo'):null;
    if(fig&&fig.getAttribute('data-demo-kind')==='interactive')return;
    var fit=st.querySelector(':scope > .ai-demo__fit');
    if(!fit){
      var cs=st.style;
      fit=document.createElement('div'); fit.className='ai-demo__fit';
      fit.style.cssText='display:'+(cs.display||'flex')+';align-items:'+(cs.alignItems||'center')
        +';justify-content:'+(cs.justifyContent||'center')+';gap:'+(cs.gap||'0')
        +';padding:'+(cs.padding||'0')+';flex-shrink:0;box-sizing:border-box';
      var kids=[],c;
      for(c=st.firstChild;c;c=c.nextSibling){kids.push(c);}
      for(var j=0;j<kids.length;j++){
        c=kids[j];
        if(c.nodeType===1&&c.classList&&c.classList.contains('ai-demo__mobile-model'))continue;
        fit.appendChild(c);
      }
      st.insertBefore(fit,st.firstChild);
      st.style.padding='0';
      if(parseFloat(cs.height))st.dataset.h0=parseFloat(cs.height);
    }
    if(!(+st.dataset.natw>0)){
      var fr=fit.getBoundingClientRect();
      if(fr.width<10)return; // piilossa (<=430 px reflow-tila) — mitataan kun tulee nakyviin
      st.dataset.natw=Math.round(fr.width); st.dataset.nath=Math.round(fr.height);
      if(!st.dataset.h0)st.dataset.h0=Math.round(fr.height);
    }
    var natW=+st.dataset.natw, natH=+st.dataset.nath, h0=+st.dataset.h0||natH, avail=st.clientWidth;
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

// ---- Demo-ohjaimet: nakyvyyskaynnistys, Pysayta/Jatka, Toista alusta ----
function adSetPaused(fig,paused){
  fig.classList.toggle('ad-paused',paused);
  var b=fig.querySelector('.ad-toggle');
  if(b&&!b.disabled){b.textContent=paused?'Jatka':'Pysäytä';}
}
function adEnd(fig){
  fig.classList.add('ad-ended');
  var b=fig.querySelector('.ad-toggle');
  if(b){b.disabled=true;b.textContent='Valmis';}
}
function adArmEnd(fig){
  if(!fig.querySelector('[data-once]'))return;
  clearTimeout(fig.__adT);
  var wrap=fig.querySelector('[data-once]');
  var dur=parseFloat(getComputedStyle(wrap).animationDuration)||0;
  if(dur>0){var left=Math.max(0,dur-(fig.__adEl||0));var t0=Date.now();
    fig.__adT=setTimeout(function(){fig.__adEl=dur;adEnd(fig);},left*1000+200);
    fig.__adT0=t0;}
}
function adHold(fig){clearTimeout(fig.__adT);
  if(fig.__adT0){fig.__adEl=(fig.__adEl||0)+(Date.now()-fig.__adT0)/1000;fig.__adT0=null;}}
function adRestart(fig){
  var st=fig.querySelector('.ai-demo__stage');
  fig.classList.remove('ad-ended');fig.__adEl=0;fig.__adUser=false;
  var b=fig.querySelector('.ad-toggle');
  if(b){b.disabled=false;}
  st.classList.add('ad-reset');void st.offsetHeight;st.classList.remove('ad-reset');
  adSetPaused(fig,false);adArmEnd(fig);
}
function initDemoCtrls(){
  if(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  var figs=document.querySelectorAll('.ai-demo');
  var io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){
    es.forEach(function(e){var fig=e.target;
      if(fig.classList.contains('ad-ended')||fig.__adUser)return;
      if(e.isIntersecting){adSetPaused(fig,false);adArmEnd(fig);}
      else{adSetPaused(fig,true);adHold(fig);}
    });
  },{threshold:0.3}):null;
  for(var i=0;i<figs.length;i++){(function(fig){
    var st=fig.querySelector('.ai-demo__stage');if(!st)return;
    if(!fig.querySelector('[data-once]'))return;
    if(fig.getAttribute('data-demo-kind')==='interactive')return;
    var bar=document.createElement('div');bar.className='ai-demo__ctrl';
    var tg=document.createElement('button');tg.type='button';tg.className='ad-btn ad-toggle';
    tg.textContent='Jatka';
    var rs=document.createElement('button');rs.type='button';rs.className='ad-btn ad-restart';rs.textContent='Toista alusta';
    bar.appendChild(tg);bar.appendChild(rs);
    var cap=fig.querySelector('figcaption');
    fig.insertBefore(bar,cap||null);
    tg.addEventListener('click',function(){
      var p=!fig.classList.contains('ad-paused');
      fig.__adUser=p;adSetPaused(fig,p);
      if(p)adHold(fig);else adArmEnd(fig);
    });
    rs.addEventListener('click',function(){adRestart(fig);});
    adSetPaused(fig,true);
    if(io)io.observe(fig);else{adSetPaused(fig,false);adArmEnd(fig);}
  })(figs[i]);}
}

// ---- Init ----
function ciInit(){
  initConsent();
  initMermaid();
  updProg();updCards();
  initViewSwitch();
  initTabs();
  initDemoKeyboard();
  initL20Quiz();
  initScrollableRegions();
  if(window.CI&&window.CI.lid){
    window.cid=window.CI.lid; // twReflect (practice.js) lukee bcai-reflect-avaimen tästä
    enhancePanels();
    tabFromHash();
    trackEvent('lesson_open',{lesson_id:window.CI.lid,lesson_num:window.CI.num,lesson_title:window.CI.title||window.CI.lid});
    if(window.CI.ptasks)initPractice(window.CI.lid,window.CI.ptasks);
    runMermaid();
  }
  fitAiDemos();
  initDemoCtrls();
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',ciInit);}else{ciInit();}
window.addEventListener('load',fitAiDemos);
window.addEventListener('resize',fitAiDemosDebounced);
"""


def write_assets(out_dir):
    """Kirjoittaa assets/site.js ja assets/practice.js. site.css on committoitu erikseen."""
    adir = os.path.join(out_dir, 'assets')
    os.makedirs(adir, exist_ok=True)
    with open(os.path.join(adir, 'practice.js'), 'w', encoding='utf-8') as f:
        f.write(PRACTICE_JS)
    with open(os.path.join(adir, 'site.js'), 'w', encoding='utf-8') as f:
        f.write(SITE_JS)
