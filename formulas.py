def mentor_successful_interaction(soft_skills):
    return (soft_skills*2 + 10) / 100


def idea_generation_time(percent, team_soft_skills):
    return (percent*10 + 300)*4*2/team_soft_skills


def final_score(soft_skills, idea, programming, design):
    return (idea*1.5 + programming + design)*(soft_skills + 5) / 30
