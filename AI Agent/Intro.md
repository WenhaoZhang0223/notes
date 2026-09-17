## Intro
Agent = LLM + context + tools
### agent basic
1. ReAct: 思考 → 行动 → 观察”的迭代过程  

2. prompt Engineering: 包括流程化设计、工
具描述、业务规则细化）与提示注入（Prompt Injection)攻防、Agent Skills 的按需加载机制、Agent 状态
栏技术，以及上下文压缩（Context Compression）策略  

3. （用户记忆和知识库）:RAG, 多模态信
息提取, 更高级的知识组织方法 智能体化 RAG（Agentic RAG，即让 Agent 自主决定何时检索、检索
什么）

4. 绍 MCP 工具执行工具的 "安全机制" 以及事件"驱动"的异步 Agent 架构

5. OpenClaw 架构为主线，剖析Coding Agent 的工作流程和实现技巧 

6. （Agent 的评估）

7. 深入 SFT（监督微调，即用标注数据教模型“照样学样 （强化学习，即让模型
通过试错和奖励反馈自主提升）

8. ）研究如何把 Agent 的运行经验转化为下一版本的能力  

9. 。覆盖语音 Agent（从串行流水线到端到
端模型）、Computer Use（让 Agent 像人一样操作图形界面）和机器人操作（VLA（视觉-语言-动作模型）控
制与 Sim2Real 迁移），揭示多模态和实时性带来的共同架构挑战。 

10. 讨论 AI Agent 系统的终极形态 多个 Agent 如何分工合作

## 1.1 现代 Agent = LLM + 上下文 + 工具
：Agent = 大脑 + 眼睛 + 手脚  
大脑 LLM 策略（Policy） Agent 决定“下一步做什么”的决策逻辑——面对当
前看到的信息，从所有可选行动中挑出最合适的一个  

眼睛 上下文 观察空间（Observation Space） Agent 能看到的所有信息——能看到什么、读到什么、记住什么、能访问哪些系统  


手脚 工具 动作空间（Action Space） Agent 能做的所有事情的集合——有哪些“手段”可用，从发消息到执行代码再到操控界面  

### 1.1.1 观察空间与动作空间：模型与世界的接口
观察空间与动作空间共同构成了 LLM 与外部环境之间的接口  

在底层模型固定时，提升 Agent 任务表现最主要的系统工程手段，往往就是重新定义或扩展观察空间与动作空间  

Agent共同特征：
1. 开放式的动作空间
2. 能内部思考
3. 持续交互 你

### 工具：Agent 的手脚
