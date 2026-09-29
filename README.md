# 八爪鱼通用 Skill 仓库

集中维护可供 WorkBuddy 使用的八爪鱼 Skill。当前共 27 个可独立安装的 Skill：2 个 DataHub 版 Skill，以及 VOC-25 客户洞察 Skill 组。每个 Skill 使用独立目录，目录根部保留可安装的 `SKILL.md` 和运行所需资源。

## 当前内容

| 目录 | Skill | 版本 | 用途 |
|---|---|---:|---|
| [`skills/hot-news-brief-datahub/`](skills/hot-news-brief-datahub/) | 热点快报（八爪鱼） | 2.0.0 | 检索严格近 7 天热点，快速模式 1 批、深度模式 6 批，输出新闻清单、决策提示或内容选题。 |
| [`skills/global-public-opinion-analysis-datahub/`](skills/global-public-opinion-analysis-datahub/) | 全球舆情与品牌口碑分析（八爪鱼） | 2.8.0 | 采集全球公开资讯，完成品牌舆情、产品 VOC、竞品口碑及事件声誉分析。 |

### VOC-25 客户洞察 Skill 组

[`collections/voc-25-customer-insight-suite/`](collections/voc-25-customer-insight-suite/) 收录 25 个可独立安装的 VOC Skill，覆盖多源研究、用户洞察、产品创新、营销策略、监测与风险。运行目录位于 `skills/voc-01-*` 至 `skills/voc-25-*`。

- Skill 数：25
- 每个 Skill 均包含独立 `SKILL.md`、数据政策、报告政策和统一 HTML 报告模板
- 正式报告门槛：`n_valid >= 100`
- 集合目录提供分类索引、双语元数据、来源识别表、数据路由矩阵和一键校验脚本

## 目录约定

```text
skills/
  <skill-name>/
    SKILL.md
    references/
    assets/
    mcp.json              # 需要连接器时才提供
    connector-meta.json   # 需要连接器时才提供
    subskills/            # 多 Skill 编排时才提供
    scripts/              # 需要执行脚本时才提供
collections/
  <collection-name>/
    README.md
    metadata/
    validate_collection.py
```

- 一个目录对应一个可独立安装和更新的 Skill。
- 根 `SKILL.md` 是 Skill 入口；`subskills/` 仅用于有内部阶段编排的 Skill。
- `mcp.json` 只声明服务地址和工具，不保存访问凭证。
- DataHub 版 Skill 首次使用时会提示客户在 WorkBuddy「连接器」中连接 DataHub，并使用自己的账号授权。
- 仓库不保存 Word 文档、发布 ZIP、运行输出、缓存或 API Key。

## DataHub

当前两个 DataHub 版 Skill 使用以下工具：

- `get_data_app_details`
- `run_data_app`
- `get_run_status`
- `get_run_result`

固定公开资讯 App：

- 关键词检索：`app_ce135270dd97`
- 一句话检索：`app_75e95cb205ca`
- 条件检索：`app_d0b3c5d95406`
