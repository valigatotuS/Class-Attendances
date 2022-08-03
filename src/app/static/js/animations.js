function cursussenShow() {
    var x = document.getElementById("cursussen-dropdown");
    if (x.style.left == "84px") {
        x.style.left = "-295px";
        x.style.display = "flex";
    } else {
        x.style.left = "84px";
    }
}


function activePage() {
    currentLinks = document.querySelectorAll('button[href="'+document.URL+'"]')
    currentLinks.forEach(function(link) { link.className += ' active'});
}
activePage();
