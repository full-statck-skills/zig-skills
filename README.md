# Zig Skills

Agent Skills for Zig 0.16.0 and adjacent Zig ecosystem workflows.

## Overview

This repository now centers on one large main Zig skill plus two ecosystem skills:

- `zig-0.16`: the primary Zig 0.16.0 language, std, build system, migration, and review skill
- `zig-raylib`: Zig projects using raylib-zig
- `zig-sdl3-bindings`: Zig projects using zig-sdl3

This matches the original repository shape more closely than the earlier over-split `zig-0.16-*` plan, while still keeping the content versioned and grounded in the official 0.16.0 docs.

## Repository Layout

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

## Skills

### `zig-0.16`

The main aggregate skill for Zig 0.16.0.

It consolidates:

- the official language reference
- the official introduction
- the official standard library index
- the Zig Chinese homepage positioning and sample
- the local offline `references/` set copied from the existing `zig` skill
- local `examples/` entry points for quick offline use

Use it when you need:

- modern Zig 0.16 syntax and semantics
- `build.zig` and `build.zig.zon` guidance
- std module selection and usage
- comptime, metaprogramming, and builtins
- C interop or toolchain workflows
- migration away from stale 0.14/0.15-era examples
- Zig code review and debugging

### `zig-raylib`

The ecosystem skill for building games and graphics applications with raylib-zig.

### `zig-sdl3-bindings`

The ecosystem skill for building multimedia and cross-platform applications with zig-sdl3.

## Relationship To `zig`

`skills/zig/` remains in the repository as the previous aggregate skill and as the source of the local reference corpus.

`skills/zig-0.16/` is now the preferred main skill for current work because it:

- keeps the same aggregate-skill shape the repository already used
- updates the guidance to Zig 0.16.0
- adds stronger official source mapping
- keeps offline references and examples so the skill still works without live fetching

## Official Documentation Sources

The main `zig-0.16` skill is grounded in:

- https://ziglang.org/documentation/0.16.0/
- https://ziglang.org/documentation/0.16.0/#Introduction
- https://ziglang.org/documentation/0.16.0/std/
- https://ziglang.org/zh-CN/
- https://ziglang.org/learn/build-system/
- https://ziglang.org/download/0.16.0/release-notes.html

## Notes

- `skills/zig-0.16/` is the preferred entry point for main Zig language work.
- `skills/zig/` remains useful as a compatibility and source-material skill.
- The repository no longer treats the earlier fine-grained `zig-0.16-*` split as the primary direction.
