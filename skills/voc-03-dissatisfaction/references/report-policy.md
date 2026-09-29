# 用户不满场景深度洞察 — Report Policy

## 1. Canonical HTML

`../assets/report-skeleton.html` 是唯一报告母模板。该资产必须与原始 VOC-25 包中的 canonical `report-skeleton.html` 字节级一致。

Canonical SHA256：`5fd8b79acad641871e1ebca4c854790d047b3d4812b3123b18c7eb45f3513580`

生成 `report.html` 时：

- 复制 canonical 模板；
- 只填充模板占位符和既有内容区域；
- 不重写 CSS；
- 不修改布局、颜色、字体、组件体系；
- 不用 Markdown 转 HTML 替代模板。

## 2. 完整报告 Gate

完整报告必须满足 `n_valid >= 100`。报告中显式展示：

- 有效数据 `n_valid`；
- 正式报告门槛 100；
- 状态 `PASS`。

不足100：先提示并继续补数；能力耗尽仍不足只能输出 `SAMPLE_LIMITED` 探索性结果，禁止套完整报告标题。

## 3. 固定 Q1–Q4

- Q1: 最主要的不满发生在哪些使用场景？
- Q2: 各痛点在当前样本中的频率和严重度如何？
- Q3: 哪些原因有证据支持，哪些仍只是根因假设？
- Q4: 应优先验证和改善什么？

## 4. 专属深度分析

- 场景化痛点矩阵
- TOP痛点深度拆解
- 典型原声
- 改进优先级

专属模块只能使用母模板已有视觉组件填入 `sec-extra` 等既有区域。

## 5. 证据等级

- 数据明确支持：直接证据充分且口径匹配；
- 当前样本倾向：总体可观察但子群/渠道证据较弱；
- 需要更多数据确认：因果、根因、外推、市场规模等超出当前证据。

达到100条不代表每一个子结论自动升级为“数据明确支持”。子群、市场、渠道、时间段仍需显示自己的 n。

## 6. 来源展示与合规

- Amazon Review：可写“Amazon Product Review 数据显示/当前 Amazon Review 样本中”；
- 小红书/抖音等：写“公开平台内容显示/公开可见讨论中”，不写“我们抓取/搜库得到”；
- Web Search 二手引用：写“公开网页摘要/二手引用”；
- 不在客户报告中展示 API Key、MCP Endpoint 或认证信息。

## 7. 输出路径

建议 `outputs/voc/voc-03-dissatisfaction/<case>/report.html`。不得修改 Skill 安装目录。
