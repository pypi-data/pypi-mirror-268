from setuptools import setup

__version__ = "2.4.2"

if __name__ == "__main__":
    setup(
        install_requires=[
            "hiredis",
            "louie",
            "numpy",
            "scipy",
            "msgpack",
            "requests",
            "typeguard>=4.0.1",
            "pyyaml",
            "redis",
            "toolz",
            "rich",
            "pylint",
            "loguru",
            "psutil",
            "fpdf",
            "fastjsonschema",
            "lmfit",
            "pydantic~=2.0",
        ],
        extras_require={
            "dev": [
                "pytest",
                "pytest-random-order",
                "pytest-timeout",
                "coverage",
                "pandas",
                "black~=24.0",
                "isort",
                "pylint",
                "fakeredis",
            ]
        },
        entry_points={
            "console_scripts": ["bec-channel-monitor = bec_lib:channel_monitor_launch"],
            "pytest11": [
                "bec_lib_fixtures = bec_lib.tests.fixtures",
            ],
        },
        package_data={"bec_lib.tests": ["*.yaml"], "bec_lib.configs": ["*.yaml", "*.json"]},
        version=__version__,
    )
