document.querySelector('form').onsubmit = function() {
  email = document.querySelector("input[name='email']").value

  if(!email.includes('@')) {
    document.querySelector("input[name='email']").focus();
    alert('You must provide a valid email address!');
    return false;
  }


};
