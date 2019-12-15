# School_District_Analysis

# Module 4 and Challenge

In this module, we used Jupyter Notebook and the Pandas library analysis of school district that contained two csv files. In this analysis, we merged datasets for further analysis of the school and student data. With the analysis, we provide district and school summary, top 5 and bottom 5 preforming schools, average math and reading scores received by students in each grade level, school performance based on spending per student, size of the school and type of school. 

In this challenge, the grades of the ninth graders at Thomas High School were compromised. We decided the best approach of the analysis was to remove the ninth- grade math and reading scores from Thomas High school, but keep all other data associated with the nine- grade students and Thomas High School. 

# District Summary (How was the district summary affected?)

In the district summary, see that the average math score decreased by 0.1 while the average reading score stayed the same. Note, since we did not remove any student and school data, the total number of schools and students remained the same. 
-	The percent passing for math and reading also decreased by 1 %.
-	The percent overall passing decreased by 1%

# A high-level snapshot of the district's key metrics, presented in a table format
 
Out of the 15 schools that were part of this analysis and 39, 170 students, below was the breakdown:

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

# School Summary 
How was the district summary affected? 

| School Type           | Total Students | Total School Budget | Per Student Budget | Average Math Score | Average Reading Score | % Passing Math | % Passing Reading | % Overall Passing |           |
|-----------------------|----------------|---------------------|--------------------|--------------------|-----------------------|----------------|-------------------|-------------------|-----------|
| Bailey High School    | District       | 4976                | $3,124,928.00      | $628.00            | 77.048432             | 81.033963      | 66.680064         | 81.933280         | 74.306672 |
| Cabrera High School   | Charter        | 1858                | $1,081,356.00      | $582.00            | 83.061895             | 83.975780      | 94.133477         | 97.039828         | 95.586652 |
| Figueroa High School  | District       | 2949                | $1,884,411.00      | $639.00            | 76.711767             | 81.158020      | 65.988471         | 80.739234         | 73.363852 |
| Ford High School      | District       | 2739                | $1,763,916.00      | $644.00            | 77.102592             | 80.746258      | 68.309602         | 79.299014         | 73.804308 |
| Griffin High School   | Charter        | 1468                | $917,500.00        | $625.00            | 83.351499             | 83.816757      | 93.392371         | 97.138965         | 95.265668 |
| Hernandez High School | District       | 4635                | $3,022,020.00      | $652.00            | 77.289752             | 80.934412      | 66.752967         | 80.862999         | 73.807983 |
| Holden High School    | Charter        | 427                 | $248,087.00        | $581.00            | 83.803279             | 83.814988      | 92.505855         | 96.252927         | 94.379391 |
| Huang High School     | District       | 2917                | $1,910,635.00      | $655.00            | 76.629414             | 81.182722      | 65.683922         | 81.316421         | 73.500171 |
| Johnson High School   | District       | 4761                | $3,094,650.00      | $650.00            | 77.072464             | 80.966394      | 66.057551         | 81.222432         | 73.639992 |
| Pena High School      | Charter        | 962                 | $585,858.00        | $609.00            | 83.839917             | 84.044699      | 94.594595         | 95.945946         | 95.270270 |
| Rodriguez High School | District       | 3999                | $2,547,363.00      | $637.00            | 76.842711             | 80.744686      | 66.366592         | 80.220055         | 73.293323 |
| Shelton High School   | Charter        | 1761                | $1,056,600.00      | $600.00            | 83.359455             | 83.725724      | 93.867121         | 95.854628         | 94.860875 |
| Thomas High School    | Charter        | 1635                | $1,043,130.00      | $638.00            | 83.418349             | 83.848930      | 93.272171         | 97.308869         | 95.290520 |
| Wilson High School    | Charter        | 2283                | $1,319,574.00      | $578.00            | 83.274201             | 83.989488      | 93.867718         | 96.539641         | 95.203679 |
| Wright High School    | Charter        | 1800                | $1,049,400.00      | $583.00            | 83.682222             | 83.955000      | 93.333333         | 96.611111         | 94.972222 |
