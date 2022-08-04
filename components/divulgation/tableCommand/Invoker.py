from components.divulgation.tableCommand.Command import Command

class Invoker:
    """
    Invoker, associated with one or several commands, sends a request
    to the command
    """

    __template = None

    def set_template(self, command: Command):
        self.__template = command

    def getting_template(self) -> None:
        """
        Invoker don't depend on concrete command or receiver. It only
        passes a request to a receiver indirectly, by executing a command
        """
        if isinstance(self.__template, Command):
            return self.__template.execute()