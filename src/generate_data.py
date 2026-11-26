# -*- coding: utf-8 -*-
import numpy as np, pandas as pd
rng = np.random.default_rng(23)
n = 3000
rows=[]
for i in range(n):
    period = "before" if i % 2 == 0 else "after"
    p_bad = 0.041 if period=="before" else 0.032
    bad = int(rng.random() < p_bad)
    kw = int(bad and rng.random()<0.82 or (rng.random()<0.02))
    if bad:
        emo = round(float(rng.uniform(0.05,0.40)),2)
    else:
        emo = round(float(rng.uniform(0.45,0.98)),2)
    rows.append(dict(conv_id=f"C{i:05d}", period=period, agent=f"A{i%40:02d}",
                     label_bad=bad, keyword_flag=kw, emotion=emo))
pd.DataFrame(rows).to_csv("data/dataset.csv", index=False)
print("wrote conversations", len(rows))
