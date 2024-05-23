# Exploratory Data Analysis

# tasks:
# 1. create a line plot that shows the overall hourly wage trend over time
# 2. comparing the overall hourly wage trend (total employees) against health and 
# engineering professionals

######################

# filtering the dataframe hourly_wages_overall for the selected occupations
selected_occupations = hourly_wages_overall[hourly_wages_overall['National Occupational Classification (NOC)'].isin(['Professional occupations in engineering [213]', 'Professional occupations in health [31]', 'Total employees, all occupations [00-95]'])]

# pivot the 'selected_occupations' dataframe to plot
pivot_df = selected_occupations.pivot_table(index='REF_DATE', columns='National Occupational Classification (NOC)', values='VALUE', aggfunc = 'mean')

# plotting the pivoted dataframe selected_occupations
pivot_df.plot(figsize=(10, 6), marker='o')
plt.title('Hourly Wage Trends: Total Employees vs. Health and Engineering Professionals')
plt.xlabel('Year')
plt.ylabel('Average Hourly Wage ($)')
plt.xticks(rotation=45)
plt.legend(title='Occupation')
plt.tight_layout() 
plt.show() 

############

# compare the average weekly wage between full-time and part-time employees
# using a bar chart to for visualization
# calculation method: finding the average between all the available years in the dataset for both types of work

# calculating the mean (average) of the weekly wages for full-time and part-time employees from corresponding DataFrames
mean_weekly_wage_full_time = hourly_wages_fullTime['VALUE'].mean()
mean_weekly_wage_part_time = hourly_wages_partTime['VALUE'].mean()

# creating a new Pandas DataFrame for visualization
mean_wages_df = pd.DataFrame({
    'Type of Work': ['Full-time', 'Part-time'],
    'Average Weekly Wage': [mean_weekly_wage_full_time, mean_weekly_wage_part_time]
})

# plotting the average wages
mean_wages_df.plot(kind='bar', x='Type of Work', y='Average Weekly Wage', figsize=(8, 8), legend = False, color=['skyblue', 'lightgreen'])

formatter = ticker.FuncFormatter(lambda x, pos: f'${x:,.2f}')
plt.gca().yaxis.set_major_formatter(formatter)

plt.title('Average Weekly Wage: Full-time vs Part-time Employees')
plt.xlabel('Type of Work')
plt.ylabel('Average Weekly Wage ($)')
plt.xticks(rotation=0)  # Keep the labels on the x-axis readable
plt.tight_layout()  # Adjust layout to make room for the rotated x-labels
plt.show()

######################

# next tasks:
# identify the top 5 occupations with the highest average wage
# plot a heatmap of those top 5 occupations average wages by occupation and sex 
#   to visualize the distribution across these dimensions
# compare the bottom 3 and top 3 occupations for the average hourly wage between sexes

# grouping data by NOC, calculating the mean wage and resetting the index
mean_wages_by_occupation = av_hourly_wages_overall.groupby('National Occupational Classification (NOC)')['VALUE'].mean().reset_index()

# sorting dataframe top_5_occupations by 'VALUE' in order to find the top 5 occupations with the highest average wage
top_5_occupations = mean_wages_by_occupation.sort_values(by='VALUE', ascending=False).head(5)

# filtering the original dataframe av_hourly_wages_overall for these top 5 occupations
filtered_for_heatmap = av_hourly_wages_overall[av_hourly_wages_overall['National Occupational Classification (NOC)'].isin(top_5_occupations['National Occupational Classification (NOC)'])]

# pivoting the filtered dataframe for the heatmap visualization plot
heatmap_data = filtered_for_heatmap.pivot_table(index='Sex',
                                                columns='National Occupational Classification (NOC)',
                                                values='VALUE',
                                                aggfunc='mean')

# creating abbreviations for the x-value labels
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
heatmap_data.columns = [abbreviations.get(noc, noc) for noc in heatmap_data.columns]

# plotting the heatmap
plt.figure(figsize=(10, 8)) 
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f") 
plt.title('Average Wages by Occupation and Age Group')
plt.ylabel('Sex')
plt.xlabel('Occupation')
plt.xticks(rotation=45, ha="right") 
plt.tight_layout() 
plt.show()


# now focusing on comparing the bottom 3 and top 3 occupations for the average hourly wage between sexes

# recalculating mean wages by occupation for the entire dataset
mean_wages_by_occupation = av_hourly_wages_overall.groupby('National Occupational Classification (NOC)')['VALUE'].mean().reset_index()

# identifying the top 3 and bottom 3 occupations based on average wage
top_3_occupations = mean_wages_by_occupation.nlargest(3, 'VALUE')['National Occupational Classification (NOC)']
bottom_3_occupations = mean_wages_by_occupation.nsmallest(3, 'VALUE')['National Occupational Classification (NOC)']

# filtering our original dataframe av_hourly_wages_overall to include only top 3 and bottom 3 occupations
filtered_df = av_hourly_wages_overall[
    av_hourly_wages_overall['National Occupational Classification (NOC)'].isin(top_3_occupations) |
    av_hourly_wages_overall['National Occupational Classification (NOC)'].isin(bottom_3_occupations)
].copy()  # .copy() to avoid SettingWithCopyWarning

# adding a new column (named 'Category') to distinguish between top and bottom occupations
filtered_df['Category'] = filtered_df['National Occupational Classification (NOC)'].apply(
    lambda x: 'Top 3' if x in top_3_occupations.tolist() else 'Bottom 3'
)

filtered_df['Abbreviated NOC'] = filtered_df['National Occupational Classification (NOC)'].map(abbreviations)
abbreviated_order = [abbreviations[noc] for noc in top_3_occupations.tolist() + bottom_3_occupations.tolist() if noc in abbreviations]

# plotting the boxplots comparing average hourly wage between sexes
plt.figure(figsize=(8, 8))
sns.boxplot(data=filtered_df, x='Abbreviated NOC', y='VALUE', hue='Sex', dodge=True, palette="Set3", order=abbreviated_order) 
plt.title('Comparison of Average Hourly Wage Between Sexes for Top and Bottom Occupations')
plt.xticks(rotation=45)
plt.xlabel('Occupations')
plt.ylabel('Average Hourly Wage')
plt.tight_layout()
plt.show()




