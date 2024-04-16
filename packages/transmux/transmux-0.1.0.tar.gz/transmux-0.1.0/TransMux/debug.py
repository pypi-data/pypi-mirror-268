# CopyRight: TransMux InEase28@gmail.com
import builtins
from functools import wraps
import threading
import sys
import traceback


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


orig_print = builtins.print


@wraps(orig_print)
def myprint(*values, **kwargs):
    sep = kwargs.pop("sep", " ")
    end = kwargs.pop("end", "\n")
    kwargs.setdefault("flush", True)

    return orig_print(f"{sep.join(str(v) for v in values)}{end}", end="", **kwargs)


def patch(block=True, better=True, flush=True):
    """
    Patch the builtins.print function to flush after every call.
    If block is True, Errors will be handled in block
    If better is True, use better_exceptions to format the exception.
    If flush is True, flush every print.
    """

    if better:
        import better_exceptions

        better_exceptions.hook()

    if flush:
        builtins.print = myprint

    if block and better:
        from better_exceptions import format_exception

        def sys_excepthook(exc_type, exc_value, exc_traceback):
            print(
                f"\n{bcolors.FAIL}-> Exception in thread {threading.current_thread()} <-\n{bcolors.ENDC}",
                "".join(format_exception(exc_type, exc_value, exc_traceback)),
                file=sys.stderr,
            )

        def thread_excepthook(args):
            print(
                f"\n{bcolors.FAIL}-> Exception in thread {args.thread} <-\n{bcolors.ENDC}",
                "".join(
                    format_exception(args.exc_type, args.exc_value, args.exc_traceback)
                ),
                file=sys.stderr,
            )

        sys.excepthook = sys_excepthook
        threading.excepthook = thread_excepthook
    elif block and not better:

        def sys_excepthook(exc_type, exc_value, exc_traceback):
            print(
                f"\n{bcolors.FAIL}-> Exception in thread {threading.current_thread()} <-\n{bcolors.ENDC}",
                "".join(traceback.format_exception(exc_type, exc_value, exc_traceback)),
                file=sys.stderr,
            )

        def thread_excepthook(args):
            print(
                f"\n{bcolors.FAIL}-> Exception in thread {args.thread} <-\n{bcolors.ENDC}",
                "".join(
                    traceback.format_exception(
                        args.exc_type, args.exc_value, args.exc_traceback
                    )
                ),
                file=sys.stderr,
            )

        sys.excepthook = sys_excepthook
        threading.excepthook = thread_excepthook
