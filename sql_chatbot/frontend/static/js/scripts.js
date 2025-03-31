async function sendPrompt() {
    const prompt = document.getElementById("userPrompt").value;
    const responseBox = document.getElementById("responseBox");

    responseBox.innerHTML = "Generating SQL and fetching data...";

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
    });

    const data = await response.json();

    if (data.error) {
        responseBox.innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
    } else {
        responseBox.innerHTML = `
            <strong>SQL:</strong> <code>${data.sql}</code><br><br>
            <strong>Result:</strong><br><pre>${JSON.stringify(data.result, null, 2)}</pre>
        `;
    }
}
