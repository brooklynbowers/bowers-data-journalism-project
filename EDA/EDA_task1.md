# Exploratory Data Analysis

## Task 1 - Comparing Health and Engineering Professions with Overall Hourly Wage Trends

The first task of the exploratory data analysis section was to create a line plot 
that shows the overall hourly wage trend over time, and then comparing the overall 
hourly wage trend against health and engineering professionals. 

I first filtered the dataframe `hourly_wages_overall` for the selected occupations, 
and then pivoted the `selected_occupations` dataframe. 

```
selected_occupations = hourly_wages_overall[hourly_wages_overall['National Occupational Classification (NOC)'].isin(['Professional occupations in engineering [213]', 'Professional occupations in health [31]', 'Total employees, all occupations [00-95]'])]
pivot_df = selected_occupations.pivot_table(index='REF_DATE', columns='National Occupational Classification (NOC)', values='VALUE', aggfunc = 'mean')
```

Next, I created the line plot to display the overall hourly wage trend over time.

```
pivot_df.plot(figsize=(10, 6), marker='o')
plt.title('Hourly Wage Trends: Total Employees vs. Health and Engineering Professionals')
plt.xlabel('Year')
plt.ylabel('Average Hourly Wage ($)')
plt.xticks(rotation=45) 
plt.legend(title='Occupation')
plt.tight_layout()
plt.show() 
```

Output of the plot:
![hourly_trends_EDA1](https://github.com/brooklynbowers/data_journalism_project/assets/151276772/bdce2896-7d7e-4816-b6cf-880adafde20b)

Finally, to prepare for the Generative AI output, I summarized the analysis of the plot.

### Analysis of the Line Plot and Health, Engineering, and Overall Hourly Wage Trends

**Observations**

Individuals in engineering occupations have the highest average hourly wage among the 
three groups. There's a consistent upward trend across the years, with wages increasing 
from just below $45 to over $50. Those in health occupations also see an increase in 
average hourly wages over time, but the wages are consistently lower than for engineering 
professionals. The wages for health professionals increase from around $40 to approximately 
$45. The average hourly wage for all employees across all occupations shows a steady 
increase but remains significantly lower than the wages for the specialized professions 
of engineering and health. The trend starts from around $32 and approaches $35 by 2023.

**Inferences**

All groups show wage growth over the observed period, but the rate of growth is different, 
with engineering professionals seeing the most significant increase. There appears to be a 
'specialization premium' for professionals in engineering and health, with these occupations 
earning higher wages than the average across all occupations. This premium could be 
attributed to factors like higher educational requirements, specialized skills, or greater 
demand for these professionals. The consistent increase in wages could indicate economic 
growth, inflation, or changes in the labor market dynamics, such as increased demand for 
skilled workers in these fields.

**Additional Context**

Further analysis could compare these trends to other sectors to determine if similar 
wage growth patterns exist or if these trends are unique to the engineering and health 
sectors. Additional factors such as demographic shifts, regional economic developments, 
and changes in industry-specific regulations could also influence wage trends.

**Engineering Professionals**

The steady increase in wages for engineering professionals could be influenced 
by a few factors. Continuous innovation requires skilled engineers, increasing demand 
and wages. Investments in STEM education may have enhanced the skill set of engineers, 
which justifies higher wages. The current expansion in sectors like tech, renewable 
energy, or infrastructure might elevate demand for engineering skills.

**Health Professionals**

Wages for health professionals are also on the rise, likely due to a few factors, such as
an aging population and greater focus on health and wellness can increase demand for 
healthcare professionals. Increased healthcare spending and policies like universal 
healthcare coverage could raise demand and wages in this field. Furthermore, if this timeframe 
includes the COVID-19 pandemic or similar health crises, that could have significantly 
impacted the demand for healthcare workers.

**Total Employees Across All Occupations**

The general upward trend for all employees suggests that the health of the 
economy is good. An overall healthy economy with growth in GDP and corporate profits 
usually enables higher wages. Increases in the minimum wage can push up the 
lower end of the wage spectrum, affecting the average. A tight labor market with 
low unemployment rates can lead to across-the-board wage increases as businesses 
compete for workers.

**Inferences and Considerations**

The wage gap between specialized and general occupations could reflect differences 
in supply and demand dynamics, where specialized skills are in higher demand but lower 
supply. Consider the impact of recent changes in policy, such as educational subsidies 
for specific fields, healthcare reforms, or infrastructure spending, which could 
influence these trends. Overlaying these trends with key economic indicators like 
inflation, GDP growth, and unemployment rates could provide more context. If wages 
are growing but not outpacing inflation, the real wage growth could be minimal. If the 
period includes the pandemic years, the significant changes in wages, especially in 
health professions, could partly reflect temporary pandemic-related demand surges.


