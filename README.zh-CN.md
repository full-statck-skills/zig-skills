<div align="center">

# zig-skills

**Zig 语言技能 — 0.16.0、raylib、SDL3、代码审查、Tiger Style**

[![GitHub](https://img.shields.io/badge/github-full--statck--skills%2Fzig-skills-green.svg)](https://github.com/full-statck-skills/zig-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-兼容-purple.svg)](https://agentskills.io)

[English](./README.md) | 简体中文

[简介](#-简介) · [安装](#-安装) · [技能列表](#-技能列表-6) · [仓库布局](#-仓库布局) · [关系说明](#-关系说明) · [官方来源](#-官方来源) · [支持的智能体](#-支持的智能体) · [生态](#-生态)

</div>

---

## 📖 简介

**Zig 技能** 是一组面向 Zig 编程语言及其生态的 AI 编码智能体技能，属于 [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) 生态，由 [PartMe.AI](https://github.com/partme-ai) 维护。

本包包含 **6 个技能**，以一个 Zig 0.16.0 综合主技能为核心，辅以生态和工具链技能。每个技能是独立的 `SKILL.md` 文件，AI 智能体按需加载。

## 📦 安装

```bash
npx skills add full-statck-skills/zig-skills
```

或安装特定技能：`npx skills add full-statck-skills/zig-skills --skill <skill-name>`

## 🎯 技能列表 (6)

| 技能 | 描述 |
|------|------|
| `zig-0.16` | **主技能。** 最新的 Zig 0.16.0 语言与标准库指南。适用于编写、调试、审查或迁移 Zig 代码，以及使用 `build.zig`/`build.zig.zon`、标准库模块、comptime、C 互操作和现代 0.16 API。 |
| `zig-0.15` | 上一代综合技能（Zig 0.15.x），保留作为本地参考语料库和兼容性回退。涵盖语言模式、构建系统 API、I/O、分配器和已删除的语言特性。 |
| `zig-code-review` | 审查 Zig 项目代码的风格、正确性和逻辑。适用于审查 PR/diff、评估项目约定或进行 Zig 代码质量审计。 |
| `zig-tiger-style` | 从 TigerBeetle 生产代码库提炼的 TigerStyle Zig 编码规范。适用于以性能优先的风格编写、审查或重构 Zig 代码。 |
| `zig-raylib` | raylib 5.5 游戏开发库的 Zig 绑定。涵盖 2D/3D 图形、输入、纹理/音频/模型加载、游戏循环，以及惯用 Zig 模式（defer、错误处理、Camera2D/Camera3D）、碰撞检测、骨骼动画、着色器和音频播放。 |
| `zig-sdl3-bindings` | SDL3 多媒体库的 Zig 绑定。涵盖跨平台窗口管理、渲染、GPU 计算、事件、手柄、音频流、网络和 Zig 特有绑定模式。 |

## 📚 仓库布局

```text
zig-skills/
├── skills/
│   ├── zig-0.15/                   # 上一代综合技能 (0.15.x)
│   ├── zig-0.16/                   # 当前主技能 (0.16.0)
│   │   ├── examples/               # 离线快速入门示例
│   │   └── references/             # 40+ 标准库与语言参考
│   ├── zig-code-review/            # 代码审查技能
│   ├── zig-tiger-style/            # Tiger Style 指南
│   ├── zig-raylib/                 # raylib-zig 生态技能
│   └── zig-sdl3-bindings/          # zig-sdl3 生态技能
├── scripts/
│   └── create_zig_016_skill.py     # zig-0.16 技能生成脚本
├── README.md
└── README.zh-CN.md
```

## 🧭 关系说明

`skills/zig-0.16/` 是当前首选的主技能，因为它：

- 将指南升级到了 **Zig 0.16.0**（最新的稳定版）
- 保持仓库原有的综合技能形态
- 增加了明确的**官方来源映射**（语言参考、标准库索引、介绍）
- 维护完整的离线 `references/` 和本地 `examples/`，无需在线获取

`skills/zig-0.15/` 保留作为**上一代综合技能**（Zig 0.15.x）和本地参考语料库来源，对旧代码兼容和补充参考仍有价值。

`zig-code-review` 和 `zig-tiger-style` 技能为 `zig-0.16` 补充了集中的审查和风格指引，而 `zig-raylib` 和 `zig-sdl3-bindings` 则覆盖了 Zig 主流图形/游戏开发生态库。

## 📖 官方来源

`zig-0.16` 主技能依据以下官方文档整理：

- [Zig 语言参考 0.16.0](https://ziglang.org/documentation/0.16.0/)
- [Zig 介绍](https://ziglang.org/documentation/0.16.0/#Introduction)
- [标准库索引 0.16.0](https://ziglang.org/documentation/0.16.0/std/)
- [Zig 中文主页](https://ziglang.org/zh-CN/)
- [构建系统指南](https://ziglang.org/learn/build-system/)
- [0.16.0 发布说明](https://ziglang.org/download/0.16.0/release-notes.html)

## 🤖 支持的智能体

适用于 [Claude Code](https://code.claude.com)、[Codex](https://developers.openai.com/codex)、[Cursor](https://cursor.com)、[OpenCode](https://opencode.ai)、[Gemini CLI](https://geminicli.com)、[GitHub Copilot](https://github.com/features/copilot)、[Windsurf](https://codeium.com/windsurf) 及 [70+ 其他](https://agentskills.io/clients)。

### Claude Code 安装

**方式一：npx skills CLI（推荐）**

```bash
npx skills add full-statck-skills/zig-skills
```

**方式二：手动安装**

```bash
git clone https://github.com/full-statck-skills/zig-skills.git
cp -r zig-skills/skills/* .claude/skills/
```

更多详情请参阅 [Claude Code 技能指南](https://code.claude.com/docs/en/skills) 和 [Agent Skills 规范](https://agentskills.io/)。

## 🌐 生态

| 资源 | 链接 |
|------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **技能组总览** | [github.com/full-statck-skills](https://github.com/full-statck-skills) |
| **Agent Skills 规范** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 License

Apache 2.0 — 详见 [LICENSE](LICENSE)。
