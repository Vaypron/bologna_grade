# Bologna Grade

Calculate your current grade, as well as  the best and worst grade you can still achieve.

## Why would I need a tool for that?

Most universities have a site where you can check your grades. Unfortunately many times these systems are not up to date or do not even show your final grade.
They are also lackin' a feel for how much you can still improve.

## How to use

### Simple:
Just jump into the ```calculate.py``` to the following lines:
```python
if __name__ == "__main__":
    grades = {
        'Math1': (2.0, 9), # name : (grade, cp)
        'Math2': (3.0, 9),
        'Math3': (1.0, 9),
        'Programming': (2.0, 12),
        # ... 
    }
```
and extend the ```grades```-Dictionary with all your grades.

If your education-system`s do not include the grades 1.0 to 4.0, you will also have to adjust those grades:
```python
calc = Calculator(grades=grades,best_grade=1.0,worst_grade=4.0)
```

### "Advanced":

You can also read in all your grades from a .csv file. 
Format:
```
Name,grade,cp
Name,grade,cp
```
You will also need to pass the csv-Name into the Class-Init:
```
calc = Calculator(csv_format='filename.csv',best_grade=1.0, worst_grade=4.0)
```
