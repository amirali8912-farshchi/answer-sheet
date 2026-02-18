
function hidden(clas, dis) {
    let tag = document.querySelectorAll(`.${clas}`)

    tag.forEach(element => {
        element.style.display = `${dis}`
    });
}