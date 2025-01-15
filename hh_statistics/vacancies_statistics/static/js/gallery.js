let activePhoto = document.querySelector('.active-photo');
let previews = document.querySelectorAll('.preview-list a');

for (let preview of previews) {
    preview.onclick = function(evt) {
        evt.preventDefault();
        
        activePhoto.src = preview.href;
        let activePreview = document.querySelector('.active-item'); 
        activePreview.classList.remove('active-item');
        preview.classList.add('active-item');
    }
}