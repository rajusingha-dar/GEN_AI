document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("nameForm");
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");
  const letterPopup = document.getElementById("letter-popup");
  const letterBtn = document.getElementById("letterSelect");
  const uniqueness = document.getElementById("uniqueness");
  const uniquenessValue = document.getElementById("uniqueness-value");

  // Alphabet picker
  letterBtn.addEventListener("click", () => {
    letterPopup.classList.toggle("hidden");
    if (letterPopup.innerHTML === "") {
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").forEach(letter => {
        const btn = document.createElement("button");
        btn.textContent = letter;
        btn.onclick = () => {
          letterBtn.textContent = letter;
          letterPopup.classList.add("hidden");
        };
        letterPopup.appendChild(btn);
      });
    }
  });

  // Update slider value
  uniqueness.addEventListener("input", () => {
    uniquenessValue.textContent = uniqueness.value;
  });

  // Handle form submission
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    resultDiv.innerHTML = "";
    loadingDiv.classList.remove("hidden");

    const data = {
      country: document.getElementById("country").value,
      gender: document.getElementById("gender").value,
      language: document.getElementById("language").value,
      letter: letterBtn.textContent.length === 1 ? letterBtn.textContent : "",
      temperature: parseFloat(uniqueness.value),
      sibling_name: "",  // Optional
      description: document.getElementById("description").value,
    };

    const response = await fetch("/suggest", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });

    const result = await response.json();
    loadingDiv.classList.add("hidden");

    if (result.error) {
      resultDiv.innerHTML = `❌ Error: ${result.error}`;
    } else {
      resultDiv.innerHTML = "<h3>🍼 Suggested Baby Names:</h3>" + JSON.stringify(result, null, 2);
    }
  });
});
