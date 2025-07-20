# 🎓 Student Data Analyzer using NumPy

This project uses **NumPy in Google Colab** to analyze real student performance data from a **Kaggle dataset**.  
It finds **unique values** (like gender, groups, scores) and provides simple student-level insights using NumPy only — no Pandas or Matplotlib.

---

##  What It Does

-  Loads CSV data from Kaggle
-  Extracts unique genders
-  Extracts unique student groups
-  Finds unique math scores
-  Counts total unique students

---

## Sample Output::::
Sample Data:
[['female' 'group B' "bachelor's degree" 'standard' 'none' '72' '72' '74']
['female' 'group C' 'some college' 'standard' 'completed' '69' '90' '88']
['female' 'group B' "master's degree" 'standard' 'none' '90' '95' '93']]

Unique Genders: ['female' 'male']
Unique Groups: ['group A' 'group B' 'group C' 'group D' 'group E']
Unique Math Scores: [ 0. 18. 19. 22. 23. 24. 26. 27. 28. 29.]
Total Unique Students: 1000

