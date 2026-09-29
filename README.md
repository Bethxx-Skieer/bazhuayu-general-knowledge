# 八爪鱼通用 Skill 仓库

集中维护可供 WorkBuddy 使用的八爪鱼 Skill。每个 Skill 使用独立目录，目录根部保留可安装的 `SKILL.md`、连接器配置和运行所需资源。

## 当前 Skill

| 目录 | Skill | 版本 | 用途 |
|---|---|---:|---|
| [`skills/hot-news-brief-datahub/`](skills/hot-news-brief-datahub/) | 热点快报（八爪鱼） | 2.0.0 | 检索严格近 7 天热点，快速模式 1 批、深度模式 6 批，输出新闻清单、决策提示或内容选题。 |
| [`skills/global-public-opinion-analysis-datahub/`](skills/global-public-opinion-analysis-datahub/) | 全球舆情与品牌口碑分析（八爪鱼） | 2.8.0 | 采集全球公开资讯，完成品牌舆情、产品 VOC、竞品口碑及事件声誉分析。 |

## 目录约定

```text
skills/
  <skill-name>/
    SKILL.md
    mcp.json
    connector-meta.json
    subskills/
    references/
    scripts/
```

- 一个目录对应一个可独立安装和更新的 Skill。
- 根 `SKILL.md` 是主编排器；`subskills/` 保存内部阶段 Skill。
- `mcp.json` 只声明服务地址和工具，不保存访问凭证。
- 客户首次使用时在 WorkBuddy「连接器」中连接 DataHub，并使用自己的账号授权。
- 仓库不保存 Word 文档、发布 ZIP、运行输出、缓存或 API Key。

## DataHub

两个 Skill 都使用以下 DataHub 工具：

- `get_data_app_details`
- `run_data_app`
- `get_run_status`
- `get_run_result`

固定公开资讯 App：

- 关键词检索：`app_ce135270dd97`
- 一句话检索：`app_75e95cb205ca`
- 条件检索：`app_d0b3c5d95406`
