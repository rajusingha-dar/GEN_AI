document.addEventListener("DOMContentLoaded", () => {
    const signupForm = document.getElementById("signup-form");
  
    signupForm.addEventListener("submit", async (e) => {
      e.preventDefault();
  
      const fullName = document.getElementById("full_name").value.trim();
      const email = document.getElementById("email").value.trim();
      const phone = document.getElementById("phone").value.trim();
      const employeeId = document.getElementById("employee_id").value.trim();
      const password = document.getElementById("password").value;
  
      if (!fullName || !email || !phone || !employeeId || !password) {
        alert("Please fill in all fields.");
        return;
      }
  
      try {
        const response = await fetch("/api/auth/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            full_name: fullName,
            email: email,
            phone: phone,
            employee_id: employeeId,
            password: password
          })
        });
  
        const result = await response.json();
  
        if (response.ok) {
          alert("Signup successful! Redirecting to login...");
          window.location.href = "/";
        } else {
          alert(result.message || "Signup failed.");
        }
      } catch (err) {
        console.error("Error during signup:", err);
        alert("An error occurred. Please try again later.");
      }
    });
  });
  