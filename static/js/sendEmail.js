// EmailJs  Credit  https://www.emailjs.com/
function sendMail(contactForm) {
      emailjs.send("service_4l1t10j", "template_nv8417p", {
            name: contactForm.name.value,
            email: contactForm.email.value,
            message: contactForm.message.value,
      })
      .then(function(res) {
            alert('Your mail is sent!');
            console.log("success", res.status);
      },
      function(error) {
            alert('Oops... ' + JSON.stringify(error));
            console.log("Failed", error);
      });
      document.getElementById("myForm").reset();
      return false;
      }