// ===== Harjoittele-tehtävämoottori =====
function prGet(){try{return JSON.parse(localStorage.getItem('bcai-practice')||'{}')}catch(e){return{}}}
function prSet(o){try{localStorage.setItem('bcai-practice',JSON.stringify(o))}catch(e){}}
function prKey(lid,ti){return lid+'/'+ti}
function twShuffle(a){a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a}
function twEl(tag,cls,html){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e}
function initPractice(lid,tasks){
  if(!tasks||!tasks.length)return;
  document.querySelectorAll('#lesson-panels .task-widget').forEach(w=>{
    const ti=+w.dataset.ti,task=tasks[ti];
    if(!task||w.dataset.init)return;w.dataset.init='1';
    renderTask(w,task,lid,ti);
  });
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
  const p=twEl('div','tw-card',task.prompt||'');
  const ta=twEl('textarea','tw-ta');ta.rows=5;ta.placeholder='Kirjoita tähän omin sanoin...';
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
