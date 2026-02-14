const structure = document.getElementById('structure')
const radio_tags = document.getElementById('radio')
const RadioTag_simple = document.getElementById('simple')
const RadioTag_linear = document.getElementById('linear')
const RadioTags_tyype = document.getElementById('type_tags')
const html_tag = document.querySelector('html')
const Theme = document.getElementById('Theme')
const callme = document.getElementById('callme')
const Information = document.getElementById('Information')
const Radio_tag_p_1 = document.getElementById('Radio-tag-p-1')
const Radio_tag_p_2 = document.getElementById('Radio-tag-p-2')
const Radio_tag_img_1 = document.getElementById('Radio-tag-img-1')
const Radio_tag_img_2 = document.getElementById('Radio-tag-img-2')
const Radio_tag_1 = document.getElementById('one');
const Radio_tag_2 = document.getElementById('two');
const HelperPlus = document.getElementById('helper_plus');
const helper = document.getElementById('helper');
const sub = document.getElementById('sub');
const HiddenInput = document.getElementById('HiddenInput')

function hidden(clas, dis) {
    let tag = document.querySelectorAll(`.${clas}`)

    tag.forEach(element => {
        element.style.display = `${dis}`
    });
}
//قالب دارم
structure.addEventListener('click', () => {
    if (structure.checked == true) {
        hidden('file_choose', 'block');
        hidden('watermark', 'none');
    };
    if (structure.checked == false) {
        hidden('file_choose', 'none');
        hidden('watermark', 'flex');
    };
});
//زیر محور پاسخبرگ
radio_tags.addEventListener('click', () => {


    if (RadioTag_linear.checked == true) {
        RadioTags_tyype.style.display = 'flex'
        Radio_tag_p_1.style.background = 'var(--radio-bg)'
        Radio_tag_p_1.style.color = 'var(--text)'
        Radio_tag_p_2.style.background = 'var(--radio-bg)'
        Radio_tag_p_2.style.color = 'var(--text)'
        Radio_tag_p_2.innerHTML = 'تشریحی'
        Radio_tag_img_1.setAttribute('src', 'https://s8.uupload.ir/files/screenshot_(110)_4fgl.png')
        Radio_tag_1.setAttribute('value', 'solution')
        Radio_tag_p_1.innerHTML = 'تستی'
        Radio_tag_img_2.setAttribute('src', 'https://s8.uupload.ir/files/screenshot_(111)_xnt2.png')
        Radio_tag_2.setAttribute('value', 'anatomical')
        hidden('rows', 'flex');
    } else if (RadioTag_simple.checked == true) {
        Radio_tag_p_1.style.background = 'var(--radio-bg)'
        Radio_tag_p_1.style.color = 'var(--text)'
        Radio_tag_p_2.style.background = 'var(--radio-bg)'
        Radio_tag_p_2.style.color = 'var(--text)'
        RadioTags_tyype.style.display = 'flex'
        Radio_tag_img_1.setAttribute('src', 'https://s8.uupload.ir/files/screenshot_(108)_n3cd.png')
        Radio_tag_p_1.innerHTML = 'ابداعی'
        Radio_tag_1.setAttribute('value', 'inventive')
        Radio_tag_img_2.setAttribute('src', 'https://s8.uupload.ir/files/screenshot_(109)_id7l.png')
        Radio_tag_p_2.innerHTML = 'استاندارد'
        Radio_tag_2.setAttribute('value', 'Standard')
        hidden('rows', 'none');
    };
});

//radio_tags_hover_and selected
RadioTags_tyype.addEventListener('click', () => {
    if (Radio_tag_1.checked == true) {
        RadioTags_tyype.children[0].children[0].children[1].style.background = 'var(--radio-bg-hover)'
        RadioTags_tyype.children[0].children[0].children[1].style.color = 'black'

        RadioTags_tyype.children[1].children[0].children[1].style.background = 'var(--radio-bg)'
        RadioTags_tyype.children[1].children[0].children[1].style.color = 'var(--text)'
    } else if (Radio_tag_2.checked == true) {
        RadioTags_tyype.children[0].children[0].children[1].style.background = 'var(--radio-bg)'
        RadioTags_tyype.children[0].children[0].children[1].style.color = 'var(--text)'

        RadioTags_tyype.children[1].children[0].children[1].style.background = 'var(--radio-bg-hover)'
        RadioTags_tyype.children[1].children[0].children[1].style.color = 'black'
        if (Radio_tag_2.value == 'anatomical') {
            hidden('helper', 'flex');
            helper.style.height = `15vh`;
            document.getElementsByClassName('helper')[0].style.height = `15vh`;

        }
    }

});
// extra helpers
let height = 15;
HelperPlus.addEventListener('click', () => {
    helper.innerHTML += `                    <div class="input">
                        <input type="number" class="input_tag helper_input_tag helper_input_tag_1 " name="helper" id="helper">
                        <p> : </p>
                        <input type="number" class="input_tag helper_input_tag helper_input_tag_2" name="helper" id="helper">
                        </div>`;

    helper.style.height = `${height}vh`;
    document.getElementsByClassName('helper')[0].style.height = `${height}vh`;
    height += 5
});

sub.addEventListener('submit', (e) => {
    e.preventDefault();
    const helpertags1 = document.getElementsByClassName('helper_input_tag_1')
    const helpertags2 = document.getElementsByClassName('helper_input_tag_2')


    let help = {};

    for (let i = 0; i < helpertags1.length; i++) {
        help[helpertags1[i].value] = helpertags2[i].value;
    }

    HiddenInput.value = JSON.stringify(help)

    sub.submit();
})