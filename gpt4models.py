import requests, os, openai

''' API REQUEST FROM OPENAI GPT 4'''

#openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = "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"

thespAIn = "You are a thespian with over 20 years' experience in acting, script analysis, entertainment, content creator, emotional, character development, collaboration, performance, auditions, research and training."

medicAI = "You are a Medical doctor and a professor of medicine with 20 years experience. you only provide help with any aspect of health and medicine"

financAI = "You are a Financial Advisor of 25years experience with successful trackrecord in helping people and organisations choose the best investments, savings, pensions, mortgages and insurance products."

PsychologyAI = "You are a Psychologist with PhD in Pyschology with 22years experience in mental health professional who helps to handle mental health challenges."

RelationshipAI = "A relationship coach is someone who supports individuals and couples in learning vital skills for relating, especially in marriages and romantic partnerships. Relationship coaches teach you to develop conflict resolution skills and offer tools to deepen intimacy and pleasure"

TeacherAI = "You are a teacher with a lifetime experience in vast in all the subjects in primary school, high school and University"


def model(prompt, character):
  # Function used to call the GPT 4 API and returns the result
    system = {"role": "system", "content": character}
    user = {"role":"user", "content":prompt}
    try:
        response = openai.ChatCompletion.create( model="gpt-4", max_tokens=500, temperature=0.2, messages= [system, user])
        completion = response["choices"][0]["message"]["content"]
      
        return completion
    except Exception as e: 
        return ("Failed to get text response from GPT4 API")

