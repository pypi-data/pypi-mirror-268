import proto.dtx.messages.common.threat_pb2 as threat_pb2
import proto.dtx.services.prompts.v1.prompts_pb2 as prompts_pb2


# Description: Common data models for the SDK

# Data class representing a generated prompt
class LLMPrompt:
    def __init__(self, content: str, role="user"):
        self.role = role
        self.content = content

    def text(self):
        return self.content

# Data class representing a prompt response from an LLM model
class LLMResponse:
    def __init__(self, content: str, skip_evaluation: bool = False):
        self.content = content
        self.skip_evaluation = skip_evaluation

    def skip(self):
        """
        Skip evaluation of this response
        """
        self.skip_evaluation = True

    def is_skipped(self):
        """
        Check if the evaluation of this response is skipped
        """
        return self.skip_evaluation

# Data class representing the result of a prompt and response
# evaluation for security vulnerabilities
class LLMScanResult:
    def __init__(self):
        self.results = []

    # Store the raw protobuf response from the API for
    # rendering into various forms
    def add_raw_result(self, response: prompts_pb2.PromptEvaluationResponse):
        self.results.append(response)

    def __iter__(self):
        return iter(self.results)

    def total_count(self):
        """
        Return the number of test results stored
        """
        return len(self.results)

    def failed_count(self):
        """
        Return the number of failed test results. A test result
        is considered failed if at least one vulnerability is found.
        """
        return sum(1 for result in self.results if self.is_vulnerable(result))

    def failed_results(self):
        """
        Return a list of failed test results
        """
        return [result for result in self.results if self.is_vulnerable(result)]

    def group_by_threats(self):
        """
        Group responses by threats
        """
        all_responses = [response for result in self.results for response in result.responses]

        threats = {}
        for response in all_responses:
            for result in response.results:
                if result.status == threat_pb2.THREAT_EVALUATION_STATUS_UNSAFE:
                    if result.threat.threat_class not in threats:
                        threats[result.threat.threat_class] = {}
                    if result.threat.threat_category not in threats[result.threat.threat_class]:
                        threats[result.threat.threat_class][result.threat.threat_category] = []
                    threats[result.threat.threat_class][result.threat.threat_category].append(result)

        return threats

    def is_vulnerable(self, result: prompts_pb2.PromptEvaluationResponse):
        """
        Returns true if there is at least one response with a vulnerability
        """
        for response in result.responses:
            for result in response.results:
                if result.status == threat_pb2.THREAT_EVALUATION_STATUS_UNSAFE:
                    return True

        return False
