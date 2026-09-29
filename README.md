# 八爪鱼 WorkBuddy Skill 仓库

本仓库集中维护八爪鱼在 WorkBuddy 中使用的标准 Skill。目前共有 **27 个可独立安装的 Skill**：

- **2 个 DataHub 版 Skill**：热点快报、全球舆情与品牌口碑分析。
- **25 个 VOC 客户洞察 Skill**：覆盖研究、产品、营销、监测和风险分析。

每个 `skills/<skill-name>/` 都是一个完整的安装单位。安装或分发时应复制整个目录，不能只复制其中的 `SKILL.md`。

## 快速选择

| 需求 | 使用入口 | 底层数据能力 | 输出 |
|---|---|---|---|
| 查看近 7 天热点、生成热点清单或内容选题 | [`hot-news-brief-datahub`](skills/hot-news-brief-datahub/) | DataHub 公开资讯 App | 热点快报、决策提示、内容雷达 |
| 分析品牌、产品、竞品或事件舆情 | [`global-public-opinion-analysis-datahub`](skills/global-public-opinion-analysis-datahub/) | DataHub 公开资讯 App | 舆情分析、产品 VOC、竞品口碑、事件声誉报告 |
| 执行具体的 VOC 研究任务 | [VOC-25 客户洞察 Skill 组](collections/voc-25-customer-insight-suite/) | WorkBuddy 八爪鱼采集能力及客户授权的平台内容连接器 | 统一结构的 VOC 分析报告 |

## DataHub 版 Skill

### 1. 热点快报

目录：[`skills/hot-news-brief-datahub/`](skills/hot-news-brief-datahub/)

- 版本：`2.0.0`
- 时间范围：严格限制在执行日前 7 天内。
- 快速模式：执行 1 批检索，用于快速了解近期热点。
- 深度模式：执行 6 批检索，用于决策简报或内容策划。
- 内部保留多 Skill 编排，由主 `SKILL.md` 调度采集、清洗、价值判断、总结和渲染等阶段。

### 2. 全球舆情与品牌口碑分析

目录：[`skills/global-public-opinion-analysis-datahub/`](skills/global-public-opinion-analysis-datahub/)

- 版本：`2.8.0`
- 支持品牌舆情、产品 VOC、竞品口碑和事件声誉四类任务。
- 内部保留多 Skill 编排，包括范围判断、连接器检查、来源治理、采集、清洗、证据分析和报告渲染。
- 输出内容保持来源、时间、地区和证据边界，避免把检索结果直接当作完整市场结论。

### 首次使用 DataHub

首次运行上述两个 Skill 时，Skill 会提醒客户：

1. 打开 WorkBuddy 的「连接器」。
2. 连接 **DataHub**。
3. 使用客户自己的账号完成授权。
4. 授权完成后回到原任务继续执行。

仓库不保存客户凭证，也不会在报告中展示 MCP 消耗或余额提示。

### DataHub 工具与 App

两个 DataHub Skill 统一使用以下工具：

- `get_data_app_details`
- `run_data_app`
- `get_run_status`
- `get_run_result`

固定公开资讯 App：

| 用途 | App ID |
|---|---|
| 关键词检索 | `app_ce135270dd97` |
| 一句话检索 | `app_75e95cb205ca` |
| 条件检索 | `app_d0b3c5d95406` |

## VOC-25 客户洞察 Skill 组

集合索引：[`collections/voc-25-customer-insight-suite/`](collections/voc-25-customer-insight-suite/)

VOC-25 包含 25 个独立的项目级 Skill。它们不是一个必须整体执行的大型 Skill；客户可以根据任务直接选择其中一个。集合目录用于说明分类、数据边界、元数据和统一校验方法。

| 分类 | 数量 | 包含能力 |
|---|---:|---|
| 多源研究与研究方法 | 5 | 跨渠道研究、社媒洞察、问卷、访谈、跨文化研究 |
| 产品创新与用户需求 | 8 | 不满场景、创新机会、趋势、参数、画像、JTBD、购买障碍、旅程地图 |
| 产品策略与营销 | 6 | 爆品要素、卖点、种草、定位、PDP 优化、竞品对比 |
| 监测与风险 | 6 | 事件舆情、新品监测、星级口碑、大促风险、负面专题、汽车战败分析 |

### VOC-25 统一标准

- 正式报告通常要求 `n_valid >= 100`。
- 问卷、访谈等任务按各自 `SKILL.md` 定义有效样本单位，不能用外部资料补足主样本。
- Amazon Product Review、社媒、论坛、问卷、访谈和 CRM 数据保持来源边界。
- 每个 Skill 都包含数据政策、报告政策和统一 HTML 报告模板。
- 25 份报告模板保持同一 SHA256，避免输出格式漂移。
- 该集合保留 V3 源包的数据路由，目前不标记为 DataHub 版本。
- 需要平台内容连接器时，使用客户自己的账号和授权。

完整的 25 项名称、用途和理论边界请查看 [VOC-25 集合说明](collections/voc-25-customer-insight-suite/README.md)。

## 仓库结构

```text
bazhuayu-general-knowledge/
├─ README.md
├─ skills/
│  ├─ hot-news-brief-datahub/
│  ├─ global-public-opinion-analysis-datahub/
│  ├─ voc-01-cross-channel/
│  ├─ ...
│  └─ voc-25-auto-defeat/
└─ collections/
   └─ voc-25-customer-insight-suite/
      ├─ README.md
      ├─ metadata/
      └─ validate_collection.py
```

单个 Skill 目录可能包含：

```text
<skill-name>/
├─ SKILL.md              # 唯一运行入口
├─ references/           # 数据、来源和报告标准
├─ assets/               # 报告模板等静态资源
├─ subskills/            # 内部阶段 Skill，仅编排型 Skill 使用
├─ scripts/              # 必要的本地处理脚本
├─ mcp.json              # 连接器声明，仅需要时提供
└─ connector-meta.json   # 连接器元数据，仅需要时提供
```

## 安装与维护约定

1. 以 `skills/<skill-name>/` 完整目录为单位安装或更新。
2. 根目录的 `SKILL.md` 是该 Skill 的入口。
3. `subskills/` 由主 Skill 内部调度，不作为同一任务的独立客户入口。
4. 修改数据来源、样本门槛或报告结构时，同时检查对应的 `references/` 和模板。
5. 不在仓库中提交 API Key、访问令牌、客户账号、授权信息或运行数据。
6. 不提交 Word 文档、发布 ZIP、缓存、临时输出或客户报告。

## 校验 VOC-25

在仓库根目录执行：

```powershell
python collections/voc-25-customer-insight-suite/validate_collection.py
```

校验脚本会检查：

- VOC Skill 数量是否为 25。
- 编号是否完整覆盖 `01–25`。
- 目录名是否与 `SKILL.md` 的 frontmatter 名称一致。
- 必需的政策文件和报告模板是否存在。
- 25 份报告模板是否一致。
- 正式报告 Gate、首次使用说明和报告问题是否完整。
- 是否存在外链或 API Key 泄漏。

当前基准校验结果：`PASS`。
