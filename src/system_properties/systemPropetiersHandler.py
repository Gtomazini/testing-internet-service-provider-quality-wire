import os

from src.info_navigation.navigationProgramHandler import NavigationProgramHandler


class SystemPropertiesHandler:

    def __init__(self):
        self.operation_system = None
        self.command = "ping"
        self.address = "nada"
        self.package = "nada"
        self.command_mounted = "nada"

    def extract_os(self):
        self.operation_system = os.name

    def command_assembly_windows(self, times= 100):

        self.package = f"-n {times}"
        assistent_navigation = NavigationProgramHandler()
        assistent_navigation.search_dns_main()
        self.address = assistent_navigation.address_main
        self.command_mounted = f"{self.command} {self.package} {self.address}"

    def operator_os(self):

        self.extract_os()

        systems = {
            "nt" : self.command_assembly_windows(),
            "posix" : "Linux"
        }

        systems.get(self.operation_system, "nt")

    def command_execution(self):
        self.operator_os()
        os.system(self.command_mounted)


