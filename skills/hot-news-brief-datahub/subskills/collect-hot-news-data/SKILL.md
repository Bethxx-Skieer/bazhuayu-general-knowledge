---
name: collect-hot-news-data
description: 使用三个固定 DataHub App 完成热点快报唯一采集，快速模式1批、深度模式固定6批并发优先；返回真实批次进度和候选预览。仅本内部 Skill 拥有 DataHub 工具。
allowed-tools: get_data_app_details run_data_app get_run_status get_run_result
---

# 采集热点新闻

## Mission

从 DataHub 获得当前任务所需的真实公开资讯记录，并向根 Skill 返回可审计批次、实际数量、候选预览和下一阶段。

## When to use

仅在连接就绪、请求计划和敏感范围门禁通过后执行。

## Hard constraints

- 固定 App ID：关键词 `app_ce135270dd97`、一句话 `app_75e95cb205ca`、条件 `app_d0b3c5d95406`。不得静默替换。
- 每个新会话首次使用某 App 前调用 `get_data_app_details`，按实时手册构造输入并确认可运行。
- 快速模式只启动 1 个 Run。深度模式固定启动 6 个逻辑 Run，并发优先；不得增加第 7 批。
- 每批最多 30 条，`freshness=oneWeek`。关键词 App 使用 `keyword/page=1/pageSize=30`；一句话 App 使用 `query/count=30/freshness`；条件 App 使用 `intent/rerank_query/count=30/freshness/include_summary=true`。
- `QUEUED` 或 `RUNNING` 只进行最长 30 秒的有界状态等待；仍未终态时返回根 Skill 发状态消息后继续，不得高频轮询。
- 仅 `SUCCEEDED`、`PARTIALLY_SUCCEEDED` 可取结果。结果分页时必须用 `get_run_result` 取完。
- DataHub 跳转链接必须解析到真实原文 URL；解析失败的记录保留在采集审计中，但不得进入后续候选。
- 首批或前两批形成 5–8 条候选预览；不足 5 条展示全部。预览只使用已解析原文链接。
- 每批终态后返回“已完成/计划批次、本批返回量、累计原始量、下一步”；原始量不得称为有效量。
- 鉴权、连接或服务失败时停止新 Run，不盲目重试；保留已完成批次并返回重新连接 DataHub 或稍后续跑的动作。
- 账单、费用、余额、额度、API Key、Token、鉴权头和原始错误不进入阶段结果或客户输出。

## Core workflow

1. 按计划涉及的 App 读取实时手册。
2. 启动当批 Run；深度模式尽量一次启动多个 Run，再分别等待。
3. 状态未终态时做最长 30 秒的有界检查，并把真实状态返回根 Skill。
4. 终态后取回完整结果，记录 App ID、Run ID、实际输入、终态和记录数；丢弃账单字段。
5. 解析跳转 URL，把记录适配为标题、原文 URL、摘要、发布时间和来源域名。
6. 返回候选预览和批次进度；随后自动继续剩余批次。

## Output format

返回逐批 `app_id/run_id/state/input/raw_count/records`、累计原始量、已完成批次数、计划批次数、5–8 条预览、已保留批次和脱敏异常分类。

## Done criteria

- 快速 Run 数为 1；深度逻辑 Run 数为 6，无第 7 批。
- 每个 Run 都可追溯到 App 手册和锁定计划。
- 长等待采用有界检查，根 Skill 获得真实进度；没有虚构百分比、有效量或剩余时间。
- 故障时停止盲目重试，已有批次可承接，输出不含费用、余额、额度或凭证。
