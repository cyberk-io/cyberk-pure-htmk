/* Cyberk — Minimal vanilla JS (< 2KB) */
(function(){
  /* Header hide on scroll down, show on scroll up */
  var h=document.getElementById('site-header'),py=0;
  if(h)window.addEventListener('scroll',function(){
    var y=window.scrollY;
    h.classList.toggle('hidden',y>80&&y>py);
    py=y;
  },{passive:true});

  /* How We Work — step image switcher */
  var steps=document.getElementById('hww-steps'),img=document.getElementById('hww-image');
  if(steps&&img){
    var items=steps.querySelectorAll('.step-item'),idx=0,timer;
    function activate(i){
      items.forEach(function(el){el.classList.remove('active')});
      items[i].classList.add('active');
      img.src=items[i].dataset.img;
      img.alt='How we work — '+items[i].textContent.trim();
      idx=i;
    }
    function auto(){timer=setInterval(function(){activate((idx+1)%items.length)},3000)}
    items.forEach(function(el,i){el.addEventListener('click',function(){activate(i);clearInterval(timer);auto()})});
    auto();
  }

  /* Close mobile nav on link click */
  var toggle=document.getElementById('nav-toggle');
  if(toggle){
    document.querySelectorAll('.nav-menu a').forEach(function(a){
      a.addEventListener('click',function(){toggle.checked=false});
    });
  }
})();
