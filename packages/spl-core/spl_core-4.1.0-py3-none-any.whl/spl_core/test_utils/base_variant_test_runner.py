import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

from spl_core.test_utils.spl_build import SplBuild


class BaseVariantTestRunner(ABC):
    @property
    def variant(self) -> str:
        return re.sub(r"^Test_", "", self.__class__.__name__).replace("__", "/")

    @property
    @abstractmethod
    def component_paths(self) -> List[Path]:
        pass

    @property
    @abstractmethod
    def expected_build_artifacts(self) -> List[Path]:
        pass

    @property
    def expected_test_artifacts(self) -> List[Path]:
        return [Path("reports/coverage/index.html")]

    @property
    def expected_variant_report_artifacts(self) -> List[Path]:
        return [Path("reports/reports/index.html")]

    @property
    def expected_component_report_artifacts(self) -> List[Path]:
        return [
            Path("coverage.html"),
            Path("unit_test_results.html"),
            Path("unit_test_spec.html"),
            Path("doxygen/html/index.html"),
            Path("coverage/index.html"),
        ]

    def test_build(self) -> None:
        spl_build: SplBuild = SplBuild(variant=self.variant, build_kit="prod")
        assert 0 == spl_build.execute(target="all")  # noqa: S101
        for artifact in self.expected_build_artifacts:
            assert artifact.exists() or Path.joinpath(spl_build.build_dir, artifact).exists()  # noqa: S101

    def test_unittest(self) -> None:
        spl_build: SplBuild = SplBuild(variant=self.variant, build_kit="test")
        assert 0 == spl_build.execute(target="unittests")  # noqa: S101
        for artifact in self.expected_test_artifacts:
            assert artifact.exists()  # noqa: S101

    def test_reports(self) -> None:
        spl_build: SplBuild = SplBuild(variant=self.variant, build_kit="test")
        assert 0 == spl_build.execute(target="all")  # noqa: S101
        for artifact in self.expected_variant_report_artifacts:
            assert Path.joinpath(spl_build.build_dir, artifact).exists()  # noqa: S101
        for component in self.component_paths:
            for artifact in self.expected_component_report_artifacts:
                assert Path.joinpath(spl_build.build_dir, component, artifact).exists()  # noqa: S101
