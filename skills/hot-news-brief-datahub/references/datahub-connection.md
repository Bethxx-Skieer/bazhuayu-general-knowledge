# DataHub 连接与检索

## 客户连接

本 Skill 使用 WorkBuddy「连接器」中的 DataHub。首次使用时提示客户点击「连接」并用自己的账号完成授权；已连接则直接继续。Skill 包只定义服务地址和工具，不携带凭证，也不要求客户手动填写 Header。

运行前确认四个工具可用：`get_data_app_details`、`run_data_app`、`get_run_status`、`get_run_result`。

## 固定 App

| 用途 | App ID | 主要输入 |
|---|---|---|
| 精确关键词与分页 | `app_ce135270dd97` | `keyword`、`page`、`pageSize` |
| 自然语言探索 | `app_75e95cb205ca` | `query`、`count`、`freshness` |
| 结构化条件检索 | `app_d0b3c5d95406` | `intent`、`rerank_query`、`count`、`freshness`、`include_summary` |

每个新会话首次使用某 App 前读取实时手册。只接受 `SUCCEEDED` 或 `PARTIALLY_SUCCEEDED` 的记录。`QUEUED`/`RUNNING` 每次最多等待 30 秒，把真实状态返回根 Skill，再按 45/60 秒规则向客户提示。

## 原文与保密

DataHub 返回的 `url.sz.dataduoduo.com` 跳转链接必须解析到首个真实原文 URL；解析失败的记录不得进入最终快报。费用、账单、余额、额度和凭证字段不进入客户消息、检索审计或安装包。
