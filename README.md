# Flask Personalization Settings App with PostgreSQL

This is a simple Flask app that allows you to manage personalization settings for users, integrated with a PostgreSQL database.

## Getting Started

Follow these steps to set up and run the app locally.

### Prerequisites

- Python (3.x recommended)
- `pip` (Python package installer)
- PostgreSQL or MySQL database server

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/flask-personalization-app.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd flask-personalization-app
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Set up the PostgreSQL or MySQL database:**

   - Create a database and note the database URL.
   - Update the `SQLALCHEMY_DATABASE_URI` in `app.py` with your database URL.

### Usage

1. **Run the Flask app:**

   ```bash
   python app.py
   ```

2. **The app will be running at `http://127.0.0.1:5000/`. You can make requests using tools like `curl` or Postman.**

### API Endpoints

- **GET /personalization_settings/<user_id>**
  - Retrieves all the personalization settings for the given user in JSON format.

- **POST /personalization_settings/<user_id>**
  - Saves all the personalization settings for a given user. Body is in JSON format.

- **DELETE /personalization_settings/<user_id>**
  - Deletes the personalization settings for a given user.

### Examples

- To retrieve personalization settings for user with `user_id = 1`:

  ```bash
  curl http://127.0.0.1:5000/personalization_settings/1
  ```

- To save personalization settings for user with `user_id = 1`:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"setting1": true, "setting2": false}' http://127.0.0.1:5000/personalization_settings/1
  ```

- To delete personalization settings for user with `user_id = 1`:

  ```bash
  curl -X DELETE http://127.0.0.1:5000/personalization_settings/1
  ```
