#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 01:54:41 2025

@author: dannypa
"""

QUESTIONS_PATH: str = "data/all-detailed-reading-questions.json"
STEM: str = "stem"
STIMULUS: str = "stimulus"
RATIONALE: str = "rationale"
ANSWERS: str = "answerOptions"
CORRECT: str = "correct_answer" # haha, CollegeBoard mixed to cases in one response :D 
COLUMNS: list[str] = [
    STEM,
    STIMULUS,
    RATIONALE,
    ANSWERS,
    CORRECT  
]

STRING_COLUMNS: list[str] = list(filter(lambda s: s not in (ANSWERS, CORRECT), COLUMNS))
STRING_LIST_COLUMNS = [ANSWERS]
