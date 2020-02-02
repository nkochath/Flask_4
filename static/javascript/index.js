document.querySelector('form').onsubmit = function() {
  email = document.querySelector("input[name='email']").value

  if(!email.includes('@')) {
    document.querySelector("input[name='email']").focus();
    alert('You must provide a valid email address!');
    return false;
  }

  domain = email.slice(email.indexOf('@') + 1);
  if (domain != 'gmail.com' && domain != 'yahoo.com' && domain != 'outlook.com') {
    alert('You must provide a valid domain for your email address!');
    return false;
  }
  
};
