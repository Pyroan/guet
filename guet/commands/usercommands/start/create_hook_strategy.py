from guet.commands.usercommands.start.hook_strategy import HookStrategy
from guet.git.git import Git


class CreateHookStrategy(HookStrategy):
    def apply(self):
        self.git.create_hooks()
