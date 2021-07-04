/*
To override this behavior, you can activate strict mode, 
which reduces silent errors, improves performance, provides
you with more warnings, and fewer unsafe features.
*/

'use strict'

const switcher = document.querySelector('.btn');

switcher.addEventListener('click', function() {
    document.body.classList.toggle('dark-theme');

    var className = document.body.className;
    if(className == "light-theme") {
        this.textContent = ' ';
    }
    else {
        this.textContent = ' ';
    }

});


