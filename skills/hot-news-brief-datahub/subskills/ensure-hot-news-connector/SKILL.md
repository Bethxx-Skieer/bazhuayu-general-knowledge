---
name: ensure-hot-news-connector
description: 在热点快报开始前检查 WorkBuddy 的 DataHub 连接器和四个必需工具；缺失时引导客户用自己的账号完成授权。只负责连接状态，不搜索。
---

# DataHub 连接就绪检查

## Mission

确认 `get_data_app_details`、`run_data_app`、`get_run_status` 和 `get_run_result` 全部可用，且客户账号授权有效。

## When to use

每次新会话首次调用热点快报时执行；连接状态变化或客户回复“已连接”时复检。

## Hard constraints

- 先于请求规划和任何 DataHub Run 执行；配置文件存在不等于连接已经授权。
- 四个工具缺一不可。未就绪时不得生成查询或启动 App。
- WorkBuddy「连接器」负责本人账号授权。不得索取 API Key、Token 或手动 Header。
- 客户回复“已连接”后重新检查工具与授权状态，再继续原主题。
- 只向根 Skill 返回阶段结果；根 Skill 统一发送客户提示。

## Core workflow

1. 检查宿主暴露的四个工具与连接认证状态。
2. 就绪时返回 `ready`、可用工具和检查时间。
3. 未就绪时返回缺失项和客户动作：“打开 WorkBuddy「连接器」，找到 DataHub，点击「连接」并使用您自己的账号完成授权；完成后回复‘已连接’。”

## Output format

返回 `status`、`can_proceed`、`required_tools`、`available_tools`、`missing_tools`、`next_action` 和已脱敏的 `customer_message`。

## Done criteria

- 四个工具均可用且 `can_proceed=true`；或已明确连接动作并停在门禁，DataHub Run 数为 0。
