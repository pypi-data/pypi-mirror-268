from enum import IntEnum
import subprocess
import tomllib as toml
from cleo.io.io import IO
from cleo.events.console_events import COMMAND
from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.event_dispatcher import EventDispatcher
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

class Verbosity(IntEnum):
    QUIET = 0
    VERBOSE = 1
    VERY_VERBOSE = 2
    DEBUG = 3

class PoetryPlugin(ApplicationPlugin):
    is_active: bool = False
    __command: str | None = None
    run_in_venv: bool = False
    venv_path = ".venv"

    def activate(self, application: Application):
        self.read_pyproject_toml()
        application.event_dispatcher.add_listener(
            COMMAND, self.main
        )

    def main(
        self,
        event: ConsoleCommandEvent,
        event_name: str,
        dispatcher: EventDispatcher
    ) -> None:
        command = event.command
        if not isinstance(command, EnvCommand):
            return
        io = event.io

        verbose_level= Verbosity(io.is_verbose() + io.is_very_verbose() + io.is_debug())
        
        if self.is_active:
            self._run_command(io, verbose_level)
        elif verbose_level >= Verbosity.VERBOSE:
            io.write_line("Watson not set to run any command.")

    def read_pyproject_toml(self) -> None:
        try:
            with open("pyproject.toml", "rb") as file:
                config = toml.load(file)

                self.is_active =  config.get("tool", {}).get("watson", {}).get("is_active", False)
                self.__command = config.get("tool", {}).get("watson", {}).get("command", self.__command)
                self.run_in_venv = config.get("tool", {}).get("watson", {}).get("run_in_venv", self.run_in_venv)
                self.venv_path = config.get("tool", {}).get("watson", {}).get("venv_path", self.venv_path)

        except FileNotFoundError:
            self.is_active = False

    def _run_command(self, io: IO, verbosity: Verbosity):
        if self.run_in_venv:
            if verbosity is Verbosity.DEBUG:
                io.write_line(f"Adding prefix to activate venv: source {self.venv_path}/bin/activate &&")
            prefix = f"source {self.venv_path}/bin/activate && "
        else: 
            if verbosity is Verbosity.DEBUG:
                io.write_line("No prefix to activate venv.")
            prefix = ""

        io.write_line(f"<info>Running command: {prefix}{self.__command}</info>")
        process = subprocess.run(f"{prefix}{self.__command}", capture_output=True, shell=True, text=True)
        if process.returncode != 0:
            if verbosity is Verbosity.DEBUG:
                io.write_line(f"Command failed with return code {process.returncode}.")
            if verbosity > Verbosity.VERBOSE:
                if process.stdout:
                    io.write_line("Command output:")
                    io.write(process.stdout)
                if process.stderr:
                    io.write_line("Command error:")
                    io.write(process.stderr)
            raise subprocess.CalledProcessError(process.returncode, process.args)
