document.addEventListener("DOMContentLoaded", () => {
    const button = document.getElementById("submitBtn");
    if (button) {
      button.addEventListener("click", sendPrompt);
    }
  });
  
  async function sendPrompt() {
    const prompt = document.getElementById("userPrompt").value;
    const sqlOutput = document.getElementById("sqlOutput");
    const resultOutput = document.getElementById("resultOutput");
  
    if (!sqlOutput || !resultOutput) {
      console.error("Missing #sqlOutput or #resultOutput elements");
      return;
    }
  
    sqlOutput.innerText = "Generating SQL...";
    resultOutput.innerHTML = "Fetching result...";
  
    try {
      const response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt })
      });
  
      const data = await response.json();
  
      if (data.error) {
        sqlOutput.innerText = "⚠️ " + data.error;
        resultOutput.innerHTML = "";
      } else {
        sqlOutput.innerText = data.sql;
        resultOutput.innerHTML = renderTableFromJSON(data.result);
      }
    } catch (error) {
      sqlOutput.innerText = "Error: " + error.message;
      resultOutput.innerHTML = "";
    }
  }
  
  function renderTableFromJSON(data) {
    if (!Array.isArray(data) || data.length === 0) return "<p>No results found.</p>";
  
    const columns = Object.keys(data[0]);
    const table = document.createElement("table");
    table.classList.add("result-table");
  
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    columns.forEach(col => {
      const th = document.createElement("th");
      th.innerText = col;
      headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);
  
    const tbody = document.createElement("tbody");
    data.forEach(row => {
      const tr = document.createElement("tr");
      columns.forEach(col => {
        const td = document.createElement("td");
        td.innerText = row[col];
        tr.appendChild(td);
      });
      tbody.appendChild(tr);
    });
    table.appendChild(tbody);
  
    return table.outerHTML;
  }
  