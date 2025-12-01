# BestEcoTutor
BestEcoTutor is an AI agent system built using Google’s Agent Development Kit (ADK) that empowers individuals, students, and households to understand and reduce their environmental impact through personalized guidance, actionable plans, and interactive educational content.

# BestEcoTutor — AI Sustainability Coach & Learning Companion

BestEcoTutor is an AI agent system built using **Google’s Agent Development Kit (ADK)** that empowers individuals, students, and households to understand and reduce their environmental impact through personalized guidance, actionable plans, and interactive educational content.

The project demonstrates real-world use of **multi-agent workflows, custom and built-in tools, session memory management, long-running operations, and agent evaluation** — designed as an **AI for Good** solution supporting sustainability and climate action.

---

## 🌍 Problem Statement
Climate change is one of the biggest challenges of our time, yet most people lack:
- Clear understanding of their personal carbon footprint
- Actionable steps tailored to their lifestyle and region
- Motivation and educational reinforcement to sustain long-term behavior change

Existing sustainability resources are **generic, fragmented, and not personalized**, making it difficult for people to translate awareness into measurable results.

---

## 🤖 Why Agents?
AI agents enable a smart, interactive coaching experience that adapts to real-world behavior.

| Capability | How BestEcoTutor uses it |
|------------|--------------------------|
| Multi-agent workflow | Collects data → calculates emissions → generates a 30-day action plan |
| Tools | Custom tools for carbon calculation & simulation; built-in search & code execution |
| Sessions & Memory | Learns user goals and progress over time for personalized coaching |
| Parallel + Sequential reasoning | Efficient structured computation & planning |
| Long-running operations | Tracks goals and progress beyond a single conversation |

Agents enable sustainability coaching that is **personalized, measurable, and educational**, unlike static apps.

---

## 🏗 Architecture Overview

### Multi-Agent System
| Agent | Function |
|--------|-----------|
| **Root Orchestrator Agent** | Workflow control, reasoning & response synthesis |
| **Intake Agent** | Collects electricity/water/transport usage & context |
| **Footprint Calculator Agent** | Computes CO₂ footprint and reduction scenarios |
| **Coaching & Learning Agent** | Generates action plan, explainers & quizzes |
| **Session & Memory Services** | Stores user profile, goals and history |

### Tools
- `calculate_footprint()`
- `simulate_reduction()`
- `store_goal()`
- Search & code execution
- Optional OpenAPI integration for regional factors

### Workflow
**Intake → Footprint Analysis → Recommendations → 30-Day Plan → Tracking & Review**

---

## 🎮 Demo Example Interaction

**User:** I use 275 kWh electricity, 7200 liters water and drive 160 km per month. Help me reduce 20%.

**BestEcoTutor:**  
- Your current footprint is **201.6 kg CO₂ / month**  
- Target reduction: **40.3 kg CO₂** (20%)  
- **30-Day Personalized Plan:**  
  - Reduce AC use by 1 hour/day (save 18 kg/month)  
  - Fix faucet leakage: 2500 L/month saved  
  - Replace 4 bulbs with LEDs  
  - Carpool once a week  
- **Quiz:** What is the largest contributor to household CO₂ emissions?

---

## 🧪 Evaluation
Example: `eco_tutor.test.json`
```
Expected: call.calculate_footprint AND generate recommendations
Success criteria: valid numeric output + actionable plan
```

---

## 📎 Attachments

| Type | Link |
|------|------|
| GitHub Repo | https://github.com/raxitdesai/BestEcoTutor |


---

## 🛠 Technology Stack
- Google ADK
- Gemini 2.5 Flash LLM
- Python
- Memory & Sessions
- Custom and built-in tools
- Vertex AI Agent Engine / Cloud Run
- Logging & metrics

---

## 🚀 How to Run Locally
```
git clone https://github.com/username/BestEcoTutor
cd BestEcoTutor
pip install -r requirements.txt
adk run eco_tutor_agent
```

---

## 🔮 Future Enhancements
- IoT integration (smart meters, solar trackers, water sensors)
- Gamified leaderboard & badges
- Real-time government rebates data
- Mobile & voice interface
- Multi-language support

---

## ❤️ AI for Good
Making sustainability **simple, measurable and personalized**, enabling everyone to contribute to climate action.

---
