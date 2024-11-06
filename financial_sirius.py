import pandas as pd
import matplotlib.pyplot as plt

# Data: Total Revenue for SiriusXM and Pandora over several quarters
data = {
    'Quarter': ['1Q20', '2Q20', '3Q20', '4Q20', '1Q21', '2Q21', '3Q21', '4Q21', '1Q22', '2Q22', '3Q22', '4Q22', '1Q23', '2Q23', '3Q23', '4Q23'],
    'SiriusXM_Total_Revenue': [1585, 1578, 1594, 1615, 1611, 1641, 1666, 1696, 1713, 1735, 1750, 1792, 1799, 1805, 1800, 1680],
    'Pandora_Total_Revenue': [369, 336, 438, 555, 442, 516, 538, 575, 467, 495, 505, 535, 539, 495, 500, 495],
}

# Data: Adjusted EBITDA for SiriusXM and Pandora over several quarters
ebitda_data = {
    'Quarter': ['1Q20', '2Q20', '3Q20', '4Q20', '1Q21', '2Q21', '3Q21', '4Q21', '1Q22', '2Q22', '3Q22', '4Q22', '1Q23', '2Q23', '3Q23', '4Q23'],
    'SiriusXM_Adjusted_EBITDA': [639, 615, 661, 660, 682, 700, 719, 672, 699, 706, 730, 760, 775, 785, 789, 800],
    'Pandora_Adjusted_EBITDA': [105, 70, 162, 234, 137, 193, 197, 217, 210, 218, 235, 255, 265, 245, 230, 240],
}

# Convert data into Pandas DataFrame
df_revenue = pd.DataFrame(data)
df_ebitda = pd.DataFrame(ebitda_data)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Plot Total Revenue for SiriusXM and Pandora
ax1.plot(df_revenue['Quarter'], df_revenue['SiriusXM_Total_Revenue'], label='SiriusXM Total Revenue', color='blue', marker='o')
ax1.plot(df_revenue['Quarter'], df_revenue['Pandora_Total_Revenue'], label='Pandora Total Revenue', color='green', marker='o')
ax1.set_title('Total Revenue for SiriusXM and Pandora (by Quarter)', fontsize=14)
ax1.set_xlabel('Quarter', fontsize=12)
ax1.set_ylabel('Total Revenue ($ millions)', fontsize=12)
ax1.legend()

# Plot Adjusted EBITDA for SiriusXM and Pandora
ax2.plot(df_ebitda['Quarter'], df_ebitda['SiriusXM_Adjusted_EBITDA'], label='SiriusXM Adjusted EBITDA', color='blue', marker='o')
ax2.plot(df_ebitda['Quarter'], df_ebitda['Pandora_Adjusted_EBITDA'], label='Pandora Adjusted EBITDA', color='green', marker='o')
ax2.set_title('Adjusted EBITDA for SiriusXM and Pandora (by Quarter)', fontsize=14)
ax2.set_xlabel('Quarter', fontsize=12)
ax2.set_ylabel('Adjusted EBITDA ($ millions)', fontsize=12)
ax2.legend()

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Tight layout for better spacing
plt.tight_layout()

# Save the chart as an image file
image_filename = 'siriusxm_pandora_financials.png'
plt.savefig(image_filename)

# Create HTML content with embedded image
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SiriusXM and Pandora Financials</title>
</head>
<body>
    <h1>SiriusXM and Pandora Financials</h1>
    <h2>Total Revenue and Adjusted EBITDA (by Quarter)</h2>
    
    <h3>Total Revenue</h3>
    <p>This chart shows the Total Revenue for SiriusXM and Pandora over several quarters:</p>
    <img src="{image_filename}" alt="Total Revenue and Adjusted EBITDA Chart" width="800px">
    
    <p>Generated by Python and Matplotlib.</p>
</body>
</html>
"""

# Save the HTML content to a file
html_filename = 'financials_report.html'
with open(html_filename, 'w') as html_file:
    html_file.write(html_content)

print(f"Chart saved as {image_filename} and HTML file saved as {html_filename}")