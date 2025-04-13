from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from backend.utils.logger import logger
from backend.utils.config import get_db_connection
import hashlib 



router = APIRouter()

# 🔐 Dummy user data (replace with real DB logic in production)
users = {
    "1001": {
        "employee_id": "1001",
        "name": "Raju Singha",
        "password": "Mirik@1993"  # Replace with hashed password in real systems
    }
}

@router.post("/login")
async def login(request: Request):
    try:
        data = await request.json()
        employee_id = data.get("employee_id")
        password = data.get("password")

        logger.info(f"Login attempt for employee_id: {employee_id}")

        if not all([employee_id, password]):
            return JSONResponse(content={"message": "Employee ID and password are required."}, status_code=400)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE employee_id = %s", (employee_id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            # ✅ Hash the incoming password for comparison
            hashed_input = hashlib.sha256(password.encode()).hexdigest()

            if hashed_input == user["password"]:
                response = JSONResponse(content={"message": "Login successful!"})
                response.set_cookie(key="employee_name", value=user["name"])
                return response

        logger.warning("Invalid credentials")
        return JSONResponse(content={"message": "Invalid employee ID or password."}, status_code=401)

    except Exception as e:
        logger.error(f"Login error: {str(e)}")
        return JSONResponse(content={"message": "Internal server error."}, status_code=500)



# from fastapi import APIRouter, Request
# from fastapi.responses import JSONResponse
# from backend.utils.logger import logger
# from backend.utils.config import get_db_connection
# import hashlib

# router = APIRouter()

@router.post("/signup")
async def signup(request: Request):
    try:
        data = await request.json()
        full_name = data.get("full_name")
        email = data.get("email")
        phone = data.get("phone")
        employee_id = data.get("employee_id")
        password = data.get("password")

        if not all([full_name, email, phone, employee_id, password]):
            return JSONResponse(content={"message": "All fields are required."}, status_code=400)

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # ✅ Check for existing employee in correct table
        cursor.execute("SELECT * FROM users WHERE employee_id = %s", (employee_id,))
        if cursor.fetchone():
            return JSONResponse(content={"message": "Employee ID already exists."}, status_code=409)

        # ✅ Hash password before storing
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # ✅ Insert into correct table and column names
        cursor.execute(
            "INSERT INTO users (name, email, phone, employee_id, password) VALUES (%s, %s, %s, %s, %s)",
            (full_name, email, phone, employee_id, hashed_password)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return JSONResponse(content={"message": "Signup successful!"}, status_code=201)

    except Exception as e:
        logger.error(f"Signup error: {str(e)}")
        return JSONResponse(content={"message": "Internal server error."}, status_code=500)
