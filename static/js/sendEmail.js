// EmailJs  Credit  https://www.emailjs.com/
// Sweetalerts credit https://sweetalert.js.org/docs/ customized alert box idea from https://github.com/Benrobo/Send-Mail-Using-Email.js  and modified for project needs.
function validate() {
      let name = document.querySelector(".name");
      let email = document.querySelector(".email");
      let subject = document.querySelector(".subject");
      let message = document.querySelector(".message");
      let btn = document.querySelector(".message-btn");

      btn.addEventListener("click", (e) => {
            e.preventDefault();
            if (name.value == "" || email.value == "" || subject.value == "" || message.value == "") {
            emptyerror();
            } 
            else {
                  sendMail(name.value, email.value, subject.value, message.value);
                  success();
                  document.getElementById("myForm").reset();
                  return false;     
            }
      });
    }
validate();

           
function sendMail(name, email, subject, message) {
      emailjs.send("service_4l1t10j", "template_nv8417p", {
            name: name.value,
            email: email.value,
            subject: subject.value,
            message: message.value,
      })
      
}


function emptyerror() {
      swal({
            icon: "error",
            title: "Oops...",
            text: "Fields cannot be empty!",
      });
      }

function error() {
      swal({
            icon: "error",
            title: "Oops...",
            text: "Something went wrong!",
      });
}

function success() {
      swal({
            icon: "success",
            title: "Success...",
            text: "Successfully sent message",
      });
}