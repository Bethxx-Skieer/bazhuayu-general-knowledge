# VOC-25 客户洞察 Skill 组

这是一组面向 WorkBuddy 的 25 个项目级 VOC Skill。每个 Skill 都放在仓库根目录的 `skills/` 下，可独立安装、更新和触发；本目录只负责集合索引、元数据与一致性校验。

## 运行标准

- 正式报告统一要求 `n_valid >= 100`；问卷和访谈类 Skill 使用各自定义的有效样本单位。
- Amazon Product Review 是商品评论载体；社媒、论坛、问卷、访谈和 CRM 数据保持来源边界。
- 每个 Skill 均包含 `SKILL.md`、`references/data-policy.md`、`references/report-policy.md` 和 `assets/report-skeleton.html`。
- 25 个 Skill 使用同一份 HTML 报告骨架，避免交付格式漂移。
- 顶层 Skill 由客户手动触发，`disable-model-invocation: true` 保留 WorkBuddy 项目级 Skill 的调用约束。

## 连接器说明

这 25 个 Skill 保留 V3 源包的数据路由：使用 WorkBuddy 官方八爪鱼采集能力，并在需要平台内容库时使用客户自己授权的私有平台内容连接器。仓库不包含连接器地址、API Key 或客户凭证，也不把这组 Skill 标记为 DataHub 版本。

## Skill 索引

### 多源研究与研究方法

| 编号 | Skill | 中文名称 | 主要用途 |
|---:|---|---|---|
| 01 | [`voc-01-cross-channel`](../../skills/voc-01-cross-channel/) | 跨渠道 VOC 桌面研究 | 跨渠道互证、冲突与覆盖盲区分析 |
| 02 | [`voc-02-social-insight`](../../skills/voc-02-social-insight/) | 社媒用户深度洞察 | 社媒场景、动机、需求与内容偏好 |
| 04 | [`voc-04-survey`](../../skills/voc-04-survey/) | 问卷数据 VOC 深度分析 | 问卷清洗、统计、交叉分析与开放题分析 |
| 05 | [`voc-05-interview`](../../skills/voc-05-interview/) | 用户访谈 VOC 结构化分析 | 访谈编码、主题聚类、旅程与典型故事 |
| 16 | [`voc-16-cross-culture`](../../skills/voc-16-cross-culture/) | 跨国 / 跨文化 VOC 研究 | 跨市场需求、场景与本地化差异 |

### 产品创新与用户需求

| 编号 | Skill | 中文名称 | 主要用途 |
|---:|---|---|---|
| 03 | [`voc-03-dissatisfaction`](../../skills/voc-03-dissatisfaction/) | 用户不满场景深度洞察 | 负面体验、痛点强度与原因假设 |
| 06 | [`voc-06-innovation`](../../skills/voc-06-innovation/) | 创新机会捕捉 | 未满足需求、愿望表达与替代方案 |
| 08 | [`voc-08-trend`](../../skills/voc-08-trend/) | 品类趋势与前瞻性洞察 | 可比时间窗口内的趋势与前瞻信号 |
| 09 | [`voc-09-golden-params`](../../skills/voc-09-golden-params/) | 产品黄金参数定义 | 参数关注度、偏好区间与候选组合 |
| 10 | [`voc-10-persona`](../../skills/voc-10-persona/) | 用户画像与细分市场 | 基于行为、场景、需求与态度的细分 |
| 11 | [`voc-11-jtbd`](../../skills/voc-11-jtbd/) | JTBD 用户任务分析 | 功能、情感和社会任务分析 |
| 19 | [`voc-19-purchase-barrier`](../../skills/voc-19-purchase-barrier/) | 购买障碍与转化分析 | 购前问答、比较、犹豫与竞品考虑 |
| 24 | [`voc-24-journey-map`](../../skills/voc-24-journey-map/) | 用户体验旅程地图 | 将用户声音映射到完整客户旅程 |

### 产品策略与营销

| 编号 | Skill | 中文名称 | 主要用途 |
|---:|---|---|---|
| 07 | [`voc-07-hit-product`](../../skills/voc-07-hit-product/) | 爆品成功要素拆解 | 用户认可的功能、体验、设计与价格因素 |
| 12 | [`voc-12-selling-point`](../../skills/voc-12-selling-point/) | 卖点感知与传播效果分析 | 主推卖点与用户实际感知的匹配 |
| 13 | [`voc-13-seeding`](../../skills/voc-13-seeding/) | 社媒种草效果分析（PGC + UGC） | PGC/UGC 主题、表达与互动信号比较 |
| 14 | [`voc-14-positioning`](../../skills/voc-14-positioning/) | 产品差异化定位分析 | 本品与竞品的感知差异和定位空白 |
| 18 | [`voc-18-pdp-optimize`](../../skills/voc-18-pdp-optimize/) | 电商详情页卖点优化 | 购买疑虑、信息缺口与 PDP 改进建议 |
| 23 | [`voc-23-competitor`](../../skills/voc-23-competitor/) | 竞品 VOC 对比分析 | 同口径竞品比较、机会与威胁识别 |

### 监测与风险

| 编号 | Skill | 中文名称 | 主要用途 |
|---:|---|---|---|
| 15 | [`voc-15-event-sentiment`](../../skills/voc-15-event-sentiment/) | 营销事件舆情分析 | 事件阶段、立场、触发因素与舆情风险 |
| 17 | [`voc-17-new-product-monitor`](../../skills/voc-17-new-product-monitor/) | 新品上市反馈监测 | 上市窗口反馈快照与风险信号 |
| 20 | [`voc-20-star-rating`](../../skills/voc-20-star-rating/) | 星级评分与口碑提升专项 | Amazon 星级分布、低星原因与改善优先级 |
| 21 | [`voc-21-promo-risk`](../../skills/voc-21-promo-risk/) | 大促前口碑风险扫描 | 大促可能放大的风险与应对预案 |
| 22 | [`voc-22-negative-deepdive`](../../skills/voc-22-negative-deepdive/) | 负面口碑专题深度研究 | 明确负面问题的场景、影响与原因假设 |
| 25 | [`voc-25-auto-defeat`](../../skills/voc-25-auto-defeat/) | 车型战败与流失分析 | 汽车转投、流失与真实战败原因 |

## 元数据

`metadata/` 保留原始目录中的四份机器可读清单：

- `VOC-25_Metadata.csv`：基础名称、描述、证据单元与理论边界。
- `VOC-25_Metadata_Bilingual.csv`：中英文双语元数据。
- `VOC-25_Source_Recognition.csv`：各 Skill 的来源识别规则。
- `VOC-25_Data_Routing_Matrix.csv`：数据能力与 Skill 的路由矩阵。

## 校验

在仓库根目录运行：

```powershell
python collections/voc-25-customer-insight-suite/validate_collection.py
```

校验内容包括 Skill 数量、目录名与 frontmatter 名称一致、必需文件、统一报告模板、运行标准、外链与 API Key 泄漏。
