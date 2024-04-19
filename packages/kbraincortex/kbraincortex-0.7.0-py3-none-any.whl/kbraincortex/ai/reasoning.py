import re
from kbraincortex.guidance.azure import initialize_instruct_guidance
from kbraincortex.llms.encodings import count_tokens
from guidance import instruction, gen, select
from guidance.models._model import ConstraintException
import logging 
def decide(query, choices, examples, argument_temperature=0.7, decision_temperature=0, given_argument=None, attempt=0):
    print("Hello world!")
    decider = initialize_instruct_guidance()
     
    completion_tokens = 0
    prompt_tokens = 0

    directive = "Make a terse argument about which choice is the best decision to respond to the query with given the choices and their descriptions.\n"
    directive += "Based on your argument, make a decision to select the choice that best aligns with the query.\n"
    directive += "Ensure that the decision matches the conclusion of the argument. If there is a mismatch, reevaluate your decision and try again.\n"
    directive += "--------\n"
    directive += "Here are the possible choices to decide from:\n"
    directive += "\n".join([ f"{choice['label']}: {choice['description']}" for choice in choices]) + "\n"
    directive += "Examples\n"
    directive += "--------\n"
    for example in examples:
        directive += f"Query:{example['query']}\n"
        directive += f"Argument:{example['argument']}\n"
        directive += f"Now make a choice consistent with the argument:{example['decision']}\n"
        directive += "\n"    
    
    directive += "--------\n"
    directive += f"Query:{query}\n"
    directive += "Argument:" 
    prompt_tokens = count_tokens(decider.model_name, directive)
    if given_argument is not None:
        directive += given_argument + "\n"
        directive += "Now make a choice consistent with the argument:"
        prompt_tokens = count_tokens(decider.model_name, directive)    

    with instruction():
      decider += directive

    if given_argument is None:
        decider += gen("argument", temperature=argument_temperature)
        argument = decider["argument"]
        completion_tokens = decider.token_count
        argument, decision, new_completion_tokens, new_prompt_tokens = decide(query, choices, examples, argument_temperature, decision_temperature, given_argument=argument)
        completion_tokens += new_completion_tokens
        prompt_tokens += new_prompt_tokens
        return argument, decision, completion_tokens, prompt_tokens
    
    final_decision = None
    try:
        decider += select([ choice["label"] for choice in choices], "decision")
        final_decision = decider['decision']
        completion_tokens = decider.token_count
    except ConstraintException as e:
        logging.info(str(e))
        logging.info("Retrying decision with prompt modifications.")
        if attempt > 3:
            raise e
        # The regular expression pattern
        pattern = r"The model attempted to generate b'(.+)' after the prompt"

        # Use the re module to find matches
        matches = re.findall(pattern, str(e))
        modified_argument = given_argument + ". In the last attempt, the model attempted to generate " + matches[0] + ". Stop that."
        argument, decision, new_completion_tokens, new_prompt_tokens = decide(query, choices, examples, argument_temperature, decision_temperature, given_argument=modified_argument, attempt=attempt+1)
        completion_tokens += new_completion_tokens
        prompt_tokens += new_prompt_tokens
        final_decision = decision
        
    return given_argument, final_decision, completion_tokens, prompt_tokens
    