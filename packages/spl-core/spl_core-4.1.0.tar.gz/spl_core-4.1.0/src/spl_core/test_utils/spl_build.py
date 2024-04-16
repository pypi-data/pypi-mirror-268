import time
from pathlib import Path
from typing import List, Optional

from py_app_dev.core.logging import time_it

from spl_core.common.command_line_executor import CommandLineExecutor


class SplBuild:
    """Class for building an SPL repository."""

    def __init__(self, variant: str, build_kit: str):
        """
        Initialize a SplBuild instance.

        Args:
            variant (str): The build variant.
            build_kit (str): The build kit.

        """
        self.variant = variant
        self.build_kit = build_kit

    @property
    def build_dir(self) -> Path:
        """
        Get the build directory.

        Returns:
            Path: The build directory path.

        """
        return Path(f"build/{self.variant}/{self.build_kit}")

    @time_it()
    def execute(self, target: str, additional_args: Optional[List[str]] = None) -> int:
        """
        Build the target

        Args:
            target (str): The build target.
            additional_args (List[str], optional): Additional arguments for building. Defaults to ["-build"].

        Returns:
            int: 0 in case of success.

        """
        if additional_args is None:
            additional_args = ["-build"]
        return_code = -1
        while True:
            cmd = [
                "build.bat",
                "-buildKit",
                self.build_kit,
                "-variants",
                self.variant,
                "-target",
                target,
                "-reconfigure",
            ]
            cmd.extend(additional_args)
            result = CommandLineExecutor().execute(cmd)
            return_code = result.returncode
            if result.returncode:
                if result.stdout:
                    if any(error in str(result.stdout) for error in ["No valid floating license", "No valid license", "GHS_LMHOST = N/A"]):
                        print("Probably a license issue, retrying ...")
                        time.sleep(10)
                    else:
                        break
                else:
                    break
            else:
                break
        return return_code
