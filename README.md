# Welcome to IoT-Fuzzing

A list of resources (papers, books, talks, frameworks, tools) for understanding fuzzing for IoT/embedded devices.

## Contents
- [Papers](#papers)
	- [State-of-the-Art Fuzzers](#state-of-the-art-fuzzers)
	- [IoT/Embedded Devices Fuzzing](#iotembedded-devices-fuzzing)
	- [Firmware Emulators](#firmware-emulators)
- [Books](#books)
- [Videos](#videos)
- [Tutorials and Blogs](#tutorials-and-blogs)
- [Tools](#tools)
	- [Fuzzers](#fuzzers)
	- [Benchmarking Fuzzers](#benchmarking-fuzzers)
	- [Binary analysis](#binary-analysis)
	- [Symbolic execution](#symbolic-execution)
	- [Re-hosting frameworks](#re-hosting-frameworks)
	- [Emulators](#emulators)
	- [IoT Testbeds](#iot-testbeds)

## Papers

### State-of-the-Art Fuzzers

TODO

### IoT/Embedded Devices Fuzzing

TODO

### Firmware Emulators

TODO

## Books

[The fuzzing book](https://www.fuzzingbook.org/)

[Practical Binary Analysis. Build Your Own Linux Tools for Binary Instrumentation, Analysis, and Disassembly](https://www.amazon.com/Practical-Binary-Analysis-Instrumentation-Disassembly-ebook/dp/B07BPKWJVT)

## Videos

[STÖK - FUZZING FOR BEGINNERS (KUGG teaches STÖK American fuzzy lop)](https://youtu.be/O3hb6HV1ZQo)

[NDC Conferences - Fuzzing with AFL - Erlend Oftedal](https://youtu.be/DFQT1YxvpDo)

[GynvaelEN - Hacking Livestream #17: Basics of fuzzing](https://youtu.be/BrDujogxYSk)

[GynvaelEN - Hacking Livestream #18: Genetic fuzzing (theory)](https://youtu.be/JhsHGms_7JQ)

[GynvaelEN - Hacking Livestream #19: Genetic fuzzing (implementation)](https://youtu.be/HN_tI601jNU)

[Analyzing Programs with Z3](https://youtu.be/ruNFcH-KibY)

[Hack In The Box Security Conference - VIRTUAL LAB: Qiling Framework: Build a Fuzzer Based on a 1day Bug - Lau Kai Jern](https://youtu.be/e3_T3KLh2NU)

## Tutorials and blogs

[afl-unicorn: Fuzzing Arbitrary Binary Code](https://medium.com/hackernoon/afl-unicorn-fuzzing-arbitrary-binary-code-563ca28936bf)

[afl-unicorn: Part 2 — Fuzzing the ‘Unfuzzable’](https://hackernoon.com/afl-unicorn-part-2-fuzzing-the-unfuzzable-bea8de3540a5)

[Analyzing a buffer overflow in the DLINK DIR-645 with Qiling framework, Part I](https://github.com/nahueldsanchez/blogpost_qiling_dlink_1)

[Analyzing a buffer overflow in the DLINK DIR-645 with Qiling framework, Part II](https://github.com/nahueldsanchez/blogpost_qiling_dlink_2)


## Tools

### Fuzzers

[AFL](https://github.com/google/AFL)

[AFLplusplus](https://github.com/AFLplusplus/AFLplusplus)

[AFLgo](https://github.com/aflgo/aflgo)

[afl-unicorn](https://github.com/Battelle/afl-unicorn) *Note:* Integrates AFL with Unicorn Engine.

[unicornafl](https://github.com/AFLplusplus/unicornafl) *Note:* Integrates AFLplusplus with Unicorn Engine.

[hal-fuzz](https://github.com/ucsb-seclab/hal-fuzz) *Note:* Integrates AFL with HALucinator.

[Triforce-AFL](https://github.com/nccgroup/TriforceAFL) *Note:* Integrates QEMU with AFL.

### Benchmarking Fuzzers

[Google FuzzBench](https://github.com/google/fuzzbench)

[LAVA](https://github.com/panda-re/lava)

[Magma](https://github.com/HexHive/magma)

### Binary Analysis

[Avatar<sup>2](https://github.com/avatartwo/avatar2)

[angr](https://github.com/angr/angr)

[LIEF](https://lief.quarkslab.com/)

[Capstone](https://www.capstone-engine.org/)

### Symbolic execution

[S2E](https://github.com/S2E/s2e)

[Triton](https://triton.quarkslab.com/)

[Z3 - SMT solver](https://github.com/Z3Prover/z3)

### Re-hosting Frameworks

[HALucinator](https://github.com/embedded-sec/halucinator)

[P2IM](https://github.com/RiS3-Lab/p2im)

[DICE](https://github.com/RiS3-Lab/DICE-DMA-Emulation)

[Pretender](https://github.com/ucsb-seclab/pretender)

[ndss18_wycinwyc](https://github.com/avatartwo/ndss18_wycinwyc) *Note:* The fuzzing experiments from the paper "What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices". 

### Emulators

[Qiling](https://github.com/qilingframework/qiling)

[Unicorn](https://github.com/unicorn-engine/unicorn)

[Qemu](https://www.qemu.org/)

### IoT Testbeds

[FIT IoT-LAB](https://www.iot-lab.info/)
[Renode](https://renode.io/)
