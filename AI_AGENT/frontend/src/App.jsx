// src/App.jsx
import { useState } from "react";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  async function sendMessage(e) {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessage = { role: "user", content: input };
    setMessages([...messages, newMessage]);

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await res.json();

    setMessages((msgs) => [
      ...msgs,
      { role: "assistant", content: data.reply, think: data.think },
    ]);
    setInput("");

    console.log(msg.think)
  }

  return (
    <div className="p-4 max-w-lg mx-auto">
      <div className="h-96 overflow-y-auto border rounded p-2 mb-2 bg-gray-50">
        {messages.map((msg, i) => (
          <div key={i} className={`mb-2 ${msg.role === "user" ? "text-right" : "text-left"}`}>
            <span
              className={`inline-block px-3 py-2 rounded-lg ${msg.role === "user" ? "bg-blue-500 text-white" : "bg-gray-200"
                }`}
            >
              {msg.content}
            </span>
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="flex">
        <input
          className="flex-grow border rounded-l px-3 py-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button className="bg-blue-500 text-white px-4 rounded-r">Send</button>
      </form>
    </div>
  );
}

export default App;
