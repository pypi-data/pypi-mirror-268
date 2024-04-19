from komodo.framework.komodo_context import KomodoContext
from komodo.framework.komodo_runtime import KomodoRuntime
from komodo.framework.komodo_tool_registry import KomodoToolRegistry
from komodo.models.framework.chat_message import ChatMessage


class ModelRequest:
    def __init__(self, prompt: str, runtime: KomodoRuntime, **kwargs):
        self.prompt = prompt
        self.runtime = runtime
        self.kwargs = kwargs

    def __str__(self):
        return str(self.runtime)

    def build_openai_params(self, stream=False):
        params = {
            "model": self.runtime.model,
            "messages": self.prepare_messages(),
            "stream": stream,
            "temperature": self.runtime.temperature,
            "top_p": self.runtime.top_p,
            "seed": self.runtime.seed,
            "max_tokens": self.runtime.max_tokens,
        }

        agent = self.runtime.agent
        if agent.tools:
            params["tools"] = KomodoToolRegistry.get_definitions(agent.tools)

        if agent.provider == "openai" and agent.output_format and 'json' in agent.output_format:
            from openai.types.chat.completion_create_params import ResponseFormat
            params['response_format'] = ResponseFormat(type="json_object")

        return params

    def prepare_detailed_prompt(self):
        conversation = []
        messages = self.prepare_messages()
        for message in messages:
            conversation.append(message['role'] + ": " + message['content'])
        conversation.append("Prompt: " + self.prompt)
        return "\n".join(conversation)

    def prepare_messages(self):
        agent = self.runtime.agent
        messages = self.prepare_agent_messages(agent)

        if collection := self.runtime.selected_collection:
            if agent.autoload_collection:
                messages += self.prepare_file_messages(agent, collection)

        workflow_context = self.kwargs.get('workflow_context', KomodoContext())
        workflow_messages = ChatMessage.convert_from_context(workflow_context)
        messages += [m.add_tag('Workflow') for m in workflow_messages]

        history = self.kwargs.get('history', [])
        messages += self.prepare_history(history)

        workflow_inputs = self.kwargs.get('workflow_inputs', [])
        messages += [m.add_tag('Workflow Agent Outputs') for m in workflow_inputs]

        return messages

    def prepare_file_messages(self, agent, collection):
        max_files = agent.max_files_per_request
        max_tokens_per_file = agent.max_tokens_per_file
        max_total_tokens = agent.max_total_tokens
        collection_context = collection.get_collection_context(max_files, max_tokens_per_file, max_total_tokens)
        collection_messages = ChatMessage.convert_from_context(collection_context)
        return [m.add_tag('Files') for m in collection_messages]

    def prepare_agent_messages(self, agent):
        instructions = ChatMessage.build("Instructions", agent.instructions)
        agent_messages = [instructions]

        if agent.allow_hallucinations:
            agent_messages.append(
                ChatMessage.build("Creativity", "You may make up fake data or hallucinate information."))
        else:
            agent_messages.append(
                ChatMessage.build("Creativity", "Do NOT make up fake data or hallucinate information."))

        if agent.tools:
            agent_messages.append(
                ChatMessage.build("Guidance", "Prioritize tools provided to you to answer the questions."))

        agent_messages.extend(ChatMessage.convert_from_context(agent.generate_context(self.prompt, self.runtime)))
        return [m.add_tag('Agent') for m in agent_messages]

    def prepare_history(self, history: [ChatMessage]):
        messages = []
        # only show last 5 previous run tool messages
        previously_run_tools = [m for m in history if "Previously Run: Tool" in m.content]
        count = len(previously_run_tools)
        max_history = self.runtime.tools_max_history or 5
        max_length = self.runtime.tools_max_length or 256

        for m in history:
            if "Previously Run: Tool" not in m.content:
                messages.append(m)
            else:
                if count <= max_history:
                    message = ChatMessage(role=m.role, content=self.previous_run(m.content, max_length))
                    messages.append(message)
                count -= 1
        return messages

    def previous_run(self, input_string, limit):
        import re

        # Using regex to extract the components
        match = re.search(r"Tool: (.*?): Arguments: (.*?) Output: (.*)", input_string)

        if match:
            tool_shortcode = match.group(1)
            arguments = match.group(2)
            output = match.group(3)

            truncated_output = (output[:limit] + "...") if len(output) > limit else output

            # Create the new format string
            formatted_string = f"Previously Run: Tool: {tool_shortcode}: Arguments: {arguments} Output: {truncated_output}"
            return formatted_string
        else:
            print("Failed to parse the string.")
            return input_string
