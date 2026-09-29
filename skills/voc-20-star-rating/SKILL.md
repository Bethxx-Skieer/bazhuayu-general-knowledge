---
name: voc-20-star-rating
description: >-
  严格以 Amazon Product Review 作为评分和商品评论数据源，通过已上架的「八爪鱼|Amazon商品数据抓取」Skill 获取真实星级与Review，分析低星原因和改善优先级。 适用于「星级评分与口碑提升专项」相关任务；顶层 Skill 由客户手动触发。
disable-model-invocation: true
---

# 星级评分与口碑提升专项

**English name:** Rating & Reputation Improvement Analysis

用真实Amazon星级Review解释评分分布和低星驱动因素，形成口碑改善与前后期验证计划。

## First-use introduction

**MUST：当前会话/任务第一次触发本 Skill 时，在任何正式取数或分析之前，先向客户展示一次完整介绍；后续追问不要重复。**

首次介绍需说明：

- 当前使用：**星级评分与口碑提升专项**
- 主要用途：用真实Amazon星级Review解释评分分布和低星驱动因素，形成口碑改善与前后期验证计划。
- 可能使用的数据能力：用户提供数据；Amazon Product Review / 「八爪鱼|Amazon商品数据抓取」Skill
- 正式报告统一要求：**清洗去重后的有效分析数据 `n_valid >= 100`**
- 数据/方法边界：评分分布/均分只能来自真实Amazon带星Review；无前后期数据不预测改善后星级；不加载无关实时/库搜能力。

### 示例提示词

1. “分析这款Amazon商品最近1–3星Review，找拉低评分的问题。”
2. “根据真实带星评论制定星级提升优先级。”
3. “分析我上传的Amazon评分+评论数据并设计跟踪指标。”

## 适用边界

评分分布/均分只能来自真实Amazon带星Review；无前后期数据不预测改善后星级；不加载无关实时/库搜能力。

## 输入

缺关键项先问；能够从用户已有输入中确认的内容不要重复询问。

- Amazon产品/ASIN或链接
- 低星定义（默认1–3星）
- 时间范围
- 改进维度
- 目标/跟踪指标（可选）

## 本 Skill 数据能力声明

| 能力 | 本 Skill 状态 | 规则 |
|---|---|---|
| 用户提供数据 | COND | 用户已经有适用数据时优先使用，不重复采集 |
| Amazon Product Review | YES | 商品评论/评分/星级统一以 Amazon 为载体 |
| 八爪鱼官方实时采集 | NO | 本 Skill 不使用八爪鱼实时采集 |
| 八爪鱼平台存量库搜 | NO | 本 Skill 不使用平台存量库搜 |
| WorkBuddy 全网搜索 | NO | 本 Skill 默认不使用全网搜索 |

详细执行规则见 `references/data-policy.md`。

## User-facing transition notices

### Amazon 商品评论切换（调用前 MUST 提示）

当本次分析需要新增 Amazon Product Review 时，在调用「八爪鱼|Amazon商品数据抓取」Skill **之前**先告诉客户：

> 当前分析需要真实 Amazon Product Review 作为证据。我会先使用已上架的 「八爪鱼|Amazon商品数据抓取」Skill 获取评论数据；数据返回后继续由当前 VOC Skill 做清洗、分析和报告，不需要重新选择 Skill。

已有足够 Amazon Review 时不要重复采集。社媒评论、论坛帖子、新闻和其他电商评论都不得冒充 Amazon Review。

## 100 条正式报告 Gate（一级硬规则）

本 Skill 的有效数据口径：

> 1条带真实评分字段的Amazon Product Review=1条；正式报告 n_valid≥100。

执行中必须持续计算 `n_valid`。

### 当 `n_valid < 100`

必须先向客户明确提示：

> 当前已获得 **{n_valid} 条**有效分析数据，尚未达到完整 VOC 报告所需的 **100 条**标准。如果本次目标是完整报告，我会继续使用当前 Skill 允许的数据能力补充数据，达到 100 条后再生成完整报告。

如果客户目标是完整报告：

1. 提示后继续执行，不要反复询问“是否继续”；
2. 只使用本 Skill 已声明且合规的数据能力补数；
3. 达到 `n_valid >= 100` 后才进入完整报告渲染；
4. 如果所有允许能力耗尽仍不足 100，只能输出明确标注的“探索性 / 样本不足结果”，**禁止生成完整 VOC 报告**；
5. 禁止用错误类型数据凑数量。

## Report Questions

完整报告 Q1–Q4 固定如下，禁止临场重新编题：

1. 当前Amazon评分分布和低星原因是什么？
2. 哪些问题最集中、影响最大？
3. 哪些原因是证据支持的根因假设？
4. 应优先改善什么，并如何做前后期验证？

## 分析步骤

```text
Task Progress:
- [ ] 已完成首次 Skill 介绍（仅首次）
- [ ] 已确认分析对象、范围和主证据单元
- [ ] 已按本 Skill 声明选择正确数据能力
- [ ] 商品评论场景已严格限定 Amazon Product Review
- [ ] 实时采集与平台库搜未混用
- [ ] 已去重清洗并计算 n_valid
- [ ] n_valid <100 时已提示并继续合规补数
- [ ] n_valid >=100 后才进入完整报告
- [ ] 已逐题回答固定 Q1–Q4，并绑定可回溯证据
- [ ] 已完成本 Skill 专属分析模块
- [ ] 已说明仍不能确定的结论和数据边界
- [ ] 已严格按 assets/report-skeleton.html 渲染最终 HTML
```

## 专属深度分析模块

- 评分分布
- 低星问题优先级矩阵
- 行动计划
- 客服话术
- 前后期验证指标

这些模块体现本 Skill 的业务特色，不得被统一“洞察表”替代。

## 报告生成强约束

1. `assets/report-skeleton.html` 是唯一母模板。
2. 禁止自己新建 HTML/CSS、Markdown 转 HTML 或改变模板视觉体系。
3. 生成时复制母模板并填充已有占位符/内容区域；CSS、布局、组件样式保持原样。
4. 固定 Q1–Q4 必须来自本文件 `Report Questions`。
5. 本 Skill 专属内容只能填入模板现有专属分析区域，不改母模板 CSS。
6. 完整报告只能在 `n_valid >=100` 时生成。
7. 输出到任务工作区，例如 `outputs/voc/voc-20-star-rating/<case>/report.html`，禁止写回 Skill 安装目录。

详细规则见 `references/report-policy.md`。

## 数据来源与表达边界

- 商品评论 / Review / 星级 / 差评：默认且唯一商品评论载体为 **Amazon Product Review**。
- 小红书、抖音、微博、B站、论坛等属于公开平台内容，不属于 Amazon Review。
- 小红书/抖音报告禁止写“我们抓取了/搜出来了”；使用“公开平台内容显示”“公开可见讨论中”等表述。
- WebSearch 命中转述平台内容的网页，只能标“公开网页摘要/二手引用”。
- 任何样本内结论不得无依据扩大为全市场事实。
