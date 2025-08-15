from src.info_navigation.navigationProgramHandler import NavigationProgramHandler
from src.system_properties.systemPropetiersHandler import SystemPropertiesHandler


class NetworkTestingHandler:

    def __init__(self):
        self.times = 100

    def network_execute(self):

        system_handler = SystemPropertiesHandler()

        system_handler.command_execution()