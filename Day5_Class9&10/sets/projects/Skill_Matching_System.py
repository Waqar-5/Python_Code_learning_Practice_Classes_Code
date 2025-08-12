# 22Skill Matching System


students = [
    ("Ali", ["Python", "HTML", "CSS", "Python"]),
    ("Sara", ["Python", "Java", "C++", "Java"]),
    ("Zain", ["Python", "C", "JavaScript", "C++"]),
    ("Fatima", ["HTML", "CSS", "Python", "JavaScript"])
]

def find_common_skills(data):
    common = set(data[0][1])
    for _, skills in data[1:]:
        common &= set(skills)
    return common

def find_unique_skills(data):
    all_skills = set()
    for _, skills in data:
        all_skills |= set(skills)
    for name, skills in data:
        others = all_skills - set(skills)
        unique = set(skills) - others
        print(f"🔹 {name}'s Unique Skills: {unique}")

def recommend_skills(data):
    all_skills = set()
    for _, skills in data:
        all_skills |= set(skills)
    for name, skills in data:
        missing = all_skills - set(skills)
        print(f"🧠 Recommend to {name}: {missing}")

print("✅ Common Skills:", find_common_skills(students))
print("\n✨ Unique Skills Per Student:")
find_unique_skills(students)
print("\n📚 Skill Recommendations:")
recommend_skills(students)
