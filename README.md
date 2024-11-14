# dataScience

![alt text](image.png)

Code Explanation

This code reads data from two Excel files containing survey results from the spring and autumn of 2024. Each survey file includes responses to a question regarding Python programming experience levels. The goal is to generate side-by-side bar plots of the frequency of each experience level, ensuring that each experience category is represented by the same color in both plots for easier comparison.

Code Breakdown

    1.	Libraries Imported:
    •	pandas is used for data manipulation and reading Excel files.
    •	matplotlib.pyplot and seaborn are used for visualization.
    2.	Data Loading:
    •	The files list contains the filenames for the two survey datasets.
    •	The data list stores the frequency counts for each unique response (experience level) in both datasets by reading each Excel file and grouping by the experience level column (assumed to be at index 5).
    3.	Defining Consistent Colors for Categories:
    •	To ensure consistent coloring for each category across both plots, the unique experience levels from both datasets are combined and sorted.
    •	A color palette is defined using sns.color_palette('Dark2', len(unique_categories)).
    •	A dictionary color_dict maps each unique category to a specific color from the palette.
    4.	Plotting:
    •	plt.subplots creates a 1x2 grid of subplots to display the two bar plots side-by-side.
    •	A loop iterates through each dataset and file, plotting the bar chart for each dataset using sns.barplot.
    •	The palette parameter is set by mapping the color dictionary to the categories in each dataset, ensuring consistent colors across plots.
    •	The title, labels, and visual styling (like hiding the top and right spines) are applied to each subplot.
    5.	Final Display:
    •	plt.tight_layout() ensures that the subplots do not overlap.
    •	plt.show() displays the figure.

Output Explanation

The output shows two bar plots side-by-side, representing the distribution of responses for Python programming experience levels in the spring and autumn surveys.
• Consistent Colors: Each experience level (e.g., “Medium”, “Starter”, “Strong”) is displayed in the same color in both plots. This consistency makes it easy to compare the frequencies of each category across the two survey periods.
• Survey Insights:
• In both surveys, categories like “Medium” and “Strong” have high frequencies, indicating these are common levels of experience among respondents.
• “Very Strong” is the least frequent category in both datasets, suggesting fewer respondents have an advanced level of Python programming experience.

This approach enhances the readability and comparability of the bar plots, making it easier to analyze changes in experience levels between the spring and autumn surveys.
