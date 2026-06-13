<div align="center">

# zig-skills

**Zig language skills — 0.16.0, raylib, SDL3, code review, Tiger Style**

[![GitHub](https://img.shields.io/badge/github-full--statck--skills%2Fzig-skills-green.svg)](https://github.com/full-statck-skills/zig-skills)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-purple.svg)](https://agentskills.io)

English | [简体中文](./README.zh-CN.md)

[Introduction](#-introduction) · [Install](#-install) · [Skills](#-skills) · [Repository Layout](#-repository-layout) · [Relationship](#-relationship--migration) · [Official Sources](#-official-sources) · [Supported Agents](#-supported-agents) · [Ecosystem](#-ecosystem)

</div>

---

## 📖 Introduction

**Zig Skills** is a curated collection of Agent Skills for AI coding agents focused on the [Zig programming language](https://ziglang.org) and its ecosystem, part of the [Full Stack Skills](https://github.com/partme-ai/full-stack-skills) ecosystem maintained by [PartMe.AI](https://github.com/partme-ai).

This package includes **6 skills**, centered on one primary Zig 0.16.0 aggregate skill plus ecosystem and tooling companions. Each skill is a self-contained `SKILL.md` file that AI agents load on-demand.

## 📦 Install

```bash
npx skills add full-statck-skills/zig-skills
```

Or install specific skills: `npx skills add full-statck-skills/zig-skills --skill <skill-name>`

## 🎯 Skills (6)

| Skill | Description |
|-------|-------------|
| `zig-0.16` | **Primary skill.** Up-to-date Zig 0.16.0 language and standard library guidance. Use for writing, reviewing, debugging, or migrating Zig code, working with `build.zig`/`build.zig.zon`, std modules, comptime, C interop, and modern 0.16 APIs. |
| `zig-0.15` | Previous-generation aggregate skill for Zig 0.15.x. Retained as a local reference corpus and compatibility fallback. Covers language patterns, build system APIs, I/O, allocators, and removed language features. |
| `zig-code-review` | Review Zig project code for style, correctness, and logic. Invoke when reviewing PRs/diffs, assessing project conventions, or requesting a Zig-focused code quality audit. |
| `zig-tiger-style` | TigerStyle Zig coding guidelines — distilled from the TigerBeetle production codebase. Use when writing, reviewing, or refactoring Zig code with a focus on performance-correct style conventions. |
| `zig-raylib` | Zig bindings for raylib 5.5 game development library. Covers 2D/3D graphics, input, textures/sounds/models, game loops, idiomatic Zig patterns (defer, error handling, Camera2D/Camera3D), collision detection, skeletal animation, shaders, and audio playback. |
| `zig-sdl3-bindings` | Zig bindings for SDL3 multimedia library. Covers cross-platform windowing, rendering, GPU compute, events, gamepads, audio streams, networking, and Zig-specific binding patterns. |

## 📚 Repository Layout

```text
zig-skills/
├── skills/
│   ├── zig-0.15/                   # Previous aggregate skill (0.15.x)
│   ├── zig-0.16/                   # Current primary skill (0.16.0)
│   │   ├── examples/               # Offline quick-start examples
│   │   └── references/             # 40+ std lib & language references
│   ├── zig-code-review/            # Code review skill
│   ├── zig-tiger-style/            # Tiger Style guidelines
│   ├── zig-raylib/                 # raylib-zig ecosystem skill
│   └── zig-sdl3-bindings/          # zig-sdl3 ecosystem skill
├── scripts/
│   └── create_zig_016_skill.py     # Generator for zig-0.16 skill
├── README.md
└── README.zh-CN.md
```

## 🧭 Relationship & Migration

`skills/zig-0.16/` is the **preferred main skill** for current Zig work because it:

- Updates guidance to **Zig 0.16.0** (the latest stable release)
- Keeps the same aggregate-skill shape the repository originally used
- Adds strong **official source mapping** (language reference, std index, introduction)
- Maintains a complete offline `references/` set and local `examples/` so the skill works without live fetching

`skills/zig-0.15/` is retained as a **previous-generation aggregate skill** (Zig 0.15.x) and as the source of the local reference corpus. It remains useful for compatibility with older codebases and as supplemental reference material.

The `zig-code-review` and `zig-tiger-style` skills complement `zig-0.16` with focused review and style guidance, while `zig-raylib` and `zig-sdl3-bindings` cover the leading Zig graphics/game development ecosystem libraries.

## 📖 Official Sources

The `zig-0.16` main skill is grounded in these official documentation sources:

- [Zig Language Reference 0.16.0](https://ziglang.org/documentation/0.16.0/)
- [Zig Introduction](https://ziglang.org/documentation/0.16.0/#Introduction)
- [Standard Library Index 0.16.0](https://ziglang.org/documentation/0.16.0/std/)
- [Zig 中文主页](https://ziglang.org/zh-CN/)
- [Build System Guide](https://ziglang.org/learn/build-system/)
- [0.16.0 Release Notes](https://ziglang.org/download/0.16.0/release-notes.html)

## 🤖 Supported Agents

Works with [Claude Code](https://code.claude.com), [Codex](https://developers.openai.com/codex), [Cursor](https://cursor.com), [OpenCode](https://opencode.ai), [Gemini CLI](https://geminicli.com), [GitHub Copilot](https://github.com/features/copilot), [Windsurf](https://codeium.com/windsurf), and [70+ others](https://agentskills.io/clients).

### Claude Code Installation

**Option 1: npx skills CLI (Recommended)**

```bash
npx skills add full-statck-skills/zig-skills
```

**Option 2: Manual Installation**

```bash
git clone https://github.com/full-statck-skills/zig-skills.git
cp -r zig-skills/skills/* .claude/skills/
```

For more details, see the [Claude Code Skills Guide](https://code.claude.com/docs/en/skills) and [Agent Skills Spec](https://agentskills.io/).

## 🌐 Ecosystem

| Resource | Link |
|----------|------|
| **Full Stack Skills** | [github.com/partme-ai/full-stack-skills](https://github.com/partme-ai/full-stack-skills) |
| **All Skill Groups** | [github.com/full-statck-skills](https://github.com/full-statck-skills) |
| **Agent Skills Spec** | [agentskills.io](https://agentskills.io) |
| **Skills CLI** | [github.com/vercel-labs/skills](https://github.com/vercel-labs/skills) |

## 📄 License

Apache 2.0 — see [LICENSE](LICENSE).
