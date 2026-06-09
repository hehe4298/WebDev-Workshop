import os
import json
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from fpdf import FPDF
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize tools
search_tool = DuckDuckGoSearchRun()

# Initialize LLM (Ensure OPENAI_API_KEY is set in your .env file or environment)
# You can change the model if you prefer (e.g., gpt-4-turbo)
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# --- Define Agents ---

# 1. Company & Product Researcher
market_researcher = Agent(
    role='Inverter Market & Product Researcher',
    goal='Gather comprehensive information on inverter companies available in India, their market share, and list their popular products suitable for home use.',
    backstory='You are an expert market analyst specializing in electrical home appliances in India. You know all the top inverter brands (like Luminous, Microtek, Su-Kam, Exide, V-Guard, etc.) and their market standing.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 2. Product Analyst
product_analyst = Agent(
    role='Inverter Product Analyst',
    goal='Analyze the provided list of inverters, specifically filtering and comparing products that fall strictly under a 20,000 INR budget and are available in Hyderabad (Bachupally). Evaluate their capacities, battery requirements, and efficiency.',
    backstory='You are a meticulous technical analyst who understands the electrical requirements of a standard home in Hyderabad, especially considering frequent power cuts. You are strict about budgets and technical specifications like VA ratings and sine wave vs square wave.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 3. Reddit Reviewer
reddit_reviewer = Agent(
    role='Reddit & Forum Sentiment Analyst',
    goal='Search Reddit and other forums for the filtered products to find genuine user reviews, focusing on long-term disadvantages, customer service issues in India, and actual performance during power cuts.',
    backstory='You are a skeptical consumer advocate who doesn\'t trust marketing copy. You dig deep into Reddit (r/india, r/hyderabad, r/HomeImprovement) to find what real users complain about after using these inverters for months or years.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 4. Verification Agent
verification_agent = Agent(
    role='Fact-Checker & Verification Specialist',
    goal='Verify the technical specifications, current pricing (confirming it is <= 20,000 INR), and brand claims against official company websites or trusted retailers (like Amazon India or Flipkart). Ensure all data provided by previous agents is factual and up-to-date.',
    backstory='You are an auditor with a keen eye for detail. You cross-reference claims made by analysts and reviewers with official sources to ensure the final report contains no hallucinations or outdated information.',
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# 5. Report Compiler Agent
report_compiler = Agent(
    role='Executive Report Writer',
    goal='Compile all verified research into a highly structured, professional final report specifically formatted for easy PDF conversion. The report must exactly follow the user\'s requested structure.',
    backstory='You are a professional technical writer who synthesizes complex research from multiple agents into clear, actionable, and cleanly formatted reports.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# --- Define Tasks ---

task1_market_research = Task(
    description='Identify the top inverter companies operating in India. Provide a brief overview of each, estimate their market share, and list their major inverter series/products meant for home use.',
    expected_output='A detailed summary of top Indian inverter companies, their market share, and a list of their main home inverter products.',
    agent=market_researcher
)

task2_product_analysis = Task(
    description='''
    Based on the companies and products identified, filter down to specific inverter models that cost LESS THAN OR EQUAL TO 20,000 INR (including basic battery setup if possible, or note if the budget only covers the inverter).
    Consider the context: a home in Bachupally, Hyderabad experiencing constant power cuts.
    Compare these filtered products based on capacity (VA rating), type (Pure Sine Wave etc.), and features.
    ''',
    expected_output='A filtered list of inverters under 20k INR suitable for Hyderabad, with technical comparisons of their capacities and features.',
    agent=product_analyst
)

task3_reddit_reviews = Task(
    description='Take the filtered list of inverters (under 20k INR) and search Reddit/forums for long-term user experiences. Explicitly list the disadvantages, common failures, and customer support experiences for these specific brands/models in India.',
    expected_output='A critical analysis of the long-term disadvantages and real-world issues for the shortlisted inverters based on Reddit/forum user experiences.',
    agent=reddit_reviewer
)

task4_verification = Task(
    description='Review all the data collected so far (products, prices, specs, and disadvantages). Verify the prices to ensure they truly fit the 20,000 INR budget. Check official websites to confirm specifications. Flag and correct any inaccuracies.',
    expected_output='A fully verified and fact-checked dataset of the shortlisted inverters, confirming prices, specs, and valid criticisms.',
    agent=verification_agent
)

task5_compile_report = Task(
    description='''
    Create the final report using the verified data. The report MUST be structured exactly as follows using Markdown:

    # Inverter Market Overview
    [Details of all company names and how much market they occupy]

    # Comprehensive Product List
    [Details of all products offered by these companies generally]

    # Shortlisted Products (Under 20k INR for Hyderabad)
    [The products that meet the criteria from agents 1-5, including verified specs]

    # Individual Product Reports & Long-term Disadvantages
    [Detailed report on each shortlisted product, including the Reddit disadvantages]

    # Final Comparison
    [A clear comparison between the final shortlisted products to help the user choose]
    ''',
    expected_output='A cleanly formatted Markdown report containing all requested sections.',
    agent=report_compiler
)

# --- Create Crew ---
inverter_crew = Crew(
    agents=[market_researcher, product_analyst, reddit_reviewer, verification_agent, report_compiler],
    tasks=[task1_market_research, task2_product_analysis, task3_reddit_reviews, task4_verification, task5_compile_report],
    verbose=True,
    process=Process.sequential
)

# --- PDF Generation Function ---
def create_pdf(markdown_text, filename="Inverter_Report_Hyderabad.pdf"):
    print("Generating PDF report...")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Try to load a font that supports standard characters, fallback to default if not available
    pdf.set_font("Helvetica", size=11)

    # Simple markdown parsing for the PDF
    for line in markdown_text.split('\n'):
        # Handle headers
        if line.startswith('# '):
            pdf.set_font("Helvetica", style='B', size=16)
            pdf.multi_cell(0, 10, line.replace('# ', '').strip())
            pdf.ln(2)
        elif line.startswith('## '):
            pdf.set_font("Helvetica", style='B', size=14)
            pdf.multi_cell(0, 8, line.replace('## ', '').strip())
            pdf.ln(2)
        elif line.startswith('### '):
            pdf.set_font("Helvetica", style='B', size=12)
            pdf.multi_cell(0, 6, line.replace('### ', '').strip())
            pdf.ln(1)
        elif line.startswith('**') and line.endswith('**'):
            pdf.set_font("Helvetica", style='B', size=11)
            pdf.multi_cell(0, 6, line.replace('**', '').strip())
        else:
            # Normal text
            pdf.set_font("Helvetica", size=11)
            # Remove bold markdown for inline text to keep it simple in FPDF
            clean_line = line.replace('**', '')

            # FPDF sometimes struggles with special characters like ₹, encode safely
            try:
                # Use latin-1 compatible encoding or replace chars
                safe_line = clean_line.encode('latin-1', 'replace').decode('latin-1')
                pdf.multi_cell(0, 6, safe_line)
            except Exception as e:
                pass # skip unprintable lines

    pdf.output(filename)
    print(f"PDF successfully saved as {filename}")

if __name__ == "__main__":
    print("Starting Inverter Research Crew. This may take a few minutes as agents search the web...")

    # Run the crew
    result = inverter_crew.kickoff()

    # Output the raw result
    print("\n\n" + "="*50 + "\n")
    print("RAW MARKDOWN OUTPUT:")
    print(result)
    print("\n" + "="*50 + "\n")

    # Generate the PDF
    create_pdf(str(result))
