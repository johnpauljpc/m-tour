
const navToggler = document.querySelector(".nav-toggler");
navToggler.addEventListener("click", navToggle);

function navToggle() {
   navToggler.classList.toggle("active");
   const nav = document.querySelector(".nav");
   nav.classList.toggle("open");
   if(nav.classList.contains("open")){
       nav.style.maxHeight = nav.scrollHeight + "px";
   }
   else{
       nav.removeAttribute("style");
   }
} 






// register, get started application options

secOpt = document.querySelector(".sec-opt2")
    
    function show(){
        secOpt.style.display = 'inline'
    }

    function hide(){
        secOpt.style.display = 'none'
    }

    trvOpt2 = document.querySelector('.trv-opt2')
    trvOpt22 = document.querySelector('.trv-opt22')
    
    
    function showTr(){
        trvOpt2.style.display = 'inline'
        trvOpt22.style.display = 'inline'
    }

    function hideTr(){
        trvOpt2.style.display = 'none'
        trvOpt22.style.display = 'none'
    }


    const Diff = document.querySelector('.diff')
    function differ(){
        Diff.style.display = 'inline'
    }

    
