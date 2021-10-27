// Wait for the DOM to be ready
function checkValues() {
  // Initialize form validation on the registration form.
  // It has the name attribute "registration"
  console.log("running check");
  
  $("form[name='ticket-buy-form']").validate({
    // Specify validation rules
    rules: {
      // The key name on the left side is the name attribute
      // of an input field. Validation rules are defined
      // on the right side
      ticket_holder_first_name: {
        required:true, 
        minlength:2,
      },
      ticket_holder_last_name: "required",
      ticket_holder_email: {
        required: true,
        // Specify that ticket_holder_email should be validated
        // by the built-in "ticket_holder_email" rule
        ticket_holder_email: true
      }
    },
    // Specify validation error messages
    messages: {
      ticket_holder_first_name: "Please enter valid first name",
      ticket_holder_last_name: "Please enter valid last name",
      ticket_holder_email: "Please enter a valid email address"
    },
    // Make sure the form is submitted to the destination defined
    // in the "action" attribute of the form when valid
    submitHandler: function(form) {
      form.submit();
    }
  });
};
