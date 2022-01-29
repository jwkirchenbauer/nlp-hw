class SimpleQARunner:

    response_table = {
        "who"  : "Hatschepsut",
        "when" : "1215",
        "where": "Mount Meru",
        "what" : "Tofu",
        "why"  : "42" 
    }
    default_response = "I don't know"

    def __init__(self):
        """Default Constructor for SimpleQARunner."""
        pass

    def execute_query(self, question_text: str) -> str:
        """Complete this method to achieve the desired behavior from SimpleQARunner."""

        response = self.default_response

        # Not expected that a hidden test case violates stub signature, 
        # but short circuit if so...
        if type(question_text) != str:
            return response
        
        # Tokenize input string by whitespace
        token_list = question_text.split()
        token_count = len(token_list)        

        # Adjust response based on lookup table
        if token_count >= 1:
            """At least one token """
            first_lowercased = token_list[0].lower()
            if first_lowercased in self.response_table:
                response = self.response_table[first_lowercased]

        # Else fall through returning default response
        return response

class SimpleQATestHarness:

    test_cases = {
        "who is the father"  : "Hatschepsut",
        "WhO is the father"  : "Hatschepsut",
        "whoisnt"  : "I don't know",
        "whowho who"  : "I don't know",
        "who what"  : "Hatschepsut",
        "What who the father"  : "Tofu",
        "this is a test": "I don't know",
        "😗 emoji test": "I don't know",
        "blahblah": "I don't know",
        "": "I don't know",
        4: "I don't know"
    }

    def __init__(self):
        """Default Constructor for SimpleQATestHarness."""
        pass
    
    def run_tests(self, runner: SimpleQARunner, verbose=False) -> int:
        status = 0
        try:
            runner_instance = SimpleQARunner()

            for i,(test_in, test_out) in enumerate(self.test_cases.items()):
                resp = runner_instance.execute_query(test_in)
                if verbose: print(f"{i} | test_in: {test_in} | test_out: {test_out} | response: {resp}")
                if resp != test_out:
                   status = 1
                   print(f"test {i} FAIL") 
            return status

        except Exception as e: 
            status = 1
            print(f"Encountered exception [{e}] when running tests.")

# # Run custom tests
# runner = SimpleQARunner() 
# tester = SimpleQATestHarness()
# status = tester.run_tests(runner, verbose=False)
# print(f"Test status: {'PASS' if status==0 else 'FAIL'}",)
