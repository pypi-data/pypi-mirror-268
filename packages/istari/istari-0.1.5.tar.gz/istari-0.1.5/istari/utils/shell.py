import subprocess


class ShellCommandMixin:
    def run_command(self, command: str, as_list=False) -> str:
        process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = process.stdout.decode('utf-8').rstrip('\n')
        if as_list is True:
            return output.split('\n')
        return output
