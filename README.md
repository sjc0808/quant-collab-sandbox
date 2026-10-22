# quant-collab-sandbox

用于验证 GPT → Trae → Codex → 人工合并协作链路的**公开虚构测试仓库**。

> 本仓库只包含虚构测试代码，不包含生产策略、真实行情、真实持仓、账户信息或密钥。

## 目标

- 验证 Issue → 分支 → PR → CI → Codex 审核 → 人工合并。
- 验证分支保护、CODEOWNERS 和状态检查。
- 不承担任何实际交易或生产职责。

## 运行

```powershell
python -m pytest -q
ruff check .
```