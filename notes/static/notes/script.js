document.addEventListener('DOMContentLoaded', function(){
    fetch('/api/subjects')
    .then(response => response.json())
    .then(data =>{
        const subjectsDropDown = document.getElementById("subjectsDropDown");
        subjectsDropDown.innerHTML = ''

        data.forEach(subject => {
            const listItem = document.createElement('li');
            const link = document.createElement('a');
            link.className = 'dropdown-item';
            link.href = `/subjects/${subject.id}`;
            link.textContent = subject.name;

            listItem.appendChild(link);

            subjectsDropDown.appendChild(listItem);

        });


    })
    .catch(error => console.error('Error fetching subjects:', error));
})