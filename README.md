# Little-lemon-project

Welcome to the **Little-lemon-project** repository! This project is a RESTful API designed to manage a restaurant's menu system. It allows users to interact with menu items, including fetching all items, retrieving details for a single item, and providing administrative actions to add, update, or delete items.

---

## Table of Contents
- [Project Overview](#project-overview)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Installation](#installation)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The **Little-lemon-project** provides a simple way to manage restaurant menu items through a set of API endpoints. Whether you're an admin looking to modify the menu or a customer wanting to view the menu, this project has you covered.

### Features:
- Get all menu items.
- Get a single menu item by ID.
- Admin capabilities to add, update, or delete menu items.

---

## API Endpoints

### 1. **Get All Menu Items**
- **Endpoint:** `GET /api/menu-items`
- **Description:** Retrieve a list of all menu items.
  
### 2. **Get Single Menu Item by ID**
- **Endpoint:** `GET /api/menu-items/{id}`
- **Description:** Get details of a single menu item using its ID.
  
### 3. **Admin: Add New Menu Item**
- **Endpoint:** `POST /api/admin/menu-item`
- **Description:** Add a new menu item.
  
### 4. **Admin: Update Menu Item by ID**
- **Endpoint:** `PUT /api/admin/menu-item/{id}`
- **Description:** Update an existing menu item by its ID.

### 5. **Admin: Delete Menu Item by ID**
- **Endpoint:** `DELETE /api/admin/menu-item/{id}`
- **Description:** Delete a menu item based on its ID.

---

## Authentication

Certain API endpoints require **admin authentication**. Ensure you are authenticated when performing actions like adding, updating, or deleting menu items.

- **Authorization Method:** Bearer token (API key).
- The API key should be sent in the headers of each request.

Example of how to add the token to a request:
```http
Authorization: Bearer YOUR_API_KEY
