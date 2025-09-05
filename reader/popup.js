document.getElementById("send").addEventListener("click", async () => {
    const input = document.getElementById("input").value;
    if (!input) return;
  
    addMessage("You: " + input);
  
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => document.body.innerText // get page text
    });
  
    // Send both query + page text to your LangChain backend
    const response = await fetch("http://127.0.0.1:8000/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        question: input,
        text: result
      })
    });
  
    const data = await response.json();
    addMessage("AI: " + data.answer);
  });
  
  function addMessage(msg) {
    const messages = document.getElementById("messages");
    const div = document.createElement("div");
    div.textContent = msg;
    messages.appendChild(div);
  }
  