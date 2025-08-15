from src.graphic_user_interface.graphicUserInterfaceHandler import GraphicUserInterfaceHandler
from src.network_core.networkTestingHandler import NetworkTestingHandler

graphic_interface = GraphicUserInterfaceHandler()
teste = NetworkTestingHandler()


graphic_interface.execute_screen("Testador de rede Internet Service Provider Shit - ISPSHIT", "Testar", lambda: teste.network_execute())





