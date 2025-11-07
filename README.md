
# 🧠 Travel Booking Agent – A Production-Grade Agentic AI System

> **An intelligent travel assistant that *thinks*, *plans*, and *acts* — not just chats.**

This repository demonstrates how to build a **production-style Agentic AI system** from scratch, designed for **autonomous decision-making**, **tool use**, and **explainable orchestration**.  
Unlike a rule-based chatbot, this agent dynamically reasons about user intent, decides *which tools* to call (e.g., flight search, hotel search, itinerary planning), and synthesizes natural, contextual answers.

---

## 🌍 Why Agentic AI for Travel?

Traditional AI assistants provide surface-level answers — “Here are a few flights.”  
An **agentic travel system** does much more:

- **Understands goals**, not just keywords (e.g., “family trip to Europe under ₹1L in June”).  
- **Plans actions**: chooses tools, fetches data, and revises decisions iteratively.  
- **Synthesizes context**: merges flight + hotel + itinerary results coherently.  
- **Explains reasoning**, making it transparent and debuggable.

This repo demonstrates those design principles **end-to-end** with clear modular code.

---

## ⚙️ Architecture Overview

```
travel_booking_agent/
  src/travel_agent/
    llm/          -> Language model and tool schemas
    tools/        -> Domain capabilities (flights, hotels, itinerary)
    agent/        -> Core orchestration, routing, state management
  scripts/        -> CLI & deployable entrypoints
  tests/          -> Tool-level validation
  notebooks/      -> Teaching and demo notebooks
```

### 🧩 System Components

| Layer | Role | Example File |
|-------|------|---------------|
| **LLM Interface** | Understands intent, decides tool usage | `llm/client.py`, `llm/toolspecs.py` |
| **Tools Layer** | Connects to APIs or domain logic | `tools/flights.py`, `tools/hotels.py` |
| **Agent Layer** | Orchestrates reasoning, state, and retries | `agent/runner.py`, `agent/router.py` |
| **Interface Layer** | Exposes via CLI or API | `scripts/run_cli_agent.py` |

---

## 🧠 The Agentic Flow

```mermaid
flowchart TD
    U[User Query] -->|Natural Language| A[LLM Agent]
    A -->|Tool Call| F[search_flights()]
    F -->|JSON Results| A
    A -->|Tool Call| H[search_hotels()]
    H -->|JSON Results| A
    A -->|Reason, Summarize| U[Response to User]
```

At runtime:
1. The **LLM** interprets user intent.  
2. The **AgentRunner** passes tool specs (what actions are allowed).  
3. The model chooses a tool + parameters.  
4. The **Router** executes the Python tool (may call APIs).  
5. The tool’s structured JSON is fed back to the LLM.  
6. The LLM reasons over the data and gives a final answer.

---

## 🧩 Example Interaction

```bash
$ python -m scripts.run_cli_agent

=== Travel Booking Agent ===
Type 'exit' to quit.

You: Find me a one-way flight from Hyderabad to London on 2025-11-15 under 60000 INR.
[agent] Decided to call tool 'search_flights' with args: {...}
[agent] Tool returned 2 flights.

Agent:
Here are the best options under your budget:
1️⃣ Emirates – ₹59,000 (1 stop via Dubai)  
2️⃣ IndiGo + Qatar – ₹52,000 (1 stop via Doha)
```

---

## 🧰 Modular Tools

All tools follow a **plug-and-play** pattern:

```python
def run_search_flights_tool(tool_args: dict) -> str:
    options = fake_web_flight_search(...)
    return json.dumps({"flights": [asdict(o) for o in options]}, ensure_ascii=False)
```

To go production-ready:
- Replace `fake_web_flight_search` with your real **Skyscanner / Amadeus API** client.  
- Extend `run_search_hotels_tool` similarly for Booking.com / Expedia APIs.  
- Implement authentication, caching, and rate-limiting around tool calls.

---

## 🧠 Design Principles

### 1. **Tool-First Design**
Each tool is a *contract* between the model and your code.
- Clearly defined name, description, parameters, and types.  
- The LLM decides *when and how* to call it.  
- You control *what it can do* — ensuring safety and reliability.

### 2. **Reasoning over Retrieval**
The agent doesn’t just return raw data. It:
- Filters results intelligently (budget, stops, location)
- Merges multi-tool outputs
- Generates a coherent human summary

### 3. **Traceable Behaviour**
Every tool call, argument, and output is logged — critical for debugging and explainability.

---

## 🧪 Testing

Tests focus on **tool correctness** and **schema consistency**.

```bash
pytest -q
```

Example test:
```python
def test_fake_web_flight_search_price_filter():
    flights = fake_web_flight_search(
        origin="HYD", destination="LHR",
        depart_date="2025-11-15", max_price=55000
    )
    assert all(f.price_inr <= 55000 for f in flights)
```

---

## 🚀 Extending the Agent

| Feature | How to Add |
|----------|------------|
| 🧩 **New domain tool** | Add a new Python file under `tools/` and register its spec in `toolspecs.py`. |
| 🌐 **Web or API integration** | Replace `fake_*` functions with real HTTP clients. |
| 🧱 **Memory / Profiles** | Persist `ConversationState` to Redis or a database. |
| 🧭 **Guardrails** | Validate tool arguments, cap budgets, filter unsafe URLs. |
| 💬 **FastAPI Interface** | Wrap `AgentRunner` in a REST endpoint for web use. |

---

## 🏗️ Setup & Run

```bash
git clone <repo-url>
cd travel_booking_agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then run:
```bash
python -m scripts.run_cli_agent
```

Environment:
```
OPENAI_API_KEY=<your-key>
```

---

## 🧭 Key Learnings for Engineers

1. **Agents are orchestrators, not monoliths** — separate thinking (LLM) from doing (tools).  
2. **Declarative contracts** via tool schemas make your LLM controllable and debuggable.  
3. **State management** is crucial — agents are stateful systems, not stateless chatbots.  
4. **Layered abstraction** lets you scale from CLI demo → production API → enterprise workflow.  
5. **LLM ≠ product** — orchestration + constraints + safety = usable AI.

---

## 💡 Vision

This travel booking agent is a **blueprint for enterprise Agentic AI systems** — whether in finance, logistics, healthcare, or HR.  
It shows how to go from *prompting* to *autonomous reasoning* and *tool-based decision-making* with clean, testable architecture.

> **From Chatbots → Agents → Orchestrated Intelligence.**

---

### 🧑‍💻 Author & Inspiration
Designed with a research-grade engineering mindset — balancing **clarity**, **control**, and **capability**.  
Built to inspire engineers to think beyond LLMs and towards **systemic intelligence**.
