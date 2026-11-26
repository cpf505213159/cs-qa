# 客服会话全量质检

> 质检结果一旦挂钩绩效，数据就不可信了

## 项目背景
把会话质检从人工抽检 3% 改为全量自动质检（关键词规则 + 情绪打分），提升覆盖率、降低差评率、压缩质检人力。

## 数据集
conversations（脱敏合成）：每条会话含关键词命中、情绪分与人工标注的差评标签，用于评估自动质检的查准/查全。

## 方法与口径
自动质检判定：关键词命中 或 情绪分<0.4 判为风险会话；以人工标注为金标准计算 Precision/Recall。差评率按阶段对比。

## 关键结果（脱敏合成样本上复现）
| 指标 | 数值 |
|---|---|
| 质检覆盖率（人工抽检→全量） | 3% → 100% |
| 质检分类 Precision / Recall | 0.66 / 1.00 |
| 差评率 前→后 | 4.1% → 3.0% |
| 质检人力（全职人数） | 3 人 → 1 人复核 |

## 目录结构
```
cs-qa/
├── data/dataset.csv
├── src/ (generate_data.py, analysis.py)
├── notebooks/01_analysis.ipynb
├── reports/analysis-report.md
├── sql/01_conversations.sql
└── outputs/metrics.json
```
## 复现
```bash
pip install -r requirements.txt
python src/generate_data.py     # 生成 data/dataset.csv（固定随机种子，可复现）
python src/analysis.py          # 计算指标，输出 outputs/metrics.json
# 或打开 notebooks/01_analysis.ipynb 逐步运行
```

## 数据说明
本仓库数据为**脱敏/合成**数据，用于可复现地演示分析方法；量级与真实业务口径可能存在差异，方法本身即为项目交付物的核心。
