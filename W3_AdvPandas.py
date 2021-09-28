import pandas as pd
staff_df = pd.DataFrame({"Name":["Kelly", "Sally", "James"],
                         "Role":["Director of HR", "Course liasion", "Grader"],
                         "Location":["x", "y", "z"]})
student_df = pd.DataFrame({"Name":["James", "Mike", "Sally"],
                         "School":["Business", "Law", "Engineering"],
                           "Location":["a", "b", "c"]})
#conflicts b/w DataFrame
staff_df = staff_df.set_index("Name")
student_df = student_df.set_index("Name")
print(staff_df)
print(student_df)
merge = pd.merge(staff_df, student_df, how="outer", on="Name")  #use index both df have as index
print(merge)
merge = pd.merge(staff_df, student_df, how="inner", left_index=True, right_index=True)
print(merge)
merge = pd.merge(staff_df, student_df, how="left", left_index=True, right_index=True)
print(merge)
merge = pd.merge(staff_df, student_df, how="right", left_index=True, right_index=True)
print(merge)
print(len(merge))


