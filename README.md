# CritSectionSem — Critical Section with `Lock` vs `BoundedSemaphore`

This mini–project (Parallel Programming module) implements **two correct solutions** to protect a shared counter across **multiple processes** using Python’s `multiprocessing`:

- `CritSectionLock.py` — mutual exclusion with a **single `multiprocessing.Lock`**
- `CritSectionBoundedSemaphore.py` — mutual exclusion with a **single `multiprocessing.BoundedSemaphore(1)`**

Both programs spawn `N = 8` processes; each process performs 10 increments on a shared counter. With proper cross-process synchronization, the final value is **80** (`8 * 10`).

## Why not `threading.Semaphore`?
`threading.*` primitives only coordinate **threads within the same process**. For **separate processes**, you must use **`multiprocessing`** synchronization objects **created in `main` and passed to all processes**.

## Requirements
- Python **3.8+**
- Standard library only (`multiprocessing`, `time`, `random`)

## How to run
```bash
python CritSectionLock.py
python CritSectionBoundedSemaphore.py
