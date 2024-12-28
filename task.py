from crewai import Agent, Task, Process, Crew
from agents import Agents 
from tools import search_tool, scrape


class Tasks:
    def __init__(self, event, language):
        self.information_note = event
        self.gbook_note = event
        self.language = language

    from crewai import Agent, Task, Process, Crew
from agents import Agents 
from tools import search_tool, scrape


class Tasks:
    def __init__(self, event, language):
        self.information_note = event
        self.gbook_note = event
        self.language = language

    def information_task(self):
        search_task = Task(
            description=f"""
            If the question is not related to SMKN 5 Jember, search for information based on {self.information_note}
            using [search_tool] and gather additional details using [Scrape].

            If there is no specific question and the user wants to start a conversation, engage the user in a friendly and meaningful conversation.
            
            If the question is related to SMKN 5 Jember, focus on finding relevant information from the following sources:
            - https://www.smkn5jember.sch.id/
            - https://dapo.kemdikbud.go.id/sekolah/5A63CD6299F2F0AD2604
            - https://sekolah.data.kemdikbud.go.id/index.php/chome/profil/1fed6e6c-60db-496d-81d1-151b9d2659c3
            - https://annibuku.com/sekolah/138766-smkn-5-jember

            If the gathered information is not sufficient or relevant, search for additional data from other trusted sources.
            Do not perform any search related to SMKN 5 Jember if the question does not explicitly mention it.
            """,
            expected_output=f"""A comprehensive report in {self.language} that includes:
           - Data Summary Clearly present key insights and findings in {self.language}, 
           - Detailed Answers Provide concise and accurate responses addressing the user's query, ensuring the use of {self.language}, 
           - Source Citations List all sources referenced, formatted for easy verification, and written in {self.language},  
           and Conversation (if no specific question is asked) Engage the user with thoughtful and friendly dialogue in {self.language}, ensuring a positive user experience.
            """, 
            agent=Agents().information_agent(), 
            tools=[search_tool, scrape]
        )
        
        # Additional logic to engage in a conversation if no specific question is asked
        if not self.information_note:
            conversation_task = Task(
                description="Start a friendly conversation in the specified language (e.g., sharing interesting facts, asking about user's preferences, etc.).",
                expected_output=f"A friendly and engaging conversation in {self.language}.",
                agent=Agents().conversation_agent(),  
                tools=[]  
            )
            
            return conversation_task
        
        return search_task

    
    def freind_task(self):
        freind_task = Task(
            description= f"""Answer based on {self.information_note} Engage in a friendly and supportive conversation with the user. The task involves understanding
        the user's input, providing empathetic and thoughtful responses, and maintaining a positive tone
        throughout the interaction.""",
            expected_output= f"""A comprehensive language {self.language} A conversational response that is friendly, empathetic, and contextually appropriate. The agent should
        ensure the user feels understood, supported, and engaged in a meaningful way.""",
            agent=Agents().freind_agent(),
        )
        return freind_task
