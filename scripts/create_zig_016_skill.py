from pathlib import Path
import shutil
import textwrap


REPO = Path(__file__).resolve().parents[1]
OLD_SKILL = REPO / "skills" / "zig"
NEW_SKILL = REPO / "skills" / "zig-0.16"


SKILL_MD = """
---
name: zig-0.16
description: Up-to-date Zig programming language patterns for version 0.16.0. Use when writing, reviewing, or debugging Zig code, working with build.zig and build.zig.zon files, using the Zig standard library, or migrating older examples to Zig 0.16.
---

# Zig Language Reference (v0.16.0)

Zig 0.16.0 is a fast-moving language and toolchain release. Training data and many older examples are stale. This skill combines the official Zig 0.16.0 language reference, the official standard-library index, the Chinese Zig homepage, and this repository's local reference notes into one large Zig skill.

## Official Positioning

From the Zig 0.16.0 documentation and Chinese homepage, Zig is a general-purpose programming language and toolchain for building robust, optimal, and reusable software.

### Core design ideas
- No implicit control flow.
- No implicit memory allocation.
- No preprocessor and no macros.
- Comptime makes types and code generation first-class.
- Zig can be used both as a language and as a cross-platform toolchain for Zig, C, and C++ projects.

### Primary official sources
- [Language reference](https://ziglang.org/documentation/0.16.0/)
- [Introduction](https://ziglang.org/documentation/0.16.0/#Introduction)
- [Standard library index](https://ziglang.org/documentation/0.16.0/std/)
- [Chinese homepage](https://ziglang.org/zh-CN/)
- [Build system documentation](https://ziglang.org/learn/build-system/)
- [0.16.0 release notes](https://ziglang.org/download/0.16.0/release-notes.html)

## Critical: How to use this skill

1. Confirm the user is targeting Zig 0.16.0 or explicitly wants modern Zig patterns.
2. Prefer local repository references in `references/` when you need concrete examples fast.
3. Use official documentation links for authority and API confirmation.
4. Treat this as the main Zig language skill; only switch away for ecosystem-specific bindings such as raylib or SDL3.

## Critical: Official 0.16.0 coverage map

The official Zig 0.16.0 language reference covers these major areas:

- Introduction and Zig Standard Library entry.
- Hello World, comments, doc comments, identifiers, values, assignment, and destructuring.
- Zig Test, test declarations, doctests, leak reporting, test output, and the testing namespace.
- Variables, integers, floats, operators, arrays, vectors, pointers, and slices.
- `struct`, `enum`, `union`, `opaque`, tuples, anonymous literals, and non-exhaustive enums.
- Blocks, `switch`, `while`, `for`, `if`, `defer`, `unreachable`, and `noreturn`.
- Functions, errors, optionals, casting, result location semantics, and zero-bit types.
- `comptime`, generic data structures, builtin functions, atomics, async functions, and assembly.
- C interop related builtins such as `@cImport`, `@cInclude`, `@extern`, and `@export`.
- The Zig Build System, which points to the dedicated build-system documentation.

## Critical: Standard library 0.16.0 coverage map

The official Zig 0.16.0 standard-library index exposes the modules most often needed for application work:

- `std.Build`, `std.zig`, `std.zon`
- `std.Io`, `std.fs`, `std.process`, `std.os`, `std.c`
- `std.heap`, `std.mem`, `std.fmt`, `std.ascii`, `std.unicode`
- `std.http`, `std.json`, `std.Uri`, `std.log`, `std.debug`, `std.testing`
- `std.math`, `std.hash`, `std.crypto`, `std.Random`, `std.time`, `std.tz`
- `std.Thread`, `std.atomic`, `std.meta`, `std.simd`
- `std.ArrayList`, `std.HashMap`, `std.ArrayHashMap`, `std.MultiArrayList`, `std.StaticStringMap`, `std.bit_set`, `std.PriorityQueue`

Use the official std index to confirm module names and the local `references/` folder for curated examples and practical notes.

## Critical: Build System

The official 0.16.0 docs describe the Zig Build System as a cross-platform, dependency-free way to declare project build logic in `build.zig`.

To work with the build system:
- Run `zig build --help` to inspect project-specific steps and options.
- Use the dedicated build docs: [https://ziglang.org/learn/build-system/](https://ziglang.org/learn/build-system/)
- Use the local reference: [std.Build reference](references/std-build.md)

### Modern build pattern
```zig
const std = @import("std");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const exe = b.addExecutable(.{
        .name = "app",
        .root_module = b.createModule(.{
            .root_source_file = b.path("src/main.zig"),
            .target = target,
            .optimize = optimize,
        }),
    });

    b.installArtifact(exe);
}
```

## Critical: Practical Zig 0.16 patterns

### `std.Io` writer pattern
```zig
var buf: [4096]u8 = undefined;
var stdout_writer = std.fs.File.stdout().writer(&buf);
const stdout = &stdout_writer.interface;
try stdout.print("Hello\\n", .{});
try stdout.flush();
```

### Empty and init patterns for stateful types
```zig
var list: std.ArrayList(u32) = .empty;
var map: std.AutoHashMapUnmanaged(u32, u32) = .empty;
var gpa: std.heap.DebugAllocator(.{}) = .init;
var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
```

### Chinese homepage sample pattern
```zig
const std = @import("std");
const parseInt = std.fmt.parseInt;

test "parse integers" {
    const input = "123 67 89,99";
    const gpa = std.testing.allocator;

    var list: std.ArrayList(u32) = .empty;
    defer list.deinit(gpa);

    var it = std.mem.tokenizeAny(u8, input, " ,");
    while (it.next()) |num| {
        const n = try parseInt(u32, num, 10);
        try list.append(gpa, n);
    }

    const expected = [_]u32{ 123, 67, 89, 99 };
    for (expected, list.items) |exp, actual| {
        try std.testing.expectEqual(exp, actual);
    }
}
```

## Quick Fixes

| Error | Fix |
|-------|-----|
| `no field 'root_source_file'` | Use `root_module = b.createModule(.{...})` in `addExecutable`/`addLibrary` |
| `std.io` examples don't compile | Use `std.Io` patterns and explicit writer or reader interfaces |
| Old container init example uses `.{}` | Prefer `.empty` or `.init` depending on the type |
| Need module-specific details | Load the matching local `references/*.md` file |
| Build-system API uncertainty | Check both the local `std-build.md` and the official build-system docs |

## Language References

Load these references when working with core language features:

### Code Style
- **[Style Guide](references/style-guide.md)** - Official Zig naming conventions, whitespace rules, doc comment guidance, redundancy avoidance, `zig fmt`

### Language Basics & Built-ins
- **[Language Basics](references/language.md)** - Core language: types, control flow, error handling, optionals, structs, enums, unions, pointers, slices, comptime, functions
- **[Built-in Functions](references/builtins.md)** - All `@` built-ins: casts, arithmetic, bit ops, memory, atomics, introspection, SIMD, C interop

## Standard Library References

Load these references when working with specific modules:

### Memory & Slices
- **[std.mem](references/std-mem.md)** - Slice search, split or tokenize, alignment, endianness, byte conversion

### Text & Encoding
- **[std.fmt](references/std-fmt.md)** - Format strings, integer and float parsing, custom formatters
- **[std.ascii](references/std-ascii.md)** - ASCII classification, case conversion, case-insensitive comparison
- **[std.unicode](references/std-unicode.md)** - UTF-8 and UTF-16 handling, codepoint iteration, validation
- **[std.base64](references/std-base64.md)** - Base64 encoding and decoding

### Math & Random
- **[std.math](references/std-math.md)** - Floating-point ops, trig, checked arithmetic, constants
- **[std.Random](references/std-random.md)** - PRNGs, random integers or floats, shuffle, distributions
- **[std.hash](references/std-hash.md)** - Hash functions, checksums, auto-hashing

### SIMD & Vectorization
- **[std.simd](references/std-simd.md)** - SIMD vector utilities and patterns

### Time & Timing
- **[std.time](references/std-time.md)** - Timestamps, timers, epoch conversions, calendar helpers
- **[std.Tz](references/std-tz.md)** - Timezone database parsing and timezone handling

### Sorting & Searching
- **[std.sort](references/std-sort.md)** - Sorting algorithms, binary search, min and max helpers

### Core Data Structures
- **[std.ArrayList](references/std-arraylist.md)** - Dynamic arrays and buffer-backed patterns
- **[std.HashMap / AutoHashMap](references/std-hashmap.md)** - Hash maps, string maps, ordered maps
- **[std.ArrayHashMap](references/std-array-hash-map.md)** - Insertion-order preserving maps
- **[std.MultiArrayList](references/std-multi-array-list.md)** - Struct-of-arrays storage
- **[std.SegmentedList](references/std-segmented-list.md)** - Stable pointers and arena-friendly storage
- **[std.DoublyLinkedList / SinglyLinkedList](references/std-linked-list.md)** - Intrusive linked lists
- **[std.PriorityQueue](references/std-priority-queue.md)** - Binary heap based queues
- **[std.PriorityDequeue](references/std-priority-dequeue.md)** - Double-ended priority extraction
- **[std.Treap](references/std-treap.md)** - Balanced tree with ordered keys
- **[std.bit_set](references/std-bit-set.md)** - Static and dynamic bit sets
- **[std.BufMap / BufSet](references/std-buf-map.md)** - String-owning maps and sets
- **[std.StaticStringMap](references/std-static-string-map.md)** - Compile-time string lookup
- **[std.enums](references/std-enums.md)** - EnumSet, EnumMap, EnumArray

### Allocators
- **[std.heap](references/std-allocators.md)** - Allocator selection guide and custom allocator patterns

### I/O & Files
- **[std.io / std.Io](references/std-io.md)** - Reader and Writer API patterns, buffered I/O, binary data
- **[std.fs](references/std-fs.md)** - Files, directories, iteration, atomic writes, paths
- **[std.tar](references/std-tar.md)** - Tar archive handling
- **[std.zip](references/std-zip.md)** - ZIP archive handling
- **[std.compress](references/std-compress.md)** - Compression and decompression modules

### Networking
- **[std.http](references/std-http.md)** - HTTP client or server patterns, TLS, compression
- **[std.net / std.Io.net](references/std-net.md)** - Socket basics, address parsing, DNS
- **[std.Uri](references/std-uri.md)** - URI parsing, percent-encoding, relative resolution

### Process Management
- **[std.process](references/std-process.md)** - Child process spawning, environment, arguments, exec

### OS-Specific APIs
- **[std.os](references/std-os.md)** - Platform-specific APIs, syscalls, Windows or WASI access
- **[std.c](references/std-c.md)** - C ABI types and libc bindings

### Concurrency
- **[std.Thread](references/std-thread.md)** - Thread spawning, mutexes, rw locks, conditions, semaphores
- **[std.atomic](references/std-atomic.md)** - Atomic operations, orderings, compare-and-swap

### Patterns & Best Practices
- **[Zig Patterns](references/patterns.md)** - Practical patterns for writing and reviewing Zig code
- **[Code Review](references/code-review.md)** - Review checklist and stale-pattern detection

### Serialization
- **[std.json](references/std-json.md)** - JSON parsing, serialization, dynamic values, streaming
- **[std.zon](references/std-zon.md)** - ZON parsing and serialization for `build.zig.zon` and configs

### Testing & Debug
- **[std.testing](references/std-testing.md)** - Unit test assertions and utilities
- **[std.debug](references/std-debug.md)** - Panic, assert, stack traces, hex dump
- **[std.log](references/std-log.md)** - Scoped logging and configurable levels

### Metaprogramming
- **[Comptime Reference](references/comptime.md)** - Comptime fundamentals, reflection, generic patterns
- **[std.meta](references/std-meta.md)** - Type introspection, field iteration, stringToEnum, generic programming

### Compiler Utilities
- **[std.zig](references/std-zig.md)** - AST parsing, tokenization, source analysis, linters, formatters, ZON parsing

### Security & Cryptography
- **[std.crypto](references/std-crypto.md)** - Hashing, AEAD, signatures, key exchange, password hashing, secure random

### Build System
- **[std.Build](references/std-build.md)** - Build system, modules, dependencies, steps, options, testing, C or C++ integration

### Interoperability
- **[C Interop](references/c-interop.md)** - Exporting C-compatible APIs, calling conventions, libraries, headers, module maps
"""


def main() -> None:
    NEW_SKILL.mkdir(parents=True, exist_ok=True)
    refs_src = OLD_SKILL / "references"
    refs_dst = NEW_SKILL / "references"
    if refs_dst.exists():
        shutil.rmtree(refs_dst)
    shutil.copytree(refs_src, refs_dst)
    (NEW_SKILL / "SKILL.md").write_text(textwrap.dedent(SKILL_MD).strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
