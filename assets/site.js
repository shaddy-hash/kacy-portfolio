(function(){
  var t=document.querySelector('.menu-toggle'),n=document.getElementById('nav');
  if(t&&n){t.addEventListener('click',function(){var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o)});}

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
  document.addEventListener('keydown',function(e){if(!lb.classList.contains('open'))return;if(e.key==='Escape')hide();if(e.key==='ArrowLeft')show(i-1);if(e.key==='ArrowRight')show(i+1)});
})();
