# Student Skill Mapper & Duplicates Resolver



# -------------------------------
# 👥 Sample data
# -------------------------------

students = [
    ("Ali", ["Python", "HTML", "CSS", "Python"]),
    ("Sara", ["Python", "Java", "C++", "Java"]),
    ("Ahmed", ["HTML", "CSS", "JavaScript", "HTML"]),
    ("Fatima", ["Python", "C++", "C", "Rust"]),
    ("Asad", ["Java", "JavaScript", "C++", "PYthon"]),
]


# -------------------------------
# 🔧 Functions
# -------------------------------

def clean_skills(skills_list):
    """Remove duplicates using set"""
    return set(skills_list)


def display_student_skills(data):
    print("\n🎯 Unique Skills Per Student:")
    for name, skills in data:
        skill_set = clean_skills(skills)
        print(f"- {name}: {skill_set}")


def find_all_unique_skills(data):
    """Combine all skills using union"""
    all_skills = set()
    for _, skills in data:
        all_skills |= clean_skills(skills)
    return all_skills


def find_common_skills(data):
    """Find intersection of skills"""
    all_sets = [clean_skills(skills) for _, skills in data]
    if all_sets:
        common = all_sets[0]
        for skill_set in all_sets[1:]:
            common &= skill_set
        return common
    return set()


def compare_students(data):
    """Check if any students have same skills"""
    print("\n🔁 Students with same skill sets:")
    compared = set()
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            name1, skills1 = data[i]
            name2, skills2 = data[j]
            set1 = clean_skills(skills1)
            set2 = clean_skills(skills2)
            if set1 == set2 and (name2, name1) not in compared:
                print(f"✔️ {name1} and {name2} have identical skills!")
                compared.add((name1, name2))


# -------------------------------
# 🚀 Run Project
# -------------------------------

# 1. Show cleaned skills
display_student_skills(students)

# 2. All unique skills
unique = find_all_unique_skills(students)
print("\n📚 All Unique Skills:", unique)

# 3. Common skills to everyone
common = find_common_skills(students)
print("\n🧠 Skills shared by all students:", common)

# 4. Check duplicates
compare_students(students)