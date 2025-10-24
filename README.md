# 🐾 PetMarket
A Full-Stack Web Marketplace for Buying and Selling Pets

---

## 📝 Overview
PetMarket is a web-based marketplace where pet owners can list their pets for sale, and buyers can browse listings and view pet details. The platform includes secure user authentication and full CRUD operations for pet listings, with ownership enforcement ensuring only listing owners can modify or delete their pets.

---

## 🎯 Goals & Success Criteria

### Primary Goals
- 👤 Allow authenticated owners to list pets for sale with full CRUD functionality.
- 👀 Allow all users to browse listings and view pet details.
- 🔒 Enforce ownership: only the listing owner can edit or delete their listings.
- 🗄️ Use PostgreSQL as the primary data store.

### Success Criteria
- ✅ Users can sign up / sign in.
- 🐶 Owners can create, view, edit, and delete pet listings.
- 🖼️ Listings display pet details, including images.
- ⚠️ Authorization prevents unauthorized edits or deletions.

---

## ⚙️ Functional Requirements
- 🔐 **Authentication:** User sign-up, sign-in, and sign-out.
- 🐕 **Pet Listings (CRUD):** Owners can create, read, update, and delete listings.
- 🔑 **Ownership Enforcement:** Only listing owners can modify or delete pets.

---

## 📊 Data Models

### 👤 Owner (User)
- `id` (UUID or serial PK)  
- `name` (string, required)  
- `email` (string, required, unique)  
- `mobile` (string)  
- `address` (text)  

### 🐾 Pet
- `id` (UUID or serial PK)  
- `owner_id` (FK → owners.id, required)  
- `name` (string, required)  
- `age` (integer or string — e.g., months/years)  
- `breed` (string)  
- `type` (string — dog, cat, bird, reptile, other)  
- `color` (string)  
- `description` (text)  
- `price` (decimal, nullable)  

---

## 🗂️ User Stories

- **US-3: 📝 User Sign-up**  
  As a registered user, I want to create an account so I can list pets.  
  **Acceptance Criteria:** Sign-up validates email and stores hashed password.

- **US-4: 🐾 Create Pet Listing**  
  As an owner, I want to create a pet listing so I can sell a pet.  
  **Acceptance Criteria:** Form saves pet with `owner_id` and appears in my listings.

- **US-5: ✏️ Edit/Delete Pet Listing**  
  As an owner, I want to edit and delete my pet listings so I can keep them up to date.  
  **Acceptance Criteria:** Only the owner can edit/delete; other users receive a `403/forbidden`.

---

## 💻 Tech Stack
- 🌐 **Frontend:** React, HTML5, CSS3, JavaScript  
- 🖥️ **Backend:** Python, Django  
- 🗄️ **Database:** PostgreSQL  
- 🔐 **Authentication:** JWT / Django Auth  
- 🔧 **Version Control:** Git, GitHub  
- ☁️ **Deployment:** Render / Heroku / Railway
