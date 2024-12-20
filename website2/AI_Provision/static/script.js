gsap.registerPlugin(ScrollTrigger);

gsap.to("#nav",{
    backgroundColor:"#000",
    duration:0.5,
    height:"120px",
    scrollTrigger:{
     trigger:"#nav",
     scroller:"body",
     marker:true,
     start:"top-10%",
     end:"top-11%",
     scrub:true,
   }


})