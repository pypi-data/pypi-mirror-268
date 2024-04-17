from istari import __version__
from istari.cli.base import BaseCommand
from istari.utils.shell import ShellCommandMixin


class Command(BaseCommand, ShellCommandMixin):
    def handle(self, **options):
        requirements = self.run_command('pip freeze', as_list=True)
        for requirement in requirements:
            # if istari is installed in editable mode
            # replace with actual package version
            if requirement.startswith('-e') and requirement.endswith('#egg=istari'):
                print(f'istari=={__version__}')
            else:
                print(requirement)
