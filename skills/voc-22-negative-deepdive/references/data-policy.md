# 负面口碑专题深度研究 — Data Policy

## 1. 主证据单元与正式报告门槛

指定问题相关的Amazon Review、投诉或公开证据 n_valid≥100；按来源分别标注。

统一正式报告 Gate：`n_valid >= 100`。

不足 100 必须先向客户提示；若目标是完整报告，继续使用本文件允许的能力补数，达到 100 后才渲染完整报告。所有允许来源耗尽仍不足时，只能输出 SAMPLE_LIMITED 探索性结果。

## 2. 能力声明

| 能力 | 本 Skill 状态 | 规则 |
|---|---|---|
| 用户提供数据 | COND | 用户已经有适用数据时优先使用，不重复采集 |
| Amazon Product Review | YES | 商品评论/评分/星级统一以 Amazon 为载体 |
| 八爪鱼官方实时采集 | COND | 仅实时/准实时非 Amazon Review 结构化采集 |
| 八爪鱼平台存量库搜 | COND | 只允许 `search_platform_content` / `list_platforms` |
| WorkBuddy 全网搜索 | COND | 新闻、官网、评测、泛网背景；不能替代指定平台库搜 |

## 3. 全局数据边界

### Amazon Product Review

商品评论、Review、评分、星级、低星/差评的统一商品评论载体是 Amazon Product Review。其他平台内容不可冒充 Amazon Review。Amazon 样本只代表当前 Amazon 数据范围，不代表全市场。

### 平台存量库搜

若本 Skill 的平台库搜状态不是 NO，库搜主工具只能使用 `search_platform_content`；仅平台标识/支持范围未知时使用 `list_platforms`。

禁止使用 `search_templates` / `execute_task` / `export_data` 做库搜。

### 八爪鱼官方实时采集

若实时采集状态不是 NO，仅在需要实时/准实时非 Amazon Review 结构化数据时使用官方采集器。模板链路与库搜严格隔离。

### WorkBuddy 全网搜索

用于新闻、官网、评测、行业资料和泛网背景；不能替代用户明确指定的平台库搜，也不能制造 Amazon Review。

## 4. 来源记录

每条证据内部至少保留：`source_type`、`source_platform`、`acquisition_method`、`source_id`。

建议 `acquisition_method`：`user_provided` / `amazon_skill` / `realtime_template` / `platform_search` / `web_search`。

报告来源标签必须由实际 acquisition_method 决定，不得按正文中“提到了哪个平台”反推来源。

## 5. 本 Skill 方法边界

5Why/鱼骨图形成的是证据支持的原因假设；技术根因必须由质量/工程/售后数据确认。

## 6. 禁止凑样本

不同证据类型不能为了达到100条被错误混为同一分析单元。背景网页、页面说明、官方文案只有在它本身是分析对象时才能计入对应样本。
