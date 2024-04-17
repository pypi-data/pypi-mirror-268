import random

class MotivationalQuotes:
    def __init__(self):
        self.quotes = [
    "Networking Matters: Don't underestimate the power of networking. Building professional relationships can often lead to job opportunities that aren't advertised.",
    "Customize Your Resume: Tailor your resume to each job application by highlighting relevant skills and experiences that match the job requirements.",
    "Practice Interviewing: Practice answering common interview questions with a friend or mentor to feel more confident and prepared during actual interviews.",
    "Continuous Learning: Stay updated with industry trends and developments by engaging in continuous learning through online courses, workshops, and seminars.",
    "Online Presence: Maintain a professional online presence on platforms like LinkedIn. Recruiters often search for candidates online, so make sure your profile is up-to-date and showcases your skills and experiences effectively.",
    "Follow Up: After an interview or networking event, send a personalized thank-you email to express your gratitude and reiterate your interest in the position or company.",
    "Stay Positive: Job searching can be challenging, but try to stay positive and persistent. Set realistic goals and celebrate small victories along the way.",
    "Volunteer or Intern: Consider volunteering or interning in your desired field to gain relevant experience and expand your professional network.",
    "Prepare Questions: Have thoughtful questions prepared to ask during interviews to demonstrate your interest in the company and the role.",
    "Seek Feedback: Don't be afraid to ask for feedback after interviews or job rejections. Constructive feedback can help you improve and refine your job search strategy."
    ]
    def get_random_jobtips(self):
        return random.choice(self.quotes)