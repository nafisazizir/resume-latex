import json

def personal_info(data):
    name = data['name']
    email = data['email']
    phone = data['phone']
    website = data['website']
    github = data['github']
    linkedin = data['linkedin']

    name_tex = fr"\name{{{name}}}"
    email_tex = fr"\href{{mailto:{email}}}{{{email}}}"
    phone_tex = fr"\href{{tel:{phone}}}{{{phone}}}"
    website_tex = fr"\href{{www.{website}}}{{{website}}}"
    github_tex = fr"\href{{https://{github}}}{{{github}}}"
    linkedin_tex = fr"\href{{https://{linkedin}}}{{{linkedin}}}"
    addr_tex = fr"\address{{{email_tex} \\ {phone_tex} \\ {website_tex} \\ {github_tex} \\ {linkedin_tex}}}"

    return name_tex + "\n" + addr_tex + "\n"


def education(data):
    edus = data["education"]

    res_tex = ""

    for edu in edus:
        institution = edu['institution']
        start_date = edu['startDate']
        end_date = edu['endDate']
        res_tex += fr"{{\bf {institution}}} \hfill {{{start_date} - {end_date}}}" + "\n"
        res_tex += fr"\vspace{{-0.75em}}" + "\n"

        highlight = edu['highlights']
        if highlight:
            res_tex += fr"\begin{{itemize}}" + \
                "\n" + fr"\itemsep -7pt {{}}" + "\n"

            for item in highlight:
                res_tex += fr"\item {item}" + "\n"

            res_tex += fr" \end{{itemize}}" + \
                "\n" + fr" \vspace{{-0.25em}}" + "\n"

        res_tex += "\n"

    return res_tex.replace("&", fr"\&")


def skills(data):
    res_tex = ""

    for skill in data['skills']:
        for skill_name in skill:
            res_tex += skill_name + " & "
            for item in skill[skill_name]:
                res_tex += item + ", "

            res_tex = res_tex[:-2]
            res_tex += rf" \\" + "\n"

    return res_tex


def experiences(data):
    experiences = data['experiences']
    res_tex = ""

    for exp in experiences:
        organization = exp['organization']
        title = exp['title']
        location = exp['location']
        start_date = exp['startDate']
        end_date = exp['endDate']
        highlights = exp['highlights']

        res_tex += fr"\textbf{{{title}}} \hfill {start_date} - {end_date} \\" + "\n"
        res_tex += fr"{organization} \hfill \textit{{{location}}}" + "\n"
        res_tex += fr"\vspace{{-0.75em}}" + "\n"

        if highlights:
            res_tex += fr"\begin{{itemize}}" + \
                "\n" + fr"\itemsep -7pt {{}}" + "\n"

            for item in highlights:
                res_tex += fr"\item {item}" + "\n"

            res_tex += fr" \end{{itemize}}" + \
                "\n" + fr" \vspace{{-0.25em}}" + "\n"

        res_tex += "\n"

    return res_tex


def projects(data):
    projects = data['projects']
    res_tex = ""

    for project in projects:
        name = project['name']
        highlights = project['highlights']

        res_tex += fr"{{\bf {name}}}" + "\n"
        res_tex += fr"\vspace{{-0.75em}}" + "\n"

        if highlights:
            res_tex += fr"\begin{{itemize}}" + \
                "\n" + fr"\itemsep -7pt {{}}" + "\n"

            for item in highlights:
                res_tex += fr"\item {item}" + "\n"

            res_tex += fr" \end{{itemize}}" + \
                "\n" + fr" \vspace{{-0.25em}}" + "\n"

        res_tex += "\n"

    return res_tex.replace("&", fr"\&")


def achievements(data):
    achievements = data['achievements']
    res_tex = ""

    if achievements:
        res_tex += fr"\begin{{itemize}}" + \
            "\n" + fr"\itemsep -7pt {{}}" + "\n"

        for item in achievements:
            res_tex += fr"\item {item}" + "\n"

        res_tex += fr" \end{{itemize}}" + \
            "\n" + fr" \vspace{{-0.25em}}" + "\n"

    res_tex += "\n"

    return res_tex


def write_to_latex(data_tex):
    with open("tex_template.txt", 'r') as file:
        lines = file.readlines()

    with open("resume.tex", 'w') as file:
        for line in lines:
            if line in data_tex:
                file.write(data_tex[line])
            else:
                file.write(line)

def main():
    # Read the JSON file
    with open("resume.json", "r") as file:
        json_data = file.read()

    # Convert JSON to Python dictionary
    data = json.loads(json_data)

    data_tex = {
        "[PERSONAL PLACEHOLDER]\n": personal_info(data),
        "[EDUCATION PLACEHOLDER]\n": education(data),
        "[SKILLS PLACEHOLDER]\n": skills(data),
        "[EXPERIENCES PLACEHOLDER]\n": experiences(data),
        "[PROJECTS PLACEHOLDER]\n": projects(data),
        "[ACHIEVEMENTS PLACEHOLDER]\n": achievements(data)
    }

    write_to_latex(data_tex)


if __name__ == '__main__':
    main()
