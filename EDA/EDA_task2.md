# Exploratory Data Analysis

## Task 2 - Analyzing Casual and Permanent Employment

The second task of the exploratory data analysis section was to compare the average weekly wage between full-time and part-time employees, and then use a bar chart to visualize the data.

First, I needed to calculate the mean of the weekly wages for full-time and part-time employees from the corresponding DataFrames.

```
mean_weekly_wage_full_time = hourly_wages_fullTime['VALUE'].mean()
mean_weekly_wage_part_time = hourly_wages_partTime['VALUE'].mean()
```

Then, I created a new Dataframe to visualize these results.

```
mean_wages_df = pd.DataFrame({
    'Type of Work': ['Full-time', 'Part-time'],
    'Average Weekly Wage': [mean_weekly_wage_full_time, mean_weekly_wage_part_time]
})
```

Finally, I plotted the data to visualize the full and part time average wages.

```
mean_wages_df.plot(kind='bar', x='Type of Work', y='Average Weekly Wage', figsize=(8, 8), legend = False, color=['skyblue', 'lightgreen'])

formatter = ticker.FuncFormatter(lambda x, pos: f'${x:,.2f}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Average Weekly Wage: Full-time vs Part-time Employees')
plt.xlabel('Type of Work')
plt.ylabel('Average Weekly Wage ($)')
plt.xticks(rotation=0)  # Keep the labels on the x-axis readable
plt.tight_layout()  # Adjust layout to make room for the rotated x-labels
plt.show()
```

Output of plot:

![bar_chart_data_journalism](https://github.com/brooklynbowers/data_journalism_project/assets/151276772/73cec8d4-8366-4908-8d6a-8a8547d9e885)


To prepare for the Generative AI output, I summarized the analysis of the plot.

### Analysis of the Bar Graph and Casual and Permanent Employment

**Bar Graph Analysis**

The bar chart indicates a clear disparity in earnings between full-time and part-time employees. Full-time employees have a significantly higher average weekly wage compared to part-time employees. This difference highlights a crucial aspect of employment types and financial stability, where full-time employment typically offers more financial stability due to higher and consistent earnings. Full-time employees are more likely to receive additional benefits from their employer, which are not usually provided to part-time employees. These benefits can include health insurance, retirement benefits, paid time off, and more, contributing to the greater overall financial security of full-time employees. While part-time employment may offer flexibility and the possibility to combine work with other activities such as studying or caregiving, it often leads to lower overall earnings. Recieving a lower income can result in less financial stability, making it challenging for part-time workers to manage unexpected expenses or save for long-term goals.

The significant difference in wages as seen in the graph can have various implications. Those in part-time employment may have less disposable income, which could impact their purchasing power and overall economic participation. The disparity may prompt considerations for policy interventions to ensure part-time workers are supported, perhaps through wage supplements or access to pro-rated benefits based on hours worked.








