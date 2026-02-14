const html_tag = document.querySelector('html')
const Theme = document.getElementById('Theme')
const callme = document.getElementById('callme')
const Information = document.getElementById('Information')

function hidden(clas, dis) {
    let tag = document.querySelectorAll(`.${clas}`)

    tag.forEach(element => {
        element.style.display = `${dis}`
    });
}
//checking - the local storage
if (localStorage.getItem('theme') == 'dark') {
    them('dark')
} else if (localStorage.getItem('theme') == 'light') {
    them('light')
}
//function - theme
function them(theme) {
    if (theme == 'dark') {
        html_tag.className = '';
        Theme.className = 'icon bi-moon';
        localStorage.setItem('theme', 'dark')
    } else if (theme == 'light') {
        html_tag.className = 'light';
        Theme.className = 'icon bi-sun';
        localStorage.setItem('theme', 'light')
    }

};

//Theme
Theme.addEventListener('click', () => {
    if (html_tag.className == 'light') {
        them('dark');
    } else if (html_tag.className == '') {
        them('light');
    };
});
//callme
callme.addEventListener('click', () => {
    if (callme.className == 'icon bi-envelope') {
        hidden('form', 'none');
        hidden('callme', 'flex');
        callme.className = 'icon bi-arrow-90deg-left'
    } else if (callme.className == 'icon bi-arrow-90deg-left') {
        hidden('form', 'flex');
        hidden('callme', 'none');
        callme.className = 'icon bi-envelope'
    }
});
//Information
Information.addEventListener('click', () => {
    if (Information.className == 'icon bi-question-circle') {
        hidden('form', 'none');
        hidden('help-me', 'flex');
        Information.className = 'icon bi-arrow-90deg-left'
    } else if (Information.className == 'icon bi-arrow-90deg-left') {
        hidden('form', 'flex');
        hidden('help-me', 'none');
        Information.className = 'icon bi-question-circle'
    }
});