import { useState } from "react";

function Chatbot() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!message) return;

    const res = await fetch("http://127.0.0.1:5000/chatbot", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await res.json();

    setChat([...chat, { user: message, bot: data.reply }]);
    setMessage("");
  };

  return (
    <div style={{ width: "400px", margin: "20px auto" }}>
      <h3>Climate Chatbot</h3>

      {chat.map((c, i) => (
        <div key={i}>
          <p><b>User:</b> {c.user}</p>
          <p><b>Bot:</b> {c.bot}</p>
        </div>
      ))}

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask about climate..."
      />

      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;