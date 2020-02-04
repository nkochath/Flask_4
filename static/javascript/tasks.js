function edit(button) {
  let tr = button.parentNode.parentNode;
  let description_cell = tr.children[2];
  let text_area = document.createElement('textarea');

  text_area.setAttribute('name', 'task_description');
  description_cell.replaceWith(text_area);
  button.setAttribute('onclick','submit(this)');
  button.innerHTML = 'Submit'
}

function submit(button) {
  let tr = button.parentNode.parentNode;
  let name = tr.children[1].innerHTML;
  let description = tr.children[2].value;

  let task = {name: name, description: description};

  $.post('/edittask', task, function(data) {
    if (data == 'Task Updated') {
      let tr = button.parentNode.parentNode;
      let td = document.createElement('td');
      tr.children[2].replaceWith(td);
      td.innerHTML = description;


      button.innerHTML = 'Edit';
      button.setAttribute('onclick', 'edit(this)');

    }
  });
}

function deleteTask(button) {
  let tr = button.parentNode.parentNode;
  let name = tr.children[1].innerHTML;

  $.post('/deletetask', {name:name}, function(data) {
    if (data == 'Task Deleted') {
      tr.parentNode.removeChild(tr);
    }
  });
}
