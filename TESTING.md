<h1 align="center">Xtreme Fitness Club<a name="#top"></a></h1>

- Back To [Readme](README.md)

## Testing

### Functionality Testing




- EmailJs Error in Gmail accont: 
  - No name , email and message value.

   <img src="readme/testing/empty-email.png" height="300px"/> 
```
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
```
- Quick fix:
  - Delete .value after the value of name, email, subject, message from sendMail function.
  - In the validate function use this value.

      <img src="readme/testing/not-empty-email.png" height="300px"/> 
```

function sendMail(name, email, subject, message) {
      emailjs.send("service_4l1t10j", "template_nv8417p", {
            name: name,
            email: email,
            subject: subject,
            message: message,
      })
      
}
```


### Validator

#### CSS3 validator
Validate by direct input [CSS Validator](https://jigsaw.w3.org/css-validator/)
- First Test results: 2 Errors

   <img src="readme/testing/css-validator.png" height="300px"/> 
   - Quick fix: 
       - border-radius: none  -to - botder-radius: 0
       - transform: transition .3s ease  -to - transition: .3s ease

- Second Test results: No Errors

   <img src="readme/testing/css-validator02.png" height="300px"/>

I got 24 Warning about Vendor Extensions


#### HTML5 validator
Vaidate by URI [HTML5 Validator](https://validator.w3.org/#validate_by_uri)
Test result : No Error


#### JavaScript validator
Validate by direct input [JavaScript Validator](https://jshint.com/)
- Test result : No Error Found But Warning

#### Python validator
Validate by direct input [Python Validator](http://pep8online.com/)
Test result : No Error

#### Usability Testing

- This is website shared with friends to check on different device and accessbility.

#### Compatibility Testing

- Browser Compatibility
   - Tested on Chrome, Firefox, Safari.

- OS Compatibility
   - Tested on iOS , Android.

#### Performance Testing

- Tested on Developer Tools Lighthouse.

   - To run a report
     - Download Google Chrome for Desktop.
     - In Google Chrome, go to the URL you want to check. You can check any URL on the web.
     - Open Chrome DevTools.
     - Click the Lighthouse tab.
     - To the left is the viewport of the page that will be checked. To the right is the Lighthouse panel of Chrome DevTools.
     - Choose Desktop or Mobil device, DevTools shows you a list of categories. Leave them all enabled.
     - Click Generate report.

- A Lighthouse report in Chrome DevTools

    - Home page Desktop and Mobile
      <img src="readme/testing/home-lighthouse.jpg" height="300px"/>

    - About page Desktop and Mobile
      <img src="readme/testing/about-lighthouse.jpg" height="300px"/>

    - Products(all) page Desktop and Mobile
      <img src="readme/testing/products-lighthouse.jpg" height="300px"/>

    - Product_details page Desktop and Mobile
      <img src="readme/testing/product_details-lighthouse.jpg" height="300px"/>

    - Contact page Desktop and Mobile
      <img src="readme/testing/contact-lighthouse.jpg" height="300px"/>

    - Blog page Desktop and Mobile
      <img src="readme/testing/blog-lighthouse.jpg" height="300px"/>

    - Blog_details page Desktop and Mobile
      <img src="readme/testing/blog_details-lighthouse.jpg" height="300px"/>

    - Bag page Desktop and Mobile
      <img src="readme/testing/bag-lighthouse.jpg" height="300px"/>

    - Checkout page Desktop and Mobile
      <img src="readme/testing/checkout-lighthouse.jpg" height="300px"/>

    - Checkout_success page Desktop and Mobile
      <img src="readme/testing/checkout_success-lighthouse.jpg" height="300px"/>

    - Subcribe page Desktop and Mobile
      <img src="readme/testing/subscribe-lighthouse.jpg" height="300px"/>

    - Product mangment page Desktop and Mobile
      <img src="readme/testing/product-man-lighthouse.jpg" height="300px"/>

    - Profile page Desktop and Mobile
      <img src="readme/testing/profile-lighthouse.jpg" height="300px"/>

    - Register page Desktop and Mobile
      <img src="readme/testing/register-lighthouse.jpg" height="300px"/>

    - Sign-In page Desktop and Mobile
      <img src="readme/testing/signin-lighthouse.jpg" height="300px"/>


#### Testing User Stories

- Generic User, Shopper, Site User

  - I easily understand the purpose and the layout of the site without additional instructions needed.
  - All pages of website has navigation bar, search box and footer.
  - With navigation bar I can easily access diiferent page and go anywhere from present page and come back.
  - Footer has social link. If I click on link it open the relevant page on different tab so I can easily check the social activity.
  - I am able to use the website on any device.

    - View a list of products:
      - Training page(all) - I get all training plans of the Fitness club.
      - Shop page(all). - I get all shopping products of the Fitness club.

    - View individual product details:
      - Product_details. -  I can see product description of specific product.

    - Easily view the total of my purchases at any time:
      - On all pages.  - I can see the bag icon in the rigth corner with my total amont of the purchases.

    - Register for an accont:
      - Register pages.  - Have a personal accont and view my profile.

    - Log-in and Log-out:
      - Log-In pages.  - I can Log-in to my profile. 
      - Log-out page.  - I can Log-out.