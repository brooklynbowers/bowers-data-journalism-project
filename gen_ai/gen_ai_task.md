# Generative AI - Data Journalism Output

## Task - Structure the generative ai response along with the visuals developed in the EDA section

To complete this task, I first needed to create an API key from OpenAI, create a .txt file with the api key and then upload this .txt file to google collab. 

```
from google.colab import files
uploaded = files.upload()
api_key_path = 'file_for_api_key_goes_here.txt'
```

Next, I had the model read the API key and then set the API key in the environment.

```
with open('file_for_api_key_goes_here.txt', 'r') as file:
    api_key = file.readline().strip()
os.environ['OPENAI_API_KEY'] = api_key
```

Next, I initialized the OpenAI client and specified the model that I wanted to use.
```
client = OpenAI(api_key=api_key)
model = "gpt-3.5-turbo"
```

Then I included the text needed for the analysis, using both the data and the description of the data for context.

```
text = """
Analyze and discuss the data on Canadian wages with a focus on three key aspects.

1. First, provide insight into overall wage trends over time, considering economic factors and policy impacts that have influenced these trends.

Observations: Individuals in engineering occupations have the highest average hourly wage among the three groups. There's a consistent upward trend across the years, with wages increasing from just below \$45 to over \$50. Those in health occupations also see an increase in average hourly wages over time, but the wages are consistently lower than for engineering professionals. The wages for health professionals increase from around \$40 to approximately \$45. The average hourly wage for all employees across all occupations shows a steady increase but remains significantly lower than the wages for the specialized professions of engineering and health. The trend starts from around \$32 and approaches \$35 by 2023.

Inferences: All groups show wage growth over the observed period, but the rate of growth is different, with engineering professionals seeing the most significant increase. There appears to be a 'specialization premium' for professionals in engineering and health, with these occupations earning higher wages than the average across all occupations. This premium could be attributed to factors like higher educational requirements, specialized skills, or greater demand for these professionals. The consistent increase in wages could indicate economic growth, inflation, or changes in the labor market dynamics, such as increased demand for skilled workers in these fields.

Additional Context: Further analysis could compare these trends to other sectors to determine if similar wage growth patterns exist or if these trends are unique to the engineering and health sectors. Additional factors such as demographic shifts, regional economic developments, and changes in industry-specific regulations could also influence wage trends.

Engineering Professionals: The steady increase in wages for engineering professionals could be influenced by the following:
- Continuous innovation requires skilled engineers, increasing demand and wages.
- Investments in STEM education may have enhanced the skill set of engineers, which justifies higher wages.
- The current expansion in sectors like tech, renewable energy, or infrastructure might elevate demand for engineering skills.

Health Professionals: Wages for health professionals are also on the rise, likely due to the following:
- An aging population and greater focus on health and wellness can increase demand for healthcare professionals.
- Increased healthcare spending and policies like universal healthcare coverage could raise demand and wages in this field.
- If this timeframe includes the COVID-19 pandemic or similar health crises, that could have significantly impacted the demand for healthcare workers.

Total Employees Across All Occupations: The general upward trend for all employees suggests:
- The economic health of the economy is good. An overall healthy economy with growth in GDP and corporate profits usually enables higher wages.
- Increases in the minimum wage can push up the lower end of the wage spectrum, affecting the average.
- A tight labor market with low unemployment rates can lead to across-the-board wage increases as businesses compete for workers.

Inferences and Considerations: The wage gap between specialized and general occupations could reflect differences in supply and demand dynamics, where specialized skills are in higher demand but lower supply. Consider the impact of recent changes in policy, such as educational subsidies for specific fields, healthcare reforms, or infrastructure spending, which could influence these trends. Overlaying these trends with key economic indicators like inflation, GDP growth, and unemployment rates could provide more context. If wages are growing but not outpacing inflation, the real wage growth could be minimal. If the period includes the pandemic years, the significant changes in wages, especially in health professions, could partly reflect temporary pandemic-related demand surges.

2. Second, detail the gender wage difference, highlighting the ongoing issue of pay equity between men and women across different sectors.

Bar Graph Analysis: The bar chart indicates a clear disparity in earnings between full-time and part-time employees. Full-time employees have a significantly higher average weekly wage compared to part-time employees. This difference highlights a crucial aspect of employment types and financial stability, where full-time employment typically offers more financial stability due to higher and consistent earnings. Full-time employees are more likely to receive additional benefits from their employer, which are not usually provided to part-time employees. These benefits can include health insurance, retirement benefits, paid time off, and more, contributing to the greater overall financial security of full-time employees. While part-time employment may offer flexibility and the possibility to combine work with other activities such as studying or caregiving, it often leads to lower overall earnings. Recieving a lower income can result in less financial stability, making it challenging for part-time workers to manage unexpected expenses or save for long-term goals. The significant difference in wages as seen in the graph can have various implications. Those in part-time employment may have less disposable income, which could impact their purchasing power and overall economic participation. The disparity may prompt considerations for policy interventions to ensure
part-time workers are supported, perhaps through wage supplements or access to pro-rated benefits based on hours worked.

3. Lastly, explore the employment types to uncover disparities in earnings, especially focusing on how financial stability affects the hourly rates

Heatmap Analysis: The heat map indicates that in every occupation listed in this analysis, males have higher average wages than females, which indicates a persistent gender wage gap. The heat map also indicated that males in legislative and senior management positions earn significantly more on average than females in the same occupation, and this wage gap is more pronounced than in other professions.

Boxplot Analysis: The boxplots indicate that across all occupations in this analysis, males tend to have a higher median wage than females. This is indicated by the median of the male boxplots generally being higher than the female median. The Legislative/Senior Management occupation shows the widest wage gap, with the median male wage significantly higher than the median female wage. Specialized Middle Management and Professional Law occupations also show a noticeable wage gap, though not as prominent as in legislative/senior management. The wage gap appears narrower in the Sales/Service Support, Labourers, Care Providers/Public Protection occupations, but it's still present, with males having a higher median wage than females.

Inferences and Contextualization: The wage gaps may be partially explained by occupational segregation, where women and men are concentrated in different types of jobs, which may have different levels of pay. Despite efforts to address pay equity, these graphs illustrate that significant wage disparities between genders persist, particularly in higher-paying occupations. Policies aimed at reducing the gender wage gap, such as equal pay legislation, transparency in compensation, and parental leave policies, may not have fully bridged the gap between males and females. Further analysis could determine the effectiveness of such policies over time. Differences in negotiation practices and promotion rates between men and women could contribute to the wage gap. Women are also more likely to engage in part-time work and take career breaks due to caregiving, which can impact their average wages.

Each of these points should form a separate paragraph, together building a coherent narrative for a data journalism piece.
"""
```

Finally, I prepared messages for the model, sent the request to the model, and then extracted and printed the response.

```
messages = [
    {"role": "system", "content": "You are a data journalism assistant"},
    {"role": "user", "content": f"Write a small paragraph here to analyze this data:\n{text}. The goal is to interpret it in a way that's interesting for a Data journalism piece."}
]
response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=0
)
response_message = response.choices[0].message.content
print(response_message)
```

Below is the final output from the model of the Data Journalism article that I requested from the prompt:

#insert gif here
