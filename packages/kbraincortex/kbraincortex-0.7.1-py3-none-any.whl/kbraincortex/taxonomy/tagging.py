import logging
from kbraincortex.guidance.azure import initialize_instruct_guidance
from guidance import instruction, gen
from kbraincortex.llms.encodings import count_tokens

def tag_document(content, temperature = None):

    if temperature is None:
        temperature = 0.7

    logging.info(f"Tagging document with content: {content}")
    tagger = initialize_instruct_guidance()

    prompt = "Given a chunk of content, analyze it to understand the primary subjects, themes, and key elements." \
    + "Based on your analysis, generate a list of semantically relevant tags that accurately represent the content's main ideas and aspects." \
    + "Ensure that the tags are concise and descriptive, capturing the essence of the content. Separate each tag with a comma." \
    + "Consider the context, tone, and specific details within the content to create a comprehensive set of tags that could be used " \
    + "for categorization, search optimization, or content discovery purposes. Your response should prioritize relevance and " \
    + "specificity to ensure the tags are directly related to the content provided.\n\n" \
    + "Content: In recent years, the tech industry has seen a significant shift towards sustainable technology practices. Companies are now prioritizing the development of energy-efficient devices, the reduction of carbon footprints, and the implementation of green computing initiatives. This move is not only driven by environmental concerns but also by consumer demand for eco-friendly products and the long-term cost savings associated with sustainable practices. Moreover, advancements in renewable energy sources, such as solar and wind power, are being integrated into tech manufacturing processes. The industry is also witnessing a rise in the recycling and repurposing of electronic waste, further contributing to environmental conservation efforts. These trends indicate a growing recognition within the tech sector of its responsibility towards the planet and highlight the potential for technology to play a pivotal role in combating climate change.\n" \
    + "Tags:Sustainable technology,Energy-efficient devices,Carbon footprint reduction,Green computing,Environmental concerns,Eco-friendly products,Cost savings,Renewable energy sources,Solar power,Wind power,Tech manufacturing processes,Recycling,Repurposing,Electronic waste,Environmental conservation,Tech sector responsibility,Planet,Climate change mitigation\n" \
    + f"Content: {content}\n" \
    + "Tags:"
    
    prompt_tokens = count_tokens(tagger.model_name, prompt)  

    with instruction():
        tagger += prompt

    tagger += gen("tags", temperature=temperature)
    completion_tokens = tagger.token_count
    tags = tagger["tags"]
    logging.info(tags)
    tag_list = tags.split(",")
    tag_list = [tag.strip() for tag in tag_list]
    tokens = {}
    tokens["tokens_completion"] = completion_tokens
    tokens["tokens_prompt"] = prompt_tokens
    tokens["tokens_total"] = completion_tokens + prompt_tokens
    return tag_list, tokens
