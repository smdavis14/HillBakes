# HillBakes

Capstone Proposal

HillBakes - Cookies and Cakes

I am going to build a website for selling cookies and cakes. My friend has a website on Wix but we can do better.

Project Overview

This will be a website were customers can view and purchase cookies and cakes. The user will be able to create an account if they choose to or remain a guest. As an account holder you will be able to look back and your order history. I will be using django framework and CSS styling. I may use Materialize but I haven’t decided, I’m not familiar with it so there is another learning curve.

Functionality

- User will be able to look at the menu of cookies and cakes with the prices listed.
- User will be able to sign up for an account if they choose to.
  - A logged in user will be able to look at their order history,.
- User will be able to get their order total and checkout (not really as it won’t be connected to any payment system.)

  Data Model

  User:

- username
- password
- email
  ProductType:
- Type
  - Cookies
  - Cake
  - Cake Balls
- Price
  $5
  $12
- Quantity

  Product:

- Name
- ProductType(ForiegnKey)

  UserHistory:

- ProductType(ForeignKey)
- quantity
- Product(ForeignKey)
- User(ForeignKey)

  Schedule

  Week 1:
  Build django backend

- all models created
- create needed views

  Week 2:
  Build HTML pages

- hybrid with frontend and backend
  Start JavaScript interaction

  Week 3:
  Complete frontend and backend interaction
  CSS styling, pictures, icons

  Week 4:
  Polish and work out any bugs
