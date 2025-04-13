document.addEventListener("DOMContentLoaded", async () => {
    const chatWindow = document.getElementById("chat-window");
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
  
    const appendMessage = (message, sender = "bot") => {
      const msgDiv = document.createElement("div");
      msgDiv.classList.add("message", sender === "user" ? "user-msg" : "bot-msg");
      msgDiv.textContent = message;
      chatWindow.appendChild(msgDiv);
      chatWindow.scrollTop = chatWindow.scrollHeight;
    };
  
    // ✅ Initial greeting from agent
    try {
      const greetRes = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: "__greet__" })
      });
      const greetData = await greetRes.json();
      appendMessage(greetData.response);
    } catch (err) {
      appendMessage("⚠️ Unable to greet user at the moment.");
    }
  
    chatForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const message = userInput.value.trim();
      if (!message) return;
  
      appendMessage(message, "user");
      userInput.value = "";
  
      try {
        const res = await fetch("/api/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ prompt: message })
        });
        const data = await res.json();
        appendMessage(data.response);
      } catch (err) {
        appendMessage("⚠️ Assistant failed to respond.");
      }
    });
  });
  