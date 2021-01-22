const toggleButton = document.getElementsByClassName('togglebutton')[0]
const navbarLinks = document.getElementsByClassName('links')[0]

toggleButton.addEventListener('click', () => {
  navbarLinks.classList.toggle('active')
})


// Get the container element
var btnContainer = document.getElementById("NAVbar");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("a");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");

    // If there's no active class
    if (current.length > 0) {
      current[0].className = current[0].className.replace(" active", "");
    }

    // Add the active class to the current/clicked button
    this.className += " active";
  });
} 


