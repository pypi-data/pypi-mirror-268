import os
import signal
import psutil

def kill_process_tree(
    pid, sig=signal.SIGTERM, include_parent=True,
    timeout=None, on_terminate=None
):
    """
    Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callback function which is
    called as soon as a child terminates.
    See `https://psutil.readthedocs.io/en/latest/index.html#kill-process-tree`.
    """
    if include_parent:
        assert pid != os.getpid(), "won't kill myself"
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        try:
            p.send_signal(sig)
        except psutil.NoSuchProcess:
            pass
    killed, alive = psutil.wait_procs(
        children, timeout=timeout,
        callback=on_terminate
    )
    return killed, alive