from pathlib import Path

from komodo.framework.komodo_config import KomodoConfig
from komodo.framework.komodo_runtime import KomodoRuntime
from komodo.framework.komodo_user import KomodoUser
from komodo.models.framework.agent_runner import AgentRunner
from sample.appliance.appliance import SampleAppliance

APPLIANCE_FOLDER = Path(__file__).parent.parent.resolve()


class ApplianceConfig(KomodoConfig):
    def __init__(self, data_directory=None, **kwargs):
        definitions_directory = APPLIANCE_FOLDER / "definitions"
        super().__init__(data_directory=data_directory, definitions_directory=definitions_directory, **kwargs)

    def get_serpapi_key(self):
        return self.get_secret("SERP_API_KEY")


class LocalConfig(ApplianceConfig):
    def __init__(self):
        super().__init__(data_directory=APPLIANCE_FOLDER / "data" / "komodo")


if __name__ == "__main__":
    config = LocalConfig()
    # loader = ApplianceLoader(config.definitions_directory, config.data_directory)
    # loader.setup_appliance("sample")
    # loader = AgentLoader(config.definitions_directory, config.data_directory)
    # loader.setup_agent("dasher")

    sample = SampleAppliance(config)
    agent = sample.get_agent("chatdoc")
    user = KomodoUser.default()
    user.groups = ['admin', 'debug']
    user.language = 'es'

    runner = AgentRunner(KomodoRuntime(agent=agent, config=LocalConfig(), user=user))
    for token in runner.run_streamed("How are you today?"):
        print(token)

    print(sample)
