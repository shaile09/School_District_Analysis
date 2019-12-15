# School_District_Analysis

# Module 4 and Challenge

In this module, we used Jupyter Notebook and the Pandas library analysis of school district that contained two csv files. In this analysis, we merged datasets for further analysis of the school and student data. With the analysis, we provide district and school summary, top 5 and bottom 5 preforming schools, average math and reading scores received by students in each grade level, school performance based on spending per student, size of the school and type of school. 

In this challenge, the grades of the ninth graders at Thomas High School were compromised. We decided the best approach of the analysis was to remove the ninth- grade math and reading scores from Thomas High school, but keep all other data associated with the nine- grade students and Thomas High School. 

# District Summary (How was the district summary affected?)

In the district summary, see that the average math score decreased by 0.1 while the average reading score stayed the same. Note, since we did not remove any student and school data, the total number of schools and students remained the same. 
-	The percent passing for math and reading also decreased by 1 %.
-	The percent overall passing decreased by 1%
 
Out of the 15 schools that were part of this analysis, 39, 170 students and the budget was $24,649,428, below was the breakdown:

Total Schools: 15
Total Students: 39170
Average Math Score: 79.0
Average Reading Score: 81.9
% Passing Math: 75 %
% Passing Reading: 86 %
% Overall Passing: 80%

As part of this challenge, we removed the reading and math scores of ninth graders in Thomas High School. Below was the breakdown:

Total Schools: 15
Total Students: 39170
Average Math Score: 78.9
Average Reading Score: 81.9
% Passing Math: 74 %
% Passing Reading: 85 %
% Overall Passing: 79 %

# School Summary (How was the district summary affected?)


Looking at the overall school summary of the data, Cabrera High School, Thomas High School, Pena High School, Griffin High School, and Wilson High School has the top 5 percent overall passing with Thomas High School having 95.29%. In addition, the passing percentage for reading was 97.30 and math was 93.27.

However, once we remove the scores of the 9th graders from Thomas High School the passing rate drops drastically to 68.28%. In addition, the passing percentage drops to 66.91% for math and 69.66 for reading. As a result, Thomas High School is now (after removing the 9th grade reading and math scores) in the bottom percent overall grade. 

Top 5 Percent (Overall Passing) All Student and School Data Included

| school Type         | Total Students | Total School Budget | Per Student Budget | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing |           |
|---------------------|----------------|---------------------|--------------------|--------------------|-----------------------|----------------|-------------------|-------------------|-----------|
| Cabrera High School | Charter        | 1858                | $1,081,356.00      | $582.00            | 83.061895             | 83.975780      | 94.133477         | 97.039828         | 95.586652 |
| Thomas High School  | Charter        | 1635                | $1,043,130.00      | $638.00            | 83.418349             | 83.848930      | 93.272171         | 97.308869         | 95.290520 |
| Pena High School    | Charter        | 962                 | $585,858.00        | $609.00            | 83.839917             | 84.044699      | 94.594595         | 95.945946         | 95.270270 |
| Griffin High School | Charter        | 1468                | $917,500.00        | $625.00            | 83.351499             | 83.816757      | 93.392371         | 97.138965         | 95.265668 |
| Wilson High School  | Charter        | 2283                | $1,319,574.00      | $578.00            | 83.274201             | 83.989488      | 93.867718         | 96.539641         | 95.203679 |

Bottom 5 Percent (Overall Passing) Data with removed 9th graders scores for math and reading in Thomas High School

|                       | School Type | Total Students | Total School Budget | Per Student Budget | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing |
|-----------------------|-------------|----------------|---------------------|--------------------|--------------------|-----------------------|----------------|-------------------|-------------------|
| Thomas High School    | Charter     | 1635           | $1,043,130.00       | $638.00            | 83.350937          | 83.896082             | 66.911315      | 69.663609         | 68.287462         |
| Rodriguez High School | District    | 3999           | $2,547,363.00       | $637.00            | 76.842711          | 80.744686             | 66.366592      | 80.220055         | 73.293323         |
| Figueroa High School  | District    | 2949           | $1,884,411.00       | $639.00            | 76.711767          | 81.158020             | 65.988471      | 80.739234         | 73.363852         |
| Huang High School     | District    | 2917           | $1,910,635.00       | $655.00            | 76.629414          | 81.182722             | 65.683922      | 81.316421         | 73.500171         |
| Johnson High School   | District    | 4761           | $3,094,650.00       | $650.00            | 77.072464          | 80.966394             | 66.057551      | 81.222432         | 73.639992         |

# How does removing the ninth graders’ math and reading scores affect Thomas High School’s performance, relative to the other schools?
Removing the ninth grade data for the math and reading scores affected the preformace data of the Thomas High School. However the other schools around Thomas High School were affected in terms of preformace when comparing the 15 schools, but the overall passing percentage was not affected. Below are a few highlights:
- In the top school output, Thomas high school scored in the top 5 and was listed as number 2. When we removed the 9th grade data, Pena High School took the second place.
- The average math score of Thomas High School slightly decreased from 83.41% to 83.35%
- The average reading score of Thomad High School slightly increased from 83.89% to 83.84%
- The other 14 schools were not affected

# How does removing the ninth-grade scores affect the Math and Reading Scores by Grade, Scores by School Spending, Scores by School Size, and Scores by School Type? 

When looking at the math and reading scores by grade, we can see clearly that the 9th grade was removed from Thomas high school. 

The table below is for reading - Thomas High School 9th grade data has been removed 
|                       | 9th  | 10th | 11th | 12th |
|-----------------------|------|------|------|------|
| Bailey High School    | 81.3 | 80.9 | 80.9 | 80.9 |
| Cabrera High School   | 83.7 | 84.3 | 83.8 | 84.3 |
| Figueroa High School  | 81.2 | 81.4 | 80.6 | 81.4 |
| Ford High School      | 80.6 | 81.3 | 80.4 | 80.7 |
| Griffin High School   | 83.4 | 83.7 | 84.3 | 84.0 |
| Hernandez High School | 80.9 | 80.7 | 81.4 | 80.9 |
| Holden High School    | 83.7 | 83.3 | 83.8 | 84.7 |
| Huang High School     | 81.3 | 81.5 | 81.4 | 80.3 |
| Johnson High School   | 81.3 | 80.8 | 80.6 | 81.2 |
| Pena High School      | 83.8 | 83.6 | 84.3 | 84.6 |
| Rodriguez High School | 81.0 | 80.6 | 80.9 | 80.4 |
| Shelton High School   | 84.1 | 83.4 | 84.4 | 82.8 |
| Thomas High School    | nan  | 84.3 | 83.6 | 83.8 | 
| Wilson High School    | 83.9 | 84.0 | 83.8 | 84.3 |
| Wright High School    | 83.8 | 83.8 | 84.2 | 84.1 |

Spending range per student remained the same $630-644, since we are using the same number of students, we wouldn't expect this to change 

The average spending per student did not change since we are not using the scores for this calculation. Instead, we created bins and used the capita to calculate the average spending. Below was the reslut:
