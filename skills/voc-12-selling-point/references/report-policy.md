# 卖点感知与传播效果分析 — Report Policy

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

- Q1: 哪些卖点被用户主动提及和正确理解？
- Q2: 哪些卖点存在理解偏差或感知缺口？
- Q3: 哪些卖点与真实需求最匹配？
- Q4: 应怎样调整表达并继续验证？

## 4. 专属深度分析

- 卖点感知排序
- 理解偏差
- 卖点-需求匹配矩阵
- 话术优化
- 高潜卖点

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

建议 `outputs/voc/voc-12-selling-point/<case>/report.html`。不得修改 Skill 安装目录。
