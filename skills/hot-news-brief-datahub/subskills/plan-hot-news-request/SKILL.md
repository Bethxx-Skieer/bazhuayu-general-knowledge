---
name: plan-hot-news-request
description: 解析热点快报主题、输出模式、深度强触发词和固定查询角色，并为三个 DataHub App 生成1批或6批计划。只负责规划，不运行 App。
---

# 规划热点快报请求

## Mission

形成当前任务唯一的主题、近 7 天窗口、检索模式、输出模式、查询角色和 App 分配。

## When to use

仅在 DataHub 连接检查通过后执行。

## Hard constraints

- 默认 `search_mode=fast`；深度强触发词固定为 `deep`，不得降级。
- 深度强触发词后没有主题时只返回主题追问，Run 数为 0。
- 快速模式恰好 1 批，使用一句话 App `app_75e95cb205ca`。
- 深度模式恰好 6 批，App 顺序固定为：一句话、关键词、条件、条件、关键词、一句话。
- 敏感主题立即停止，Run 数为 0。
- 固定中文可信信源优先、近 7 天、最多 10 条。

## Core workflow

规范主题并删除模式指令词；确定 `news_list`、`decision_brief`、`content_radar` 或 `both`；生成批次角色、查询文本、App ID 和实时手册所需输入草案。

## Output format

向根 Skill 返回 `topic`、`search_mode`、`output_mode`、`freshness=oneWeek`、`logical_batch_count` 和逐批 `batch_role/app_id/query`。

## Done criteria

- 快速计划 1 批；深度计划 6 批且角色唯一、三个 App 均被使用。
- 没有工具、终端或文件操作。
