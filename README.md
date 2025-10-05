# Ex.07 Restaurant Website
# Date:05.10.2025
# AIM:
To develop a static Restaurant website to display the food items and services provided by them.

# DESIGN STEPS:
## Step 1:
Requirement collection.

## Step 2:
Creating the layout using HTML and CSS.

## Step 3:
Updating the sample content.

## Step 4:
Choose the appropriate style and color scheme.

## Step 5:
Validate the layout in various browsers.

## Step 6:
Validate the HTML code.

## Step 7:
Publish the website in the given URL.

# PROGRAM:
~~~
home.html

<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hungry Chicken</title>
    <style>
      body {
          background-color: rgba(233, 158, 7, 0.955);
          
          font-family: Arial, sans-serif;
          margin: 0;
      }
      img {
          display: block;
          margin: 0;}
      nav {
        background-color: #3d3c3d;
        height: 50px;
        margin: 0;
        overflow: hidden;
        font-family:Arial, Helvetica, sans-serif;
        }
        nav a {
        float: right;
        display: block;
        color: white;
        padding: 0.75em 1em;
        text-decoration: none;
        }
        nav a:hover {
        background-color: #575757;
        }
                .banner {
                        text-align: center;
                        background-image: url('static/banner.png');
                        background-position: center;
                        background-size: cover;
                        background-repeat: no-repeat;
                        height: 250px;
                        width: 90%;
                        margin: 20px 0 0 0;
                        border-radius: 60px;
                        position: absolute;
                        left: 78px;
                }
                .menu {
                        position: absolute;
                        top: 700px;
                        left: 30px;
                        width: calc(100% - 60px);
                        display: flex;
                        flex-wrap: wrap;
                        flex-direction: row;
                        gap: 25px;
                        justify-content: center;
                }
                
                .container {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        text-align: center;
                        gap: 10px;
                        padding: 28px;
                        border-radius: 16px;
                        background-color: #343131;
                        color: #fff;
                        box-sizing: border-box;
                        flex: 0 0 270px;
                        height: 350px;
                        min-width: 180px;
                        max-width: 300px;
                       
                }
                .container:hover{
                        background-color: #575757;
                        transform: scale(1.05);
                        transition: transform 0.3s, background-color 0.3s;
                }
              .container img {
                        width: 200px;
                        height: 150px;
                        object-fit: cover;
                        border-radius: 8px;
                        }
                .container h3 {
                        margin: 0;
                        font-size: 1.2em;
                }
                .container p {
                        font-size: 0.9em;
                        line-height: 1.4;
                }
                 footer {
                color: rgb(255, 254, 254);
                text-align: center;
                padding: 20px;
                bottom: 0;
                width: 1851px;
                position: relative;
                margin: 0;
                background-color: #343131;
                top: 1700px;
            }
    </style>
</head>
<body>
    <header>
       <img src="static/logo.jpg" alt="Hungry Chicken Logo" width="650px" style="margin: 0;">
    </header>
    <nav>
        <a href="contactus.html" style="font-size: larger;font-weight: bold;">Contact Us</a>
        <a href="administration.html" style="font-size: larger;font-weight: bold;">Administration</a>
        <a href="menu.html" style="font-size: larger;font-weight: bold;">Menu</a>
        <a href="home.html" style="font-size: larger;font-weight: bold;">Home</a>
    </nav>
    <div class="banner">
         <h1 style="font-size: 50px; font-family:fantasy; font-weight:
         lighter; color: rgba(255, 255, 255, 0.881);">Diwali Special: 20% Off On First 10 Orders 
         <br> Everyday till Diwali</h1>
      <h1 style="font-size: 50px; color: white;font-family:monospace; text-align: center; position: relative; top: 90px;" >Home</h1>
    </div>
     <div class="menu" style="left: 30px;">
                         <div class="container">
                                 <h3>1. Chicken Biryani - $10.99</h3>
                                 <img src="static/ChickenBiryani.png" alt="chicken biryani">
                                 <p>Delicious chicken biryani with fragrant spices and basmati rice.</p>
                         </div>
                  <div class="container">
                          <h3>2. Grilled Chicken - $12.99</h3>
                          <img src="static/Grilled Chicken.png" alt="Grilled Chicken">
                          <p>Juicy grilled chicken marinated in herbs and spices.</p>
                  </div>
                  <div class="container">
                          <h3>3. Chicken Curry - $11.99</h3>
                          <img src="static/Chicken Curry.png" alt="Chicken Curry">
                          <p>Classic chicken curry cooked in a rich and flavorful sauce.</p>
                  </div>
                  <div class="container">
                          <h3>4. Chicken Sandwich - $8.99</h3>
                          <img src="static/Chicken Sandwich.png" alt="Chicken Sandwich">
                          <p>Grilled chicken sandwich with lettuce, tomato, and mayo.</p>
                  </div>
                  <div class="container">
                          <h3>5. Chicken Salad - $9.99</h3>
                          <img src="static/Chicken Salad.png" alt="Chicken Salad">
                          <p>Fresh chicken salad with mixed greens and vinaigrette dressing.</p>
                  </div>
                  <div class="container">
                          <h3>6. Chicken Wings - $10.99</h3>
                          <img src="static/Chicken Wings.png" alt="Chicken Wings">
                          <p>Spicy chicken wings served with blue cheese dip.</p>
                  </div>
                  <div class="container">
                          <h3>7. Chicken Tacos - $9.99</h3>
                          <img src="static/Chicken Tacos.png" alt="Chicken Tacos">
                          <p>Soft tacos filled with seasoned chicken, lettuce, and cheese.</p>
                  </div>
            <div class="container">
                    <h3>8. Chicken Alfredo - $13.99</h3>
                    <img src="static/Chicken Alfredo.png" alt="Chicken Alfredo">
                    <p>Creamy chicken alfredo pasta with parmesan cheese.</p>
            </div>
            <div class="container">
                    <h3>9. Chicken Wrap - $8.99</h3>
                    <img src="static/Chicken Wrap.png" alt="Chicken Wrap">
                    <p>Grilled chicken wrap with veggies and ranch dressing.</p>
            </div>
            <div class="container"> 
                    <h3>10. Chicken Nuggets - $7.99</h3>
                    <img src="static/Chicken Nuggets.png" alt="Chicken Nuggets">
                    <p>Crispy chicken nuggets served with your choice of dipping sauce.</p>
            </div>
            <div class="container">
                    <h3>11. Chicken Fried Rice - $10.99</h3>
                    <img src="static/Chicken Fried Rice.png" alt="Chicken Fried Rice">
                    <p>Stir-fried rice with chicken, vegetables, and soy sauce.</p>
            </div>
            <div class="container">
                    <h3>12. Chicken Quesadilla - $9.99</h3>
                    <img src="static/Chicken Quesadilla.png" alt="Chicken Quesadilla">
                    <p>Grilled quesadilla filled with chicken, cheese, and peppers.</p>
            </div>
            <div class="container">
                    <h3>13. Chicken Parmesan - $14.99</h3>
                    <img src="static/Chicken Parmesan.png" alt="Chicken Parmesan">
                    <p>Breaded chicken breast topped with marinara sauce and melted cheese.</p>
            </div>
            <div class="container"> 
                    <h3>14. Chicken Soup - $6.99</h3>
                    <img src="static/Chicken Soup.png" alt="Chicken Soup">
                    <p>Warm and comforting chicken soup with vegetables and noodles.</p>
            </div>
            <div class="container">
                    <h3>15. BBQ Chicken Pizza - $15.99</h3>
                    <img src="static/BBQ Chicken Pizza.png" alt="BBQ Chicken Pizza">
                    <p>Delicious pizza topped with BBQ chicken, red onions, and cilantro.</p>
            </div>
            <div class="container">
                    <h3>16. Chicken Caesar Salad - $10.99</h3>
                    <img src="static/Chicken Caesar Salad.png" alt="Chicken Caesar Salad">
                    <p>Classic Caesar salad topped with grilled chicken and croutons.</p>
            </div>

     </div>
     <footer> &copy; 2025 My Website. All rights reserved.</footer>
</body>
</html>

menu.html


<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hungry Chicken</title>
    <style>
      body {
          background-color: rgba(233, 158, 7, 0.955);
          
          font-family: Arial, sans-serif;
          margin: 0;
      }
      img {
          display: block;
          margin: 0;}
      nav {
        background-color: #3d3c3d;
        height: 50px;
        margin: 0;
        overflow: hidden;
        font-family:Arial, Helvetica, sans-serif;
        }
        nav a {
        float: right;
        display: block;
        color: white;
        padding: 0.75em 1em;
        text-decoration: none;
        }
        nav a:hover {
        background-color: #575757;
        }
               
                .menu {
                        position: absolute;
                        top: 420px;
                        left: 30px;
                        width: calc(100% - 60px);
                        display: flex;
                        flex-wrap: wrap;
                        flex-direction: row;
                        gap: 25px;
                        justify-content: center;
                }
                
                .container {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        text-align: center;
                        gap: 10px;
                        padding: 28px;
                        border-radius: 16px;
                        background-color: #343131;
                        color: #fff;
                        box-sizing: border-box;
                        flex: 0 0 270px;
                        height: 350px;
                        min-width: 180px;
                        max-width: 300px;
                }
              .container img {
                        width: 200px;
                        height: 150px;
                        object-fit: cover;
                        border-radius: 8px;
                        }
                .container h3 {
                        margin: 0;
                        font-size: 1.2em;
                }
                .container p {
                        font-size: 0.9em;
                        line-height: 1.4;
                }
                .container:hover{
                        background-color: #575757;
                        transform: scale(1.05);
                        transition: transform 0.3s, background-color 0.3s;
                }
                 footer {
                color: rgb(255, 254, 254);
                text-align: center;
                padding: 20px;
                bottom: 0;
                width: 1851px;
                position: relative;
                margin: 0;
                background-color: #343131;
                top: 1300px;
            }
    </style>
</head>
<body>
    <header>
       <img src="static/logo.jpg" alt="Hungry Chicken Logo" width="650px" style="margin: 0;">
    </header>
    <nav>
        <a href="contactus.html" style="font-size: larger;font-weight: bold;">Contact Us</a>
        <a href="administration.html" style="font-size: larger;font-weight: bold;">Administration</a>
        <a href="menu.html" style="font-size: larger;font-weight: bold;">Menu</a>
        <a href="home.html" style="font-size: larger;font-weight: bold;">Home</a>
    </nav>
     <h1 style="font-size: 50px; color: white;font-family:monospace; text-align: center;" >Menu</h1>
  
     <div class="menu" style="left: 30px;">
                         <div class="container">
                                 <h3>1. Chicken Biryani - $10.99</h3>
                                 <img src="static/ChickenBiryani.png" alt="chicken biryani">
                                 <p>Delicious chicken biryani with fragrant spices and basmati rice.</p>
                         </div>
                  <div class="container">
                          <h3>2. Grilled Chicken - $12.99</h3>
                          <img src="static/Grilled Chicken.png" alt="Grilled Chicken">
                          <p>Juicy grilled chicken marinated in herbs and spices.</p>
                  </div>
                  <div class="container">
                          <h3>3. Chicken Curry - $11.99</h3>
                          <img src="static/Chicken Curry.png" alt="Chicken Curry">
                          <p>Classic chicken curry cooked in a rich and flavorful sauce.</p>
                  </div>
                  <div class="container">
                          <h3>4. Chicken Sandwich - $8.99</h3>
                          <img src="static/Chicken Sandwich.png" alt="Chicken Sandwich">
                          <p>Grilled chicken sandwich with lettuce, tomato, and mayo.</p>
                  </div>
                  <div class="container">
                          <h3>5. Chicken Salad - $9.99</h3>
                          <img src="static/Chicken Salad.png" alt="Chicken Salad">
                          <p>Fresh chicken salad with mixed greens and vinaigrette dressing.</p>
                  </div>
                  <div class="container">
                          <h3>6. Chicken Wings - $10.99</h3>
                          <img src="static/Chicken Wings.png" alt="Chicken Wings">
                          <p>Spicy chicken wings served with blue cheese dip.</p>
                  </div>
                  <div class="container">
                          <h3>7. Chicken Tacos - $9.99</h3>
                          <img src="static/Chicken Tacos.png" alt="Chicken Tacos">
                          <p>Soft tacos filled with seasoned chicken, lettuce, and cheese.</p>
                  </div>
            <div class="container">
                    <h3>8. Chicken Alfredo - $13.99</h3>
                    <img src="static/Chicken Alfredo.png" alt="Chicken Alfredo">
                    <p>Creamy chicken alfredo pasta with parmesan cheese.</p>
            </div>
            <div class="container">
                    <h3>9. Chicken Wrap - $8.99</h3>
                    <img src="static/Chicken Wrap.png" alt="Chicken Wrap">
                    <p>Grilled chicken wrap with veggies and ranch dressing.</p>
            </div>
            <div class="container"> 
                    <h3>10. Chicken Nuggets - $7.99</h3>
                    <img src="static/Chicken Nuggets.png" alt="Chicken Nuggets">
                    <p>Crispy chicken nuggets served with your choice of dipping sauce.</p>
            </div>
            <div class="container">
                    <h3>11. Chicken Fried Rice - $10.99</h3>
                    <img src="static/Chicken Fried Rice.png" alt="Chicken Fried Rice">
                    <p>Stir-fried rice with chicken, vegetables, and soy sauce.</p>
            </div>
            <div class="container">
                    <h3>12. Chicken Quesadilla - $9.99</h3>
                    <img src="static/Chicken Quesadilla.png" alt="Chicken Quesadilla">
                    <p>Grilled quesadilla filled with chicken, cheese, and peppers.</p>
            </div>
            <div class="container">
                    <h3>13. Chicken Parmesan - $14.99</h3>
                    <img src="static/Chicken Parmesan.png" alt="Chicken Parmesan">
                    <p>Breaded chicken breast topped with marinara sauce and melted cheese.</p>
            </div>
            <div class="container"> 
                    <h3>14. Chicken Soup - $6.99</h3>
                    <img src="static/Chicken Soup.png" alt="Chicken Soup">
                    <p>Warm and comforting chicken soup with vegetables and noodles.</p>
            </div>
            <div class="container">
                    <h3>15. BBQ Chicken Pizza - $15.99</h3>
                    <img src="static/BBQ Chicken Pizza.png" alt="BBQ Chicken Pizza">
                    <p>Delicious pizza topped with BBQ chicken, red onions, and cilantro.</p>
            </div>
            <div class="container">
                    <h3>16. Chicken Caesar Salad - $10.99</h3>
                    <img src="static/Chicken Caesar Salad.png" alt="Chicken Caesar Salad">
                    <p>Classic Caesar salad topped with grilled chicken and croutons.</p>
            </div>

     </div>
     <footer> &copy; 2025 My Website. All rights reserved.</footer>
</body>
</html>


administratiion.html

<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hungry Chicken</title>
    <style>
      body {
          background-color: rgba(233, 158, 7, 0.955);
          
          font-family: Arial, sans-serif;
          margin: 0;
      }
      img {
          display: block;
          margin: 0;}
      nav {
        background-color: #3d3c3d;
        height: 50px;
        margin: 0;
        overflow: hidden;
        font-family:Arial, Helvetica, sans-serif;
        }
        nav a {
        float: right;
        display: block;
        color: white;
        padding: 0.75em 1em;
        text-decoration: none;
        }
        nav a:hover {
        background-color: #575757;
        }
                .banner {
                        text-align: center;
                        background-image: url('static/banner.png');
                        background-position: center;
                        background-size: cover;
                        background-repeat: no-repeat;
                        height: 250px;
                        width: 90%;
                        margin: 20px 0 0 0;
                        border-radius: 60px;
                        position: absolute;
                        left: 78px;
                }
                .menu {
                        position: absolute;
                        top: 490px;
                        left: 30px;
                        width: calc(100% - 60px);
                        display: flex;
                        flex-wrap: wrap;
                        flex-direction: row;
                        gap: 25px;
                        justify-content: center;
                }
                
                .container {
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        text-align: center;
                        gap: 10px;
                        padding: 28px;
                        border-radius: 16px;
                        background-color: #343131;
                        color: #fff;
                        box-sizing: border-box;
                        flex: 0 0 270px;
                        height: 350px;
                        min-width: 180px;
                        max-width: 300px;
                }
              .container img {
                        width: 200px;
                        height: 150px;
                        object-fit: cover;
                        border-radius: 8px;
                        }
                .container h3 {
                        margin: 0;
                        font-size: 1.2em;
                }
                .container p {
                        font-size: 0.9em;
                        line-height: 1.4;
                }
                .container:hover{
                        background-color: #575757;
                        transform: scale(1.05);
                        transition: transform 0.3s, background-color 0.3s;
                }
        footer {
                color: rgb(255, 254, 254);
                text-align: center;
                padding: 20px;
                bottom: 0;
                width: 1851px;
                position: relative;
                margin: 0;
                background-color: #343131;
                top: 1000px;
            }
    
    </style>
</head>
<body>
    <header>
       <img src="static/logo.jpg" alt="Hungry Chicken Logo" width="650px" style="margin: 0;">
    </header>
    <nav>
        <a href="contactus.html" style="font-size: larger;font-weight: bold;">Contact Us</a>
        <a href="administration.html" style="font-size: larger;font-weight: bold;">Administration</a>
        <a href="menu.html" style="font-size: larger;font-weight: bold;">Menu</a>
        <a href="home.html" style="font-size: larger;font-weight: bold;">Home</a>
    </nav>
     <h1 style="font-size: 50px; color: white;font-family:monospace; text-align: center; position: relative; top: 50px;" >Administration</h1>
<main>
     <div class="menu" style="left: 30px;">
                 <div class="container">
                                 <h3>- Restaurant Manager (General Manager)</h3>
                                 <img src="static/1.png" alt="">
                                 <p>Pavan</p>
                         </div>
                  <div class="container">
                          <h3>Head Chef / Kitchen Manager</h3>
                          <img src="static/2.png" alt="">
                          <p>Kalyan</p>
                  </div>
                  <div class="container">
                          <h3>Finance & Accounts Manager</h3>
                          <img src="static/3.png" alt="">
                          <p>Kavin</p>
                  </div>
                  <div class="container">
                          <h3>Human Resources (HR) / Staff Coordinator</h3>
                          <img src="static/4.png" alt="">
                          <p>Balaji</p>
                  </div>
                  <div class="container">
                          <h3>Marketing & Customer Relations Manager</h3>
                          <img src="static/5.png" alt="">
                          <p>Tharun</p>
                  </div>
                  <div class="container">
                          <h3>Procurement & Inventory Manager</h3>
                          <img src="static/6.png" alt="">
                          <p>Aaditya</p>
                  </div>
                  

     </div>
</main>
     <footer> &copy; 2025 My Website. All rights reserved.</footer>
</body>
</html>


contactus.html


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Us - Hungry Chicken</title>
  <link rel="stylesheet" href="styles.css">
  <style>
      body {
          background-color: rgba(233, 158, 7, 0.955);
          
          font-family: Arial, sans-serif;
          margin: 0;
      }
      img {
          display: block;
          margin: 0;}
      nav {
        background-color: #3d3c3d;
        height: 50px;
        margin: 0;
        overflow: hidden;
        font-family:Arial, Helvetica, sans-serif;
        }
        nav a {
        float: right;
        display: block;
        color: white;
        padding: 0.75em 1em;
        text-decoration: none;
        }
        nav a:hover {
        background-color: #575757;
        }
             
        
                 footer {
                color: rgb(255, 254, 254);
                text-align: center;
                padding: 20px;
                bottom: 0;
                width: 1851px;
                position: relative;
                margin: 0;
                background-color: #343131;
                top: 150px;
            }
    .contact-section {
      max-width: 800px;
      margin: 80px auto;
      padding: 20px;
      background: #373434;
      color: aliceblue;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
 
    </style>
</head>
<body>
    <header>
       <img src="static/logo.jpg" alt="Hungry Chicken Logo" width="650px" style="margin: 0;">
    </header>
    <nav>
        <a href="contactus.html" style="font-size: larger;font-weight: bold;">Contact Us</a>
        <a href="administration.html" style="font-size: larger;font-weight: bold;">Administration</a>
        <a href="menu.html" style="font-size: larger;font-weight: bold;">Menu</a>
        <a href="home.html" style="font-size: larger;font-weight: bold;">Home</a>
    </nav>

  <section class="contact-section">
    <h2>Contact Us</h2>
    <p>We’d love to hear from you! Reach out for reservations, catering, or feedback.</p>

    <div class="contact-grid">
      <!-- Contact Info -->
      <div class="contact-card">
        <h3>📍 Visit Us</h3>
        <p>123 Flavor Street<br>Food City, TN 600060</p>
      </div>

      <div class="contact-card">
        <h3>📞 Call Us</h3>
        <p>+91 98765 43210</p>
        <p>+91 91234 56789</p>
      </div>

      <div class="contact-card">
        <h3>✉️ Email Us</h3>
        <p>info@hungrychicken.com</p>
        <p>orders@hungrychicken.com</p>
      </div>

      <div class="contact-card">
        <h3>🕒 Hours</h3>
        <p>Mon–Sun: 11 AM – 11 PM</p>
      </div>
    </div>

    
    <form class="contact-form">
      <input type="text" placeholder="Your Name" required>
      <input type="email" placeholder="Your Email" required>
      <textarea placeholder="Your Message" required></textarea>
      <button type="submit">Send Message</button>
    </form>

    
    <div class="social-links">
      <a href="#">Instagram</a>
      <a href="#">Facebook</a>
      <a href="#">Twitter</a>
    </div>
  </section>
    <footer> &copy; 2025 My Website. All rights reserved.</footer>
</body>
</html>



~~~
# OUTPUT:
![alt text](<Screenshot (23).png>)
![alt text](<Screenshot (24).png>)
![alt text](<Screenshot (25).png>)
![alt text](<Screenshot (26).png>)
# RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
