from komodo import KomodoApp
from komodo.core.agents.chatdoc_agent import ChatdocAgent
from komodo.core.agents.collection_builder import CollectionBuilderAgent
from komodo.core.agents.default import translator_agent, summarizer_agent

from komodo.framework.komodo_context import KomodoContext
from komodo.framework.komodo_features import KomodoFeatures
from komodo.framework.komodo_user import KomodoUser
from komodo.loaders.filesystem.appliance_loader import ApplianceLoader
from sample.appliance.workflow import SampleWorkflow


class SampleAppliance(KomodoApp):
    shortcode = 'sample'
    name = 'Sample Appliance'
    purpose = 'To test the Komodo Appliances SDK'

    def __init__(self, config):
        base = ApplianceLoader(config.definitions_directory, config.data_directory).load(self.shortcode)
        super().__init__(**base)
        self.config = config

        self.add_agent(summarizer_agent())
        self.add_agent(translator_agent())

        chatdoc = ChatdocAgent()
        chatdoc.max_tokens_per_file = 500
        chatdoc.max_total_tokens = 2000

        self.add_agent(chatdoc)
        self.add_agent(CollectionBuilderAgent())
        self.add_workflow(SampleWorkflow())

    def generate_context(self, prompt=None, runtime=None):
        context = KomodoContext()
        context.add("Sample", f"Develop context for the {self.name} appliance")
        return context

    def configuration(self, user: KomodoUser):
        print(f"Generating configuration for {user.email}")
        if user and user.groups and 'beta' in user.groups:
            config = self.configuration_for_beta_user()
        else:
            config = self.configuration_for_normal_user()
        return {
            "shortcode": self.shortcode,
            "name": self.name,
            "company": self.company,
            "type": self.type.name,
            "purpose": self.purpose,
            "user": user.email,
            "configuration": config
        }

    def configuration_for_normal_user(self):
        shortcodes = ['summarizer', 'translator']
        agents = [a for a in self.get_all_agents() if a.shortcode in shortcodes]
        return [
            {
                "feature": KomodoFeatures.chat.name,
                "description": "Chat with the agents",
                "agents": [a.summary() for a in agents]
            },
            {
                "feature": KomodoFeatures.chatdoc.name,
                "description": "Chat with documents",
                "agents": [ChatdocAgent().summary()]
            }
        ]

    def configuration_for_beta_user(self):
        agents = self.get_all_agents()
        return [
            {
                "feature": KomodoFeatures.chat.name,
                "description": "Chat with the agents",
                "agents": [a.summary() for a in agents]
            },
            {
                "feature": KomodoFeatures.chatdoc.name,
                "description": "Chat with documents",
                "agents": [ChatdocAgent().summary()]
            },
            {
                "feature": KomodoFeatures.chat.name,
                "description": "Chat with top 1 agents",
                "agents": [a.summary() for a in agents[:1]]
            },
            {
                "feature": KomodoFeatures.chat.name,
                "description": "Chat with top 2 agents",
                "agents": [a.summary() for a in agents[:2]]
            }, {
                "feature": KomodoFeatures.chatdoc.name,
                "description": "More chat with documents",
                "agents": [ChatdocAgent().summary()]
            }, {
                "feature": KomodoFeatures.reportbuilder.name,
                "description": "Report Builder #1",
                "agents": []
            }, {
                "feature": KomodoFeatures.reportbuilder.name,
                "description": "Report Builder #2",
                "agents": []
            }, {
                "feature": KomodoFeatures.dashboard.name,
                "description": "Komodo Dashboard #1",
                "agents": []
            }, {
                "feature": KomodoFeatures.dashboard.name,
                "description": "Komodo Dashboard #2",
                "agents": []
            }
        ]
