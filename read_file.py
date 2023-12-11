def get_profiles(file_path: str) -> list[tuple]:
    file = open(file_path, 'r')
    is_user = False
    category = ''
    profiles = []

    for line in file:
        # category
        if line == '<hashtag>\n':
            is_user = False
            continue
        elif line == '<user>\n':
            is_user = True
            continue
        # value
        if is_user == False:  # category
            category = line.strip()
        else:  # user
            user = line.strip()
            profiles.append((category, user))
    file.close()
    return profiles
