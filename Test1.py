import pandas as pd
s1 = pd.Series({1: 'Alice', 2: 'Jack', 3: 'Molly'})
s2 = pd.Series({'Alice': 1, 'Jack': 2, 'Molly': 3})
print(s1.append(s2))