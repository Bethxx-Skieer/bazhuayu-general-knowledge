---
name: voc-03-dissatisfaction
description: >-
  以 Amazon Product Review 作为商品评论载体，并可结合八爪鱼公开平台内容，识别负面体验、不满场景、痛点强度和有证据支持的原因假设。 适用于「用户不满场景深度洞察」相关任务；顶层 Skill 由客户手动触发。
disable-model-invocation: true
---

# 用户不满场景深度洞察

**English name:** Dissatisfaction Scenario Deep Dive

聚焦负面反馈，按使用场景拆解不满和痛点，并形成产品/服务改善优先级。

## First-use introduction

**MUST：当前会话/任务第一次触发本 Skill 时，在任何正式取数或分析之前，先向客户展示一次完整介绍；后续追问不要重复。**

首次介绍需说明：

- 当前使用：**用户不满场景深度洞察**
- 主要用途：聚焦负面反馈，按使用场景拆解不满和痛点，并形成产品/服务改善优先级。
- 可能使用的数据能力：用户提供数据；Amazon Product Review / 「八爪鱼|Amazon商品数据抓取」Skill；八爪鱼官方实时采集器；用户级八爪鱼平台内容搜索 MCP；WorkBuddy 全网搜索
- 正式报告统一要求：**清洗去重后的有效分析数据 `n_valid >= 100`**
- 数据/方法边界：5Why只能输出证据支持的根因假设；技术根因需质量、售后或工程数据验证；Amazon洞察不扩展成全市场事实。

### 示例提示词

1. “分析这款 Amazon 产品最近低星 Review 里最集中的不满场景。”
2. “找出用户在安装、使用和售后阶段最严重的痛点。”
3. “基于我上传的投诉记录，按场景拆解不满并给改善优先级。”

## 适用边界

5Why只能输出证据支持的根因假设；技术根因需质量、售后或工程数据验证；Amazon洞察不扩展成全市场事实。

## 输入

缺关键项先问；能够从用户已有输入中确认的内容不要重复询问。

- 产品/品类
- 负面关键词或问题方向
- 场景维度（使用前/中/后）
- 时间范围
- 已有投诉/评论数据（可选）

## 本 Skill 数据能力声明

| 能力 | 本 Skill 状态 | 规则 |
|---|---|---|
| 用户提供数据 | COND | 用户已经有适用数据时优先使用，不重复采集 |
| Amazon Product Review | YES | 商品评论/评分/星级统一以 Amazon 为载体 |
| 八爪鱼官方实时采集 | COND | 仅实时/准实时非 Amazon Review 结构化采集 |
| 八爪鱼平台存量库搜 | COND | 只允许 `search_platform_content` / `list_platforms` |
| WorkBuddy 全网搜索 | COND | 新闻、官网、评测、泛网背景；不能替代指定平台库搜 |

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

> 负面 Amazon Review、投诉或公开抱怨等有效负向证据，去重后 n_valid≥100；不同来源不得混成“Amazon差评”。

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

1. 最主要的不满发生在哪些使用场景？
2. 各痛点在当前样本中的频率和严重度如何？
3. 哪些原因有证据支持，哪些仍只是根因假设？
4. 应优先验证和改善什么？

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

- 场景化痛点矩阵
- TOP痛点深度拆解
- 典型原声
- 改进优先级

这些模块体现本 Skill 的业务特色，不得被统一“洞察表”替代。

## 报告生成强约束

1. `assets/report-skeleton.html` 是唯一母模板。
2. 禁止自己新建 HTML/CSS、Markdown 转 HTML 或改变模板视觉体系。
3. 生成时复制母模板并填充已有占位符/内容区域；CSS、布局、组件样式保持原样。
4. 固定 Q1–Q4 必须来自本文件 `Report Questions`。
5. 本 Skill 专属内容只能填入模板现有专属分析区域，不改母模板 CSS。
6. 完整报告只能在 `n_valid >=100` 时生成。
7. 输出到任务工作区，例如 `outputs/voc/voc-03-dissatisfaction/<case>/report.html`，禁止写回 Skill 安装目录。

详细规则见 `references/report-policy.md`。

## 数据来源与表达边界

- 商品评论 / Review / 星级 / 差评：默认且唯一商品评论载体为 **Amazon Product Review**。
- 小红书、抖音、微博、B站、论坛等属于公开平台内容，不属于 Amazon Review。
- 小红书/抖音报告禁止写“我们抓取了/搜出来了”；使用“公开平台内容显示”“公开可见讨论中”等表述。
- WebSearch 命中转述平台内容的网页，只能标“公开网页摘要/二手引用”。
- 任何样本内结论不得无依据扩大为全市场事实。
