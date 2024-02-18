import os


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise Exception(f"Error: File '{file_path}' not found.")
    except Exception as e:
        raise e


def write_to_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)


def validate_duplicates(acts):
    normalized_acts = set()
    for act in acts:
        normalized_act = ''.join(
            char.lower() for char in act if char.isalnum()
        )
        if normalized_act in normalized_acts:
            raise ValueError(f'Duplicate found: {act}')
        normalized_acts.add(normalized_act)


html_template = read_file('./template.html')
headliners = read_file('acts/headliners.txt').split('\n')
large_acts = read_file('acts/large-acts.txt').split('\n')
other_acts = read_file('acts/other-acts.txt').split('\n')

validate_duplicates(headliners + large_acts + other_acts)

poster = html_template.replace(
    '<!-- HEADLINERS -->',
    "\n".join([f"<span>{s}</span>" if len(s) > 0 else '' for s in headliners])
).replace(
    '<!-- LARGE ACTS -->',
    "\n".join([f"<span>{s}</span>" if len(s) > 0 else '' for s in large_acts])
).replace(
    '<!-- OTHER ACTS -->',
    "\n".join([f"<span>{s}</span>" if len(s) > 0 else '' for s in other_acts])
)

write_to_file('output/poster.html', poster)
