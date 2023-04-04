from main.src.executor.get_executor import ExecutorFactory


class Runner:

    @staticmethod
    def runCommand(command):
        commands = command.split(" ")
        _executor_class = ExecutorFactory.get_executor(commands[0])

        if len(commands) > 1:
            _executor_class.execute(commands[1:])
        else:
            _executor_class.execute([])
