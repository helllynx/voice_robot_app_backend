from commands import Command


class Parser:

    def __init__(self):
        self.current_command = None
        self.current_params = None
        self.full_command_text = None

    def parser_english(self, command: str):
        print(command)
        self.full_command_text = command.split(" ")

        if "yes" in self.full_command_text or "okay" in self.full_command_text:
            print(f"<< YES or OKAY - command {self.current_command}")
            self.current_command(self.current_params)
            self.current_command = None
            self.full_command_text = None

        if "no" in self.full_command_text or "cancel" in self.full_command_text:
            self.current_command = None
            self.full_command_text = None

        if "folder" in self.full_command_text or "open" in self.full_command_text:
            self.current_command = Command().dir
            self.current_params = command.split(" ")

