class CLIMenu:

    def __init__(self, program_name, command_map) -> None:
        """This form: 
        {
            "menu_text" : action /sub_menu
        }"""
        self.__command_map = command_map
        self.program_name = program_name

    def show_main(self):
        while True:
            print(f'{self.program_name:=^50}\n')
            for i, cmd in enumerate(self.__command_map.items(), start=1):
                print(f'{i}. {cmd[0]}')
            try:
                user_choice = int(
                    input("Alege un numar din lista de mai sus: "))
            except ValueError:
                print(
                    'Eroare: Te rog sa alegi din valoare de mai sus, trebuie sa fie numar. ')
            else:
                print(f"Ai ales: {user_choice}")
