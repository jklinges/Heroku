function loadTasks() {
    d3.json('/api/tasks-postgres').then(data => {
        data.forEach((task) => {
            var listGroup = d3.select('#tasks');
            var listItem = listGroup.append('li');
            listItem.text(task.description);
            listItem.attr('class','list-group-item');
        });
    });
}

loadTasks();