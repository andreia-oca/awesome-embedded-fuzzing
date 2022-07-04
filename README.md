# Awesome Embedded Fuzzing

![Last Update](https://img.shields.io/github/last-commit/andreia-oca/awesome-embedded-fuzzing)

---

- [Description](#description)
- [Labels Indexes](#labels-indexes)
    - [By Type](#by-type)
    - [By Purpose](#by-purpose)
- [Papers](#papers)
- [Resources](#resources)
- [Contribution](#contribution)
- [Credits](#credits)

---

## Description

A **list of helpful fuzzing tools and research materials** for embedded applications can be found in this repository.

All resources are alphabetically organized and labeled, making it simple to locate them simply searching one item from the index on the entire page (with `CTRL+F`). The ones not having a link attached are present in the `documents/` folder.

## Labels Indexes

### By Type

- ![Type: awesome](https://img.shields.io/badge/Type-awesome-lightgrey)
- ![Type: benchmark](https://img.shields.io/badge/Type-benchmark-lightgrey)
- ![Type: blog%20post](https://img.shields.io/badge/Type-blog%20post-lightgrey)
- ![Type: book](https://img.shields.io/badge/Type-book-lightgrey)
- ![Type: code%20snippets](https://img.shields.io/badge/Type-code%20snippets-lightgrey)
- ![Type: community](https://img.shields.io/badge/Type-community-lightgrey)
- ![Type: demo](https://img.shields.io/badge/Type-demo-lightgrey)
- ![Type: emulator](https://img.shields.io/badge/Type-emulator-lightgrey)
- ![Type: library](https://img.shields.io/badge/Type-library-lightgrey)
- ![Type: presentation](https://img.shields.io/badge/Type-presentation-lightgrey)
- ![Type: reverse%20engineering](https://img.shields.io/badge/Type-reverse%20engineering-lightgrey)
- ![Type: testbed](https://img.shields.io/badge/Type-testbed-lightgrey)
- ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
- ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey)
- ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)

### By Purpose

- ![Purpose: benchmark](https://img.shields.io/badge/Purpose-benchmark-blue)
- ![Purpose: binary%20analysis](https://img.shields.io/badge/Purpose-binary%20analysis-blue)
- ![Purpose: binary%20disassembly](https://img.shields.io/badge/Purpose-binary%20disassembly-blue)
- ![Purpose: directed%20fuzzing](https://img.shields.io/badge/Purpose-directed%20fuzzing-blue)
- ![Purpose: embedded%20fuzzing](https://img.shields.io/badge/Purpose-embedded%20fuzzing-blue)
- ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue)
- ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- ![Purpose: firmware%20testing](https://img.shields.io/badge/Purpose-firmware%20testing-blue)
- ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- ![Purpose: fuzzing%20network%20protocols](https://img.shields.io/badge/Purpose-fuzzing%20network%20protocols-blue)
- ![Purpose: fuzzing%20x86%20binaries](https://img.shields.io/badge/Purpose-fuzzing%20x86%20binaries-blue)
- ![Purpose: instrumentation](https://img.shields.io/badge/Purpose-instrumentation-blue)
- ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)
- ![Purpose: synthetic%20bugs](https://img.shields.io/badge/Purpose-synthetic%20bugs-blue)

## Papers

| Paper Title | Abstract | Venue | Publication Date |
| --- | --- | --- | --- |
| **[JetSet](https://www.usenix.org/system/files/sec21-johnson.pdf)** | <details> <summary>Click to see the abstract!</summary> The ability to execute code in an emulator is a fundamental part of modern vulnerability testing. Unfortunately, this poses a challenge for many embedded systems, where firmware expects to interact with hardware devices specific to the target. Getting embedded system firmware to run outside its native environment, termed rehosting, requires emulating these hardware devices with enough accuracy to convince the firmware that it is executing on the target hardware. However, full fidelity emulation of target devices (which requires considerable engineering effort) may not be necessary to boot the firmware to a point of interest for an analyst (for example, a point where fuzzer input can be injected). We hypothesized that, for the firmware to boot successfully, it is sufficient to emulate only the behavior expected by the firmware, and that this behavior could be inferred automatically. To test this hypothesis, we developed and implemented Jetset, a system that uses symbolic execution to infer what behavior firmware expects from a target device. Jetset can generate devices models for hardware peripherals in C, allowing an analyst to boot the firmware in an emulator (e.g., QEMU). We successfully applied Jetset to thirteen distinct pieces of firmware together representing three architectures, three application domains (power grid, avionics, and consumer electronics), and five different operating systems. We also demonstrate how Jetset-assisted rehosting facilitates fuzztesting, a common security analysis technique, on an avionics embedded system, in which we found a previously unknown privilege escalation vulnerability </details> | USENIX 2021 | 2021 |
| **[SoK: Enabling Security Analyses of Embedded Systems via Rehosting](https://megele.io/rehosting-sok-asiaccs2021.pdf)** | <details> <summary>Click to see the abstract!</summary> Closely monitoring the behavior of a software system during its execution enables developers and analysts to observe, and ultimately understand, how it works. This kind of dynamic analysis can be instrumental to reverse engineering, vulnerability discovery, exploit development, and debugging. While these analyses are typically wellsupported for homogeneous desktop platforms (e.g., x86 desktop PCs), they can rarely be applied in the heterogeneous world of embedded systems. One approach to enable dynamic analyses of embedded systems is to move software stacks from physical systems into virtual environments that sufficiently model hardware behavior. This process which we call “rehosting” poses a significant research challenge with major implications for security analyses. Although rehosting has traditionally been an unscientific and ad-hoc endeavor undertaken by domain experts with varying time and resources at their disposal, researchers are beginning to address rehosting challenges systematically and in earnest. In this paper, we establish that emulation is insufficient to conduct large-scale dynamic analysis of real-world hardware systems and present rehosting as a firmwarecentric alternative. Furthermore, we taxonomize preliminary rehosting efforts, identify the fundamental components of the rehosting process, and propose directions for future research. </details> | ASIACCS 2021 | 2021 |


## Resources

- **[AFL](https://github.com/google/AFL)**
    - Description: state-of-the-art fuzzer
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[AFL++](https://github.com/AFLplusplus/AFLplusplus)**
    - Description: state-of-the-art fuzzer
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[afl-unicorn](https://github.com/Battelle/afl-unicorn)**
    - Description: AFL-based fuzzer integrated with Unicorn
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- **[afl-unicorn: Fuzzing Arbitrary Binary Code](https://medium.com/hackernoon/afl-unicorn-fuzzing-arbitrary-binary-code-563ca28936bf)**
    - Description: tutorial for afl-unicorn
    - Type: ![Type: blog%20post](https://img.shields.io/badge/Type-blog%20post-lightgrey) ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue) ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[afl-unicorn: Part 2 Fuzzing the ‘Unfuzzable’](https://hackernoon.com/afl-unicorn-part-2-fuzzing-the-unfuzzable-bea8de3540a5)**
    - Description: tutorial for afl-unicorn
    - Type: ![Type: blog%20post](https://img.shields.io/badge/Type-blog%20post-lightgrey) ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue) ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[AFLGo](https://github.com/aflgo/aflgo)**
    - Description: directed fuzzer
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: directed%20fuzzing](https://img.shields.io/badge/Purpose-directed%20fuzzing-blue)
- **[Analyzing a buffer overflow in the DLINK DIR-645 with Qiling framework, Part I](https://github.com/nahueldsanchez/blogpost_qiling_dlink_1)**
    - Description: reverse enginerring for DLINK DIR645
    - Type: ![Type: reverse%20engineering](https://img.shields.io/badge/Type-reverse%20engineering-lightgrey) ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue) ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- **[Analyzing a buffer overflow in the DLINK DIR-645 with Qiling framework, Part II](https://github.com/nahueldsanchez/blogpost_qiling_dlink_2)**
    - Description: reverse enginerring for DLINK DIR645
    - Type: ![Type: reverse%20engineering](https://img.shields.io/badge/Type-reverse%20engineering-lightgrey) ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue) ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- **[Analyzing Programs with Z3](https://youtu.be/ruNFcH-KibY)**
    - Description: symbolic execution with Z3
    - Type: ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey) ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)
- **[angr](https://github.com/angr/angr)**
    - Description: binary analysis platform
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: binary%20analysis](https://img.shields.io/badge/Purpose-binary%20analysis-blue)
- **[Avatar<sup>2](https://github.com/avatartwo/avatar2)**
    - Description: dynamic analysis of embedded devices' firmware!
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: binary%20analysis](https://img.shields.io/badge/Purpose-binary%20analysis-blue)
- **[Awesome list for directed-fuzzing](https://github.com/strongcourage/awesome-directed-fuzzing)**
    - Description: awesome list for directed-fuzzing
    - Type: ![Type: awesome](https://img.shields.io/badge/Type-awesome-lightgrey)
    - Purpose: ![Purpose: directed%20fuzzing](https://img.shields.io/badge/Purpose-directed%20fuzzing-blue)
- **[Capstone](https://www.capstone-engine.org/)**
    - Description: disassembly platform
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: binary%20disassembly](https://img.shields.io/badge/Purpose-binary%20disassembly-blue)
- **[DICE](https://github.com/RiS3-Lab/DICE-DMA-Emulation)**
    - Description: nan
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: embedded%20fuzzing](https://img.shields.io/badge/Purpose-embedded%20fuzzing-blue) ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[Firmware Rehosting Community](https://rehosti.ng/)**
    - Description: firmware Rehosting Community
    - Type: ![Type: community](https://img.shields.io/badge/Type-community-lightgrey)
    - Purpose: ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[FIT IoT-LAB](https://www.iot-lab.info/)**
    - Description: nan
    - Type: ![Type: testbed](https://img.shields.io/badge/Type-testbed-lightgrey)
    - Purpose: ![Purpose: firmware%20testing](https://img.shields.io/badge/Purpose-firmware%20testing-blue)
- **[Google FuzzBench](https://github.com/google/fuzzbench)**
    - Description: benchmark for fuzzers
    - Type: ![Type: benchmark](https://img.shields.io/badge/Type-benchmark-lightgrey)
    - Purpose: ![Purpose: benchmark](https://img.shields.io/badge/Purpose-benchmark-blue) ![Purpose: fuzzing%20x86%20binaries](https://img.shields.io/badge/Purpose-fuzzing%20x86%20binaries-blue)
- **[GynvaelEN - Hacking Livestream #17: Basics of fuzzing](https://youtu.be/BrDujogxYSk)**
    - Description: fuzzing 101 tutorial
    - Type: ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey) ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[GynvaelEN - Hacking Livestream #18: Genetic fuzzing](https://youtu.be/JhsHGms_7JQ)**
    - Description: fuzzing 101 tutorial
    - Type: ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey) ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[GynvaelEN - Hacking Livestream #19: Genetic fuzzing](https://youtu.be/HN_tI601jNU)**
    - Description: fuzzing 101 tutorial
    - Type: ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey) ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[Hack In The Box Security Conference - VIRTUAL LAB: Qiling Framework: Build a Fuzzer Based on a 1day Bug - Lau Kai Jern](https://youtu.be/e3_T3KLh2NU)**
    - Description: workshop about Qiling (emulator)
    - Type: ![Type: demo](https://img.shields.io/badge/Type-demo-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue)
- **[hal-fuzz](https://github.com/ucsb-seclab/hal-fuzz)**
    - Description: embedded fuzzer based in HALucinator
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- **[HALucinator](https://github.com/embedded-sec/halucinator)**
    - Description: nan
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[JetSet](https://www.youtube.com/watch?v=xp3gTOS0Zq8&ab_channel=USENIX)**
    - Description: presentation for Jetset
    - Type: ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[JetSet](https://github.com/aerosec/jetset)**
    - Description: repository for JetSet
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[LAVA](https://github.com/panda-re/lava)**
    - Description: benchmark for fuzzers
    - Type: ![Type: benchmark](https://img.shields.io/badge/Type-benchmark-lightgrey)
    - Purpose: ![Purpose: benchmark](https://img.shields.io/badge/Purpose-benchmark-blue) ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue) ![Purpose: synthetic%20bugs](https://img.shields.io/badge/Purpose-synthetic%20bugs-blue)
- **[LIEF](https://lief.quarkslab.com/)**
    - Description: library to do binary instrumentation
    - Type: ![Type: library](https://img.shields.io/badge/Type-library-lightgrey)
    - Purpose: ![Purpose: instrumentation](https://img.shields.io/badge/Purpose-instrumentation-blue)
- **[Maat](https://maat.re/)**
    - Description: symbolic execution framework
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)
- **[Magma](https://github.com/HexHive/magma)**
    - Description: benchmark for fuzzers
    - Type: ![Type: benchmark](https://img.shields.io/badge/Type-benchmark-lightgrey)
    - Purpose: ![Purpose: benchmark](https://img.shields.io/badge/Purpose-benchmark-blue) ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue) ![Purpose: synthetic%20bugs](https://img.shields.io/badge/Purpose-synthetic%20bugs-blue)
- **[NDC Conferences - Fuzzing with AFL - Erlend Oftedal](https://youtu.be/DFQT1YxvpDo)**
    - Description: fuzzing 101 tutorial
    - Type: ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey) ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[ndss18_wycinwyc](https://github.com/avatartwo/ndss18_wycinwyc)**
    - Description: fuzzing experiments from the paper "What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices"
    - Type: ![Type: code%20snippets](https://img.shields.io/badge/Type-code%20snippets-lightgrey)
    - Purpose: ![Purpose: embedded%20fuzzing](https://img.shields.io/badge/Purpose-embedded%20fuzzing-blue)
- **[P2IM](https://github.com/RiS3-Lab/p2im)**
    - Description: nan
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: embedded%20fuzzing](https://img.shields.io/badge/Purpose-embedded%20fuzzing-blue) ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[Practical Binary Analysis. Build Your Own Linux Tools for Binary Instrumentation, Analysis, and Disassembly](https://www.amazon.com/Practical-Binary-Analysis-Instrumentation-Disassembly-ebook/dp/B07BPKWJVT)**
    - Description: book with example and approaches for binary analysis
    - Type: ![Type: book](https://img.shields.io/badge/Type-book-lightgrey)
    - Purpose: ![Purpose: binary%20analysis](https://img.shields.io/badge/Purpose-binary%20analysis-blue)
- **[Pretender](https://github.com/ucsb-seclab/pretender)**
    - Description: nan
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: embedded%20fuzzing](https://img.shields.io/badge/Purpose-embedded%20fuzzing-blue) ![Purpose: firmware%20rehosting](https://img.shields.io/badge/Purpose-firmware%20rehosting-blue)
- **[ProFuzzBench](https://github.com/profuzzbench/profuzzbench)**
    - Description: benchmark for fuzzers focused on network protocols
    - Type: ![Type: benchmark](https://img.shields.io/badge/Type-benchmark-lightgrey)
    - Purpose: ![Purpose: benchmark](https://img.shields.io/badge/Purpose-benchmark-blue) ![Purpose: fuzzing%20network%20protocols](https://img.shields.io/badge/Purpose-fuzzing%20network%20protocols-blue)
- **[Qemu](https://www.qemu.org/)**
    - Description: nan
    - Type: ![Type: emulator](https://img.shields.io/badge/Type-emulator-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue)
- **[Qiling](https://github.com/qilingframework/qiling)**
    - Description: nan
    - Type: ![Type: emulator](https://img.shields.io/badge/Type-emulator-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue)
- **[Renode](https://renode.io/)**
    - Description: nan
    - Type: ![Type: testbed](https://img.shields.io/badge/Type-testbed-lightgrey)
    - Purpose: ![Purpose: firmware%20testing](https://img.shields.io/badge/Purpose-firmware%20testing-blue)
- **[S2E](https://github.com/S2E/s2e)**
    - Description: symbolic execution
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)
- **[STÖK - Fuzzing for Beginners](https://youtu.be/O3hb6HV1ZQo)**
    - Description: fuzzing 101 tutorial
    - Type: ![Type: tutorial](https://img.shields.io/badge/Type-tutorial-lightgrey) ![Type: video](https://img.shields.io/badge/Type-video-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[Symbolic Execution Summary](https://docs.google.com/presentation/d/1E3uE-4mYpenw0s40rtMbIdxj3fJgC79aHCeiIlJSY5Y/edit#slide=id.g11285b0bdfc_0_310)**
    - Description: presentation on Symbolic Execution 
    - Type: ![Type: presentation](https://img.shields.io/badge/Type-presentation-lightgrey)
    - Purpose: ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)
- **[The fuzzing book](https://www.fuzzingbook.org)**
    - Description: book with practical examples about fuzzing
    - Type: ![Type: book](https://img.shields.io/badge/Type-book-lightgrey)
    - Purpose: ![Purpose: fuzzing](https://img.shields.io/badge/Purpose-fuzzing-blue)
- **[Triforce-AFL](https://github.com/nccgroup/TriforceAFL)**
    - Description: AFL/QEMU fuzzing with full-system emulation.
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- **[Triton](https://triton.quarkslab.com/)**
    - Description: symbolic execution
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)
- **[Unicorn](https://github.com/unicorn-engine/unicorn)**
    - Description: nan
    - Type: ![Type: emulator](https://img.shields.io/badge/Type-emulator-lightgrey)
    - Purpose: ![Purpose: emulation](https://img.shields.io/badge/Purpose-emulation-blue)
- **[unicornafl](https://github.com/AFLplusplus/unicornafl)**
    - Description: AFL-based fuzzer integrated with Unicorn
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: fuzzing%20firmware](https://img.shields.io/badge/Purpose-fuzzing%20firmware-blue)
- **[Z3 - SMT solver](https://github.com/Z3Prover/z3)**
    - Description: symbolic execution
    - Type: ![Type: tool](https://img.shields.io/badge/Type-tool-lightgrey)
    - Purpose: ![Purpose: symbolic%20execution](https://img.shields.io/badge/Purpose-symbolic%20execution-blue)


## Contribution

1. Edit the `resources.csv` file.
2. Push the changes into the GitHub repository.
3. Wait for the GitHub action to automatically recompile `README.md`.

## Credits

The template is inspired from this [repository](https://github.com/CyberReasoningSystem/awesome-binary-analysis).
