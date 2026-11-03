(function(){
  var t=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  if(t&&n){
    function setMenu(o){n.classList.toggle('open',o);t.setAttribute('aria-expanded',o);t.textContent=o?'Close':'Menu';document.body.classList.toggle('menu-open',o);}
    t.addEventListener('click',function(){setMenu(!n.classList.contains('open'))});
    n.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
    window.addEventListener('resize',function(){if(window.innerWidth>860)setMenu(false)});
  }

  var items=[].slice.call(document.querySelectorAll('[data-zoom]'));
  if(!items.length)return;
  var lb=document.createElement('div');lb.className='lightbox';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');
  lb.innerHTML='<button class="lb-btn lb-close" aria-label="Close">&times;</button><button class="lb-btn lb-prev" aria-label="Previous">&#8249;</button><img alt=""><button class="lb-btn lb-next" aria-label="Next">&#8250;</button><div class="cap"></div>';
  document.body.appendChild(lb);
  var img=lb.querySelector('img'),cap=lb.querySelector('.cap'),i=0;
  function show(k){i=(k+items.length)%items.length;var el=items[i],im=el.querySelector('img');img.src=im.src;img.alt=im.alt;var fc=el.closest('figure');var c=fc&&fc.querySelector('figcaption');cap.textContent=c?c.textContent:im.alt;lb.classList.add('open');document.body.style.overflow='hidden';}
  function hide(){lb.classList.remove('open');document.body.style.overflow='';}
  items.forEach(function(el,k){el.tabIndex=0;el.addEventListener('click',function(){show(k)});el.addEventListener('keydown',function(e){if(e.key==='Enter')show(k)})});
  lb.querySelector('.lb-close').onclick=hide;
  lb.querySelector('.lb-prev').onclick=function(e){e.stopPropagation();show(i-1)};
  lb.querySelector('.lb-next').onclick=function(e){e.stopPropagation();show(i+1)};
  lb.addEventListener('click',function(e){if(e.target===lb)hide()});
  var sx=null;
  lb.addEventListener('touchstart',function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener('touchend',function(e){if(sx===null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)show(i+(dx<0?1:-1));sx=null});
  document.addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;if(e.key==='Escape')hide();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)});
})();
