document.getElementById("uploadBtn").addEventListener("click", () => {
  document.getElementById("fileInput").click();
});

document.getElementById("fileInput").addEventListener("change", async (e) => {
  const file = e.target.files[0];
  if (!file) return;

  showLoader();

  const formData = new FormData();
  formData.append("image", file);

  try {
    const res = await fetch("/upload", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    hideLoader();

    if (data.extracted) {
      addChatBubble(data.extracted, "user");
    }

    if (data.reply) {
      addChatBubble(data.reply, "bot");
      speakText(data.reply); // voice reply
    }

    saveChatToLog(data.extracted, data.reply);

  } catch (err) {
    hideLoader();
    console.error("Error:", err);
    addChatBubble("❌ Error processing image.", "bot");
  }
});

function addChatBubble(message, sender = "bot") {
  const chatContainer = document.getElementById("chatContainer");
  const bubble = document.createElement("div");
  bubble.className = sender === "user" ? "user-message" : "bot-message";
  bubble.innerHTML = `<strong>${sender === "user" ? "You" : "Transcend"}:</strong> ${message}`;
  chatContainer.appendChild(bubble);
  chatContainer.scrollTop = chatContainer.scrollHeight;
}

function showLoader() {
  document.getElementById("loader").style.display = "flex";
}

function hideLoader() {
  document.getElementById("loader").style.display = "none";
}

function speakText(text) {
  if (!("speechSynthesis" in window)) {
    console.warn("Text-to-speech not supported in this browser.");
    return;
  }

  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = "en-US"; // or "en-IN" for Indian English
  utterance.pitch = 1;
  utterance.rate = 1;
  utterance.volume = 1;

  // Optional: ensure a voice is available
  const voices = speechSynthesis.getVoices();
  if (voices.length > 0) {
    utterance.voice = voices[0]; // Choose the first available voice
  }

  speechSynthesis.cancel(); // Stop previous speech if overlapping
  speechSynthesis.speak(utterance);
}


function saveChatToLog(userMsg, botReply) {
  const logs = JSON.parse(localStorage.getItem("chatLogs") || "[]");
  logs.push({ user: userMsg, bot: botReply });
  localStorage.setItem("chatLogs", JSON.stringify(logs));
}

// New Chat Button Functionality
document.getElementById("newChatBtn").addEventListener("click", () => {
  // Clear the chat UI
  const chatContainer = document.getElementById("chatContainer");
  if (chatContainer) {
    chatContainer.innerHTML = "";
  }

  // Clear localStorage logs (optional)
  localStorage.removeItem("chatLogs");

  // Optionally clear chat logs from backend
  fetch("/clearlog", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      console.log("✅ Chat log cleared:", data.status);
    })
    .catch(err => {
      console.error("❌ Error clearing chat log:", err);
    });
});

// Send text input via ">" button or Enter key
document.getElementById("sendBtn").addEventListener("click", handleTextMessage);
document.getElementById("chatInput").addEventListener("keypress", function (e) {
  if (e.key === "Enter") handleTextMessage();
});

function handleTextMessage() {
  speechSynthesis.cancel(); // ⛔ Stop any ongoing speech
  const input = document.getElementById("chatInput");
  const msg = input.value.trim();

  addChatBubble(msg, "user");
  input.value = "";
  showLoader();

  fetch("/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ message: msg })
  })
    .then(res => res.json())
    .then(data => {
      hideLoader();
      if (data.reply) {
        addChatBubble(data.reply, "bot");
        speakText(data.reply); // voice output
        saveChatToLog(msg, data.reply);
      }
    })
    .catch(err => {
      hideLoader();
      console.error("❌ Error sending message:", err);
      addChatBubble("⚠️ Error sending message.", "bot");
    });
}

// 🔇 Stop speech on pressing Esc key
document.addEventListener("keydown", function (e) {
  if (e.key === "Escape") {
    speechSynthesis.cancel();
  }
});
