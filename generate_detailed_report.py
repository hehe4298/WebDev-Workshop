import sys
from fpdf import FPDF

def create_detailed_pdf(filename="Comprehensive_Inverter_Report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # ---------------------------------------------
    # SECTION 1: Market Overview & Company Details
    # ---------------------------------------------
    pdf.add_page()
    pdf.set_font("Helvetica", style='B', size=16)
    pdf.cell(0, 10, "1. Inverter Market Overview & Company Details", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", size=11)
    overview_text = """The Indian inverter market is expansive, driven by both residential power backup needs and a booming solar energy sector. The market is primarily dominated by legacy brands that have built extensive after-sales service networks across the country, alongside new entrants focusing on solar and lithium-ion technologies.

Below are the details of the top companies and their estimated market presence:

1. Luminous Power Technologies: One of the largest players in India. Founded in 1988, Luminous commands a massive chunk of the residential power backup market (estimated 25-30% share in the home segment). They are known for their reliable service network and wide range of products.
2. Microtek International: A major competitor to Luminous, heavily dominating the budget-friendly segment. They hold an estimated 20-25% of the residential market share.
3. Exide Industries: Primarily a battery giant, Exide leverages its battery dominance to sell heavy-duty inverters. They occupy roughly 15-20% of the market, particularly favored in regions with extremely long power cuts.
4. V-Guard Industries: A dominant force in South India, V-Guard is known for smart, aesthetically pleasing, and highly efficient inverters. Market share is around 10-15%.
5. Su-Kam (and Su-Vastika): Pioneers of the Indian inverter industry. While Su-Kam faced corporate restructuring, the founder's new venture, Su-Vastika, focuses heavily on Lithium-ion and solar innovations.
6. Livguard: A newer but rapidly growing brand backed by heavy marketing and strong dealer networks, capturing about 5-8% of the market.
7. Amaron: Known mostly for automotive batteries, Amaron's home inverters and batteries are respected for their longevity and zero-maintenance claims.
8. Genus Power: Highly focused on solar hybrid inverters and smart metering, holding a strong presence in rural and semi-urban solar markets.
9. Eastman Auto & Power: A veteran company providing robust power solutions primarily in Northern India.
10. Havells India: A giant in electrical goods that has recently entered the solar and residential inverter space with premium, feature-rich products.
11. Waaree Energies & Delta Electronics: Primarily industrial and heavy-duty solar inverter manufacturers, dominating the commercial rooftop and utility-scale solar sectors."""

    pdf.multi_cell(0, 6, overview_text)
    pdf.ln(10)

    # ---------------------------------------------
    # SECTION 2: Comprehensive Product List
    # ---------------------------------------------
    pdf.add_page()
    pdf.set_font("Helvetica", style='B', size=16)
    pdf.cell(0, 10, "2. Comprehensive Product Offerings by Company", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", size=10)
    products_text = """Luminous Power Technologies:
- Entry/Square Wave: Eco Watt Neo Series (700VA - 1500VA). Budget-friendly, basic backup.
- Pure Sine Wave: Eco Volt Neo, Zelio+ Series (Smart inverters with digital displays).
- High Capacity: Cruze Series (2KVA - 10KVA) for running ACs and entire homes.
- Solar Hybrid: Solar NXG, NXG PRO (PWM and MPPT solar charge controllers).

Microtek:
- Entry/Square Wave: Super Power Series (basic, robust).
- Pure Sine Wave: Luxe Series (LCD displays), Smart Hybrid Series.
- High Capacity: Jumbo Series (High KVA for small businesses).
- Solar: Solar PCU, SSG Series.

Exide Industries:
- Pure Sine Wave: GQP Series, Inverterz Star, Magic Series (highly durable PCBs).
- Solar: Solar Hybrid PCUs designed to work seamlessly with Exide Tubular batteries.
- Batteries: InvaTubular (IT series) which is the industry standard for durability.

V-Guard:
- Smart Inverters: Prime 1150, Smart Pro Series (Bluetooth/App controlled).
- Pure Sine Wave: V-Guard Smart Series, built for modern home aesthetics.

Livguard:
- Residential: LG Series (Pure Sine Wave) with fast charging technology.
- Batteries: InverTuff tall tubular batteries.

Su-Vastika / Su-Kam:
- Advanced Tech: Heavy duty Lithium-ion based inverters (wall mounted, space-saving).
- Pure Sine Wave: Falcon Plus series.

Amaron:
- Residential: Amaron Hi-Back (Pure Sine Wave). Known for silent operation and pairing with their zero-maintenance batteries."""

    pdf.multi_cell(0, 6, products_text)
    pdf.ln(10)

    # ---------------------------------------------
    # SECTION 3: Shortlisted Products (<20k INR)
    # ---------------------------------------------
    pdf.add_page()
    pdf.set_font("Helvetica", style='B', size=16)
    pdf.cell(0, 10, "3. Shortlisted Products for Hyderabad (Under 20,000 INR)", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", size=11)
    shortlist_text = """Criteria: Budget <= 20,000 INR, Location: Bachupally, Hyderabad.
Context: Frequent power cuts require Pure Sine Wave technology (to protect electronics) and a 150Ah Tall Tubular battery for 4-6 hours of backup.

1. Luminous Eco Volt Neo 1050 (900VA) + Luminous RC18000 (150Ah) Combo
- Price: INR 15,500 - 18,500
- Specs: Pure Sine Wave, Low Voltage Fast Charging (LVFC), 150Ah Tubular Battery.
- Warranty: 24 Months (Inverter), 36 Months (Battery).

2. Exide GQP 12V 1050VA + Exide Inva Tubular IT500 (150Ah) Combo
- Price: INR 18,000 - 19,800
- Specs: Pure Sine Wave, Heavy duty transformer, 150Ah IT500 Battery (industry standard).
- Warranty: 24 Months (Inverter), Up to 60 Months (Battery pro-rata).

3. Microtek Super Power 1100 + Microtek Smart Tall Tubular Battery (150Ah)
- Price: INR 14,500 - 16,500
- Specs: Pure Sine Wave, Microcontroller based design, 150Ah Battery.
- Warranty: 24 Months (Inverter), 36 Months (Battery).

4. V-Guard Prime 1150 + V-Guard VJ145 135Ah/150Ah Battery Combo
- Price: INR 17,500 - 19,500
- Specs: Pure Sine Wave, Battery Water Topping Reminder, Mute Buzzer option.
- Warranty: 24 Months (Inverter), 36 Months (Battery)."""

    pdf.multi_cell(0, 6, shortlist_text)
    pdf.ln(10)

    # ---------------------------------------------
    # SECTION 4: Individual Reports & Disadvantages
    # ---------------------------------------------
    pdf.add_page()
    pdf.set_font("Helvetica", style='B', size=16)
    pdf.cell(0, 10, "4. Individual Reports & Long-term Disadvantages", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", size=11)
    reports_text = """Based on long-term user reviews from forums (Reddit r/india, r/hyderabad, TeamBHP) and technical evaluations:

1. Luminous Eco Volt Neo 1050 Combo
- Report: Excellent overall performer. The LVFC technology is a massive boon in Hyderabad where grid voltage can fluctuate. Switchover time is <15ms, meaning PCs and Wi-Fi routers do not restart.
- Disadvantages: Users complain about the frequency of water topping required for the RC18000 battery during peak Hyderabad summers (needs checking every 2-3 months). The inverter's cooling fan can be slightly noisy when charging a completely depleted battery.

2. Exide GQP 1050VA Combo
- Report: The IT500 battery is highly praised; many users report it lasting 5 to 7 years with proper maintenance. The inverter handles heavy starting surges well.
- Disadvantages: The inverter PCB boards have been reported to fail after 3-4 years in areas with extreme voltage spikes. Exide's after-sales service for the *inverter* (repairing the box) is often reported as slower than Luminous, though battery replacements are seamless.

3. Microtek Super Power 1100 Combo
- Report: The ultimate budget option. Very rugged internal components.
- Disadvantages: The plastic outer casing feels flimsy. Users report that Microtek batteries tend to degrade faster in backup time after the 3-year mark compared to Exide. Customer service can be hit-or-miss depending on the specific locality in Hyderabad.

4. V-Guard Prime 1150 Combo
- Report: Highly rated for its modern design and smart features (like the water topping reminder, which solves the Luminous complaint).
- Disadvantages: Slightly more expensive for similar technical specs. V-Guard batteries are often white-labeled, meaning they don't manufacture the batteries themselves, leading to occasional inconsistencies in battery lifespan."""

    pdf.multi_cell(0, 6, reports_text)
    pdf.ln(10)

    # ---------------------------------------------
    # SECTION 5: Final Comparison
    # ---------------------------------------------
    pdf.add_page()
    pdf.set_font("Helvetica", style='B', size=16)
    pdf.cell(0, 10, "5. Final Comparison Matrix", ln=True)
    pdf.ln(5)

    pdf.set_font("Helvetica", size=10)
    comparison_text = """Comparing the 4 shortlisted products to finalize the best purchase decision:

| Feature | Luminous | Exide | Microtek | V-Guard |
|-----------------------|--------------------|--------------------|--------------------|--------------------|
| Max Load Capability | ~750 Watts | ~850 Watts | ~760 Watts | ~800 Watts |
| Backup Time (Avg) | 4.5 Hours | 5.0 Hours | 4.0 Hours | 4.5 Hours |
| Battery Durability | Very Good | Excellent | Good | Good |
| Inverter Tech | Fast Charging | Heavy Duty | Standard | Smart/App-based |
| Est. Combo Price | INR 17,000 | INR 19,000 | INR 15,500 | INR 18,500 |
| Hyderabad Service | Excellent | Good | Variable | Very Good |

FINAL RECOMMENDATION:
For a 20,000 INR budget in Bachupally, Hyderabad, the Luminous Eco Volt Neo 1050 + RC18000 Combo is the most balanced choice. It offers the best combination of fast charging (crucial for frequent cuts), reliable local service, and leaves INR 3,000 in your budget to purchase a high-quality trolley stand and cover electrician installation fees."""

    pdf.multi_cell(0, 6, comparison_text)

    # Save the PDF
    pdf.output(filename)
    print(f"PDF generated successfully: {filename}")

if __name__ == "__main__":
    create_detailed_pdf()
