# 用户访谈 VOC 结构化分析 — Data Policy

## 1. 主证据单元与正式报告门槛

1个独立可编码语义证据单元=1条；正式报告 n_evidence_units≥100，同时必须单列 N_participants。

统一正式报告 Gate：`n_valid >= 100`。

不足 100 必须先向客户提示；若目标是完整报告，必须由用户继续补充同一主数据，达到 100 后才渲染完整报告。禁止使用外部公开数据凑足样本。

## 2. 能力声明

| 能力 | 本 Skill 状态 | 规则 |
|---|---|---|
| 用户提供数据 | YES | 用户已经有适用数据时优先使用，不重复采集 |
| Amazon Product Review | NO | 本 Skill 不使用 Amazon 商品 Review |
| 八爪鱼官方实时采集 | NO | 本 Skill 不使用八爪鱼实时采集 |
| 八爪鱼平台存量库搜 | NO | 本 Skill 不使用平台存量库搜 |
| WorkBuddy 全网搜索 | NO | 本 Skill 默认不使用全网搜索 |

## 3. 全局数据边界

## 4. 来源记录

每条证据内部至少保留：`source_type`、`source_platform`、`acquisition_method`、`source_id`。

建议 `acquisition_method`：`user_provided` / `amazon_skill` / `realtime_template` / `platform_search` / `web_search`。

报告来源标签必须由实际 acquisition_method 决定，不得按正文中“提到了哪个平台”反推来源。

## 5. 本 Skill 方法边界

不默认承诺音频自动转写；100个语义单元不得写成100位用户；不足100证据单元时要求补主数据而非外部凑数。

## 6. 禁止凑样本

不同证据类型不能为了达到100条被错误混为同一分析单元。背景网页、页面说明、官方文案只有在它本身是分析对象时才能计入对应样本。
