class Runner:

    @staticmethod
    def runCommand(commands):
        from src.executor.get_executor import ExecutorFactory
        executor = ExecutorFactory.get_executor(commands[0])

        if len(commands) > 1:
            executor.execute(commands[1:])
        else:
            executor.execute([])
