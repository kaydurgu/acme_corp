# Acme Corp Warehouse Management System

## Overview

The Acme Corp Warehouse Management System is designed to streamline the management of products and personnel within the company's warehouses. The system is divided into two main applications: **Workers** and **Products**. 

### Apps

1. **Workers**: Manages all processes involving company employees.
2. **Products**: Handles all processes related to warehouse products.

## Features

### Products Enpoints 

- **GET /products/**: List all products.
- **GET /products/cat/**: List product categories.
- **POST /products/create/**: Add a new product.
- **GET /products/{id}**: Get details of a specific product.
- **GET /products/{id}/update/**: Retrieve product update form.
- **PUT /products/{id}/update/**: Fully update a product.
- **PATCH /products/{id}/update/**: Partially update a product.
- **DELETE /products/{id}/update/**: Delete a product.

### Users Endpoints

- **GET /users/**: List all users.
- **GET /users/{id}/**: Get details of a specific user.
- **GET /users/{id}/responsible**: List tasks/items a user is responsible for.
- **GET /users/{id}/update**: Retrieve user update form.
- **PUT /users/{id}/update**: Fully update a user.
- **PATCH /users/{id}/update**: Partially update a user.
- **DELETE /users/{id}/update**: Delete a user.
- 
### Filtering and Ordering

The system supports extensive filtering and ordering options for managing products:

- **Filtering by Category**:
  - **Field**: `category`

- **Searchable Fields**:
  - **Fields**: `name`, `description`, `barcode`

- **Ordering Options**:
  - **Fields**: `price`, `manufactured_date`, `expiration_date`
  - **Default Order**: `-price` (descending order by price)

### User Roles

- **Admin Users**: Have full access to the system, including user and product management.
- **Regular Workers**: Have restricted access, typically to their relevant tasks and responsibilities.



## Data Model

### Product Model

The `Product` model represents warehouse items with the following fields:

- **name**: `CharField` (max_length=255)
- **description**: `TextField`
- **price**: `DecimalField` (max_digits=10, decimal_places=2)
- **category**: `CharField` (max_length=2, choices=CATEGORY_CHOICES, default='OT')
- **manufactured_date**: `DateField`
- **expiration_date**: `DateField`
- **barcode**: `CharField` (max_length=25)
- **location**: `CharField` (max_length=55)
- **responsible_worker**: `ForeignKey` to `Profile` (from `worker` app, on_delete=models.CASCADE, related_name='responsible_worker')

##### CATEGORY_CHOICES

- ELECTRONICS: 'EL'
- FASHION: 'FA'
- HOME: 'HO'
- TOYS: 'TO'
- BOOKS: 'BO'
- SPORTS: 'SP'
- BEAUTY: 'BE'
- AUTOMOTIVE: 'AU'
- GROCERY: 'GR'
- HEALTH: 'HE'
- OFFICE: 'OF'
- OTHER: 'OT'

### Profile Model

The `Profile` model represents users with the following fields:

- **username**: `CharField` (inherited from `AbstractUser`)
- **phone_number**: `CharField` (max_length=20, blank=True, null=True)
- **first_name**: `CharField` (max_length=30)
- **last_name**: `CharField` (max_length=30)
- **birth_date**: `DateField` (blank=True, null=True)
- **address**: `CharField` (max_length=255, blank=True, null=True)
- **position**: `CharField` (max_length=100, blank=True, null=True)
- **hire_date**: `DateField` (blank=True, null=True)
- **bio**: `TextField` (blank=True, null=True)
- **is_active**: `BooleanField` (default=True)
- **role**: `CharField` (max_length=10, choices=ROLE_CHOICES, default='worker')
- **groups**: `ManyToManyField` to `auth.Group` (related_name='custom_user_groups', blank=True)
- **user_permissions**: `ManyToManyField` to `auth.Permission` (related_name='custom_user_permissions', blank=True)

### Roles

- Worker: 'worker'
- Admin: 'admin'


## Screenshots and Video Demonstration


## Getting Started

To run the application locally, follow these steps:

1. Clone the repository: `https://github.com/kaydurgu/acme_corp.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables for API keys and database configurations.
4. Apply migrations: `python manage.py migrate`
5. Run the development server: `python manage.py runserver`

## Contributors

- Bakytbek uulu Zhanbolot

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
