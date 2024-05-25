# Exploratory Data Analysis

## Task 3 - Analyzing Wage Disparity: Comparison by Occupation and Gender

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
Finally, plotting the heatmap.

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

To prepare for the Generative AI output, I summarized the analysis of the plot.

### Analysis of the Heatmap 


