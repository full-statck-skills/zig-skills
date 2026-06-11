# Zig Skills

面向 Zig 0.16.0 与相关生态工作流的 Agent Skills 仓库。

## 总览

这个仓库现在收敛为 1 个主 Zig 技能 + 2 个生态技能：

- `zig-0.16`：主技能，覆盖 Zig 0.16.0 语言、标准库、构建系统、迁移与代码审查
- `zig-raylib`：面向 `raylib-zig` 的生态技能
- `zig-sdl3-bindings`：面向 `zig-sdl3` 的生态技能

这比之前过度拆分的 `zig-0.16-*` 方案更接近原始仓库形态，也更符合同一语言应以综合主技能为核心的使用方式。

## 仓库结构

```text
zig-skills/
├── skills/
│   ├── zig/
│   ├── zig-0.16/
│   │   ├── examples/
│   │   └── references/
│   ├── zig-raylib/
│   └── zig-sdl3-bindings/
├── scripts/
├── README.md
└── README.zh-CN.md
```

## 技能说明

### `zig-0.16`

这是当前仓库的主 Zig 综合技能。

它整合了：

- Zig 0.16.0 官方语言参考文档
- 官方 Introduction 入口
- 官方标准库索引
- Zig 中文主页中的定位与示例
- 从现有 `zig` 技能复制过来的本地 `references/`
- 为离线使用补充的本地 `examples/`

适用场景包括：

- 编写、调试、审查 Zig 0.16 代码
- 使用 `build.zig` 与 `build.zig.zon`
- 查询标准库模块和常见模式
- 使用 comptime、元编程、builtin
- 处理 C 互操作与工具链工作流
- 把旧版 Zig 示例迁移到 0.16

### `zig-raylib`

面向 `raylib-zig` 项目的生态技能，聚焦图形、游戏循环、资源管理和 raylib 绑定模式。

### `zig-sdl3-bindings`

面向 `zig-sdl3` 项目的生态技能，聚焦窗口、事件、渲染、音频、输入和 SDL3 Zig 绑定模式。

## 与 `zig` 的关系

`skills/zig/` 仍然保留，作为上一代综合技能与本地参考资料来源。

`skills/zig-0.16/` 现在是主入口，因为它：

- 保持了原来“大而全”的综合技能形态
- 把内容升级到了 Zig 0.16.0
- 增加了更明确的官方来源映射
- 保留了本地 references 与 examples，避免只靠外链

## 官方来源

`zig-0.16` 主技能主要依据以下官方内容整理：

- https://ziglang.org/documentation/0.16.0/
- https://ziglang.org/documentation/0.16.0/#Introduction
- https://ziglang.org/documentation/0.16.0/std/
- https://ziglang.org/zh-CN/
- https://ziglang.org/learn/build-system/
- https://ziglang.org/download/0.16.0/release-notes.html

## 说明

- `skills/zig-0.16/` 是当前主 Zig 技能入口。
- `skills/zig/` 继续保留，作为兼容与资料来源。
- 仓库不再把之前的细粒度 `zig-0.16-*` 拆分视为主要方向。
