document.getElementById("login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
  
    const employee_id = document.getElementById("employee_id").value;
    const password = document.getElementById("password").value;
  
    try {
      const response = await fetch("/api/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ employee_id, password }),
      });
  
      const result = await response.json();
  
      if (response.ok) {
        // Redirect to chatbot page
        window.location.href = "/chat";
      } else {
        alert(result.detail || "Login failed.");
      }
    } catch (error) {
      console.error("Login error:", error);
      alert("An error occurred during login.");
    }
  });
  