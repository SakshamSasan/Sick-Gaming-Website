const navbar = document.querySelector(".navbar");
const menu = document.querySelector(".Menu_button");

menu.addEventListener('click', () => {
    const visible = navbar.getAttribute("data-visible");
    if(visible === "false")
    {
        navbar.setAttribute("data-visible","true")
        menu.setAttribute("aria-expanded","true")
    }  
    else
    {
        navbar.setAttribute("data-visible","false");
        menu.setAttribute("aria-expanded","false");
    }
        
})