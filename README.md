# Ada-MSS

> Figure-aligned automatic program repair scaffold.

## 中文（与 proposal/figure 对齐）

当前主流程严格贴近 system figure：
1. Input: Buggy Code + Tests
2. Semantic Pruning Engine（TAC/PSS/CDS）
3. LLM Repair Agent（默认本地 Qwen）
4. Validation Sandbox（真实执行 candidate code + tests）
5. Pass Tests? -> Success；否则 Escalation Policy 提升粒度并重试
6. 达到最大上下文级别后 Repair Fail

默认本地模型：`Qwen/Qwen3-4B-Thinking-2507`（OpenAI-compatible endpoint）。

### 快速运行

```bash
PYTHONPATH=src python scripts/run_demo.py
```

### 本地模型服务示例（vLLM）

```bash
vllm serve Qwen/Qwen3-4B-Thinking-2507 --served-model-name Qwen/Qwen3-4B-Thinking-2507 --port 8000
```

### 为什么你会看到 `llm_unavailable_template_patch`
如果本地 `http://127.0.0.1:8000/v1` 没有启动，LLM 请求会失败（常见是 ConnectionRefusedError）。
本项目会自动降级到 template repair，避免直接崩掉。

### 数据集建议与部署

请看：`docs/DATASET_DEPLOYMENT.md`

---

## English

This repo now follows the figure-aligned repair loop:
- Buggy code + tests input
- Semantic pruning (TAC/PSS/CDS)
- LLM repair agent
- Validation sandbox (executes candidate code + tests)
- Escalation policy until success or max context reached

Default local model: `Qwen/Qwen3-4B-Thinking-2507`.

If local endpoint is not running, pipeline falls back to template repair.

Dataset recommendation and setup guide: `docs/DATASET_DEPLOYMENT.md`.
