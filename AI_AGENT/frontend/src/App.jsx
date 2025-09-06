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
    <div className="app-ai-agent">
      <div className="chat">
        {messages.map((msg, i) => (
          <div key={i} className={`${msg.role === "user" ? "user" : "chatbot"}`}>
            <span
              className={` ${msg.role === "user" ? "user-msg" : "chatbot-msg"
                }`}
            >
              <p>{` ${msg.role === "user" ? "You" : "Chatbot"
                }`}</p>
              {msg.content}
            </span>
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="text_field">
        <input
          className=""
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button className="">Send</button>
      </form>
    </div>
  );
}

export default App;
