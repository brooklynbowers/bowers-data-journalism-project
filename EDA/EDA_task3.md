# Exploratory Data Analysis

## Task 3 - Analyzing Wage Disparity: Comparison of Occupation and Gender

The final task of the exploratory data analysis section focused on analyzing the wage disparity between genders and occupations. First, I will identify the top 5 occupations with the highest average wage and then create a heatmap of those top 5 occupations average wages by occupation and gender to visualize the distribution across these dimensions. Finally, I will compare the bottom 3 and top 3 occupations for the average hourly wage between genders by plotting two boxplots that separate the top and bottom occupation.

First, I grouped the data by NOC (National Occupational Classification), calculated the mean wage and then reset the index to make sorting easier.

```
mean_wages_by_occupation = av_hourly_wages_overall.groupby('National Occupational Classification (NOC)')['VALUE'].mean().reset_index()
```

Now, sorting the Dataframe `top_5_occupations` by 'VALUE' in order to find the top 5 occupations with the highest average wage, and then filtering the original dataframe `av_hourly_wages_overall` for these top 5 occupations.

```
top_5_occupations = mean_wages_by_occupation.sort_values(by='VALUE', ascending=False).head(5)
filtered_for_heatmap = av_hourly_wages_overall[av_hourly_wages_overall['National Occupational Classification (NOC)'].isin(top_5_occupations['National Occupational Classification (NOC)'])]
```

Next, pivoting the filtered Dataframe for the heatmap visualization plot with 'Gender' as the index, 'NOC' as columns
and 'VALUE' (wage) as cell values. Then creating abbreviations for the x-value labels for readability.

```
heatmap_data = filtered_for_heatmap.pivot_table(index='Gender',
                                                columns='National Occupational Classification (NOC)',
                                                values='VALUE',
                                                aggfunc='mean')

abbreviations = {
    'Legislative and senior management occupations [00]': 'Legislative/ Sen Management',
    'Management occupations [00, 10, 20, 30, 40, 50, 60, 70, 80, 90]': 'Management',
    'Middle management occupations in trades, transportation, production and utilities [70, 80, 90]': 'Middle Management',
    'Professional occupations in law [411]': 'Professional Law',
    'Specialized middle management occupations [10, 20, 30, 40, 50]': 'Specialized Middle Management',
    'Care providers and public protection support occupations and student monitors, crossing guards and related occupations [44-45]': 'Care Providers/ Public Protection',
    'Sales and service support occupations [65]': 'Sales/ Service Support',
    'Labourers in processing, manufacturing and utilities [95]' : 'Labourers'
}
```
Plotting the heatmap:

```
heatmap_data.columns = [abbreviations.get(noc, noc) for noc in heatmap_data.columns]

plt.figure(figsize=(10, 8)) 
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f") 
plt.title('Average Wages by Occupation and Gender')
plt.ylabel('Gender')
plt.xlabel('Occupation')
plt.xticks(rotation=45, ha="right")  
plt.tight_layout() 
plt.show()
```

![heat_map_EDA3](https://github.com/brooklynbowers/data_journalism_project/assets/151276772/46e51aea-1945-41c1-a63a-7b3a5299c93d)

Next, we will compare the bottom and top three occupations for the average hourly wage between gender. To visualize this data, we will use boxplots and separate the top and bottom occupations in the visualization.

First, recalculating mean wages by occupation for the entire dataset.

```
mean_wages_by_occupation = av_hourly_wages_overall.groupby('National Occupational Classification (NOC)')['VALUE'].mean().reset_index()
```

Now, identifying the top 3 and bottom 3 occupations based on average wage, and then filtering the original dataframe `av_hourly_wages_overall` to include only the top three and bottom three occupations.

```
top_3_occupations = mean_wages_by_occupation.nlargest(3, 'VALUE')['National Occupational Classification (NOC)']
bottom_3_occupations = mean_wages_by_occupation.nsmallest(3, 'VALUE')['National Occupational Classification (NOC)']
filtered_df = av_hourly_wages_overall[
    av_hourly_wages_overall['National Occupational Classification (NOC)'].isin(top_3_occupations) |
    av_hourly_wages_overall['National Occupational Classification (NOC)'].isin(bottom_3_occupations)
].copy()
```

Next, I added a new column (named 'Category') to distinguish between top and bottom occupations and mapped the NOC codes to abbreviations to make the plot easier to read.

```
filtered_df['Category'] = filtered_df['National Occupational Classification (NOC)'].apply(
    lambda x: 'Top 3' if x in top_3_occupations.tolist() else 'Bottom 3'
)
filtered_df['Abbreviated NOC'] = filtered_df['National Occupational Classification (NOC)'].map(abbreviations)
```

Now determining the order of occupations for the boxplot based on their abbreviations. This was done because presenting the data in a logical order enhances clarity and understanding of the graph. Without this step, the occupations might appear in an arbitrary or default order that doesn't reflect their ranking based on average wages.

```
abbreviated_order = [abbreviations[noc] for noc in top_3_occupations.tolist() + bottom_3_occupations.tolist() if noc in abbreviations]
```

Finally, plotting the boxplots:

```
plt.figure(figsize=(8, 8))
sns.boxplot(data=filtered_df, x='Abbreviated NOC', y='VALUE', hue='Sex', dodge=True, palette="Set3", order=abbreviated_order)
plt.title('Comparison of Average Hourly Wage Between Gender for Top and Bottom Occupations')
plt.xticks(rotation=45)
plt.xlabel('Occupations')
plt.ylabel('Average Hourly Wage')
plt.legend(title='Gender') 
plt.tight_layout()
plt.show()
```

![boxplots_for_EDA3](https://github.com/brooklynbowers/data_journalism_project/assets/151276772/544fa3fb-d55a-4c2c-84c9-ffff925e5f2c)


To prepare for the Generative AI output, I summarized the analysis of both plots.

### Analysis of the Heatmap and Boxplots

**Heatmap Analysis**
The heat map indicates that in every occupation listed in this analysis, males have higher average wages than females, which indicates a persistent gender wage gap. The heat map also indicated that males in legislative and senior management positions earn significantly more on average than females in the same occupation, and this wage gap is more pronounced than in other professions.

**Boxplot Analysis**
The boxplots indicate that across all occupations in this analysis, males tend to have a higher median wage than females. This is indicated by the median of the male boxplots generally being higher than the female median. The Legislative/Senior Management occupation shows the widest wage gap, with the median male wage significantly higher than the median female wage. Specialized Middle Management and Professional Law occupations also show a noticeable wage gap, though not as prominent as in legislative/senior management. The wage gap appears narrower in the Sales/Service Support, Labourers, Care Providers/Public Protection occupations, but it's still present, with males having a higher median wage than females.

**Inferences and Contextualization**
The wage gaps may be partially explained by occupational segregation, where women and men are concentrated in different types of jobs, which may have different levels of pay. Despite efforts to address pay equity, these graphs illustrate that significant wage disparities between genders persist, particularly in higher-paying occupations.

Policies aimed at reducing the gender wage gap, such as equal pay legislation, transparency in compensation, and parental leave policies, may not have fully bridged the gap between males and females. Further analysis could determine the effectiveness of such policies over time. Differences in negotiation practices and promotion rates between men and women could contribute to the wage gap. Women are also more likely to engage in part-time work and take career breaks due to caregiving, which can impact their average wages.




