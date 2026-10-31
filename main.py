#!/usr/bin/env python3
import os
import sys

# Add source directory to Python module search path
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
if source_dir not in sys.path:
    sys.path.insert(0, source_dir)

if __name__ == "__main__":
    from patcher.utils.admin import is_admin, run_as_admin
    from patcher.utils.console import setup_console
    from patcher.cli import run_cli, confirmed

    setup_console()
    if os.name == "nt" and os.environ.get("SKIP_ELEVATION") != "1" and not is_admin():
        if run_as_admin():
            sys.exit(0)
        else:
            print("  [!] Could not elevate privileges. The script may fail to modify files.")
    elif os.name == "posix" and not is_admin():
        print("  [!] Root access is required to patch files in the root directory.")
        if confirmed("Re-launch with sudo?"):
            try:
                if getattr(sys, "frozen", False):
                    args = ["sudo", sys.executable] + sys.argv[1:]
                else:
                    args = ["sudo", sys.executable] + sys.argv
                os.execvp("sudo", args)
            except Exception as e:
                print(f"  [!] Failed to re-launch with sudo: {e}")
                sys.exit(1)
        else:
            from patcher.constants import COLOR_YELLOW
            from patcher.utils.console import color
            print(color("  [!] Proceeding without root. Write errors are possible.", COLOR_YELLOW))
            print()

    try:
        run_cli()
    except KeyboardInterrupt:
        print("\n  [i] Exiting...")
        sys.exit(0)
    except (PermissionError, OSError) as e:
        print(f"\n  [!] Filesystem error: {e}")
        if sys.platform == "darwin":
            print("  [i] macOS blocked writing inside Antigravity.app.")
            print("  [i] Close Antigravity and re-run with sudo:")
            print("        sudo python3 main.py")
        else:
            print("  [i] No write access — re-run as admin/root and close Antigravity first.")
        sys.exit(1)
    except Exception as e:
        print(f"\n  [!] Unexpected error: {e}")
        sys.exit(1)
