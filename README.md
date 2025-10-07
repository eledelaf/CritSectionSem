-->
# CritSectionSem
Se deben hacer dos programas. Uno usando un Lock y el otro un BoundedSemaphore.
--
# CritSectionSem — Critical Section with Semaphore Use

This project demonstrates a critical section problem using **multiple processes** (`multiprocessing`) and a shared counter. It intentionally shows why protecting a **read–modify–write** sequence requires a **cross-process** lock — and why a **threading** semaphore inside each process does **not** provide mutual exclusion across processes.

## 🧩 What the code does

- Spawns **N = 8** independent **processes** (`multiprocessing.Process`).
- Each process runs `task(common, tid, turn)` for **10 iterations**:
  - Simulates work in a **non-critical section** with a random sleep.
  - Enters a so-called **“critical section”** where it reads `common.value`, increments it, and writes it back.
  - Updates a `turn` variable (not used for coordination).
- The shared counter is a `multiprocessing.Value("i", 0)` named **`common`**.
