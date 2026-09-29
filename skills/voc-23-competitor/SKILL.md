---
name: voc-23-competitor
description: >-
  优先在同一Amazon数据口径下比较本品与2–5个竞品的 Product Review，并结合八爪鱼公开平台内容和全网评测识别用户感知优劣势、机会与威胁。 适用于「竞品 VOC 对比分析」相关任务；顶层 Skill 由客户手动触发。
disable-model-invocation: true
---

# 竞品 VOC 对比分析

**English name:** Competitive VOC Benchmarking

在可比来源、时间和数据口径下比较本品和竞品的用户感知差异，避免跨数据层伪比较。

## First-use introduction

**MUST：当前会话/任务第一次触发本 Skill 时，在任何正式取数或分析之前，先向客户展示一次完整介绍；后续追问不要重复。**

首次介绍需说明：

- 当前使用：**竞品 VOC 对比分析**
- 主要用途：在可比来源、时间和数据口径下比较本品和竞品的用户感知差异，避免跨数据层伪比较。
- 可能使用的数据能力：用户提供数据；Amazon Product Review / 「八爪鱼|Amazon商品数据抓取」Skill；八爪鱼官方实时采集器；用户级八爪鱼平台内容搜索 MCP；WorkBuddy 全网搜索
- 正式报告统一要求：**清洗去重后的有效分析数据 `n_valid >= 100`**
- 数据/方法边界：不能把一方Amazon Review真实统计与另一方网页摘要做精确百分比对比；不同数据层必须明确分开。

### 示例提示词

1. “对比本品和三款竞品的Amazon Review，找用户感知差异。”
2. “分析本品与竞品的主要优劣势和机会点。”
3. “结合Amazon评论和公开评测做同口径竞品VOC。”

## 适用边界

不能把一方Amazon Review真实统计与另一方网页摘要做精确百分比对比；不同数据层必须明确分开。

## 输入

缺关键项先问；能够从用户已有输入中确认的内容不要重复询问。

- 本品
- 竞品列表（2–5个）
- 对比维度
- 时间范围
- 细分市场（可选）

## 本 Skill 数据能力声明

| 能力 | 本 Skill 状态 | 规则 |
|---|---|---|
| 用户提供数据 | COND | 用户已经有适用数据时优先使用，不重复采集 |
| Amazon Product Review | YES | 商品评论/评分/星级统一以 Amazon 为载体 |
| 八爪鱼官方实时采集 | COND | 仅实时/准实时非 Amazon Review 结构化采集 |
| 八爪鱼平台存量库搜 | COND | 只允许 `search_platform_content` / `list_platforms` |
| WorkBuddy 全网搜索 | YES | 新闻、官网、评测、泛网背景；不能替代指定平台库搜 |

详细执行规则见 `references/data-policy.md`。

## User-facing transition notices

### Amazon 商品评论切换（调用前 MUST 提示）

当本次分析需要新增 Amazon Product Review 时，在调用「八爪鱼|Amazon商品数据抓取」Skill **之前**先告诉客户：

> 当前分析需要真实 Amazon Product Review 作为证据。我会先使用已上架的 「八爪鱼|Amazon商品数据抓取」Skill 获取评论数据；数据返回后继续由当前 VOC Skill 做清洗、分析和报告，不需要重新选择 Skill。

已有足够 Amazon Review 时不要重复采集。社媒评论、论坛帖子、新闻和其他电商评论都不得冒充 Amazon Review。

### 平台存量库搜切换（调用前 MUST 提示）

当本次需要指定平台存量公开内容时，在首次调用库搜前提示：

> 接下来会使用已安装的「平台内容搜索」能力补充指定平台公开存量内容。如果 WorkBuddy 首次弹出信任、启用或权限确认，请确认允许；完成后我会继续当前分析。

库搜工具白名单：`search_platform_content`（主工具）与 `list_platforms`（仅平台标识/支持范围未知时）。

**严禁**使用 `search_templates`、`execute_task`、`export_data` 冒充库搜。库搜不可用时不得静默回退 WebSearch 并声称覆盖了用户指定平台。

### 实时结构化采集

只有当本 Skill 确实需要实时/准实时的**非 Amazon Review**结构化数据时，才使用 WorkBuddy 官方八爪鱼采集器能力。按实际模板 Schema 执行 `search_templates → execute_task → export_data`。

`search_templates` 是模板发现，不是平台存量库搜。

## 100 条正式报告 Gate（一级硬规则）

本 Skill 的有效数据口径：

> 本品与竞品口径一致的可比VOC，总 n_valid≥100；Amazon Review对比尽量同站点/时间窗/评分口径。

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

1. 本品和竞品各自被Amazon用户认可和不满的是什么？
2. 在可比口径下，用户感知差异在哪里？
3. 哪些机会点和威胁有稳定证据？
4. 可以支持哪些竞争策略，哪些仍需业务数据验证？

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

- 多维VOC对比矩阵
- 优势/劣势
- 用户感知差异
- 机会与威胁
- 竞争策略

这些模块体现本 Skill 的业务特色，不得被统一“洞察表”替代。

## 报告生成强约束

1. `assets/report-skeleton.html` 是唯一母模板。
2. 禁止自己新建 HTML/CSS、Markdown 转 HTML 或改变模板视觉体系。
3. 生成时复制母模板并填充已有占位符/内容区域；CSS、布局、组件样式保持原样。
4. 固定 Q1–Q4 必须来自本文件 `Report Questions`。
5. 本 Skill 专属内容只能填入模板现有专属分析区域，不改母模板 CSS。
6. 完整报告只能在 `n_valid >=100` 时生成。
7. 输出到任务工作区，例如 `outputs/voc/voc-23-competitor/<case>/report.html`，禁止写回 Skill 安装目录。

详细规则见 `references/report-policy.md`。

## 数据来源与表达边界

- 每个产品/竞品必须单独报告样本量；某一方样本明显不足时，相应对比降级为定性，不因总样本超过100就做伪精确比较。

- 商品评论 / Review / 星级 / 差评：默认且唯一商品评论载体为 **Amazon Product Review**。
- 小红书、抖音、微博、B站、论坛等属于公开平台内容，不属于 Amazon Review。
- 小红书/抖音报告禁止写“我们抓取了/搜出来了”；使用“公开平台内容显示”“公开可见讨论中”等表述。
- WebSearch 命中转述平台内容的网页，只能标“公开网页摘要/二手引用”。
- 任何样本内结论不得无依据扩大为全市场事实。
