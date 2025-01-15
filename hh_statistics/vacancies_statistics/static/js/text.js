let cards = document.querySelectorAll('.magritte-card');

for (let card of cards) {
    card.onclick = function() {
        let desc = card.querySelector('.can-be-hide');
        if (desc.classList.contains('hide')) {
            desc.classList.remove('hide');
        } else {
            desc.classList.add('hide');
        }
        //console.log("TEST")
    }
}