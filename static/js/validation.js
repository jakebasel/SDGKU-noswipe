function validate(inputtxt) {
  console.log("test");
  var letterNumber = /^[0-9a-zA-Z@]+$/;
  if((inputtxt.value.match(letterNumber))) {
    return true;
  }
  else {
    alert("message");
    return false;
  }
}