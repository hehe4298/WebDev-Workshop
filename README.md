# Inverter Research Agents

This project contains an automated AI agent system built using CrewAI. It orchestrates multiple AI agents to research, analyze, and verify inverter options in India tailored to a specific budget (<= 20,000 INR) and location (Hyderabad).

The system then compiles this information into a formatted PDF report.

## Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.10+ installed.

### 2. Install Dependencies
Run the following command to install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Environment Variables
You need an OpenAI API key for the agents to function.
Create a `.env` file in the same directory as the script and add your key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

*Note: The script currently defaults to using `gpt-4o`. You can modify `inverter_research_agents.py` if you prefer to use `gpt-4-turbo` or another model.*

### 4. Run the Script
Execute the Python script:

```bash
python inverter_research_agents.py
```

### What to Expect
- The script will launch a crew of 5 agents:
  1. **Market Researcher:** Gathers companies and overall products.
  2. **Product Analyst:** Filters products based on the 20k INR budget and Hyderabad context.
  3. **Reddit Reviewer:** Searches Reddit for long-term user disadvantages.
  4. **Verification Agent:** Cross-references pricing and specs to ensure accuracy.
  5. **Report Compiler:** Synthesizes the data into a clean structure.
- You will see the agents "thinking" and searching the web in your terminal.
- Once complete, it will print the raw markdown and generate an `Inverter_Report_Hyderabad.pdf` file in the current directory.
