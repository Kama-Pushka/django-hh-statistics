let stat_buttons = document.querySelectorAll('.stat-buttons span');

for (let button of stat_buttons) {
    button.onclick = function(evt) {
        evt.preventDefault();

        let activeStat = document.querySelector('.active-stat'); 
        activeStat.classList.remove('active-stat');
        console.log(activeStat)
        let stat = document.querySelector('.stat-' + button.getAttribute('href')); 
        stat.classList.add('active-stat');
        console.log(stat)
        console.log('.stat-' + button.getAttribute('href'))
    }
}