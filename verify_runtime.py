"""Measure the kit entrypoint inside a network-isolated Linux filesystem."""
import os
import socket
import sys
from pathlib import Path

if __name__ == "__main__":
    interfaces = {name for _, name in socket.if_nameindex()}
    if interfaces != {"lo"}:
        raise SystemExit(f"Expected an isolated network namespace. Found {interfaces!r}.")
    if not os.statvfs("/bot").f_flag & os.ST_RDONLY:
        raise SystemExit("Expected a read-only /bot mount.")
    if Path("/output/entry.png").exists():
        raise SystemExit("Expected an empty output directory.")

    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    executable = sys.argv[1]
    env = os.environ.copy()
    env.pop("MAKEFUN_OUTPUT_DIR", None)
    pid = os.posix_spawn(executable, [executable, "/bot/main.ts"], env)
    _, status, usage = os.wait4(pid, 0)
    if status:
        raise SystemExit(os.waitstatus_to_exitcode(status))
    if not Path("/output/entry.png").is_file():
        raise SystemExit("Missing /output/entry.png.")
    if usage.ru_maxrss > 512 * 1024:
        raise SystemExit(f"Peak RSS exceeds 512 MiB: {usage.ru_maxrss} KiB.")
    print(f"Literal /output path, isolated network, 1 CPU, peak RSS {usage.ru_maxrss} KiB.")
