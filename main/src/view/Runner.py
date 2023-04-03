from main.src.executor.get_executor import ExecutorFactory


class Runner:

    @staticmethod
    def runCommand(self, command):
        self.commands = command.split(" ")
        _executor_class = ExecutorFactory.get_executor(self.commands[0])

        if len(self.commands) > 1:
            _executor_class.execute(self.commands[1:])
        else:
            _executor_class.execute([])
