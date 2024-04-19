from komodo.framework.komodo_runtime import KomodoRuntime
from komodo.models.framework.model_request import ModelRequest


def test_previously_run():
    # Prompt for the user input
    input_string = "Tool: video_search_tool: Arguments: {'query': 'mobility'} Output: {'video': 'mobility_video.mov'}"
    limit = 10

    # Create an instance of the ModelRequest class
    model_request = ModelRequest(prompt="", runtime=KomodoRuntime())

    # Call the previous_run method
    response = model_request.previous_run(input_string, limit)
    assert response == "Previously Run: Tool: video_search_tool: Arguments: {'query': 'mobility'} Output: {'video': ..."


def test_previously_run_unformatted():
    # Prompt for the user input
    input_string = "Tool: video_search_tool: Random text"
    limit = 10

    # Create an instance of the ModelRequest class
    model_request = ModelRequest(prompt="", runtime=KomodoRuntime())

    # Call the previous_run method
    response = model_request.previous_run(input_string, limit)
    assert response == "Tool: video_search_tool: Random text"
