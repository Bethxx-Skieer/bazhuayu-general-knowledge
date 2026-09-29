---
name: voc-24-journey-map
description: >-
  结合 Amazon Product Review、八爪鱼公开平台内容、购前问答和用户业务数据，将用户声音映射到认知、考虑、购买、使用、售后与推荐阶段。 适用于「用户体验旅程地图」相关任务；顶层 Skill 由客户手动触发。
disable-model-invocation: true
---

# 用户体验旅程地图

**English name:** Customer Experience Journey Mapping

构建基于VOC证据的体验旅程，识别各阶段关键触点、痛点、高光和体验断点。

## First-use introduction

**MUST：当前会话/任务第一次触发本 Skill 时，在任何正式取数或分析之前，先向客户展示一次完整介绍；后续追问不要重复。**

首次介绍需说明：

- 当前使用：**用户体验旅程地图**
- 主要用途：构建基于VOC证据的体验旅程，识别各阶段关键触点、痛点、高光和体验断点。
- 可能使用的数据能力：用户提供数据；Amazon Product Review / 「八爪鱼|Amazon商品数据抓取」Skill；八爪鱼官方实时采集器；用户级八爪鱼平台内容搜索 MCP；WorkBuddy 全网搜索
- 正式报告统一要求：**清洗去重后的有效分析数据 `n_valid >= 100`**
- 数据/方法边界：这是VOC证据旅程地图，不等于真实行为漏斗；无漏斗数据时不估算真实阶段转化/流失率。

### 示例提示词

1. “基于用户声音做从认知到售后的体验旅程地图。”
2. “分析各阶段的痛点、高光和体验断点。”
3. “结合Amazon Review、购前问答和我上传的售后数据做旅程分析。”

## 适用边界

这是VOC证据旅程地图，不等于真实行为漏斗；无漏斗数据时不估算真实阶段转化/流失率。

## 输入

缺关键项先问；能够从用户已有输入中确认的内容不要重复询问。

- 产品/服务
- 旅程阶段定义
- 体验维度
- 目标人群
- 关键触点（可选）

## 本 Skill 数据能力声明

| 能力 | 本 Skill 状态 | 规则 |
|---|---|---|
| 用户提供数据 | COND | 用户已经有适用数据时优先使用，不重复采集 |
| Amazon Product Review | COND | 商品评论/评分/星级统一以 Amazon 为载体 |
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

> 能够明确映射到旅程阶段的有效VOC n_valid≥100；未能可靠标阶段的数据不进入阶段曲线。

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

1. 各旅程阶段的主要触点和用户声音是什么？
2. 各阶段的痛点和高光时刻在哪里？
3. 哪些阶段之间存在明显体验断点？
4. 哪些体验改进应优先验证？

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

- 旅程阶段表
- 情绪/体验证据
- 痛点与高光
- 体验断点
- 改进机会

这些模块体现本 Skill 的业务特色，不得被统一“洞察表”替代。

## 报告生成强约束

1. `assets/report-skeleton.html` 是唯一母模板。
2. 禁止自己新建 HTML/CSS、Markdown 转 HTML 或改变模板视觉体系。
3. 生成时复制母模板并填充已有占位符/内容区域；CSS、布局、组件样式保持原样。
4. 固定 Q1–Q4 必须来自本文件 `Report Questions`。
5. 本 Skill 专属内容只能填入模板现有专属分析区域，不改母模板 CSS。
6. 完整报告只能在 `n_valid >=100` 时生成。
7. 输出到任务工作区，例如 `outputs/voc/voc-24-journey-map/<case>/report.html`，禁止写回 Skill 安装目录。

详细规则见 `references/report-policy.md`。

## 数据来源与表达边界

- 商品评论 / Review / 星级 / 差评：默认且唯一商品评论载体为 **Amazon Product Review**。
- 小红书、抖音、微博、B站、论坛等属于公开平台内容，不属于 Amazon Review。
- 小红书/抖音报告禁止写“我们抓取了/搜出来了”；使用“公开平台内容显示”“公开可见讨论中”等表述。
- WebSearch 命中转述平台内容的网页，只能标“公开网页摘要/二手引用”。
- 任何样本内结论不得无依据扩大为全市场事实。
