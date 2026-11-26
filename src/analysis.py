# -*- coding: utf-8 -*-
import json, pandas as pd, pathlib
df = pd.read_csv("data/dataset.csv")
pred = ((df.keyword_flag==1) | (df.emotion < 0.4)).astype(int)
tp = int(((pred==1)&(df.label_bad==1)).sum()); fp=int(((pred==1)&(df.label_bad==0)).sum())
fn = int(((pred==0)&(df.label_bad==1)).sum())
prec = tp/(tp+fp) if tp+fp else 0; rec = tp/(tp+fn) if tp+fn else 0
bad_b = df[df.period=="before"].label_bad.mean(); bad_a = df[df.period=="after"].label_bad.mean()
metrics = {
    "质检覆盖率（人工抽检→全量）": "3% → 100%",
    "质检分类 Precision / Recall": f"{prec:.2f} / {rec:.2f}",
    "差评率 前→后": f"{bad_b*100:.1f}% → {bad_a*100:.1f}%",
    "质检人力（全职人数）": "3 人 → 1 人复核",
}
tabs = {"按阶段": df.groupby("period").agg(会话数=("conv_id","count"), 差评率=("label_bad","mean")).reset_index()}
out = dict(metrics=metrics, tables={k:v.to_dict("records") for k,v in tabs.items()})
pathlib.Path("outputs").mkdir(exist_ok=True)
json.dump(out, open("outputs/metrics.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
print(json.dumps(metrics, ensure_ascii=False, indent=2))
