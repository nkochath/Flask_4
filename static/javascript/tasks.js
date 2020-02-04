function edit(button) {
  tr = button.parentNode.parentNode;
  description_cell = tr.children[2];
  description_text = description_cell.innerHTML;
  text_area = document.createElement('textarea');

  text_area.setAttribute('name', 'task_description');

  description_cell.replaceWith(text_area);
  submit_button = document.createElement('button');
  submit_button.setAttribute('onclick','submit()');
  submit_button.appendChild(document.createTextNode('Submit'));
  button.replaceWith(submit_button);
}

function submit() {
  let name = tr.children[1].innerHTML;
  let description = tr.children[2].value;

  let task = {name: name, description: description };

  $.post('/edittask', task, function(data) {
    alert(data)
  });
}
