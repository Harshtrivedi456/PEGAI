# The Career Case File — AI Persona Career Counsellor

A single-file web app that answers your career questions through four distinct
AI career-counsellor personas, each powered by the Gemini API.

## 1. Problem Statement

Students asking "what should I do with my career?" usually get one generic
answer, even though the honest answer depends on who's giving the advice — a
technical mentor, an HR recruiter, an academic advisor, and a startup founder
would each highlight different things. Most chatbot demos also burn one API
call per persona, which doesn't scale under real rate limits.

## 2. Objective

Build a web-based AI Persona Application using the Gemini API that lets a
user ask a career question to one or more personas at once, with each
persona responding according to a clearly defined **Prompt Card** (Role,
Audience, Context, Format, Constraints, Language) — and to do it with a
**single Gemini API request**, no matter how many personas are selected.

## 3. Personas

| Persona | Focus |
|---|---|
| **Technical Career Counsellor** | AI/ML, programming, software development, technical skills, projects |
| **HR & Placement Counsellor** | Resume, interviews, employability, recruitment, placement prep |
| **Academic & Research Counsellor** | Higher studies, MS/M.Tech, PhD, research, certifications |
| **Entrepreneurship Counsellor** | Startups, business ideas, freelancing, product development |

Each persona is instructed to say **"I don't know"** and explain that the
question is outside its lane if asked something unrelated to its domain,
rather than answering anyway.

## 4. Prompt Cards

Every persona is fully specified in `index.html` (see the `PERSONAS` array)
using the six required elements. Example — Technical Career Counsellor:

| Element | Value |
|---|---|
| Role | Senior Technical Career Counsellor specializing in AI, ML, and Software Engineering |
| Audience | Undergraduate/early-career Computer Science or IT student |
| Context | Considers the student's technical skill gaps, tools, and project direction |
| Format | Recommendation → Skills to Develop → Project Suggestions → Roadmap |
| Constraints | Practical, realistic; no guaranteed jobs/salaries; says "I don't know" if off-topic |
| Language | Simple, direct English |

The remaining three Prompt Cards (HR & Placement, Academic & Research,
Entrepreneurship) follow the same structure and are visible in-app by
clicking **"view prompt card"** on each persona's folder tab.

A standalone one-page Prompt Card document (all four personas, six elements
each) should be exported separately for submission alongside this repo, per
the assignment's Deliverable 3.

## 5. Technology Used

- **HTML + CSS + JavaScript** — all in one file, `index.html`, no build step
- **Gemini API** (`gemini-2.0-flash`, `generateContent` endpoint) for all
  persona responses — no hard-coded advice
- **Google Fonts** (Fraunces, Inter, Space Mono) via CDN for styling only

## 6. Gemini API Integration — the "one request" architecture

Instead of one API call per persona:

```
User Question
     ↓
Selected Personas (their Prompt Cards)
     ↓
ONE structured prompt combining all of them
     ↓
ONE Gemini API request (responseMimeType: application/json)
     ↓
JSON keyed by persona id → each with its own response
     ↓
Rendered as separate memo cards + a comparison table
```

The prompt explicitly asks Gemini to answer **as each persona separately**,
following that persona's own Role/Audience/Context/Format/Constraints/
Language, and to return strict JSON so the frontend can split the single
response back out per persona and build the comparison table.

### API key

The app asks for your **own Gemini API key** in a password-style field in
the browser. The key is stored only in that browser's `localStorage` — it is
never written into this repository and never sent anywhere except directly
from your browser to Google's Gemini endpoint.

**Get a key:** https://aistudio.google.com/app/apikey

**Never commit your real key.** Do not put it in `index.html`, a `.env`
file, or anywhere else that gets pushed to GitHub.

## 7. How to Run

1. Clone this repository.
2. Open `index.html` directly in a browser (double-click it, or serve the
   folder with any static server, e.g. `python3 -m http.server`).
3. Paste your Gemini API key into the "Gemini API key" field.
4. Type a career question, select one or more counsellors, and click
   **Get Career Advice**.

No build tools, no dependencies to install.

## 8. Sample Questions to Test

1. *"Should I prepare for placements or pursue higher studies?"*
2. *"I know Python but do not have any projects. What should I do?"*
3. *"Should I become an AI Engineer, Data Scientist, or Software Developer?"*

Test each question with:
- a single persona selected
- multiple personas selected
- a few different combinations of personas

Also try an off-topic question (e.g. "What's the best pizza topping?") with
a single persona selected to confirm it responds "I don't know."

## 9. Sample Outputs


<img width="1118" height="1355" alt="image" src="https://github.com/user-attachments/assets/5b832340-3b97-44cd-b394-ac93f61ac628" />
<img width="1118" height="1355" alt="image" src="https://github.com/user-attachments/assets/638ba035-2f0b-4204-b6ea-49f580e82b1f" />


## 11. Created by: Harsh Trivedi

## Repository Structure

```
github/Harshtrivedi456/PEGAI/Career-Case-File/
├── index.html      # complete app: HTML + CSS + JS
├── README.md
└── assets/         # screenshots / demo assets go here
```
